# RxScriptor

Drug Delivery System (DDS) research portal.

## Structure

```
modules/
├── literature/   # Paper metadata & summaries
├── briefing/     # Research reports (Quarto)
└── database/     # SQLite storage
```

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Symlink raw PDFs (local-only, outside repo)
mkdir -p ~/RxScriptor-data/raw_pdfs
ln -s ~/RxScriptor-data/raw_pdfs modules/literature/raw_pdfs

# 3. Initialize databases
python modules/database/scripts/init_db.py

# 4. Build site locally
quarto render
```

## Deploy

Push to `main` → GitHub Actions builds and deploys to `gh-pages` branch automatically.

GitHub Pages Source: `gh-pages` branch / root

## Privacy

- `modules/literature/raw_pdfs/`: gitignored (copyright)
- `modules/database/rx_private.db`: gitignored (personal notes)
- `robots.txt`: blocks search engine indexing
- Reports use hash paths (`r/[hash]-[slug]/`) to prevent URL guessing
