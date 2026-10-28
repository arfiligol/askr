import copy
import json
import os
import posixpath
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SITE_PREFIX = "/askr/"


def copy_directory(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"Required shared directory is missing: {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def copy_file(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Required shared file is missing: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def version_manifest() -> dict:
    source = ROOT / "askr-versions.json"
    return json.loads(source.read_text(encoding="utf-8"))


def relative_site_root(archive: str, root: str) -> str:
    archive_path = archive.strip("/")
    target_path = root.strip("/") or "."
    relative = posixpath.relpath(target_path, archive_path)
    return "./" if relative == "." else relative.rstrip("/") + "/"


def write_manifest(path: Path, manifest: dict) -> None:
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def generate_archive_manifests(output: Path) -> None:
    source = version_manifest()

    for archive in ("v0.9.0", "v0.10.0", "v0.11.0", "v0.12.0", "v0.12.1", "v0.13.0", "v0.13.1"):
        modern = copy.deepcopy(source)
        for item in modern["versions"]:
            root = relative_site_root(archive, item["root"])
            item["href"] = root
            if item["label"] == archive[1:]:
                item["root"] = root
            else:
                item.pop("root", None)
        write_manifest(output / archive / "askr-versions.json", modern)

    # The frozen 0.3 selector matches origin-root paths and resolves fixed hrefs
    # from the origin. Supply its repository prefix without changing its HTML.
    legacy = copy.deepcopy(source)
    for item in legacy["versions"]:
        suffix = item["root"].strip("/")
        root = PUBLIC_SITE_PREFIX + (suffix + "/" if suffix else "")
        item["root"] = root
        item["href"] = root
    write_manifest(output / "v0.3.0" / "askr-versions.json", legacy)


def main() -> None:
    if os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1":
        return

    output = ROOT / "_site"
    generate_archive_manifests(output)

    child = ROOT / "zh-TW"
    copy_directory(ROOT / "_extensions" / "askr", child / "_extensions" / "askr")
    copy_directory(ROOT / "components" / "images", child / "components" / "images")
    copy_file(ROOT / "components" / "references.bib", child / "components" / "references.bib")
    subprocess.run(["quarto", "render", str(child)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
