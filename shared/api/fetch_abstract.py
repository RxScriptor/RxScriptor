"""Unified paper fetch: CrossRef first, fall back to PubMed for abstract.

저작권 이슈를 피하기 위해 abstract는 commit하지 않고
런타임(Streamlit 앱 / Quarto 빌드)에 API로 가져옵니다.
"""
from __future__ import annotations

from .crossref import fetch_metadata_crossref
from .pubmed import fetch_abstract_pubmed


def fetch_paper(doi: str) -> dict:
    """Return paper metadata with abstract populated if available.

    Shape on success: {doi, title, authors, journal, year, abstract, url}.
    If CrossRef fails, returns {"error": "..."}.
    """
    meta = fetch_metadata_crossref(doi)
    if "error" in meta:
        return meta
    if not meta.get("abstract"):
        meta["abstract"] = fetch_abstract_pubmed(meta["doi"])
    return meta
