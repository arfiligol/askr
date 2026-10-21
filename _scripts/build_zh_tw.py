import os
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def copy_directory(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"Required shared directory is missing: {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def copy_file(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Required shared file is missing: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> None:
    if os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1":
        return

    child = ROOT / "zh-TW"
    copy_directory(ROOT / "_extensions" / "askr", child / "_extensions" / "askr")
    copy_directory(ROOT / "components" / "images", child / "components" / "images")
    copy_file(ROOT / "components" / "references.bib", child / "components" / "references.bib")
    subprocess.run(["quarto", "render", str(child)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
