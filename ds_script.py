# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors and the HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Wikipedia dataset containing cleaned articles of all languages."""


import bz2
import codecs
import json
import re
import xml.etree.cElementTree as etree
from urllib.parse import quote

import datasets
from datetime import datetime

from category_aliases import CATEGORY_ALIASES
from lang_def import WIKIPEDIA_LANGUAGES
from media_aliases import MEDIA_ALIASES
from db_operations import *

logger = datasets.logging.get_logger(__name__)


_CITATION = """\
@ONLINE {wikidump,
    author = {Wikimedia Foundation},
    title  = {Wikimedia Downloads},
    url    = {https://dumps.wikimedia.org}
}
"""

_DESCRIPTION = """\
Wikipedia dataset containing cleaned articles of all languages.
The datasets are built from the Wikipedia dump
(https://dumps.wikimedia.org/) with one split per language. Each example
contains the content of one full Wikipedia article with cleaning to strip
markdown and unwanted sections (references, etc.).
"""

_LICENSE = (
    "This work is licensed under the Creative Commons Attribution-ShareAlike "
    "3.0 Unported License. To view a copy of this license, visit "
    "http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to "
    "Creative Commons, PO Box 1866, Mountain View, CA 94042, USA."
)

# List of mirrors at https://dumps.wikimedia.org/mirrors.html
# - default mirror: https://dumps.wikimedia.org
#   yields https://dumps.wikimedia.org/enwiki/20220301/
# - example: https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/
#   yields https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20220301/
_BASE_URL_TMPL = "{mirror_url}/{lang}wiki/{date}/"
_INFO_FILE = "dumpstatus.json"


_VERSION = datasets.Version("2.0.0", "")


class WikipediaConfig(datasets.BuilderConfig):
    """BuilderConfig for Wikipedia."""

    def __init__(
        self,
        language=None,
        date=None,
        mirror_url="https://dumps.wikimedia.org",
        version=_VERSION,
        **kwargs,
    ):
        """BuilderConfig for Wikipedia.

        Args:
          language: string, the language code for the Wikipedia dump to use.
          date: string, date of the Wikipedia dump in YYYYMMDD format. A list of
            available dates can be found at https://dumps.wikimedia.org/enwiki/.
          **kwargs: keyword arguments forwarded to super.
        """
        super().__init__(
            name=f"{date}.{language}",
            description=f"Wikipedia dataset for {language}, parsed from {date} dump.",
            version=version,
            **kwargs,
        )
        self.date = date
        self.language = language
        self.mirror_url = mirror_url.rstrip("/")


# _DATE = "20220301"

class Wikipedia(datasets.BeamBasedBuilder):
    """Wikipedia dataset."""

    # Use mirror (your.org) to avoid download caps.
    BUILDER_CONFIG_CLASS = WikipediaConfig
    BUILDER_CONFIGS = [
        WikipediaConfig(
            language=lang,
            date="some future date",
        )  # pylint:disable=g-complex-comprehension
        for lang in WIKIPEDIA_LANGUAGES
    ]

    DEBUG_LIMIT=get_debug_limit()

    session_id = 0
    #logging.basicConfig(filename='unhandled_templates.log', level=logging.INFO)
    #progress = 0

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "url": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "text": datasets.Value("string"),
                }
            ),
            # No default supervised_keys.
            supervised_keys=None,
            homepage="https://dumps.wikimedia.org",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager, pipeline):
        def _base_url(lang):
            return _BASE_URL_TMPL.format(
                lang=lang.replace("-", "_"),
                date=self.config.date,
                mirror_url=self.config.mirror_url,
            )

        lang = self.config.language

        info_url = _base_url(lang) + _INFO_FILE
        print(f"Downloading info file from {info_url}")
        # Use dictionary since testing mock always returns the same result.
        downloaded_files = dl_manager.download_and_extract({"info": info_url})

        xml_urls = []
        file_names = []

        total_bytes = 0
        with open(downloaded_files["info"], encoding="utf-8") as f:
            dump_info = json.load(f)
        multistream_dump_info = dump_info["jobs"]["articlesmultistreamdump"]
        assert (
            multistream_dump_info["status"] == "done"
        ), "Specified dump (%s) multistream status is not 'done': %s" % (
            _base_url(lang),
            multistream_dump_info["status"],
        )

        for fname, info in multistream_dump_info["files"].items():
            if ".xml" not in fname:
                continue
            total_bytes += info["size"]
            xml_urls.append(_base_url(lang) + fname)
            file_names.append((fname,total_bytes))

        nbfiles = len(file_names)
        now = datetime.now()

        self.session_id = insert_new_session(now, lang, self.config.date, nbfiles)
        print(f"session_id={self.session_id}")

            # Use dictionary since testing mock always returns the same result.
        downloaded_files = dl_manager.download({"xml": xml_urls})
        if not pipeline.is_local():
            downloaded_files = dl_manager.ship_files_with_pipeline(
                downloaded_files, pipeline
            )

        return [
            datasets.SplitGenerator(  # pylint:disable=g-complex-comprehension
                name=datasets.Split.TRAIN,
                gen_kwargs={"filepaths": downloaded_files["xml"], "language": lang},
            )
        ]

    def _build_pcollection(self, pipeline, filepaths, language):
        """Build PCollection of examples in the raw (text) form."""
        import apache_beam as beam
        import mwparserfromhell


        def _extract_content(filepath):
            """Extracts article content from a single WikiMedia XML file."""
            logger.info("generating examples from = %s", filepath)
            print(f"generating examples from = {filepath}")
            counter=0
            print(f"session_id for db storage is {self.session_id}")
            print("debug limit is", self.DEBUG_LIMIT)

            fname=os.path.basename(filepath)
            create_file_progress(self.session_id,fname,counter)
            
            with beam.io.filesystems.FileSystems.open(filepath) as f:
                f = bz2.BZ2File(filename=f)
                # Workaround due to: https://github.com/tensorflow/tensorflow/issues/33563
                utf_f = codecs.getreader("utf-8")(f)
                context = etree.iterparse(utf_f, events=("end",))
                for unused_event, elem in context:
                    if self.DEBUG_LIMIT and counter > self.DEBUG_LIMIT :
                        break
                    if not elem.tag.endswith("page"):
                        continue
                    counter += 1
                    namespace = elem.tag[:-4]
                    title = elem.find(f"./{namespace}title").text
                    ns = elem.find(f"./{namespace}ns").text
                    id_ = elem.find(f"./{namespace}id").text
                    red_ = elem.find(f"./{namespace}redirect")

                    
                    # Filter pages that are not in the "main" namespace.
                    if ns != "0":
                        elem.clear()
                        continue

                    raw_content = elem.find(
                        f"./{namespace}revision/{namespace}text"
                    ).text
                    elem.clear()

                    # Filter redirects.
                    if raw_content is None or red_ is not None:
                        beam.metrics.Metrics.counter(
                            language, "filtered-redirects"
                        ).inc()
                        continue

                    beam.metrics.Metrics.counter(language, "extracted-examples").inc()
#                    yield (id_, title, raw_content)
                    ret = _clean_content((id_, title, raw_content),language)
                    if ret == None:
                        continue
                    id,jsonobj = ret
                    if counter % 10 == 0:
                        print(f"counter:{counter}")
                        update_file_progress(self.session_id,fname,counter,title,id)

                    yield id,jsonobj
                
                print(f"end loop {fname}")
                

        def _clean_content(inputs, language):
            """Cleans raw wikicode to extract text."""
            id_, title, raw_content = inputs

            try:
                text = _parse_and_clean_wikicode(
                    raw_content, parser=mwparserfromhell, language=language
                )
            except mwparserfromhell.parser.ParserError as e:
                beam.metrics.Metrics.counter(language, "parser-error").inc()
                logger.error("mwparserfromhell ParseError: %s", e)
                return

            if not text:
                beam.metrics.Metrics.counter(language, "empty-clean-examples").inc()
                return

            url = _construct_url(title, language)

            #beam.metrics.Metrics.counter(language, "cleaned-examples").inc()

            return id_, {"id": id_, "url": url, "title": title, "text": text}

        return (
            pipeline
            | "Initialize" >> beam.Create(filepaths)
            | "Extract content" >> beam.FlatMap(_extract_content)
            | "Distribute" >> beam.transforms.Reshuffle()
#            | "Clean content" >> beam.FlatMap(_clean_content, language=language)
        )

def load_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file]

def is_in_list(string_to_check, list_of_strings):
    return string_to_check.lower() in list_of_strings

tmp_to_concat = load_file_to_list("template_to_concat.txt")
tmp_to_params = load_file_to_list("template_to_params.txt")
tmp_to_ignore = load_file_to_list("template_to_ignore.txt")

def _parse_and_clean_wikicode(raw_content, parser, language):
    import mwparserfromhell

    """Strips formatting and unwanted sections from raw page content."""
    wikicode = parser.parse(raw_content)

    # Filters for magic words that are parser instructions -- e.g., __NOTOC__
    re_rm_magic = re.compile("__[A-Z]*__", flags=re.UNICODE)

    # Filters for file/image links.
    media_prefixes = "|".join(
        ["File", "Image", "Media"] + MEDIA_ALIASES.get(language, [])
    )
    re_rm_wikilink = re.compile(
        f"^(?:{media_prefixes}):", flags=re.IGNORECASE | re.UNICODE
    )

    def rm_wikilink(obj):
        return bool(re_rm_wikilink.match(str(obj.title)))

    # Filters for references and tables
    def rm_tag(obj):
        return str(obj.tag) in {"ref", "table"}

    # Leave category links in-place but remove the category prefixes
    cat_prefixes = "|".join(["Category"] + CATEGORY_ALIASES.get(language, []))
    re_clean_wikilink = re.compile(
        f"^(?:{cat_prefixes}):", flags=re.IGNORECASE | re.UNICODE
    )

    re_numbers = re.compile(r"(\d+e)", re.IGNORECASE)
    def is_category(obj):
        return bool(re_clean_wikilink.match(str(obj.title)))

    def clean_wikilink(obj):
        text = obj.__strip__()
        text = re.sub(re_clean_wikilink, "", text)
        obj.text = text

    def try_replace_obj(obj):
        try:
            clean_wikilink(obj)
        except ValueError:
            # For unknown reasons, objects are sometimes not found.
            pass

    def try_remove_obj(obj, section):
        try:
            section.remove(obj)
        except ValueError:
            # For unknown reasons, objects are sometimes not found.
            pass

    def get_template_name_and_params(template):
        template_name = template.name.strip_code().strip()
        template_params = ' '.join(param.value.strip_code().strip() for param in template.params)
        return (template_name, template_params)
    
    def clean_template(obj, section):
        try:
            name, params = get_template_name_and_params(obj)
            if name.lower().startswith("date"):
                new_text = params
            elif name.lower() in ["s","s-"]:
                eme = "ème" if params.lower()!="i" else "er"
                new_text = f"{params} {eme} siècle"
            elif name.lower() in ["-s","-s-"]:
                eme = "ème" if params.lower()!="i" else "er"
                new_text = f"{params} {eme} siècle av. JC"
            elif re_numbers.match(name):
                new_text = f"{name} {params}"
            elif name.lower().startswith("infobox"):
                return
            elif name.lower().startswith("taxobox"):
                return
            elif name.lower() == "lang":
                new_text = params[2:].strip()
            elif name.lower() == "langue":
                new_text = params[2:].strip()
            elif name.lower().startswith("lang-"):
                new_text = params
            elif is_in_list(name, tmp_to_concat):
                new_text = f"{name} : {params}"
            elif is_in_list(name, tmp_to_params):
                new_text = params
            elif is_in_list(name, tmp_to_ignore):
                return
            elif params == "":
                new_text = name
            elif name == "":
                return
            else:
                #logging.info('Template: %s, Parameters: %s', name, params)
                return
                #new_text = f"{name} {{ {params} }}"
            
            new_template = mwparserfromhell.nodes.text.Text=new_text
            section.replace(obj, new_template)
        except ValueError:
            # For unknown reasons, objects are sometimes not found.
            pass

    section_text = []
    titles_dict = {}

    # Create a dictionary of section titles and their markdown levels
    for section in wikicode.get_sections(include_lead=False, include_headings=True):
        if section.nodes and isinstance(section.nodes[0], mwparserfromhell.nodes.heading.Heading):
            heading = section.nodes[0].title.strip_code().strip()
            level = section.nodes[0].level
            # Store heading with its markdown level
            titles_dict[heading] = level
            section.nodes[0].title = f"z{heading}z"

    # Filter individual sections to clean.
    for section in wikicode.get_sections(
        flat=True, include_lead=True, include_headings=True
    ):


        for obj in section.ifilter_wikilinks(recursive=True):
            if rm_wikilink(obj):
                try_remove_obj(obj, section)
            elif is_category(obj):
                try_replace_obj(obj)
        for obj in section.ifilter_tags(matches=rm_tag, recursive=True):
            try_remove_obj(obj, section)

        section_raw = section.strip_code().strip()
        for obj in section.ifilter_templates(recursive=True):
            clean_template(obj,section)

        section_raw = section.strip_code().strip()
        for heading, level in titles_dict.items():
            # Create the markdown heading
            markdown_heading = "#" * level + " " + heading
            # Replace the heading with its markdown equivalent
            section_raw = re.sub(re.escape(f"z{heading}z"), markdown_heading, section_raw, count=1)
        section_text.append(re.sub(re_rm_magic, "", section_raw))
    return "\n\n".join(section_text)


def _construct_url(title, language):
    # See: https://meta.wikimedia.org/wiki/Help:URL
    return f"https://{language}.wikipedia.org/wiki/{quote(title)}"