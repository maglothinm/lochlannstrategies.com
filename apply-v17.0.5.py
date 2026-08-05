#!/usr/bin/env python3
"""Apply the Lochlann Strategies v17.0.5 typography normalization update.

This update is intentionally narrow: it replaces the v17 stylesheet and bumps
only the stylesheet cache key in the site's HTML files. It does not alter page
copy, images, JavaScript, navigation, metadata, or document structure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RELEASE = "17.0.5"
CSS_RELATIVE_PATH = Path("assets/lochlann-v17.0.2.css")
SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_CSS = SCRIPT_DIR / CSS_RELATIVE_PATH
EXPECTED_SOURCE_SHA256 = "ad211b89bd36c78f4fae05c3577bc01852777d0185613f8325241f8441ee7d62"

# The current site deliberately retains the established stylesheet filename.
# The query string is the release/cache identifier.
STYLE_LINK_RE = re.compile(
    r'(?P<prefix><link\b[^>]*\bhref=["\'](?:\./)?assets/lochlann-v17\.0\.2\.css)'
    r'(?:\?v=17\.0\.[0-9]+)?(?P<suffix>["\'][^>]*>)',
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temp_path = Path(handle.name)
        handle.write(data)
        handle.flush()
    temp_path.replace(path)


def discover_html(root: Path) -> list[Path]:
    excluded = {".git", "node_modules", "vendor"}
    files: list[Path] = []
    for path in root.rglob("*.html"):
        if any(part in excluded or part.startswith(".lochlann-backup-") for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def patch_html(text: str) -> tuple[str, int]:
    def replacement(match: re.Match[str]) -> str:
        return f'{match.group("prefix")}?v={RELEASE}{match.group("suffix")}'

    return STYLE_LINK_RE.subn(replacement, text)


def verify_overlay() -> None:
    if not SOURCE_CSS.is_file():
        raise RuntimeError(f"Update stylesheet is missing: {SOURCE_CSS}")
    actual = sha256(SOURCE_CSS)
    if actual != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(
            "Update stylesheet failed its integrity check. "
            f"Expected {EXPECTED_SOURCE_SHA256}, found {actual}."
        )


def assess_target(root: Path) -> dict[str, object]:
    html_files = discover_html(root)
    if not html_files:
        raise RuntimeError(f"No HTML files were found under {root}")
    index = root / "index.html"
    if not index.is_file():
        raise RuntimeError(f"The selected folder does not contain index.html: {root}")

    pages: list[dict[str, object]] = []
    total_refs = 0
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        refs = len(STYLE_LINK_RE.findall(text))
        total_refs += refs
        pages.append({"path": path.relative_to(root).as_posix(), "stylesheet_references": refs})

    if total_refs == 0:
        raise RuntimeError(
            "No references to assets/lochlann-v17.0.2.css were found. "
            "This update is intended for the current v17 site baseline."
        )

    return {
        "root": str(root),
        "html_file_count": len(html_files),
        "stylesheet_reference_count": total_refs,
        "pages": pages,
    }


def make_backup(root: Path, paths: list[Path]) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = root.parent / f"{root.name}-backup-v{RELEASE}-{stamp}"
    backup.mkdir(parents=True, exist_ok=False)

    copied: list[str] = []
    for source in paths:
        if not source.exists():
            continue
        relative = source.relative_to(root)
        destination = backup / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(relative.as_posix())

    manifest = {
        "release": RELEASE,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_root": str(root),
        "files": copied,
    }
    (backup / "backup-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return backup


def apply_update(root: Path, *, no_backup: bool) -> dict[str, object]:
    assessment = assess_target(root)
    html_files = discover_html(root)
    target_css = root / CSS_RELATIVE_PATH

    planned_html: list[tuple[Path, str, int]] = []
    for path in html_files:
        original = path.read_text(encoding="utf-8")
        updated, count = patch_html(original)
        if count:
            planned_html.append((path, updated, count))

    backup_paths = [target_css, *(path for path, _, _ in planned_html)]
    backup = None if no_backup else make_backup(root, backup_paths)

    atomic_write(target_css, SOURCE_CSS.read_bytes())
    for path, updated, _ in planned_html:
        atomic_write(path, updated.encode("utf-8"))

    # Post-apply validation.
    if sha256(target_css) != EXPECTED_SOURCE_SHA256:
        raise RuntimeError("The deployed stylesheet does not match the release stylesheet.")

    remaining_old: list[str] = []
    updated_pages: list[str] = []
    reference_count = 0
    for path in discover_html(root):
        text = path.read_text(encoding="utf-8")
        matches = STYLE_LINK_RE.findall(text)
        reference_count += len(matches)
        if "lochlann-v17.0.2.css?v=17.0.5" in text:
            updated_pages.append(path.relative_to(root).as_posix())
        if re.search(r"lochlann-v17\.0\.2\.css\?v=(?!17\.0\.5)", text):
            remaining_old.append(path.relative_to(root).as_posix())

    if remaining_old:
        raise RuntimeError(
            "Legacy stylesheet cache keys remain in: " + ", ".join(remaining_old)
        )

    return {
        **assessment,
        "release": RELEASE,
        "deployed_css": CSS_RELATIVE_PATH.as_posix(),
        "deployed_css_sha256": sha256(target_css),
        "updated_pages": updated_pages,
        "updated_page_count": len(updated_pages),
        "stylesheet_reference_count_after": reference_count,
        "backup": str(backup) if backup else None,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Apply the Lochlann Strategies v17.0.5 typography normalization update."
    )
    parser.add_argument(
        "site",
        nargs="?",
        default=".",
        help="Path to the current Lochlann website repository (default: current directory)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate compatibility without changing files",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Do not create a timestamped backup beside the site folder",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.site).expanduser().resolve()

    try:
        verify_overlay()
        if not root.is_dir():
            raise RuntimeError(f"Site folder does not exist: {root}")

        if args.check:
            report = assess_target(root)
            report.update(
                {
                    "release": RELEASE,
                    "overlay_css_sha256": EXPECTED_SOURCE_SHA256,
                    "compatible": True,
                }
            )
            print(json.dumps(report, indent=2))
            return 0

        report = apply_update(root, no_backup=args.no_backup)
        print(json.dumps(report, indent=2))
        return 0
    except (OSError, UnicodeError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
