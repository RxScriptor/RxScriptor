"""
app.py — RxScriptor Literature Summarizer
DOI 입력 → CrossRef/PubMed 메타데이터 조회 → Claude API 3종 요약
Clinical White 테마 적용.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Make repo root importable (so `shared.*` and `apps._shared.*` resolve)
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import anthropic
import streamlit as st

from apps._shared.rxscriptor_header import (
    COLOR,
    apply_theme,
    info_card,
    section_title,
    show_footer,
    show_header,
    show_mini_header,
    tag_badges,
)
from shared.api import fetch_abstract_pubmed, fetch_metadata_crossref

# ── Page config ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="RxScriptor · Literature Summarizer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_theme(mode="light")

NAVY   = COLOR["navy"]
RED    = COLOR["red"]
STEEL  = COLOR["steel"]
MUTED  = COLOR["muted"]
WHITE  = COLOR["white"]
BORDER = COLOR["border"]


# ── Claude summarization ─────────────────────────────────────────────
def summarize_with_claude(title: str, abstract: str, api_key: str, summary_type: str) -> str:
    prompts = {
        "structured": f"""You are a pharmaceutical researcher assistant specializing in DDS, CMC, and PK/PD.

Summarize the following paper in structured JSON format for a pharmaceutical researcher.

Title: {title}
Abstract: {abstract}

Respond ONLY in this JSON format:
{{
  "Background": "1-2 sentences on research context and problem",
  "Methods": "1-2 sentences on experimental approach",
  "Results": "2-3 sentences on key findings",
  "Implication": "1-2 sentences on significance for pharma R&D"
}}

Use Korean. Be concise and specific.""",

        "brief": f"""You are a pharmaceutical researcher assistant.

Read the following paper and write a 3-sentence Korean summary:
(1) what was done, (2) what was found, (3) why it matters for pharma R&D.

Title: {title}
Abstract: {abstract}

Output only the 3-sentence summary in Korean. No labels, no bullets.""",

        "commentary": f"""You are an experienced pharmaceutical researcher reviewing literature.

Write a brief Korean commentary:
1. 이 논문의 핵심 (1-2 sentences)
2. 내 연구(DDS, CMC, PK/PD)에 활용 가능한 포인트 (2-3 bullet points)
3. 한계점 또는 추가 확인 필요 사항 (1 sentence)

Title: {title}
Abstract: {abstract}""",
    }

    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompts[summary_type]}],
    )
    return msg.content[0].text


# ── Sidebar ──────────────────────────────────────────────────────────
with st.sidebar:
    show_mini_header()

    st.markdown(
        f"<p style='font-size:0.68rem;letter-spacing:0.15em;color:{MUTED};"
        f"text-transform:uppercase;margin-bottom:6px;'>Claude API Key</p>",
        unsafe_allow_html=True,
    )
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "") or st.text_input(
        "API Key", type="password", placeholder="sk-ant-...", label_visibility="collapsed"
    )

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:0.68rem;letter-spacing:0.15em;color:{MUTED};"
        f"text-transform:uppercase;margin-bottom:6px;'>Summary Mode</p>",
        unsafe_allow_html=True,
    )

    mode_labels = {
        "structured": "📋 Structured (B/M/R/I)",
        "brief":      "⚡ Brief (3-sentence)",
        "commentary": "💬 Commentary (연구 활용)",
    }
    selected_modes = [
        k for k, v in mode_labels.items()
        if st.checkbox(v, value=True, key=f"mode_{k}")
    ]

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:0.68rem;letter-spacing:0.15em;color:{MUTED};"
        f"text-transform:uppercase;margin-bottom:6px;'>History</p>",
        unsafe_allow_html=True,
    )
    if "history" not in st.session_state:
        st.session_state.history = []
    for h in reversed(st.session_state.history[-5:]):
        st.markdown(
            f"<p style='font-size:0.66rem;color:{MUTED};margin:3px 0;'>"
            f"· {h['title'][:38]}...</p>",
            unsafe_allow_html=True,
        )

# ── Main ─────────────────────────────────────────────────────────────
show_header(subtitle="Literature Summarizer")

section_title("input", "DOI 입력")

col_doi, col_btn = st.columns([5, 1])
with col_doi:
    doi_input = st.text_input(
        "DOI",
        placeholder="10.1016/j.jconrel.2023.01.001",
        label_visibility="collapsed",
    )
with col_btn:
    run_btn = st.button("Summarize →", type="primary", use_container_width=True)

st.markdown(
    f"<p style='font-size:0.66rem;color:{MUTED};margin-top:4px;'>"
    f"예시: 10.1016/j.jconrel.2022.04.048</p>",
    unsafe_allow_html=True,
)

# ── Run ──────────────────────────────────────────────────────────────
if run_btn:
    if not doi_input.strip():
        st.warning("DOI를 입력해주세요.")
    elif not api_key:
        st.warning("사이드바에서 Claude API Key를 입력해주세요.")
    elif not selected_modes:
        st.warning("Summary Mode를 하나 이상 선택해주세요.")
    else:
        with st.spinner("📡 Fetching metadata..."):
            meta = fetch_metadata_crossref(doi_input.strip())

        if "error" in meta:
            st.error(f"메타데이터 조회 실패: {meta['error']}")
        else:
            abstract = meta.get("abstract", "")
            if not abstract:
                with st.spinner("🔎 PubMed에서 abstract 조회 중..."):
                    abstract = fetch_abstract_pubmed(doi_input.strip())
            if not abstract:
                st.warning("Abstract를 찾을 수 없습니다.")
                abstract = "Abstract not available."

            # 논문 정보 카드
            section_title("paper", "논문 정보")
            st.markdown(f"""
            <div style='background:{WHITE};border:1px solid {BORDER};
                        border-left:3px solid {NAVY};border-radius:8px;
                        padding:20px 24px;margin-bottom:8px;
                        box-shadow:0 2px 8px rgba(26,46,90,.05);'>
              <p style='margin:0 0 6px;font-size:1rem;font-weight:600;
                        color:{NAVY};font-family:"Syne",sans-serif;'>{meta["title"]}</p>
              <p style='margin:0 0 4px;font-size:0.75rem;color:{MUTED};'>{meta["authors"]}</p>
              <p style='margin:0 0 8px;font-size:0.72rem;color:{STEEL};
                        letter-spacing:0.06em;'>{meta["journal"]} · {meta["year"]}</p>
              <a href='{meta["url"]}' target='_blank'
                 style='font-size:0.68rem;color:{RED};text-decoration:none;
                        letter-spacing:0.08em;'>DOI: {meta["doi"]} ↗</a>
            </div>
            """, unsafe_allow_html=True)

            with st.expander("Abstract 원문 보기"):
                st.markdown(
                    f"<p style='font-size:0.8rem;color:{MUTED};line-height:1.8;'>{abstract}</p>",
                    unsafe_allow_html=True,
                )

            st.session_state.history.append({"title": meta["title"], "doi": meta["doi"]})

            # 요약
            section_title("summary", "AI 요약")

            mode_titles = {
                "structured": ("📋 Structured Summary", "Background / Methods / Results / Implication"),
                "brief":      ("⚡ Brief Summary",      "핵심 3문장"),
                "commentary": ("💬 Commentary",         "내 연구 활용 포인트"),
            }

            for mode in selected_modes:
                title_str, sub_str = mode_titles[mode]
                with st.spinner(f"Generating {title_str}..."):
                    try:
                        result = summarize_with_claude(meta["title"], abstract, api_key, mode)

                        st.markdown(f"""
                        <p style='font-size:0.62rem;letter-spacing:0.2em;color:{RED};
                                  text-transform:uppercase;margin-bottom:4px;'>{sub_str}</p>
                        """, unsafe_allow_html=True)

                        if mode == "structured":
                            try:
                                data = json.loads(result)
                                cols = st.columns(2)
                                colors = [NAVY, RED, NAVY, RED]
                                for idx, (k, v) in enumerate(data.items()):
                                    with cols[idx % 2]:
                                        st.markdown(f"""
                                        <div style='background:{WHITE};border:1px solid {BORDER};
                                                    border-top:3px solid {colors[idx]};border-radius:8px;
                                                    padding:14px 16px;margin-bottom:12px;
                                                    box-shadow:0 1px 4px rgba(26,46,90,.04);'>
                                          <p style='margin:0 0 6px;font-size:0.62rem;
                                                    letter-spacing:0.18em;color:{colors[idx]};
                                                    text-transform:uppercase;'>{k}</p>
                                          <p style='margin:0;font-size:0.82rem;
                                                    color:{NAVY};line-height:1.75;'>{v}</p>
                                        </div>
                                        """, unsafe_allow_html=True)
                            except json.JSONDecodeError:
                                st.markdown(
                                    f"<div style='background:{WHITE};border:1px solid {BORDER};"
                                    f"border-left:3px solid {NAVY};border-radius:8px;padding:16px 20px;'>"
                                    f"<p style='margin:0;font-size:0.82rem;color:{NAVY};"
                                    f"line-height:1.8;white-space:pre-wrap;'>{result}</p></div>",
                                    unsafe_allow_html=True,
                                )
                        else:
                            st.markdown(
                                f"<div style='background:{WHITE};border:1px solid {BORDER};"
                                f"border-left:3px solid {RED};border-radius:8px;"
                                f"padding:16px 20px;margin-bottom:12px;'>"
                                f"<p style='margin:0;font-size:0.82rem;color:{NAVY};"
                                f"line-height:1.85;white-space:pre-wrap;'>{result}</p></div>",
                                unsafe_allow_html=True,
                            )
                        st.code(result, language=None)

                    except Exception as e:
                        st.error(f"{title_str} 생성 실패: {e}")

            section_title("tags", "Domain Tags")
            tag_badges(
                ["DDS", "CMC", "PK/PD", "Literature Review",
                 meta.get("journal", "")[:20], meta.get("year", "")],
                color="navy",
            )

show_footer()
