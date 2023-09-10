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


import json

import datasets
import pyarrow.parquet as pq

from .lang_def import WIKIPEDIA_LANGUAGES

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

_BASE_URL_TMPL = "data/{date}/{lang}"

_VERSION = datasets.Version("1.2.0", "")


class WikipediaConfig(datasets.BuilderConfig):
    """BuilderConfig for Wikipedia."""

    def __init__(self, language=None, date=None, version=_VERSION, **kwargs):
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


class Wikipedia(datasets.ArrowBasedBuilder):
    """Wikipedia dataset."""

    # Use mirror (your.org) to avoid download caps.
    BUILDER_CONFIG_CLASS = WikipediaConfig
    BUILDER_CONFIGS = [
        WikipediaConfig(
            language=lang,
            date=date,
        )  # pylint:disable=g-complex-comprehension
        for date in WIKIPEDIA_LANGUAGES.keys()
        for lang in WIKIPEDIA_LANGUAGES[date]
    ]

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

    def _split_generators(self, dl_manager):
        def _base_url(lang):
            return _BASE_URL_TMPL.format(lang=lang, date=self.config.date)

        lang = self.config.language

        info_file_url = _base_url(lang) + "/info.json"
        downloaded_info_file = dl_manager.download_and_extract({"info": info_file_url})
        with open(downloaded_info_file["info"], "r") as f:
            info = json.load(f)

        shard_urls = [
            _base_url(lang) + "/" + shard_name for shard_name in info["shards"]
        ]
        downloaded_files = dl_manager.download({"train": shard_urls})
        logger.info("downloaded_files = %s", downloaded_files)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"filepaths": downloaded_files["train"]},
            ),
        ]

    def _generate_tables(self, filepaths):
        """This function returns the examples in the raw (text) form."""

        for filepath in filepaths:
            with open(filepath, "rb") as f:
                pf = pq.ParquetFile(f)
                for group_i in range(pf.num_row_groups):
                    tbl = pf.read_row_group(group_i)
                    yield group_i, tbl
