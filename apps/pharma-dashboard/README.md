# Pharma Dashboard

Google News RSS에서 FDA·EMA·DDS·Pharma Business 카테고리의 최신 뉴스를 모으고, Claude API로 주간 트렌드 요약과 기사별 요약을 생성하는 Streamlit 앱.

## 로컬 실행

repo 루트에서:

```bash
pip install -r apps/pharma-dashboard/requirements.txt
streamlit run apps/pharma-dashboard/app.py
```

`app.py` 상단에서 repo 루트를 `sys.path`에 추가하므로 `shared.*`, `apps._shared.*` import가 동작합니다.

## API Key

두 가지 중 택일:

1. **`.streamlit/secrets.toml`** (gitignored):
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
2. 실행 후 사이드바 "Claude API Key" 필드에 직접 입력.

AI 요약 기능(기사별/트렌드) 없이 뉴스 피드만 볼 경우 키는 선택 사항입니다.

## Streamlit Cloud 배포

- Main file path: `apps/pharma-dashboard/app.py`
- Advanced settings → Secrets 에 `ANTHROPIC_API_KEY` 등록
- Python requirements: `apps/pharma-dashboard/requirements.txt`

## 구조상 의존

- `shared/api/news.py` — Google News RSS fetcher (공용)
- `apps/_shared/rxscriptor_header.py` — Clinical White 브랜드 헤더 (Literature Summarizer와 공유)
- `design-systems/rxscript/tokens/rxscript-tokens.json` — 색상·폰트 단일 원천

## 카테고리 커스터마이즈

`app.py`의 `CATEGORIES` 딕셔너리에서 `queries` / `keywords`를 편집하거나, 사이드바의 **Custom Keyword** 필드에 임시 키워드(예: `GLP-1`, `ADC`)를 입력해 즉석 카테고리를 추가할 수 있습니다.
