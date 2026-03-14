from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = PROJECT_ROOT / "assets"
JSON_DIR = PROJECT_ROOT / "src" / "json"


def asset_path(*parts: str) -> Path:
    return ASSETS_DIR.joinpath(*parts)


def json_path(*parts: str) -> Path:
    return JSON_DIR.joinpath(*parts)


def project_path(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)