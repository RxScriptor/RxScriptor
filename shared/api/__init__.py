"""Shared runtime fetchers for paper metadata/abstracts."""
from .crossref import fetch_metadata_crossref
from .pubmed import fetch_abstract_pubmed
from .fetch_abstract import fetch_paper
from .news import fetch_google_news

__all__ = [
    "fetch_metadata_crossref",
    "fetch_abstract_pubmed",
    "fetch_paper",
    "fetch_google_news",
]
