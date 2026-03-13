from __future__ import annotations

import json
import py_compile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
EXPECTED_FILES = [
    ROOT_DIR / "main.py",
    ROOT_DIR / "assets" / "logo.ico",
    ROOT_DIR / "assets" / "gear_config.png",
    ROOT_DIR / "src" / "json" / "best_score.json",
    ROOT_DIR / "src" / "json" / "best_score2.json",
]
IMPORT_TARGETS = [
    ROOT_DIR / "main.py",
    ROOT_DIR / "src" / "core" / "block_bricks.py",
    ROOT_DIR / "src" / "core" / "game_base.py",
    ROOT_DIR / "src" / "core" / "bot.py",
]


def ensure_expected_files() -> None:
    missing = [path for path in EXPECTED_FILES if not path.exists()]
    if missing:
        missing_paths = ", ".join(str(path.relative_to(ROOT_DIR)) for path in missing)
        raise SystemExit(f"Missing required files: {missing_paths}")


def ensure_score_files_are_valid() -> None:
    expected_keys = {
        ROOT_DIR / "src" / "json" / "best_score.json": "best_score",
        ROOT_DIR / "src" / "json" / "best_score2.json": "best_score2",
    }
    for file_path, expected_key in expected_keys.items():
        with file_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if expected_key not in payload:
            raise SystemExit(f"JSON file {file_path.relative_to(ROOT_DIR)} is missing key {expected_key}")


def ensure_sources_compile() -> None:
    for file_path in IMPORT_TARGETS:
        py_compile.compile(str(file_path), doraise=True)


def main() -> None:
    ensure_expected_files()
    ensure_score_files_are_valid()
    ensure_sources_compile()
    print("Smoke check passed.")


if __name__ == "__main__":
    main()