# RxScriptor

Drug Delivery System (DDS) research portal.

## Structure

```
design-systems/
├── rxscript/      # Public design system (tokens + docs skeleton)
└── gcbp/          # PRIVATE — GCBP Design (git submodule, opt-in)

projects/
├── _legacy/       # Pre-restructure archive (briefings + literature)
└── <name>/        # One folder per project, scaffolded via scripts/new_project.py
    ├── project.yml
    ├── _metadata.yml
    ├── briefing/
    └── literature/

modules/
├── briefing/templates/    # Scaffolding templates copied into each new project
├── literature/templates/
└── database/              # SQLite (rx_public.db, rx_private.db)

shared/                    # Shared Python utilities
assets/                    # Site-wide CSS (tokens live under design-systems/)
scripts/new_project.py     # Project scaffolding CLI
```

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. (Optional) Attach the private GCBP design system
git submodule update --init --recursive        # once the submodule is configured
# or clone fresh with:
git clone --recurse-submodules <repo-url>

# 3. Symlink raw PDFs per project (local-only, gitignored)
mkdir -p ~/RxScriptor-data/raw_pdfs
# for each project that needs PDFs:
ln -s ~/RxScriptor-data/raw_pdfs/<project> projects/<project>/literature/raw_pdfs

# 4. Initialize databases
python modules/database/scripts/init_db.py

# 5. Build site
quarto render
```

## Creating a new project

```bash
python scripts/new_project.py <name> --design rxscript   # or --design gcbp
```

This creates `projects/<name>/` with briefing + literature scaffolding, writes `project.yml` and `_metadata.yml` (selecting the design system's CSS), and appends a navbar entry to `_quarto.yml`.

## Design systems

| System | Location | Visibility | Namespace |
|---|---|---|---|
| RxScript Design | `design-systems/rxscript/` | Public | `--rx-*` |
| GCBP Design     | `design-systems/gcbp/`     | **Private** (submodule) | `--gc-*` |

RxScript is the default; use `--design gcbp` only for GC Biopharma-owned projects.

### GCBP private-repo migration (one-time)

`design-systems/gcbp/` currently lives as local files and is git-ignored. To convert it into a private submodule:

1. Create a private GitHub repo (e.g. `rxscriptor-gcbp-design`).
2. Copy `design-systems/gcbp/` into that repo, commit, push.
3. In this repo: remove `design-systems/gcbp/` from `.gitignore`, delete the local folder, then:
   ```bash
   git submodule add git@github.com:<owner>/rxscriptor-gcbp-design.git design-systems/gcbp
   ```
4. Commit the resulting `.gitmodules` + submodule pointer.

See [design-systems/gcbp/README.md](design-systems/gcbp/README.md) for detailed steps.

## Deploy

Push to `main` → GitHub Actions builds and deploys to `gh-pages` automatically.

## Privacy

- `design-systems/gcbp/`: gitignored until attached as a private submodule
- `projects/*/literature/raw_pdfs/` and `modules/literature/raw_pdfs/`: gitignored (copyright)
- `modules/database/rx_private.db`: gitignored (personal notes)
- `assets/robots.txt`: blocks search engine indexing
- Legacy reports use hash paths (`projects/_legacy/briefing/reports/r/[hash]-[slug]/`)
