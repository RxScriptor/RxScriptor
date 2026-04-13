# BriefingHub

DDS 연구팀 세미나·업체 미팅 사전 브리핑 아카이브 대시보드.

---

## 폴더 구조

```
briefing-dashboard/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← GitHub Actions 자동 배포
├── briefings/
│   └── briefing_company_molcube.html   ← 브리핑 HTML 파일들
├── briefings.json              ← 브리핑 메타 데이터 (이것만 수정)
├── index.html                  ← 대시보드 (수정 불필요)
└── README.md
```

---

## 최초 배포 (1회만)

### 1. GitHub 저장소 생성

```bash
cd briefing-dashboard
git init
git add .
git commit -m "init: BriefingHub"
git remote add origin https://github.com/parkjoo000/briefing-hub.git
git push -u origin main
```

### 2. GitHub Pages 활성화

저장소 → **Settings → Pages → Source: GitHub Actions → Save**

→ 1~2분 후 `https://parkjoo000.github.io/briefing-hub/` 접속 가능

### 3. 팀원에게 URL 공유

이후 push할 때마다 GitHub Actions가 자동으로 재배포합니다.

---

## 새 브리핑 추가 워크플로우

Claude에게 브리핑 요청 시 아래 두 파일이 함께 생성됩니다.

| 파일 | 역할 |
|------|------|
| `briefings/briefing_[이름].html` | 브리핑 상세 문서 |
| `briefings.json` | 대시보드 메타 데이터 (자동 업데이트) |

### push 명령어

```bash
git add briefings/ briefings.json
git commit -m "add: [이름] 브리핑"
git push
```

→ GitHub Actions가 자동으로 배포 (약 1분 소요)

---

## briefings.json 구조

```json
[
  {
    "id": "고유ID",
    "type": "company",        // company | speaker
    "name": "MolCube, Inc.",
    "sub": "소속 · 직위 · 지역",
    "date": "2026-04-10",     // YYYY-MM-DD
    "tags": ["LNP", "mRNA"],
    "memo": "미팅 목적 요약",
    "file": "briefings/briefing_company_molcube.html"  // 파일 없으면 ""
  }
]
```

---

## 팀 공유 정책

| 권한 | 대상 |
|------|------|
| 열람 | 팀원 전체 (URL 접근) |
| 브리핑 추가 | 본인만 (GitHub push 권한) |
| 브리핑 수정 | 본인만 (briefings.json 직접 편집) |
