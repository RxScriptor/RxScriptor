# Literature Summarizer

DOI → CrossRef/PubMed 메타데이터 조회 → Claude API 기반 3종 요약(Structured / Brief / Commentary) Streamlit 앱.

## 로컬 실행

repo 루트에서:

```bash
pip install -r apps/literature-summarizer/requirements.txt
streamlit run apps/literature-summarizer/app.py
```

`app.py` 상단에서 repo 루트를 `sys.path`에 추가하므로 `shared.*`, `apps._shared.*` import가 동작합니다.

## API Key

두 가지 중 택일:

1. **`.streamlit/secrets.toml`** (gitignored):
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
2. 실행 후 사이드바 "Claude API Key" 필드에 직접 입력.

## Streamlit Cloud 배포

- Main file path: `apps/literature-summarizer/app.py`
- Advanced settings → Secrets 에 `ANTHROPIC_API_KEY` 등록
- Python requirements: `apps/literature-summarizer/requirements.txt`

> Streamlit Cloud가 repo 루트를 작업 디렉터리로 두기 때문에 `sys.path` 주입이 그대로 동작합니다.

## 구조상 의존

- `shared/api/` — CrossRef / PubMed fetcher (repo 전역 공용)
- `apps/_shared/rxscriptor_header.py` — Clinical White 브랜드 헤더
- `design-systems/rxscript/tokens/rxscript-tokens.json` — 색상·폰트 단일 원천

토큰 JSON이 바뀌면 헤더/앱 UI가 자동 반영됩니다. CSS(`rxscript-tokens.css`)는 수동 동기화.
