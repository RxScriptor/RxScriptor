#!/usr/bin/env python3
"""
Scaffold a new RxScriptor project under projects/<name>/.

Usage:
    python scripts/new_project.py <name> --design {gcbp|rxscript}

Creates:
    projects/<name>/
        project.yml
        _metadata.yml             # wires the chosen design system's CSS
        briefing/
            index.qmd             # copied from modules/briefing/templates/
            briefings.json        # empty array
            briefings/            # per-report HTML goes here
        literature/
            summaries/            # .gitkeep
            metadata/             # .gitkeep
            raw_pdfs/             # .gitkeep (gitignored via pattern)
            templates/summary.md  # copied from modules/literature/templates/

Also adds a navbar entry to _quarto.yml pointing at the project's briefing index.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = REPO_ROOT / "projects"
BRIEFING_TPL = REPO_ROOT / "modules" / "briefing" / "templates"
LITERATURE_TPL = REPO_ROOT / "modules" / "literature" / "templates"
QUARTO_YML = REPO_ROOT / "_quarto.yml"

DESIGN_CSS = {
    "gcbp": "/design-systems/gcbp/tokens/gcbp-tokens.css",
    "rxscript": "/design-systems/rxscript/tokens/rxscript-tokens.css",
}


def scaffold(name: str, design: str) -> Path:
    project_dir = PROJECTS_DIR / name
    if project_dir.exists():
        sys.exit(f"error: {project_dir} already exists")

    (project_dir / "briefing" / "briefings").mkdir(parents=True)
    (project_dir / "literature" / "summaries").mkdir(parents=True)
    (project_dir / "literature" / "metadata").mkdir(parents=True)
    (project_dir / "literature" / "raw_pdfs").mkdir(parents=True)
    (project_dir / "literature" / "templates").mkdir(parents=True)

    (project_dir / "project.yml").write_text(
        yaml.safe_dump(
            {"name": name, "design": design, "created_at": date.today().isoformat()},
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )

    (project_dir / "_metadata.yml").write_text(
        yaml.safe_dump(
            {"format": {"html": {"css": [DESIGN_CSS[design]]}}},
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    shutil.copy(BRIEFING_TPL / "index.qmd", project_dir / "briefing" / "index.qmd")
    shutil.copy(BRIEFING_TPL / "briefings.json", project_dir / "briefing" / "briefings.json")
    shutil.copy(LITERATURE_TPL / "summary.md", project_dir / "literature" / "templates" / "summary.md")

    for stub in (
        project_dir / "literature" / "summaries" / ".gitkeep",
        project_dir / "literature" / "metadata" / ".gitkeep",
        project_dir / "literature" / "raw_pdfs" / ".gitkeep",
        project_dir / "briefing" / "briefings" / ".gitkeep",
    ):
        stub.touch()

    return project_dir


def register_in_quarto(name: str) -> None:
    data = yaml.safe_load(QUARTO_YML.read_text(encoding="utf-8"))
    nav = data.setdefault("website", {}).setdefault("navbar", {}).setdefault("left", [])

    href = f"projects/{name}/briefing/"
    if any(isinstance(e, dict) and e.get("href") == href for e in nav):
        return

    nav.append({"href": href, "text": f"{name} · Briefings"})
    QUARTO_YML.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Scaffold a new RxScriptor project.")
    ap.add_argument("name", help="Project folder name (kebab-case recommended)")
    ap.add_argument(
        "--design",
        choices=sorted(DESIGN_CSS),
        default="rxscript",
        help="Design system to wire into the project (default: rxscript)",
    )
    args = ap.parse_args()

    project_dir = scaffold(args.name, args.design)
    register_in_quarto(args.name)
    print(f"Created {project_dir.relative_to(REPO_ROOT)} using design={args.design}")
    print(f"Registered navbar entry in {QUARTO_YML.name}")


if __name__ == "__main__":
    main()
