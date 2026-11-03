import copy
import json
import os
import posixpath
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SITE_PREFIX = "/askr/"
ZH_TW_MIN_VERSION = (0, 14, 0)
ARCHIVED_SITES = (
    "v0.3.0",
    "v0.9.0",
    "v0.10.0",
    "v0.11.0",
    "v0.12.0",
    "v0.12.1",
    "v0.13.0",
    "v0.13.1",
    "v0.13.2",
    "v0.13.3",
)
MODERN_ARCHIVES = ARCHIVED_SITES[1:]


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


def copy_archives(output: Path) -> None:
    for archive in ARCHIVED_SITES:
        copy_directory(ROOT / "archives" / archive, output / archive)


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

    for archive in MODERN_ARCHIVES:
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


def stable_version(label: str) -> tuple[int, int, int] | None:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", label)
    return tuple(map(int, match.groups())) if match else None


def zh_tw_manifest() -> dict:
    """Build a language-local manifest from the root manifest authority."""
    source = version_manifest()
    manifest = copy.deepcopy(source)
    manifest["versions"] = [
        copy.deepcopy(item)
        for item in source["versions"]
        if (version := stable_version(str(item.get("label", "")))) is not None
        and version >= ZH_TW_MIN_VERSION
    ]
    return manifest


def zh_tw_target_root(item: dict) -> str:
    root = item.get("root", "/").strip("/")
    return posixpath.join(root, "zh-TW") + "/"


def generate_zh_tw_manifest(path: Path, site_root: str = "zh-TW") -> None:
    manifest = zh_tw_manifest()
    for item in manifest["versions"]:
        item["root"] = relative_site_root(site_root, zh_tw_target_root(item))
        item.pop("href", None)
    write_manifest(path, manifest)


def generate_archive_zh_tw_manifests(output: Path) -> None:
    """Write manifests only into copied modern archives that contain zh-TW."""
    for site in sorted(output.glob("v*/zh-TW")):
        archive = site.parent.name
        version = stable_version(archive.removeprefix("v"))
        if version is None or version < ZH_TW_MIN_VERSION:
            continue
        generate_zh_tw_manifest(site / "askr-versions.json", f"{archive}/zh-TW")


def main() -> None:
    if os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1":
        return

    output = ROOT / "_site"
    copy_archives(output)
    generate_archive_manifests(output)
    generate_archive_zh_tw_manifests(output)

    child = ROOT / "zh-TW"
    generate_zh_tw_manifest(child / "askr-versions.json")
    copy_directory(ROOT / "_extensions" / "askr", child / "_extensions" / "askr")
    copy_directory(ROOT / "components" / "images", child / "components" / "images")
    copy_file(ROOT / "components" / "references.bib", child / "components" / "references.bib")
    subprocess.run(["quarto", "render", str(child)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
