"""PubMed abstract fetcher by DOI (fallback when CrossRef has no abstract)."""
from __future__ import annotations

import requests

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_abstract_pubmed(doi: str) -> str:
    """Return the abstract text from PubMed for the given DOI, or '' on miss/error."""
    try:
        r = requests.get(
            ESEARCH_URL,
            params={"db": "pubmed", "term": f"{doi}[DOI]", "retmode": "json", "retmax": 1},
            timeout=8,
        )
        ids = r.json().get("esearchresult", {}).get("idlist", [])
        if not ids:
            return ""
        r2 = requests.get(
            EFETCH_URL,
            params={"db": "pubmed", "id": ids[0], "rettype": "abstract", "retmode": "text"},
            timeout=8,
        )
        return r2.text.strip()
    except requests.RequestException:
        return ""
