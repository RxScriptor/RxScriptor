# Research Archive · DDS

DDS(Drug Delivery System) 분야 논문 트래킹 대시보드.  
GitHub Pages로 배포하여 동료 연구원과 공유합니다.

---

## Repo 구조

```
/
├── index.html          ← 메인 대시보드
├── briefs/
│   └── lnpdb-2026.html ← 개별 논문 브리핑 HTML
├── assets/
│   └── .gitkeep        ← 인포그래픽 PNG 저장 위치
└── README.md
```

---

## 카테고리 & 색상

| 카테고리 | 색상 | 설명 |
|---|---|---|
| ionizable lipid | `#185FA5` | 이온화 지질 구조·설계 |
| LNP formulation | `#0F6E56` | LNP 제형 최적화 |
| manufacturing | `#4C2AA6` | 제조 공정·스케일업 |
| mRNA | `#8A3A0E` | mRNA 서열·변형·안정성 |
| DDS | `#1D9E75` | 나노입자·DDS 일반 |
| vaccine | `#D85A30` | 백신 적용 연구 |
| therapeutics | `#BA7517` | 치료제 적용·임상 연구 |

---

## 논문 1편 추가 워크플로우

### 1. 브리핑 HTML 생성
Claude에게 다음 형식으로 요청:
```
이 논문 요약해줘.
5 key findings + limitations 섹션, HTML 브리핑 파일로 만들어줘.
파일명: briefs/[논문-키워드].html
```

### 2. 인포그래픽
외부 도구(BioRender, Canva 등)로 제작 → PNG 내보내기  
→ `assets/[논문-키워드].png` 저장 (3 MB 이하 권장)

### 3. 대시보드 업데이트
`index.html`을 브라우저에서 열기 → `+ 논문 추가` (또는 `N` 키)  
→ 카테고리 선택, KP 3줄 입력  
→ 브리핑 URL: `./briefs/[키워드].html`  
→ 저장 후 인포그래픽 이미지 업로드

### 4. Git push
```bash
git init  # 최초 1회
git add .
git commit -m "Init: Research Archive v5"
git remote add origin https://github.com/parkjoo000/literature-archive.git
git push -u origin main
# → Settings → Pages → Branch: main / (root) → Save
```

---

## 키보드 단축키

| 키 | 기능 |
|---|---|
| `N` | 논문 추가 모달 열기 |
| `Esc` | 모달 / 설정 닫기 |

---

## GitHub Pages 최초 세팅 (1회)

1. GitHub repo → **Settings** → **Pages**
2. Source: `Deploy from a branch`
3. Branch: `main` / `/ (root)`
4. **Save** → 배포 URL: `https://parkjoo000.github.io/literature-archive/`
5. `index.html` 상단 `og:url`, `og:image` 값 교체 완료 ✓

---

## 데이터 백업 · 복원

논문 메타데이터와 인포그래픽 이미지는 **브라우저 localStorage**에 저장됩니다.  
브라우저 교체·초기화 전 반드시:

```
설정(⚙) → JSON 내보내기  →  research-archive.json 로컬 저장
```

복원 시:

```
설정(⚙) → JSON 가져오기  →  저장해둔 .json 파일 선택
```

> 인포그래픽 원본 PNG는 `assets/` 폴더에도 함께 보관하는 것을 권장합니다.  
> localStorage는 브라우저 단위 저장이므로, 공유 URL을 통해 열람하는 동료는 별도 데이터를 갖습니다.
