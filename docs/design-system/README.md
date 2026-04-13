# GC Biopharma Design System · v2.3

> GC녹십자(GC Biopharma) 공식 브랜드 매뉴얼 기반 통합 디자인 시스템
> 발표자료·UI·마케팅 자산 제작을 위한 단일 소스 (Single Source of Truth)

---

## 📦 배포본 구성

```
GC-Biopharma-Design-System-v2.3/
├── README.md                          ← 현재 문서 · 빠른 시작 가이드
├── docs/
│   └── DESIGN-SYSTEM.md               ← 본체 문서 (17 sections, 915+ lines)
└── assets/
    ├── fonts/                         ← Freesentation 서체 9 weights
    │   ├── Freesentation-1Thin.ttf       (w100)
    │   ├── Freesentation-2ExtraLight.ttf (w200)
    │   ├── Freesentation-3Light.ttf      (w300)
    │   ├── Freesentation-4Regular.ttf    (w400)
    │   ├── Freesentation-5Medium.ttf     (w500)
    │   ├── Freesentation-6SemiBold.ttf   (w600)
    │   ├── Freesentation-7Bold.ttf       (w700)
    │   ├── Freesentation-8ExtraBold.ttf  (w800)
    │   └── Freesentation-9Black.ttf      (w900)
    └── logos/
        ├── gc-biopharma-lockup.svg    ← 가로형 Lockup (1000×161)
        └── gc-symbol.svg              ← 심볼 단독 (372×161)
```

---

## 🚀 빠른 시작

### 1. 역할별 읽을 순서

| 역할 | 최소 필수 참조 |
|------|----------------|
| **디자이너·마케터** | `docs/DESIGN-SYSTEM.md` §0–§11 (Designer Track) + §13 가드레일 |
| **IR·RA·법무·BD** | `docs/DESIGN-SYSTEM.md` §12 용도별 버전 분기 + §13 가드레일 |
| **AI 협업 작성자** | `docs/DESIGN-SYSTEM.md` §14 AI 작성 지침 복붙 |
| **개발자** | 아래 "웹 구현" 섹션 + `docs/DESIGN-SYSTEM.md` §7 컴포넌트 스펙 |

### 2. 웹 구현 (HTML/CSS)

`docs/DESIGN-SYSTEM.md` §3-4의 @font-face 템플릿을 복사하거나, 아래 최소 예시를 사용:

```html
<!-- Freesentation 폰트 등록 -->
<style>
@font-face { font-family: 'Freesentation'; src: url('./assets/fonts/Freesentation-4Regular.ttf') format('truetype'); font-weight: 400; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./assets/fonts/Freesentation-6SemiBold.ttf') format('truetype'); font-weight: 600; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./assets/fonts/Freesentation-7Bold.ttf') format('truetype'); font-weight: 700; font-display: swap; }
@font-face { font-family: 'Freesentation'; src: url('./assets/fonts/Freesentation-9Black.ttf') format('truetype'); font-weight: 900; font-display: swap; }

body {
  font-family: 'Freesentation', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
  color: #1A1A1A;
}
</style>

<!-- 로고 삽입 -->
<img src="./assets/logos/gc-biopharma-lockup.svg" alt="GC Biopharma" style="height: 24px;" />

<!-- 파비콘 -->
<link rel="icon" type="image/svg+xml" href="./assets/logos/gc-symbol.svg" />
```

### 3. PPT·Keynote 제작

1. Freesentation 9개 TTF 파일을 OS에 설치 (더블클릭 → "설치")
2. `gc-biopharma-lockup.svg`를 슬라이드에 드래그 앤 드롭
3. 색상 팔레트는 `docs/DESIGN-SYSTEM.md` §2 참조 (Deep Navy `#002B49`, Mid Blue `#0072CE` 기본)

---

## 🎨 핵심 규정 요약 (Cheat Sheet)

### 절대 규칙 (전체 공통)

- **로고**: 풀컬러 기본, Clear Space 2X, 최소 7mm(print)/40px(screen)
- **심볼 단독 사용 금지**: 공식 자료(IR·보도자료·간판)는 반드시 가로형 Lockup
- **음수 재무 수치**: 괄호 `(386)` — 마이너스 기호 금지
- **모든 콘텐츠 슬라이드 하단**: `#002B49` Bottom Banner + 페이지 번호
- **한·영 병기**: Value Chain, Ramp-up, Pipeline, Phase I~III 등 전략 키워드

### 핵심 컬러

| 역할 | HEX |
|------|-----|
| Primary (CTA·강조) | `#002B49` Deep Navy |
| Secondary (링크·배지) | `#0072CE` Mid Blue |
| Tertiary (3번째 계열) | `#00A9E0` Light Blue |
| 패널 배경 | `#E8E8E8` Panel Gray |
| 섹션 배경 | `#F0EDE8` Warm Beige |

### 슬라이드 유형 선택 기준

| 상황 | 테마 | 컬러 계열 |
|------|------|-----------|
| 일반 IR·전략 | Trust & Baseline | Navy + Blue |
| 임상 유의성·AE | Contrast & Efficacy | Green + Red |
| MoA·제형 모식도 | Formulation & MoA | Navy 배경 + Green |

---

## ⚖️ 수신자별 버전 분기 (§12)

같은 데이터도 수신자에 따라 표현 수준이 달라져야 합니다.

| 수신자 | 가치판단 형용사 | 경쟁사 실명 | Safe Harbor |
|--------|-----------------|-------------|-------------|
| IR / Investor | ⚠️ 근거 병기 시 | ⚠️ 공시 정보만 | ✅ 필수 |
| Analyst Day | ⚠️ 최소화 | ⚠️ 공시 정보만 | ✅ 필수 |
| Regulatory | ❌ 금지 | ✅ 공식 인용 | N/A |
| Internal / C-level | ✅ 허용 | ✅ 허용 | 선택 |
| Academic / KOL | ⚠️ 문헌 근거 | ✅ 정확 인용 | N/A |
| BD / Licensing | ⚠️ 가치 강조 | ⚠️ NDA 후 | ⚠️ Teaser 단계 |
| Government Grant | ⚠️ 공익성 | ⚠️ 공개만 | N/A |
| Data Room (VDD) | ❌ 금지 | ✅ 출처와 함께 | ⚠️ 레퍼런스 |

전체 분기 규칙은 `docs/DESIGN-SYSTEM.md` §12-1 ~ §12-10 참조.

---

## 📋 배포 전 체크리스트

공식 자료 배포 직전 반드시 확인:

- [ ] 로고가 풀컬러 + Clear Space 2X 확보되었는가?
- [ ] 모든 콘텐츠 슬라이드에 Bottom Banner가 있는가?
- [ ] 음수 수치가 괄호로 표기되었는가?
- [ ] Forward-Looking 수치에 `E` suffix + Safe Harbor 참조가 있는가?
- [ ] Literature 인용에 `as of YYYY-MM-DD` 날짜가 있는가?
- [ ] Emoji가 Font Awesome으로 치환되었는가? (초안에만 emoji 허용)
- [ ] 저작권 표기 `© 2026 GC Corp. All Rights Reserved.`가 1회 들어갔는가?
- [ ] Regulatory용이라면 가치판단 형용사("우수한", "Platform ready")가 제거되었는가?
- [ ] 미공시 파트너십 실명이 공개 자료에 포함되지 않았는가?
- [ ] GC 브랜드팀 사전 검수가 완료되었는가? (CI 활용 제작물 원칙)

---

## ⚠️ 라이선스 및 사용 제한

- **Freesentation**: 한글과컴퓨터 배포 무료 서체 (상업적 사용 가능 예상). **사내 배포·재배포 시 조직 법무팀 사전 확인 필수**
- **GC 로고 SVG**: GC녹십자 등록 상표. 임의 변형·유사 상표 사용 금지
- **본 Design System 문서**: `© 2026 GC Corp. All Rights Reserved.`

---

## 🔄 버전 및 피드백

- **현재 버전**: v2.3 (2026-04-13)
- **변경 이력**: `docs/DESIGN-SYSTEM.md` §17 Changelog 참조
- **기술 오너** (디자인·자산): GC 브랜드팀
- **컴플라이언스 오너** (§12–§14): GC IR·RA·법무팀
- **개정 주기**: 반기 1회 정기 리뷰 + 브랜드 매뉴얼 개정 시 수시

실무 적용 중 발견된 gap은 GitHub Issues에 제보 → 차기 minor version 반영.

---

## 🔧 GitHub 저장소 운영

본 저장소는 GitHub을 통해 버전 관리됩니다.

### 기여 방법
1. [Issues](../../issues)에 먼저 제안 등록 (오탈자는 바로 PR 가능)
2. `develop` 브랜치에서 분기 (`feature/<이름>`, `fix/<이름>`)
3. Conventional Commits 규칙으로 커밋
4. Pull Request 생성 → 자동 리뷰어 지정

상세 절차는 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 참조.

### 운영 파일

| 파일 | 용도 |
|------|------|
| `.gitignore` | OS·IDE·민감정보 제외 |
| `LICENSE.md` | 문서·로고·폰트별 사용 조건 |
| `CONTRIBUTING.md` | 브랜치 전략·커밋 규칙·PR 절차 |
| `.github/CODEOWNERS` | 트랙별 자동 리뷰어 지정 |
| `.github/ISSUE_TEMPLATE/` | 버그·제안 템플릿 |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR 체크리스트 |
| `.github/workflows/` | 자동 링크 체크 CI |

---

*기반 문서: GC Brand Manual Book Unified ver. (2026-03) + GC Biopharma 공식 IR (2024–2025)*

© 2026 GC Corp. All Rights Reserved.
