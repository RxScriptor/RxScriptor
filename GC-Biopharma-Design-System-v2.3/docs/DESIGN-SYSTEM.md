# GC Biopharma Design System
## GC녹십자 통합 브랜드 & 발표자료 디자인 가이드

> **용도**: AI 에이전트(Claude, ChatGPT, Gemini 등) 및 개발자가 GC Biopharma(GC녹십자) 스타일의 발표자료·UI·브랜드 자산을 생성할 때 참조하는 단일 소스.
> **기반**: GC Brand Manual Book (Unified ver. 2026-03) + 2025 Investor Day / Alyglo® Business Update / 2024 4Q 경영실적 (공식 IR 3건)
> **버전**: v2.3 (2026-04-13) · 브랜드 매뉴얼 Unified + 실무 분기 + Track 구조화 + Freesentation 서체 + **가로형 Lockup & 심볼 단독 SVG 동봉**

### 문서 구조 · 2개 Track + Appendix

이 문서는 **역할별로 읽는 지점이 다르다**. 디자이너·마케터는 Designer Track만으로 90% 작업 가능하며, IR·RA·법무팀은 Compliance Track을 필수로 참조한다.

#### 🎨 Designer Track (§0–§11) — 시각 제작 필수
| # | 섹션 | 핵심 내용 | 주 사용자 |
|---|------|----------|----------|
| 0 | 브랜드 매뉴얼 원칙 | 심볼·비율·Clear Space·15종 오용 금지 | 전원 |
| 1 | 브랜드 정체성 | 슬로건·포지셔닝·Signature | 디자이너·마케터 |
| 2 | 컬러 시스템 | 공식 팔레트·웹 팔레트·확장·테마 3종 | 디자이너 |
| 3 | 타이포그래피 | Freesentation 9 Weights·타입 스케일 | 디자이너 |
| 4 | 가족사 & CI·BI | Lockup·CI·BI·파트너십 4유형 | 디자이너·법무 |
| 5 | 스페이싱 & 레이아웃 | 그리드·Radius·아키타입 | 디자이너 |
| 6 | 슬라이드 유형 | 커버부터 Closing 9종 | 디자이너·기획 |
| 7 | 컴포넌트 스펙 | Banner·Panel·Badge·Card 8종 | 디자이너·개발 |
| 8 | 픽토그램 | 공식 세트·FA 매핑 | 디자이너·개발 |
| 9 | Font Awesome | IR·디지털 전용 | 개발·디자이너 |
| 10 | Callout & AI | Notion 영감 컴포넌트 | 기획·개발 |
| 11 | 저작권 | 표기 규정 | 전원 |

#### ⚖️ Compliance Track (§12–§14) — IR·RA·법무 필수
| # | 섹션 | 핵심 내용 | 주 사용자 |
|---|------|----------|----------|
| **12** | **용도별 버전 분기** | 6유형 수신자별 분기 원칙 | IR·RA·법무·사업개발 |
| 13 | 디자인 가드레일 | Always / Never Do | 전원 (배포 전 체크) |
| 14 | AI 작성 지침 | 복붙용 프롬프트 | AI 협업 작성자 |

#### 📎 Appendix (§15–§17)
| # | 섹션 | 핵심 내용 |
|---|------|----------|
| 15 | 메시징 어휘 | 한·영 병기 (Regulatory 포함 28종) |
| 16 | 적용 매체 | Stationery·Corporate·Signage·Vehicle |
| 17 | Changelog | 개정 이력·마이그레이션 노트 |

---

## 0. 브랜드 매뉴얼 원칙 (최상위 규정)

> ⚠️ 본 섹션은 **GC Brand Manual Book Unified ver.**에서 직접 도출된 규정이며, 다른 모든 스타일 규정보다 우선한다. CI 변경 시 GC(지주사) 사용 승인, BI 개발 시 사전 검토·협의가 필수다.

### 0-1. 심볼마크 (Symbol Mark)

- **의미**: 레드(열정·도전의 역사) + 그린(건강·번영의 미래) 결합 — 전통과 혁신, 역사와 미래의 연결
- **로고타입 컬러**: Deep Blue — 정직·신뢰·전문성
- **비율**: 심볼 가로 길이가 세로보다 **1.01:1**로 약 1% 더 김 (구 녹십자 로고 계승)
- **단독 사용 금지**: 심볼만으로 로고 대체 불가. 공식 용도(보도자료·간판·IR 자료)는 반드시 로고타입(+심볼) 정식 로고 사용
- **그래픽 요소로서 심볼 단독** 사용은 장식 목적에 한해 허용

### 0-2. 로고 비율 & Clear Space

| 항목 | 규정 |
|------|------|
| 심볼 높이 기준 X | 8X (심볼 전체 높이) |
| 심볼 너비 | 8.08X |
| 심볼-로고타입 간격 | 1.7X |
| 로고타입("GC") 너비 | 8.8X, 높이 5.5X |
| Clear Space | 로고 사방 최소 **2X** 여백 확보 (권장 이상) |
| 최소 크기 (Print) | 높이 **7mm** |
| 최소 크기 (Screen) | 높이 **40px** |

### 0-3. 로고 컬러 4종 (공식)

| 타입 | 배경 | 용도 |
|------|------|------|
| **기본형 풀컬러** | 흰색/밝은 배경 | 공식 자료 기본 (마케팅·IR·패키징 필수) |
| **풀컬러 역상** | GC Deep Blue 배경 | 권장 역상 사용 |
| **단색 (Solid color)** | 밝은 배경 (그레이 0–40%) | 컬러 대비 미비, 단색 인쇄 환경 |
| **단색 역상** | 어두운 배경 (그레이 40–100%) | 모노 인쇄, 모바일 특수 환경 |

**공식 로고 파일** (본 배포본에 동봉):

| 파일명 | viewBox | 용도 |
|--------|---------|------|
| `gc_biopharma_vector_refined.svg` | `0 0 1000 161` | **가로형 Lockup** (심볼 + "GC" 워드마크) — 공식 자료 기본 |
| `gc_symbol_only.svg` | `0 0 372 161` | **심볼 단독** — 사이니지·배지·파비콘·모바일 UI 등 공간 제약 환경 |

> ⚠️ **사용 범위 준수 (§0-1 재확인)**: 심볼 단독 SVG는 **공식 용도(보도자료·간판·IR 자료 등 브랜드 대표성이 필요한 자료)에서는 단독 사용 금지**. 반드시 가로형 Lockup을 사용하고, 심볼 단독은 장식 요소·UI 아이콘·파비콘·연동 배지 등 **보조적 역할**에만 허용.

웹·HTML 슬라이드 삽입 예시:
```html
<!-- 공식 자료 기본 (가로형) -->
<img src="./gc_biopharma_vector_refined.svg" alt="GC Biopharma" style="height: 24px;" />

<!-- 공간 제약 시 심볼 단독 -->
<img src="./gc_symbol_only.svg" alt="GC" style="height: 32px; width: 32px;" />

<!-- 파비콘 -->
<link rel="icon" type="image/svg+xml" href="./gc_symbol_only.svg" />
```

**심볼 단독 SVG 권장 용도**:
- 파비콘 (브라우저 탭)
- 모바일 앱 아이콘·스플래시 스크린
- 배지·스티커·굿즈
- 슬라이드 **우상단 소형 워터마크** (브랜드 표식 용도)
- 소셜미디어 프로필 이미지
- UI 로딩 인디케이터

**심볼 단독 SVG 금지 용도**:
- 공식 로고 대체 (보도자료·IR·기업 홈페이지 헤더)
- 공식 서한·문서 레터헤드
- 간판·대형 사이니지 (반드시 워드마크 병기)
- CI 변경·BI 개발 자료

PPT·Keynote 삽입 시: SVG를 그대로 드래그 앤 드롭하거나, Illustrator에서 PDF 변환 후 삽입 권장 (EMF 변환 시 그라디언트 손실 주의).

### 0-4. 사용 금지 규정 (Incorrect Use)

다음 15종 오용은 **절대 금지**. CI 활용 모든 제작물은 GC 브랜드팀 사전 검수 필수.

| 분류 | 금지 사례 |
|------|-----------|
| 컬러 변형 | 임의컬러 변경 / 풀컬러 로고 1도 변형 / 임의 조합 |
| 형태 변형 | 비율 변경 / 회전 / 분리·재배치 / 윤곽선 적용 |
| 타이포 변형 | 임의 서체 사용 / 워드마크 변형 / 로고타입만 사용 |
| 효과 적용 | 그림자·효과 추가 / 심볼 그라데이션 단순화 |
| 배경 처리 | 유사 배경색 / 밝은 배경에 흰 로고 / 복잡한 배경 |
| 품질 저하 | 저화질 사용 |
| 기타 | 로고 내 텍스트 삽입 / 구 녹십자 로고 사용 |

---

## 1. 브랜드 정체성 & 비주얼 톤

- **회사명**: GC녹십자 / GC Biopharma (글로벌)
- **슬로건**: "Rise High, Reach Beyond"
- **포지셔닝**: Fully Integrated Value Chain 기반 글로벌 혈장분획제제·바이오파마 기업
- **Density**: Medium — 정보 밀도는 높되 절대 혼잡하지 않음
- **Mood**: Serious & Strategic. 장식적 요소 배제. Bold 타이포그래피 + 강한 색상 대비
- **Rhythm**: 2~3열 그리드. 비대칭은 위계(hierarchy) 표현에만 허용
- **Signature**: 모든 콘텐츠 슬라이드 최하단에 전체 폭 Deep Navy 배너(Takeaway Bar)

---

## 2. 컬러 시스템 (브랜드 매뉴얼 공식 팔레트)

### 2-1. 기본색 (Primary Colors) — Print/CMYK 기준

| 색상명 | HEX | RGB | CMYK | Pantone |
|--------|-----|-----|------|---------|
| **GC Red** | `#E4002B` | 228/0/43 | 0/100/90/0 | 185 C |
| **GC Yellow** | `#FFC845` | 255/200/69 | 0/18/76/0 | 1225 C |
| **GC Deep Green** | `#007A33` | 0/122/51 | 95/13/94/3 | 356 C |
| **GC Bright Green** | `#97D700` | 151/215/0 | 49/0/100/0 | 375 C |

### 2-2. 보조색 (Secondary Colors)

| 색상명 | HEX | RGB | CMYK | Pantone |
|--------|-----|-----|------|---------|
| **GC Mid Blue** | `#0072CE` | 0/114/206 | 90/48/0/0 | 285 C |
| **GC Light Blue** | `#00A9E0` | 0/169/224 | 83/0/0/0 | 2995 C |
| **GC Mid Green** | `#43B02A` | 67/176/42 | 77/0/100/0 | 361 C |
| **GC Gray** | `#9EA2A2` | 158/162/162 | 2.5/0/0/36.5 | 422 C |

### 2-3. 웹 전용 팔레트 (Gnet·G:ON·Hey GC·E-Solution Center)

> 화면 가독성을 위한 톤다운 그린 계열 — 인쇄물에 사용 금지

| 역할 | 색상명 | HEX | RGB |
|------|--------|-----|-----|
| 웹 Primary | GC Soft Green | `#60A57B` | 96/165/123 |
| 웹 Primary | GC Deep Green (Web) | `#145A50` | 20/90/80 |
| 웹 Primary | GC Warm Gray | `#F7F7F3` | 247/247/243 |
| 웹 Secondary | GC Soft Yellow | `#FFCB6E` | 255/203/110 |
| 웹 Secondary | GC Deep Red | `#BC4042` | 188/64/66 |

### 2-4. 확장 컬러 (IR 자료 전용, 브랜드 매뉴얼 외 적용)

| 역할 | HEX | 용도 |
|------|-----|------|
| **Deep Navy** | `#002B49` | IR 슬라이드 CTA 배너·섹션 헤더·Bold 강조 (로고타입 색과 별도 운용) |
| Panel Gray | `#E8E8E8` | 비교 데이터·구분선 |
| Warm Beige | `#F0EDE8` | 섹션 구분 슬라이드 배경 |
| Off-Black | `#1A1A1A` | 본문 텍스트 |

### 2-5. 그라디언트 (GC Gradient)

GC 로고 컬러 기반으로 추출 — 브랜드 핵심 이미지 유지하면서 생동감 표현.

- **구성**: GC Bright Green(`#97D700`) → GC Yellow(`#FFC845`) → GC Red(`#E4002B`) 흐름
- **용도**: 커버 슬라이드, 이미지월, 엑스배너·현수막 (그라디언트형)
- ⚠️ **브랜드팀 디자인 검수 필수** — 임의 적용 금지

### 2-6. Semantic 컬러 규칙 (IR·데이터 시각화)

| 상황 | 컬러 |
|------|------|
| 현재·핵심 데이터, 강조 | `#002B49` Deep Navy |
| 과거·비교·기준선 | `#E8E8E8` |
| 성장률 배지 (+XX%) | `#0072CE` 원형 |
| 예측·목표 | `#0072CE` 바 + 점선 |
| 승인·달성 마일스톤 | `#0072CE` filled |
| 개발 중 파이프라인 | `#002B49` filled |
| 초기 단계 파이프라인 | `#7aabcf` muted |
| 음수·손실 | 괄호 표기 `(386)` |

### 2-7. 목적별 테마 (슬라이드 단위, 혼용 금지)

#### 테마 1 — Trust & Baseline
`#002B49` · `#0072CE` · `#00A9E0` — Literature review / PK·PD Profile / Control group

#### 테마 2 — Contrast & Efficacy
Control `#007A33` · Treatment `#E4002B` · Attention `#FFC845` — in vivo / 통계 유의성 / AE
> ⚠️ 재무 IR 슬라이드 메인 사용 금지

#### 테마 3 — Formulation & MoA
배경 `#002B49` + 제형 `#97D700` + Payload `#43B02A` — DDS 제형·세포 내 전달

---

## 3. 타이포그래피

### 3-1. 공식 전용서체 — Freesentation (9 Weights)

| Weight | 파일명 | 용도 |
|--------|--------|------|
| **Freesentation 9 Black** | `Freesentation-9Black.ttf` | 간판·현수막 등 사인용 (구 GC 150 대체) |
| **Freesentation 8 ExtraBold** | `Freesentation-8ExtraBold.ttf` | 초대형 타이틀·커버 |
| **Freesentation 7 Bold** | `Freesentation-7Bold.ttf` | 제목용 (대/소제목), **가족사 로고 전용** (구 GC 140 대체) |
| **Freesentation 6 SemiBold** | `Freesentation-6SemiBold.ttf` | 주목성·가시성 우수 — 제목·서브 본문 (구 GC 130 대체) |
| **Freesentation 5 Medium** | `Freesentation-5Medium.ttf` | 본문 강조·badge 라벨 |
| **Freesentation 4 Regular** | `Freesentation-4Regular.ttf` | **본문 텍스트 기본** (구 GC 120 대체) |
| **Freesentation 3 Light** | `Freesentation-3Light.ttf` | 주목성 낮추고 싶을 때 (구 GC 110 대체) |
| **Freesentation 2 ExtraLight** | `Freesentation-2ExtraLight.ttf` | 디스플레이·장식 캡션 |
| **Freesentation 1 Thin** | `Freesentation-1Thin.ttf` | 초경량 액센트 (인쇄 최소 10pt 이상) |

> **CSS `font-weight` 매핑**: Thin=100 · ExtraLight=200 · Light=300 · Regular=400 · Medium=500 · SemiBold=600 · Bold=700 · ExtraBold=800 · Black=900

**웹 Fallback**: `'Freesentation', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif`
**영문**: Freesentation 영문 글리프 → Fallback: Calibri, Arial
**최대 2개 폰트 패밀리** 운용 (Freesentation + 숫자용 등만)

### 3-2. 타입 스케일

| Token | Size | Weight | Line-H | Letter-S | Role |
|-------|------|--------|--------|----------|------|
| `type.cover.title` | 36px | 900 (Black) | 1.15 | −0.5 | 커버 메인 타이틀 |
| `type.cover.subtitle` | 16px | 400 (Regular) | 1.4 | +0.5 | 커버 서브 (영문) |
| `type.cover.eyebrow` | 10px | 300 (Light) | 1.0 | +3 | 날짜·브랜드명 |
| `type.section.number` | 64px | 900 (Black) | 1.0 | −2 | 섹션 번호 |
| `type.section.title` | 28px | 700 (Bold) | 1.2 | −0.5 | 섹션 제목 |
| `type.slide.title` | 17–20px | 700 (Bold) | 1.25 | −0.3 | 콘텐츠 슬라이드 제목 |
| `type.panel.header` | 11px | 600 (SemiBold) | 1.3 | +0.2 | 패널 헤더 |
| `type.body.default` | 9–10px | 400 (Regular) | 1.7 | 0 | 본문 |
| `type.body.strong` | 9–10px | 700 (Bold) | 1.7 | 0 | 본문 강조 |
| `type.caption` | 7–8px | 300 (Light) | 1.6 | 0 | 차트·각주 |
| `type.banner` | 10–12px | 700 (Bold) | 1.2 | +0.1 | Bottom Banner |
| `type.eyebrow` | 8–9px | 600 (SemiBold) | 1.0 | +1.5 | 섹션 레이블 ALL CAPS |

### 3-3. 텍스트 스타일 규칙

- **섹션 레이블**: ALL CAPS, `#BBBBBB`, `#0072CE` 하단 밑줄
- **한국어·영어 병기**: 전략 키워드는 영어 원문, 내러티브는 한국어
- **가족사 로고 표기**: Freesentation Bold (w700) / Title Case / Tracking −40 / GC Deep Blue (예: `GC Genome`)

### 3-4. @font-face 선언 템플릿 (웹 구현용)

```css
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-1Thin.ttf') format('truetype'); font-weight: 100; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-2ExtraLight.ttf') format('truetype'); font-weight: 200; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-3Light.ttf') format('truetype'); font-weight: 300; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-4Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-5Medium.ttf') format('truetype'); font-weight: 500; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-6SemiBold.ttf') format('truetype'); font-weight: 600; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-7Bold.ttf') format('truetype'); font-weight: 700; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-8ExtraBold.ttf') format('truetype'); font-weight: 800; font-style: normal; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./Freesentation-9Black.ttf') format('truetype'); font-weight: 900; font-style: normal; font-display: swap; }
```

---

## 4. 가족사 로고 & CI·BI 제작 규정

### 4-1. 가족사 로고 (Lockup)

| 요소 | 규정 |
|------|------|
| 심볼 너비 | 8.7X |
| 가로형 우측 여백 | 2X |
| 글꼴 | **Freesentation Bold (w700)** |
| 표기법 | 각 단어 첫 글자 대문자 (Title Case) |
| Tracking | **−40** |
| 컬러 | **GC Deep Blue** |
| 예시 | `GC Genome`, `GC녹십자`, `GC녹십자웰빙`, `GC Biopharma` |

### 4-2. GC 조합형 CI (법인 아이덴티티)

- ✅ Freesentation Bold (w700) 사용
- ✅ GC 심볼 사용
- ✅ GC + 법인명 **띄어쓰기**
- 예: `+ GC 녹십자`, `+ GC Biopharma`
- ⚠️ CI 변경 시 GC(지주사) **사용승인 필요**

### 4-3. GC 조합형 BI (제품·서비스 아이덴티티)

- ❌ Freesentation Bold **사용 금지** (별도 서체 사용)
- ❌ GC 심볼 **사용 금지**
- ❌ GC + 브랜드명 **띄어쓰기 금지**
- 예: `GCFLU` (붙여쓰기, 별도 서체)
- ⚠️ BI 개발 시 GC(지주사) **사전 검토·협의 필요**

### 4-4. 파트너십 표기

| 관계 | 표기 |
|------|------|
| 제휴 협업 | `+ GC & PARTNER` 또는 `+ GC × PARTNER` |
| 지점·지역 | `+ GC녹십자아이메드 ǀ 강남의원` (세로 구분선) |
| 보증·후원 | `Powered by + GC Biopharma` |

---

## 5. 스페이싱 & 레이아웃

### 5-1. 그리드 시스템

- 표준 슬라이드: 좌우 22–24px / 상단 13–14px 패딩
- 콘텐츠 패널 간격: 10–12px gap / 패널 내부 10–14px
- Bottom Banner: Full bleed, 상하 9–10px · 좌우 22px

### 5-2. 스페이싱 스케일

| Token | Size | 적용 |
|-------|------|------|
| xs | 3–4px | 아이콘 gap, 배지 패딩 |
| sm | 6–8px | 리스트 항목, 차트 라벨 |
| md | 10–14px | 패널 내부·간격 |
| lg | 20–24px | 슬라이드 엣지 |
| xl | 36–48px | 섹션 구분 |

### 5-3. Border Radius

| 요소 | 값 |
|------|----|
| 패널·카드 | 7–8px |
| 버튼·배지 | 5–6px |
| 진행 바 | 3px |
| Bottom Banner | 0px |

### 5-4. 레이아웃 아키타입

| 유형 | 설명 |
|------|------|
| 2-column split | 동등한 두 패널, 각각 헤더 바 |
| 3-column grid | Key Takeaways·수치·파이프라인 |
| 4-column nav | 목차·섹션 네비게이션 |
| Full-bleed image | 배경 이미지(불투명도 7–10%) + 중앙 콘텐츠 |
| Timeline row | 카테고리 행 × 임상 단계 열 |

---

## 6. 슬라이드 유형 시스템

| 유형 | 배경 | 핵심 특징 |
|------|------|-----------|
| **커버** | Brand Gradient → `#002B49` | 중앙 대형 타이틀, 우상단 GC 로고(풀컬러), 날짜 하단 |
| **섹션 구분** | `#F0EDE8` Warm Beige | 대형 페이드 섹션 번호, Navy 액센트 바, 하단 4열 네비게이션 |
| **콘텐츠 (2-col)** | White | 좌상단 섹션 레이블, 2개 패널, Bottom Banner |
| **전략 시리즈** | White | ① ② ③ 번호 타이틀, `#002B49` 헤더 바 |
| **수치 하이라이트** | White | 3열 그리드, 대형 숫자 Navy |
| **파이프라인** | White | 행(카테고리) × 열(임상단계) |
| **Key Takeaways** | White | 3개 Navy/Blue 카드, Bottom Banner |
| **재무 테이블** | White | `#002B49` 헤더 행, 음수 `(386)` |
| **Closing** | White / Gradient | 타이틀·태그라인 중앙 정렬, 로고 |

---

## 7. 컴포넌트 스펙

### 7-1. Bottom Takeaway Banner *(필수)*

```
Background:  #002B49
Text:        white, Freesentation w700, 10–12px
Padding:     9–10px vertical / 22px horizontal
Layout:      space-between — 메시지(좌) | 페이지(우, rgba(255,255,255,0.35))
```

**메시지 패턴**: `"[수단/기반] 기반 [목표/결과]"`
예: `"자체 LNP 플랫폼 기반 mRNA·희귀질환 분야 글로벌 DDS 기업으로 도약"`

### 7-2. Content Panel

```
Border:          1.5px solid #E8E8E8
Border-radius:   7–8px
Header bar:      #002B49 or #0072CE / white / Freesentation w600 / 7–8px padding
Body:            10–14px padding / white (#FAFAFA alternate)
```

### 7-3. Section Label (좌상단)

```
Font:           Freesentation w600, 8–9px
Color:          #BBBBBB
Letter-spacing: 1.5px / uppercase
Border-bottom:  2px solid #0072CE / padding-bottom 3px
```

### 7-4. Growth Badge

```
Background:    #0072CE / white text
Font:          Freesentation w700, 6–8px
Padding:       1–2px 4–5px / Border-radius: 8–10px
Content:       "+XX%" / Position: absolute 차트 바 우상단
```

### 7-5. Progress / Data Bar

```
Track:    #E8E8E8 / radius 3px / height 6–8px
Fill:     #002B49 (primary) or #0072CE
Label:    Freesentation w600, 8–9px
```

### 7-6. Pipeline Row

```
Category:  width 88–90px / Freesentation w600, 8–9px / #002B49
Stage:     #002B49 bg / white / Freesentation w600, 8–9px / radius 좌우 5px
Track:     #F0F7FF / 1px #E8E8E8 / height 34px
Item bar:  height 40% / radius 3px
```

### 7-7. Section Nav Footer

```
Border-top:  1px solid #E8E8E8 / 4 equal columns
Active:      #002B49 bg / white / Freesentation w700
Inactive:    white bg / #BBBBBB / Freesentation w400
Font:        9–10px / padding 9px vertical
```

### 7-8. Key Takeaways Card

```
Background:  #002B49 or #0072CE
Border-radius: 8px / Padding: 14–16px
Icon:        fa-solid fa-xl, white, centered top
Title:       white / Freesentation w700 / 10–12px / centered
             border-bottom: 1px solid rgba(255,255,255,0.2)
Items:       Freesentation w400 / 8–9px / white / line-height 1.5–1.6
             prefix: fa-check fa-xs, rgba(255,255,255,0.5)
```

---

## 8. 픽토그램 시스템 *(브랜드 매뉴얼 신규 반영)*

GC 공식 픽토그램은 **선형(Line), 균일한 획 두께, 흑색(`#1A1A1A` 또는 `#002B49`)** 기본. 사이즈·위치는 환경에 따라 조정 가능하나 **형태 변경 금지**.

### 8-1. 공식 픽토그램 세트 (브랜드 매뉴얼 수록)

| 카테고리 | 항목 |
|----------|------|
| **인물·접근성** | 휠체어 사용자 / 남녀 / 임산부 / 유아동반 |
| **시설** | 엘리베이터 (상하) / 화물엘리베이터 / 샤워실 / 숙박·베드 |
| **업무** | 상담·컨설팅 / 회의실 / 프레젠테이션 |
| **방향·이동** | 대각선 화살표(↗ ↘) / 직선 화살표(→) / 계단 (2F→1F) / 에스컬레이터 |

### 8-2. 사용 규정

| 항목 | 규정 |
|------|------|
| 획 두께 | 균일 (굵기 유지, 임의 변경 금지) |
| 기본 색상 | `#1A1A1A` 또는 `#002B49` |
| 역상 배경 | 흰색 (어두운 배경 위) |
| 크기 조정 | 비례 유지, 최소 16px (web) / 7mm (print) |
| 조합 사용 | 동일 슬라이드 내 **픽토그램과 Font Awesome 혼용 금지** |
| 금지 | 그림자·그라디언트·색상 변형 / 장식적 왜곡 |

### 8-3. 디지털 대응 (Font Awesome 매핑)

브랜드 매뉴얼 픽토그램을 웹에서 구현 시 가장 근접한 **Font Awesome 6 Solid** 대체:

| 공식 픽토그램 | FA 대체 |
|---------------|---------|
| 휠체어 접근 | `fa-wheelchair` |
| 남녀 화장실 | `fa-restroom` |
| 엘리베이터 | `fa-elevator` |
| 회의실 | `fa-people-group` |
| 프레젠테이션 | `fa-chalkboard-user` |
| 임산부 | `fa-person-pregnant` |
| 상담 | `fa-handshake` |
| 숙박 | `fa-bed` |
| 계단 | `fa-stairs` |
| 에스컬레이터 | `fa-staircase` (or 커스텀) |

> 공식 인쇄물·사이니지는 **GC 원본 픽토그램 SVG** 사용 필수. FA는 디지털 UI 보조용.

---

## 9. Font Awesome 6 아이콘 (IR·디지털 전용)

**CDN**:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
```

| 컴포넌트 | FA 클래스 | 크기 |
|----------|-----------|------|
| Callout insight | `fa-lightbulb` | fa-xs |
| Callout strategy | `fa-wand-magic-sparkles` | fa-xs |
| Callout warning | `fa-triangle-exclamation` | fa-xs |
| Callout data | `fa-chart-bar` | fa-xs |
| Key Takeaways — R&D | `fa-microscope` | fa-xl |
| Key Takeaways — Global | `fa-globe` | fa-xl |
| Key Takeaways — Finance | `fa-arrow-trend-up` | fa-xl |
| AI Badge | `fa-wand-magic-sparkles` | 8px |
| 체크리스트 | `fa-check` | fa-xs |
| Toggle | `fa-chevron-right` | fa-xs |
| 파이프라인 혈장분획 | `fa-droplet` | fa-sm |
| 파이프라인 희귀질환 | `fa-dna` | fa-sm |
| 파이프라인 mRNA/LNP | `fa-syringe` | fa-sm |

**금지**: 장식 아이콘(`fa-star`, `fa-heart`) / 동일 슬라이드 3종 이상 혼용 / Brands 아이콘

---

## 10. Callout & Notion AI 영감 컴포넌트

### 10-1. Callout Block (패널당 1개)

```
Border-left:  3px solid (variant)
Border-radius: 5px / Padding: 7–9px
```

| Variant | 아이콘 | 색상 | 배경 | 용도 |
|---------|--------|------|------|------|
| insight | `fa-lightbulb` | `#0072CE` | `#F0F6FF` | 시장·인사이트 |
| strategy | `fa-wand-magic-sparkles` | `#002B49` | `#F0F4F8` | 전략 방향 |
| warning | `fa-triangle-exclamation` | `#E8A000` | `#FFFBF0` | 리스크 |
| data | `fa-chart-bar` | `#0072CE` | `#F0F6FF` | 수치 근거 |

### 10-2. AI Insight Badge

확정 재무 수치 병기 **금지**. 예측·추정·AI 생성 데이터 전용.

```html
<span style="background:linear-gradient(135deg,#002B49,#0072CE);
             color:white; border-radius:999px; padding:2px 7px;
             font-size:7px; font-weight:700;">
  <i class="fa-solid fa-wand-magic-sparkles"></i> AI 분석
</span>
```

---

## 11. 저작권 표기 (Copyright Notice)

브랜드 매뉴얼 공식 표기 규정:

```
© 2026 GC Corp. All Rights Reserved.
```

| 항목 | 규정 |
|------|------|
| 적용 대상 | 문서·웹페이지·인쇄물 등 **완성된 콘텐츠** |
| 미적용 | 제품 패키지, 단기·소모성 제작물, **로고 자체** |
| 사이즈 | 본문 대비 **0.7배 이하** |
| Clear Space | 문구 높이(1X) 기준 **최소 1X 여백** |
| 빈도 | 하나의 콘텐츠 내 **1회 표기 원칙** |

---

> ⚖️ **COMPLIANCE TRACK 진입** — 이하 §12–§14는 IR·RA·법무·사업개발 팀 필수 참조. 디자이너·마케터는 §13 가드레일만 체크하면 됩니다.

## 12. 용도별 슬라이드 버전 분기 원칙 *(실무 대응)*

> 같은 데이터라도 **수신자(audience)와 제출 목적**에 따라 슬라이드 표현 수준이 달라져야 한다. 아래 7개 유형으로 버전을 구분해 작성한다.

### 12-1. 슬라이드 용도 매트릭스 (7 Audience Types)

| 용도 | 핵심 수신자 | 표현 톤 | 특이 요구사항 |
|------|-------------|---------|---------------|
| **IR / Investor** | 애널리스트·기관투자자 | 기회·성과 강조, 간결 | Safe Harbor 필수 / 공시된 수치만 / 경쟁사 실명 주의 |
| **Analyst Day** | 섹터 전문 애널리스트 | 전략·경쟁우위 상세 | 경쟁 matrix 가능, 단 **가치판단 형용사 최소화** |
| **Regulatory** | FDA·EMA·MFDS | 객관·정량·투명 | 가치판단 형용사 **전면 금지**, ICH 가이드라인 인용 |
| **Internal / C-level** | 경영진·이사회 | 의사결정 촉진 | 민감도·리스크 솔직 기술, `CONFIDENTIAL` 워터마크 |
| **Academic / KOL** | 학계·임상의·학회 | 근거·메커니즘 중심 | 저자명·저널 정확 인용, 인용일자 명시 |
| **BD / Licensing** ⭐ | 제휴 대상사·기술이전 파트너 | 플랫폼 가치 전달 | NDA 체결 전후 2단계 / Teaser vs Full Deck 구분 |
| **Government Grant** ⭐ | 과기부·복지부·KDDF 등 | 공익성·국가전략 정합성 | 정부 R&D 지원 로고 병기, **국책과제 번호** 포함 |
| **Data Room (VDD)** ⭐ | DD 실사 팀·투자자문사 | 검증 가능·출처 명시 | 모든 수치 출처 파일·라인 번호 레퍼런스, 재무·비재무 분리 |

> ⭐ 는 v2.1에서 신규 추가된 유형. 조직·업무 특성에 따라 추가 커스텀 유형 정의 가능 (§17 Changelog 참조).

### 12-2. 경쟁 제품 비교표(Comparison Matrix) 분기 규칙

앞서 예시한 Competitive Matrix 슬라이드의 실무 비판 반영:

| 요소 | IR / Analyst Day | Regulatory Submission | BD / Licensing |
|------|------------------|------------------------|-----------------|
| 자사 열 색상 강조 | ✅ `#0072CE` 헤더 허용 | ❌ 모든 열 동일 `#002B49` | ✅ 강조 허용 |
| 가치판단 형용사 | ⚠️ 근거 각주 병기 시 허용 | ❌ 전면 금지 | ⚠️ 플랫폼 장점 강조 허용 |
| Semantic color (Low/Med/High) | ✅ 허용 | ⚠️ 객관 기준(수치 범위) 병기 필수 | ✅ 허용 |
| 경쟁사 실명 | ⚠️ 공개 정보만 | ✅ 공식 인용 출처와 함께 | ⚠️ NDA 이후만 |
| 출처 각주 | "as of [date]" | 각 셀별 reference number 필수 | 각 셀 1차 출처 |

### 12-3. 미래 예측 수치(Forward-Looking) 취급 규칙

| 수치 유형 | 표기 예 | 필수 조치 |
|----------|---------|----------|
| 확정 재무 | ₩1.87T (FY2025) | 출처 없음 허용 |
| 가이던스 | ₩2.1T (2026E) | `E` suffix + Safe Harbor 링크 |
| 장기 목표 | $680M peak sales 2030E | `E` suffix + **민감도 ±% 명시** |
| 마일스톤 | IND Q3 2026 | `target` 명시 + "subject to regulatory review" |
| AI 추정 | — | **AI Insight Badge** 필수, 확정 수치 옆 배치 금지 |

> 앞서 제시한 Timeline 슬라이드의 "IND '27", "BLA '30" 등은 모두 `target` 표기 + Safe Harbor 슬라이드 cross-reference 필요.

### 12-4. Market Sizing 신뢰도 가드

TAM/SAM/SOM 슬라이드는 **penetration 가정**이 가장 큰 변동 요인.

| 항목 | 규칙 |
|------|------|
| Penetration 가정 | 명시적으로 기재 (예: "16% penetration 가정") |
| First-in-class vs me-too | 차별 적용 — me-too는 penetration **5–10% 보수적** 상한 |
| 민감도 분석 | ±30% 범위 Warning Callout 필수 |
| 출처 | EvaluatePharma·IQVIA·GlobalData 등 **1차 DB** 명시, 자체 추정은 `company estimates` 분리 표기 |
| 환율 | 기준 환율·기준일 명시 (예: "USD/KRW 1,350 기준, 2026-01-01") |

### 12-5. Risk-Benefit 슬라이드 버전 분기

| 목적 | Risk 등급 표기 수위 |
|------|---------------------|
| **FDA Type B / Pre-IND** | 발견된 **모든 리스크** HIGH 등급도 정직하게 표기 + Mitigation 병기 (위 예시 §16 수준) |
| **IR / Analyst Day** | 동일 리스크 유지하되 **Mitigation 강조 비중 확대** (문장 길이 1.5배) |
| **BD / Licensing (post-NDA)** | Regulatory 수준과 동일하게 HIGH 리스크까지 정직 표기 — 사후 분쟁 방지 |
| **Data Room (VDD)** | Regulatory 수준 + **각 리스크 근거 파일 레퍼런스** (예: AE 리스트 Excel 시트 링크) |
| **Press Release / 보도자료** | Risk-Benefit 슬라이드 자체를 **공개 자료에 포함하지 않음** — 승인 사실·benefit만 발췌 |

### 12-6. Literature Review 인용 무결성

- **인용일자 명시**: `Cited 3,240 (Google Scholar, as of YYYY-MM-DD)` — 월 단위 변동성 반영
- **직접 인용(Direct Quote) 금지**: 논문 원문을 옮겨 쓸 때 자체 해석·문구로 재작성 (저작권 준수)
- **출처 계층**: 1차 문헌(논문) > 리뷰(review) > 뉴스·블로그 순, IR 자료에는 **1차·리뷰만 사용**
- **학회 초록(Abstract only)** 인용 시 `(Abstract, ASH 2024)` 등 단계 명시

### 12-7. 스케일업·CQA 데이터 버전 분기

CMC 슬라이드의 **동일한 공정 다이어그램**이라도 버전 달리해야 함.

| 수신자 | 표기 범위 |
|--------|----------|
| IR·전략 | Scale size만 (10mL → 200L), 공정명 수준 (Microfluidic 등) — **본 매뉴얼 §5-9 예시 수준** |
| Regulatory (ICH Q11) | 추가 필수: Batch size · Hold time · In-process control matrix · **Design Space 정의** |
| CDMO 파트너 공유 | Regulatory 버전 + **공정 파라미터 범위** (Flow rate, N/P ratio 등) |
| 공개 학술 발표 | IR 버전 + **NDA 체결 후** 일부 공정 파라미터 disclosure |

### 12-8. Executive Summary 밀도 보강 체크리스트

C-level 1-pager는 단순 KPI 나열로는 부족. 다음 요소 중 **최소 3개** 포함 권장:

- ✅ Stock price · Market cap 스냅샷
- ✅ Analyst consensus (Buy/Hold/Sell 비중·목표주가)
- ✅ Next catalyst (임박한 마일스톤 1–2건)
- ✅ Peer multiple 비교 (P/E, EV/EBITDA)
- ✅ Cash runway (monthly burn 기반 개월수)
- ✅ Open risks (Top 3 red flag, 1줄 요약)

### 12-9. Safe Harbor 법적 기반 병기

한국 기업의 글로벌 IR 자료는 **양 법역 병기**가 안전.

```
Safe Harbor Basis (권장 병기)
- Private Securities Litigation Reform Act of 1995 (US)
- 자본시장과 금융투자업에 관한 법률 제178조 (KR)
- 공정공시 의무 (한국거래소 공시규정 제7조)
```

모든 Forward-Looking 슬라이드는 마지막 슬라이드(Safe Harbor)로 **cross-reference 주석** 또는 각주 `(see Disclaimer, p.32)` 필수.

### 12-10. Emoji → Font Awesome 치환 대응

Key Takeaways 카드에서 편의상 emoji를 사용한 경우(🔬 🌐 📈), **공식 배포 전 반드시** 치환:

| 사용 Emoji | 대체 Font Awesome |
|-----------|-------------------|
| 🔬 | `fa-microscope` |
| 🌐 | `fa-globe` |
| 📈 | `fa-arrow-trend-up` |
| 💊 | `fa-pills` |
| 🧬 | `fa-dna` |
| 💉 | `fa-syringe` |
| 🏭 | `fa-industry` |
| 🤝 | `fa-handshake` |

> **Never Do**: 공식 IR·Regulatory·공시용 슬라이드에 emoji 존치 (§13 가드레일에서도 재확인).

---

## 13. 디자인 가드레일

### Always Do ✓

- 모든 콘텐츠 슬라이드 하단에 Bottom Banner
- 로고는 **풀컬러 우선**, Clear Space 2X 이상, 최소 크기(7mm/40px) 준수
- 강조색 `#002B49` 우선 (Red는 테마 2 in vivo·유의성 전용)
- 보조 강조·성장 지표에 `#0072CE`
- 전략 키워드 영어 병기, ① ② ③ 번호
- 음수 재무 괄호 표기 `(386)`
- 모든 슬라이드에 GC 로고 + 페이지 번호
- 핵심 수치·제목: Freesentation Bold (font-weight 700)
- 수치·연도 없는 전망 문구 금지
- 가족사 로고: Freesentation Bold (w700) + Title Case + Tracking −40 + Deep Blue
- 저작권 표기: `© 2026 GC Corp. All Rights Reserved.` (본문 0.7X, 콘텐츠당 1회)
- **용도별 버전 분기**: IR·Regulatory·Internal·Academic 수신자별 슬라이드 별도 작성 (§12-1)
- Forward-Looking 수치에 `E` suffix + Safe Harbor cross-reference
- Market Sizing penetration 가정 명시 + 민감도 ±% 병기
- Literature 인용에 **인용일자** 각주 (`as of YYYY-MM-DD`)
- Risk-Benefit 슬라이드는 수신자에 따라 **HIGH 리스크 표기 수위** 조정
- Emoji는 **초안용**, 배포 전 Font Awesome으로 치환 (§12-10 매핑 표)
- Executive Summary: KPI 외 Catalyst·Consensus·Risk 중 최소 3개 포함 (§12-8)

### Never Do ✗

- 로고 임의 변형 (컬러·비율·회전·효과·윤곽선 등 15종 오용)
- 심볼 단독으로 공식 로고 대체
- 구 녹십자 로고 사용
- CI와 BI 혼동 (BI에 GC 심볼·Freesentation Bold·띄어쓰기 사용)
- 콘텐츠 슬라이드 Bottom Banner 미삽입
- 빨간색·오렌지색을 일반 강조에 사용
- 테마 2(Red·Green)를 IR 재무 메인에 사용
- 슬라이드당 패널 5개 이상
- 공식 IR에 이모지 / 장식 아이콘
- AI Badge를 확정 재무 수치 옆에 배치
- 3개 이상 테마 혼용
- 그라디언트 임의 적용 (브랜드팀 검수 필수)
- 공식 픽토그램과 Font Awesome 동일 슬라이드 혼용
- **Regulatory 제출 자료**에 가치판단 형용사 ("우수한", "업계 최고", "Platform ready" 등)
- **공개 IR 자료**에 미공시 파트너십 실명 (공시 전 NDA 위반 리스크)
- Forward-Looking 수치에 `E` suffix 또는 Safe Harbor 참조 누락
- Literature 인용일자 없는 citation 수치 (`Cited 3,240` 단독 사용)
- Emoji 존치 상태로 공식 IR·Regulatory·공시 자료 배포 (§12-10)
- 공개 자료에 Risk-Benefit 슬라이드의 HIGH risk 등급 그대로 노출 (§12-5)
- TAM/SAM/SOM에서 민감도 분석 없이 단일 숫자만 제시
- 경쟁 Comparison Matrix에서 자사 컬럼에만 semantic color hyping 적용 (Regulatory용)

---

## 14. AI 작성 지침 (복사·붙여넣기용)

```
GC Biopharma (GC녹십자) IR 스타일로 발표자료를 작성하라.
기반: GC Brand Manual Book Unified ver. 2026-03

[필수 선행 질의] ← 작성 전 반드시 확인
- 수신자: IR / Analyst Day / Regulatory / Internal / Academic 중 무엇인가?
- 공시 상태: 기재할 수치·파트너십이 공시된 정보인가 NDA 대상인가?
- 시점 기준일: "as of YYYY-MM-DD" 명시할 날짜

[필수 규칙]
1. 로고: 풀컬러 기본, Clear Space 2X, 최소 7mm(print)/40px(screen)
2. 가족사 로고 표기: "GC [법인명]" 형태, Freesentation Bold (w700), Title Case, Tracking -40, #002B49
3. 모든 콘텐츠 슬라이드 하단 #002B49 배너 — "[수단] 기반 [목표]" 패턴
4. 슬라이드 제목: Freesentation Bold (w700), #002B49
5. 핵심 수치: #002B49 / 비교: #E8E8E8
6. 성장률 배지: #0072CE 원형, "+XX%"
7. 전략 연번: ① ② ③
8. 한·영 병기: Value Chain / Ramp-up / Pipeline / Phase I~III
9. 음수: 괄호 (386) — 마이너스 기호 금지
10. 패널: 헤더 바(#002B49 or #0072CE), radius 7–8px
11. 아이콘: FA 6 Solid (insight→fa-lightbulb / strategy→fa-wand-magic-sparkles
    warning→fa-triangle-exclamation / data→fa-chart-bar)
12. 리스트: ✓ 또는 fa-check
13. 테마 선택 (슬라이드 단위 통일):
    - Trust & Baseline: #002B49·#0072CE·#00A9E0
    - Contrast & Efficacy: #007A33·#E4002B·#FFC845 (in vivo·AE만)
    - Formulation & MoA: Navy 배경 + #97D700·#43B02A
14. 저작권: © 2026 GC Corp. All Rights Reserved. (콘텐츠당 1회)
15. Forward-Looking 수치: `E` suffix + Safe Harbor cross-ref
16. Literature citation: "Cited NNNN (source, as of date)" 형식
17. TAM/SAM/SOM: penetration 가정 + 민감도 ±% 병기
18. Emoji 초안 사용 허용, 배포 전 FA로 치환 (§12-10)

[수신자별 분기]
- IR: Safe Harbor 필수 / 공시 정보만 / 경쟁사 공개 정보만
- Analyst Day: 경쟁 matrix 상세 허용, 가치판단 형용사 최소화
- Regulatory: 가치판단 형용사 금지 / 정량만 / ICH 인용
- Internal: CONFIDENTIAL 배지 / 리스크 솔직 / 민감도 포함
- Academic: 1차 문헌 우선 / 저자·저널 정확 인용
- BD / Licensing: NDA 전/후 2단계 (Teaser vs Full Deck) / 플랫폼 가치 강조
- Government Grant: 정부 지원 로고 병기 / 국책과제 번호 / 공익성 톤
- Data Room (VDD): 모든 수치 파일·라인 레퍼런스 / 재무·비재무 분리

[금지 사항]
- 로고 15종 오용 (임의컬러·회전·비율변경·효과 추가 등)
- 심볼 단독 로고 대체 / 구 녹십자 로고
- CI·BI 혼동 (BI는 GC심볼·GC140·띄어쓰기 모두 금지)
- 빨강·주황을 일반 강조에 사용
- 배너 없는 콘텐츠 슬라이드
- 수치·연도 없는 모호한 전망 ("지속 성장 예상" 등)
- 슬라이드당 패널 5개 이상
- 로고·페이지 번호 없는 슬라이드
- AI Badge를 확정 재무 수치 옆에 사용
- 3개 이상 테마 혼용
- 공식 픽토그램과 FA 동일 슬라이드 혼용
- Regulatory용에 가치판단 형용사 잔존
- 공개 자료에 미공시 파트너십 실명
- Emoji 존치 상태 배포
```

---

## 15. 메시징 어휘 레퍼런스

| 한국어 | 영어 병기 (원문 유지) |
|--------|----------------------|
| 수직 계열화, 사업 구조 | Value Chain / Full Value Chain |
| 생산량 본격 증가 구간 | Ramp-up |
| 개발 단계별 제품군 | Pipeline |
| 생산 규모 확대 | Scale-up |
| 혈장분획 수익성 지표 | Plasma Economics |
| 빠른 의사결정 원칙 | Quick Win And Fast Fail |
| 2가지 전략 병행 | Two Track |
| 미충족 의료 수요 | Unmet Needs |
| 계열 내 최초 승인 | First-In-Class |
| 효소 대체 요법 | ERT (Enzyme Replacement Therapy) |
| 뇌실내 투여 제형 | ICV (Intracerebroventricular) |
| 면역글로불린 | IVIG / IG |
| 미래예측 진술 | Forward-Looking Statement |
| 안전성 고지 | Safe Harbor |
| 시장 규모 계층 | TAM / SAM / SOM |
| 유효성·안전성 균형 | Benefit-Risk Profile |
| 장기 추적 관찰 | LTFU (Long-Term Follow-Up) |
| 임상 안전성 모니터링 | DSMB (Data Safety Monitoring Board) |
| 품질 주요 속성 | CQA (Critical Quality Attributes) |
| 설계 공간 (ICH Q8) | Design Space |
| 중대 이상반응 | SAE (Serious Adverse Event) |
| 약물유해반응 | ADR / AE |
| 연간 반복 투여 | Q4W (Every 4 Weeks) / QW (Weekly) |
| 혈액뇌장벽 | BBB (Blood-Brain Barrier) |
| 항약물항체 | ADA (Anti-Drug Antibody) |
| 규제당국 사전 협의 | Pre-IND / Type B meeting |
| 희귀소아질환 지정 | RPDD (Rare Pediatric Disease Designation) |
| 우선심사 바우처 | PRV (Priority Review Voucher) |

---

## 16. 적용 매체 체크리스트 (브랜드 매뉴얼 반영)

Unified 매뉴얼이 규정하는 주요 적용 매체 — 제작 시 규격 준수 필수:

| 카테고리 | 매체 | 규격 |
|----------|------|------|
| Stationery | 명함 | 90×54mm, Freesentation w400·w700 |
| Stationery | 소봉투 | 220×104mm |
| Stationery | 대봉투 | 334×244mm |
| Corporate | 파일 폴더 | 240×310mm (R/G/B 3종) |
| Corporate | 초청장 | 180×120mm |
| Corporate | 표창장 | 210×297mm |
| Corporate | 사원증 | 54×85mm |
| Corporate | 방문증 (STAFF/GUEST) | 54×86mm |
| Corporate | 배지 | 16×16mm (기본) / 14×14mm (시그니처) |
| Signage | 지주사인 | H 1800 / 5000 / 8000mm |
| Signage | 엑스배너 | 600×1800mm |
| Vehicle | 셔틀버스 (25/45인승), 트럭 (2.5/8톤) | — |

> CI 활용 모든 제작물은 **GC 브랜드팀 사전 검수** 원칙.

---

## 17. Changelog & Migration Notes

### Version History

| Version | Date | Scope | 주요 변경사항 |
|---------|------|-------|-------------|
| **v2.3** | 2026-04-13 | 심볼 단독 SVG 추가 | `gc_symbol_only.svg` 배포본 동봉, §0-3 심볼 단독 권장/금지 용도 세분화, 라이선스 미해결 항목 신규 등재 |
| **v2.2** | 2026-04-13 | 서체 전환 + Asset 동봉 | **GC체 → Freesentation 9 weights 전환**, 공식 로고 SVG 동봉, @font-face 템플릿 §3-4 신설 |
| **v2.1** | 2026-04-13 | Track 구조화 + 수신자 확장 | Designer/Compliance Track 분리, 수신자 4→7유형 확장, §17 Changelog 신설 |
| **v2.0** | 2026-04-13 | 실무 대응 §12 신설 | 용도별 버전 분기 원칙 10개 하위 섹션, Regulatory 어휘 16종 추가 |
| **v1.0** | 2026-04-13 | 브랜드 매뉴얼 Unified 통합 | 심볼·비율·컬러·서체·픽토그램·저작권 전면 반영 |
| v0.1 | 2026-03-xx | IR 분석 기반 초안 | 2025 Investor Day / Alyglo / 4Q 경영실적 분석 |

### v2.3 Migration Notes (v2.2 → v2.3)

| 변경 | 영향 | 마이그레이션 조치 |
|------|------|-------------------|
| `gc_symbol_only.svg` 추가 | Asset 파일 1개 추가 | 배포본 복사 시 새 파일 포함 여부 확인 |
| 심볼 단독 사용 범위 명시 | 기존 자료 재검토 필요 | 공식 IR·보도자료에 심볼만 쓴 경우 워드마크 버전으로 교체 |
| 파비콘·모바일 앱 | 기존 PNG 래스터 → SVG 전환 권장 | `<link rel="icon" type="image/svg+xml">` 사용 |

### v2.2 Migration Notes (v2.1 → v2.2)

| 변경 | 영향 | 마이그레이션 조치 |
|------|------|-------------------|
| GC체 → Freesentation 전환 | 서체 명명 전체 변경 | 기존 `GC 110~150` 참조를 `Freesentation w300~w900`으로 치환 (매핑 표 §3-1 참조) |
| Weight 단계 5 → 9 | 더 세밀한 조정 가능 | 기존 5단계 매핑은 호환 유지, ExtraLight·Medium·ExtraBold·Thin은 추가 활용 |
| @font-face 선언 필수 | 웹 구현 시 9개 파일 로드 | §3-4 템플릿 복붙 후 `font-display: swap` 권장 |
| 공식 로고 SVG 동봉 | 더 이상 외부 Asset 서버 의존 X | `gc_biopharma_vector_refined.svg` 배포본과 함께 사용 |

### v2.1 Migration Notes (v2.0 → v2.1)

| 변경 | 영향 | 마이그레이션 조치 |
|------|------|-------------------|
| Track 구조 도입 | 문서 탐색 방식 변화 | 기존 참조 링크 재확인 (§ 번호는 동일 유지) |
| 수신자 유형 4 → 7 | BD·Government Grant·VDD 신규 | 기존 4유형 템플릿은 그대로 사용 가능, 신규 3유형은 §12-1 참조 |
| §12-2·§12-5에 BD/VDD 열 추가 | 기존 IR/Regulatory 열 변동 없음 | 기존 슬라이드 재작업 불필요 |
| §12-1 3유형 ⭐ 표시 | 조직 필요 시 커스텀 확장 가능 | 아래 "Custom Audience" 섹션 참조 |

### Custom Audience 확장 가이드

조직·상황에 따라 §12-1 기본 7유형 외 커스텀 수신자 추가 가능. 각 수신자 추가 시 다음 4개 속성 반드시 정의:

```
Custom Audience Template
├─ 핵심 수신자 (Who): 구체 직책·기관
├─ 표현 톤 (Tone): 강조 포인트 1줄
├─ 특이 요구사항 (Constraints): 금지/필수 표기 3개 이내
└─ 가치판단 형용사 허용도: ✅ / ⚠️ / ❌
```

예시: `Medical Affairs (MSL)` 유형 추가 시 → 수신자: 임상의·약사 / 톤: 근거·임상 경험 중심 / 요구: Off-label 정보 명시 금지, MR/MA 구분 / 형용사: ⚠️ (문헌 근거 있을 때만)

### 알려진 제약 및 향후 개선 (Known Limitations)

| 항목 | 현 상태 | 향후 계획 |
|------|---------|----------|
| Freesentation 폰트 파일 | ✅ v2.2 배포본에 포함 (9 weights TTF) | @font-face 선언은 §3-4 참조 |
| Freesentation 라이선스 | ⚠️ 미명시 | 한글과컴퓨터 배포 무료 서체로 상업적 사용 가능하나, **조직 법무팀 사전 확인 필수** · 사내 배포·재배포 시 라이선스 문구 첨부 권장 |
| 공식 로고 SVG | ✅ v2.2 배포본에 포함 (`gc_biopharma_vector_refined.svg`) | HTML/SVG 삽입 예시는 §0-3 참조 |
| 심볼 단독 SVG | ✅ v2.3 배포본에 포함 (`gc_symbol_only.svg`) | 파비콘·배지·소형 UI용, 공식 자료 단독 사용 금지 |
| Dark mode 팔레트 | Navy·Warm Beige 기반만 정의 | 향후 v3.0에서 전용 dark palette 정의 예정 |
| 한국어 폰트 fallback | Apple SD·Noto Sans KR | Adobe Fonts 라이선스 시 Pretendard 추가 검토 |
| PPT/Keynote 템플릿 | 미첨부 | 별도 `.pptx` 마스터 파일 배포 예정 |
| v2.1의 "⭐ 신규" 표시 | v2.2에서 제거 예정 | v2.2 릴리스 시 모든 유형 동등 표기 |

### 문서 책임 및 문의

- **기술 오너 (Design System)**: GC 브랜드팀
- **컴플라이언스 오너 (§12–§14)**: GC IR·RA·법무팀
- **개정 프로세스**: 반기 1회 정기 리뷰 + 브랜드 매뉴얼 개정 시 수시 반영
- **피드백**: 실무 적용 중 발견된 gap은 해당 Track 오너에 제보 → 차기 minor version에 반영

---

*출처: GC Brand Manual Book Unified ver. (2026-03) + GC Biopharma 공식 IR (2024–2025)*
*최종 업데이트: 2026-04-13 (v2.3)*

© 2026 GC Corp. All Rights Reserved.
