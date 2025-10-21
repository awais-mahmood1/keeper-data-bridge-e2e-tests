from pathlib import Path
import os

def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]

def data_dir() -> Path:
    override = os.getenv("DATA_DIR")
    return Path(override) if override else repo_root() / "tests" / "data"

def data_path(*parts: str) -> Path:
    return data_dir().joinpath(*parts)