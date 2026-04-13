# Contributing to GC Biopharma Design System

GC Biopharma Design System에 기여해주셔서 감사합니다. 본 문서는 저장소에 변경사항을 제안·반영하는 표준 절차를 안내합니다.

## 🎯 기여 가능 영역

| 영역 | 담당 Track | 리뷰어 |
|------|-----------|--------|
| 시각 자산 (로고·폰트·컬러) | Designer Track (§0–§11) | GC 브랜드팀 |
| 슬라이드 컴포넌트 스펙 | Designer Track (§5–§10) | GC 브랜드팀 + 기획팀 |
| 수신자별 분기 규칙 | Compliance Track (§12–§13) | IR·RA·법무팀 |
| AI 프롬프트 템플릿 | Compliance Track (§14) | 전체 트랙 공동 |
| 어휘 레퍼런스 확장 | Appendix (§15) | 사용 부서 제안 후 오너 승인 |

## 🔀 브랜치 전략

```
main        ← 프로덕션 배포본 (보호 브랜치, 직접 push 금지)
├── develop ← 다음 릴리스 통합 브랜치
│   ├── feature/add-pk-slide-template
│   ├── feature/update-color-tokens
│   └── fix/typo-in-section-12
└── hotfix/urgent-logo-correction ← 긴급 수정은 main에서 분기
```

### 브랜치 네이밍 규칙

- `feature/<짧은-설명>`: 새 기능·섹션 추가
- `fix/<짧은-설명>`: 오탈자·버그 수정
- `hotfix/<짧은-설명>`: 프로덕션 긴급 수정
- `docs/<짧은-설명>`: 문서만 변경
- `asset/<짧은-설명>`: 로고·폰트 등 자산 교체

## 📝 커밋 메시지 규칙 (Conventional Commits)

```
<type>(<scope>): <subject>

<body - optional>

<footer - optional>
```

### Type 종류

| Type | 용도 | 예시 |
|------|------|------|
| `feat` | 새 기능·섹션 추가 | `feat(compliance): add BD/Licensing audience type` |
| `fix` | 오탈자·오류 수정 | `fix(docs): correct color hex in §2-1` |
| `docs` | 문서 변경만 | `docs(readme): update quick start guide` |
| `style` | 포맷·공백 변경 | `style(css): unify indentation in gc-tokens.css` |
| `refactor` | 구조 재편 (내용 동일) | `refactor(docs): split §12 into track-based sections` |
| `asset` | 로고·폰트 교체 | `asset(logo): add symbol-only SVG` |
| `chore` | 빌드·설정·기타 | `chore: update .gitignore` |

### Scope 예시
`docs`, `css`, `fonts`, `logos`, `readme`, `designer-track`, `compliance`, `prompt`

## 🔁 기여 워크플로우

### 1. Issue 먼저 생성 (의무)

변경사항이 확정되기 전에 Issue로 제안 → 토론 → 합의 → 구현. 이유:
- 중복 작업 방지
- 오너 트랙별 책임자 사전 지정
- Regulatory·Compliance 관련 변경은 사전 합의 필수

### 2. Fork & Branch

```bash
git clone https://github.com/<org>/gc-biopharma-design-system.git
cd gc-biopharma-design-system
git checkout develop
git pull origin develop
git checkout -b feature/my-contribution
```

### 3. 변경 후 커밋 & Push

```bash
git add <변경 파일>
git commit -m "feat(compliance): add Medical Affairs audience type"
git push origin feature/my-contribution
```

### 4. Pull Request 생성

- **Base**: `develop` (hotfix는 예외적으로 `main`)
- **리뷰어 지정**: 영향 받는 Track 오너 최소 1명
- **체크리스트**: PR 템플릿의 항목 모두 체크

### 5. 리뷰 & 병합

- 리뷰어 승인 후 **Squash and merge** 권장 (커밋 이력 정리)
- Regulatory·Compliance 관련 변경은 **2인 승인** 필수 (IR + 법무)

## 🔢 버전 관리 (SemVer + Changelog)

```
MAJOR.MINOR.PATCH
  │     │     └─ 오탈자·경미한 수정 (예: v2.3.1)
  │     └─────── 새 섹션·수신자 유형 추가 (예: v2.4.0)
  └───────────── 전체 구조 개편·호환 깨짐 (예: v3.0.0)
```

- 모든 변경은 `docs/DESIGN-SYSTEM.md` §17 Changelog에 반영
- Release 시점에 GitHub Releases로 태깅: `git tag -a v2.4.0 -m "Release v2.4.0"`

## 🛡️ 배포 전 체크 (PR 필수 항목)

- [ ] `docs/DESIGN-SYSTEM.md` §17 Changelog에 변경 이력 기재
- [ ] 버전 번호 업데이트 (문서 상단·README·Changelog)
- [ ] 영향 받는 Track 오너 리뷰어 지정
- [ ] 자산 변경 시 파일 크기·최적화 확인
- [ ] Regulatory 영향 변경 시 법무·RA 팀 사전 검토
- [ ] 커밋 메시지가 Conventional Commits 규칙 준수
- [ ] 민감 정보(미공시 파트너십·임상 데이터) 미포함 확인

## 🚨 금지 사항

- ✗ `main` 브랜치 직접 push
- ✗ 미공시 정보·파트너십 실명·임상 미발표 데이터 커밋
- ✗ 로고 SVG 임의 변형 후 커밋
- ✗ 라이선스 변경 (LICENSE.md 수정은 법무팀 승인 후)
- ✗ Force push (`git push --force`) — 히스토리 보존 필수

## 📞 문의 및 오너십

| 영역 | 오너 | 연락 |
|------|------|------|
| Designer Track (§0–§11) | GC 브랜드팀 | (내부 연락처) |
| Compliance Track (§12–§14) | IR·RA·법무팀 | (내부 연락처) |
| Appendix (§15–§17) | 전체 공동 | (내부 연락처) |
| GitHub 저장소 운영 | (Maintainer 지정) | (내부 연락처) |

---

© 2026 GC Corp. All Rights Reserved.
