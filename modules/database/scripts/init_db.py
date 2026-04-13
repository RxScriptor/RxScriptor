"""Initialize SQLite databases for RxScriptor.

Usage:
    python init_db.py              # Both public and private
    python init_db.py --public-only  # Public only (for CI/CD)
"""
import argparse
import sqlite3
from pathlib import Path

DB_DIR = Path(__file__).parent.parent


def init_public_db():
    """공개 DB: 논문 메타데이터, 공개 참조 데이터."""
    db_path = DB_DIR / "rx_public.db"
    conn = sqlite3.connect(db_path)
    schema = (DB_DIR / "scripts" / "schema_public.sql").read_text()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print(f"✓ Public DB initialized: {db_path}")


def init_private_db():
    """비공개 DB: 개인 메모, 연구 노트."""
    db_path = DB_DIR / "rx_private.db"
    conn = sqlite3.connect(db_path)
    schema = (DB_DIR / "scripts" / "schema_private.sql").read_text()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print(f"✓ Private DB initialized: {db_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-only", action="store_true")
    args = parser.parse_args()

    init_public_db()
    if not args.public_only:
        init_private_db()
