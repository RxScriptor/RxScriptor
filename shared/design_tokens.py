"""Load RxScript design tokens from the JSON single-source-of-truth.

The CSS file (`design-systems/rxscript/tokens/rxscript-tokens.css`) and this
JSON file MUST be kept in sync manually — the JSON is what Python reads.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent
_TOKENS_PATH = _REPO_ROOT / "design-systems" / "rxscript" / "tokens" / "rxscript-tokens.json"


def load_tokens() -> dict[str, Any]:
    with _TOKENS_PATH.open(encoding="utf-8") as f:
        return json.load(f)


_TOKENS = load_tokens()

COLOR: dict[str, str] = _TOKENS["color"]
FONT: dict[str, str] = _TOKENS["font"]
WEIGHT: dict[str, int] = _TOKENS["weight"]
SPACE: dict[str, str] = _TOKENS["space"]
RADIUS: dict[str, str] = _TOKENS["radius"]
