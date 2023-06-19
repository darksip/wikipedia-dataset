import json
from typing import Dict, List, Tuple

import requests
from tqdm import tqdm

from .lang_def import WIKIPEDIA_LANGUAGES

_QUERY_TEMPLATE_MEDIA = "https://{lang}.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=namespacealiases|namespaces&format=json&formatversion=2"

_MEDIA_ALIASES_IGNORED = ["Image", "File", "Media", ""]


def create_media_and_category_aliases(
    date: str,
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """
    Create media and category aliases for a given date.

    For each Wikipedia language code,

    - query the Wikipedia API with the template above
    - get media aliases from namespaces -2 and 6
    - get category aliases from namespace 14

    """
    media_aliases = {}
    category_aliases = {}

    for language in tqdm(WIKIPEDIA_LANGUAGES[date]):
        try:
            url = _QUERY_TEMPLATE_MEDIA.format(lang=language)
            r = requests.get(url).json()

            # Media aliases (namespaces -2 and 6)
            ns_aliases = [
                alias_def["alias"]
                for alias_def in r["query"]["namespacealiases"]
                if alias_def["id"] in [-2, 6]
            ]
            aliases = [
                ns["name"]
                for ns in r["query"]["namespaces"].values()
                if ns["id"] in [-2, 6]
            ]
            merged = {
                alias
                for alias in sorted(ns_aliases + aliases)
                if alias not in _MEDIA_ALIASES_IGNORED
            }
            if merged:
                media_aliases[language] = list(sorted(merged))

            # Category aliases (namespace 14)
            cat_aliases = [
                alias_def["alias"]
                for alias_def in r["query"]["namespacealiases"]
                if alias_def["id"] in [14]
            ]
            aliases = [
                ns["name"]
                for ns in r["query"]["namespaces"].values()
                if ns["id"] in [14]
            ]
            merged = {alias for alias in sorted(cat_aliases + aliases)}
            if merged:
                category_aliases[language] = list(sorted(merged))

        except Exception as e:
            print(f"Error for language {language}: {e}")

    return media_aliases, category_aliases


def write_python_module(filename: str, varname: str, aliases):
    """
    Write a python module with the given aliases.

    For instance, if called with filename="media_aliases.py", varname="MEDIA_ALIASES",
    and aliases={"en": ["File", "Image"]}, the following Python file `media_aliases.py`
    will be written:

    ```
    MEDIA_ALIASES = {
        "en": ["File", "Image"]
    }
    ```

    We need this instead of a JSON file in order to be able to import it in the
    dataset script automatically.
    """
    with open(filename, "w") as f:
        f.write(f"{varname} = ")
        json.dump(aliases, f, indent=2, ensure_ascii=False, sort_keys=True)


# Unused at the moment.
def get_all_languages():
    """Get all languages from the wikipedia API."""
    url = "https://meta.wikimedia.org/w/api.php?action=sitematrix&format=json&formatversion=2&smlangprop=code|name|site&smtype=language"
    r = requests.get(url).json()
    languages = [lang["code"] for lang in r["sitematrix"][1]["site"]]
    return languages


if __name__ == "__main__":
    latest_date = sorted(WIKIPEDIA_LANGUAGES.keys())[-1]
    media_aliases, category_aliases = create_media_and_category_aliases(
        date=latest_date
    )

    write_python_module("media_aliases.py", "MEDIA_ALIASES", media_aliases)
    write_python_module("category_aliases.py", "CATEGORY_ALIASES", category_aliases)
