import re
import requests
import json
import os
import bz2
import xml.etree.ElementTree as ET

from tqdm import tqdm

from category_aliases import CATEGORY_ALIASES
from lang_def import WIKIPEDIA_LANGUAGES
from media_aliases import MEDIA_ALIASES
from db_operations import *


_BASE_URL_TMPL = "{mirror_url}/{lang}wiki/{date}/"
_INFO_FILE = "dumpstatus.json"
_DATE = "20240101"
mirror_url = "https://dumps.wikimedia.org"

def _base_url(lang):
    return _BASE_URL_TMPL.format(
        lang=lang.replace("-", "_"),
        date=_DATE,
        mirror_url=mirror_url,
    )

def download_status(lang):
    info_url = _base_url(lang) + _INFO_FILE
    print(f"Downloading info file from {info_url}")
    response = requests.get(info_url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(f"Failed to download or parse the file. Status code: {response.status_code}")
        return None

def get_files(lang):
    dump_info = download_status(lang)
    multistream_dump_info = dump_info["jobs"]["articlesmultistreamdump"]
    assert (
        multistream_dump_info["status"] == "done"
    ), "Specified dump (%s) multistream status is not 'done': %s" % (
        _base_url(lang),
        multistream_dump_info["status"],
    )
    xml_urls = []
    file_names = []
    total_bytes = 0

    for fname, info in multistream_dump_info["files"].items():
        if ".xml" not in fname:
            continue
        total_bytes += info["size"]
        xml_urls.append(_base_url(lang) + fname)
        file_names.append((fname, total_bytes))
    return xml_urls, file_names


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size_in_bytes = int(r.headers.get('content-length', 0))
        block_size = 8192  # 8 Kibibytes

        with open(local_filename, 'wb') as f, tqdm(
            desc=local_filename,
            total=total_size_in_bytes,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=block_size):
                bar.update(len(chunk))
                f.write(chunk)

from urllib.parse import quote

def _construct_url(title, language):
    # See: https://meta.wikimedia.org/wiki/Help:URL
    return f"https://{language}.wikipedia.org/wiki/{quote(title)}"

def load_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file]

def is_in_list(string_to_check, list_of_strings):
    return string_to_check.lower() in list_of_strings

tmp_to_concat = load_file_to_list("template_to_concat.txt")
tmp_to_params = load_file_to_list("template_to_params.txt")
tmp_to_ignore = load_file_to_list("template_to_ignore.txt")

def extract_page_range(filename):
    # Regular expression to match the pattern 'p<number>p<number>'
    match = re.search(r'p(\d+)p(\d+)', filename)
    if match:
        min_page = int(match.group(1))
        max_page = int(match.group(2))
        return min_page, max_page
    else:
        return None

import pandas as pd
import pyarrow.parquet as pq

def stream_decompress_and_parse_xml(filename,language):

    min_page,max_page=extract_page_range(filename)

    # initialize data
    data_batch=[]
    db_min=min_page
    db_max=0
    check_datadir(_DATE,language)

    with bz2.open(filename, 'rb') as file, tqdm(
        total=max_page-min_page, initial=0, unit='page', unit_scale=True, desc=f"Processing {filename}"
    ) as bar:
        parser = ET.XMLPullParser(events=("start", "end"))
        counter = 0

        for line in file:
            parser.feed(line)
            for event, elem in parser.read_events():
                if not elem.tag.endswith("page"):
                    continue
                
                if elem:
                    namespace = elem.tag[:-4]
                    title = elem.find(f"./{namespace}title").text
                    ns = elem.find(f"./{namespace}ns").text
                    id_ = elem.find(f"./{namespace}id").text
                    bar.n=int(id_)-min_page
                    bar.refresh()
                    red_ = elem.find(f"./{namespace}redirect")
                    # Filter pages that are not in the "main" namespace.
                    if ns != "0":
                        elem.clear()
                        continue

                    raw_content = elem.find(
                        f"./{namespace}revision/{namespace}text"
                    ).text
                    elem.clear()
                    counter += 1
                    try:
                        clean_content = _parse_and_clean_wikicode(raw_content,language)
                    except:
                        clean_content = raw_content
                    url = _construct_url(title, language)

                    # build the structure in memory
                    if len(data_batch)==0:
                        db_min=id_
                    data_batch.append({"id": id_, "url": url, "title": title, "text": clean_content})
                    db_max = id_

                    if counter%100==0:
                        if len(data_batch) >= 50000:
                            fname=f"data/{_DATE}/{language}/train-wikipedia-fr-p{db_min}p{db_max}.parquet"
                            df=pd.DataFrame(data_batch)
                            
                            df.to_parquet(fname,index=False)
                            data_batch=[]
        # dont forget the last batch
        fname=f"data/{_DATE}/{language}/p{db_min}p{db_max}.parquet"
        df=pd.DataFrame(data_batch)
        df.to_parquet(fname,index=False)
        data_batch=[]


def check_datadir(date,language):
    if not os.path.exists(f"data/{date}"):
        os.mkdir(path=f"data/{date}")
    if not os.path.exists(f"data/{date}/{language}"):
        os.mkdir(path=f"data/{date}/{language}")

def _parse_and_clean_wikicode(raw_content, language):
    import mwparserfromhell
    parser=mwparserfromhell
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


def main():
    lang = 'fr'  # Example language
    xml_urls, file_names = get_files(lang)
    nbfiles = len(file_names)

    print(f"number of files to download: {nbfiles}")

    first_url = xml_urls[0]
    local_filename = first_url.split('/')[-1]

    if not os.path.exists(local_filename):
        download_file(first_url, local_filename)

    stream_decompress_and_parse_xml(local_filename,lang)

if __name__ == "__main__":
    main()
