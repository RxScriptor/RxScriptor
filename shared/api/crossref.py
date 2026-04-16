"""CrossRef metadata fetcher for a DOI."""
from __future__ import annotations

import re

import requests

USER_AGENT = "rxscriptor-app/1.0 (mailto:contact@rxscriptor.dev)"
CROSSREF_URL = "https://api.crossref.org/works/{doi}"


def fetch_metadata_crossref(doi: str) -> dict:
    """Fetch paper metadata from CrossRef.

    Returns a dict with keys: doi, title, authors, journal, year, abstract, url.
    On failure returns {"error": "<message>"}.
    """
    doi = doi.strip().lstrip("https://doi.org/").lstrip("doi:")
    try:
        r = requests.get(
            CROSSREF_URL.format(doi=doi),
            timeout=10,
            headers={"User-Agent": USER_AGENT},
        )
        r.raise_for_status()
        item = r.json()["message"]
        authors = ", ".join(
            f"{a.get('family', '')}, {a.get('given', '')}"
            for a in item.get("author", [])[:5]
        )
        journal = (item.get("container-title") or [""])[0]
        year = item.get("published", {}).get("date-parts", [[""]])[0][0]
        title = (item.get("title") or [""])[0]
        abstract = re.sub(r"<[^>]+>", "", item.get("abstract", ""))
        return {
            "doi": doi,
            "title": title,
            "authors": authors,
            "journal": journal,
            "year": str(year),
            "abstract": abstract,
            "url": f"https://doi.org/{doi}",
        }
    except Exception as e:
        return {"error": str(e)}
