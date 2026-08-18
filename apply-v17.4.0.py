#!/usr/bin/env python3
"""Apply the Lochlann Strategies v17.4.0 executive-evidence update.

The patch is intentionally additive. It preserves the v17.3.0 page architecture,
base stylesheet, JavaScript, imagery, navigation, and existing content while
adding career chronology and attributable prior-role evidence.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

VERSION = "17.4.0"
RELEASE_DATE = "2026-08-18"
STYLE_NAME = "lochlann-v17.4.0-career-evidence.css"
STYLE_LINK = f'<link href="assets/{STYLE_NAME}?v={VERSION}" rel="stylesheet"/>'
ABOUT_START = "<!-- v17.4.0 executive background start -->"
ABOUT_END = "<!-- v17.4.0 executive background end -->"
EXPERIENCE_START = "<!-- v17.4.0 prior-role evidence start -->"
EXPERIENCE_END = "<!-- v17.4.0 prior-role evidence end -->"


class PatchError(RuntimeError):
    """Raised when the baseline does not match or validation fails."""


ABOUT_BLOCK = f'''{ABOUT_START}
<section aria-labelledby="executive-background-title" class="section executive-background-section surface-slate" id="executive-background">
<div class="container">
<div class="executive-background-layout">
<div class="executive-background-intro" data-reveal="">
<p class="eyebrow">Executive background</p>
<h2 id="executive-background-title">A career across the customer, growth, and delivery sides of complex work.</h2>
<p class="lead">The chronology below provides the role context behind Lochlann’s principal-led advisory model and the experience brought to each engagement.</p>
</div>
<div class="career-timeline" aria-label="Michael Maglothin career chronology">
<article data-reveal="right">
<p class="career-period">2026–Present</p>
<div class="career-role"><h3>Founder &amp; Principal</h3><p class="career-organization">Lochlann Strategies</p><p>Established a selective advisory practice focused on growth strategy, market and customer entry, capture, partner development, growth operations, and complex execution.</p></div>
</article>
<article data-reveal="right">
<p class="career-period">2019–2026</p>
<div class="career-role"><h3>Director, International Programs</h3><p class="career-organization">Global security-technology company</p><p>Connected government account growth, technical solutioning, commercial planning, partner management, and cross-functional program execution across international markets.</p></div>
</article>
<article data-reveal="right">
<p class="career-period">2017–2019</p>
<div class="career-role"><h3>Strategy &amp; Solutions Principal; Chief, Global Sales Operations</h3><p class="career-organization">L3Harris</p><p>Led market strategy, major-capture support, sales operations, CRM and ERP integration, pipeline governance, forecasting, executive reviews, and sales enablement across five global regions.</p></div>
</article>
<article data-reveal="right">
<p class="career-period">2015–2016</p>
<div class="career-role"><h3>Director, Capture Management</h3><p class="career-organization">GDIT</p><p>Led federal opportunity qualification, capture strategy, customer engagement, partner teams, pricing, proposals, risk, executive gates, and transition planning.</p></div>
</article>
<article data-reveal="right">
<p class="career-period">2012–2015</p>
<div class="career-role"><h3>Director, Business Development</h3><p class="career-organization">Honeywell</p><p>Built federal and international pipelines, governed bid investment, formed strategic teams, and led market positioning and capture across defense, infrastructure, and mission-technology opportunities.</p></div>
</article>
<article data-reveal="right">
<p class="career-period">Earlier career</p>
<div class="career-role"><h3>Government acquisition, company building &amp; technical programs</h3><p class="career-organization">U.S. Air Force · Federal systems engineering · Technology venture · Department of Energy programs</p><p>Defined operational requirements, supported acquisition and systems engineering, co-founded and built a security-technology company, and led technical work in high-consequence government and infrastructure environments.</p></div>
</article>
</div>
</div>
<div class="executive-track-heading" data-reveal="">
<div><p class="eyebrow">Executive operating scope</p><h2>Three leadership tracks behind the advisory model.</h2></div>
<p class="lead">The experience is broader than capture alone: it includes the operating systems around growth and the program discipline required to deliver the commitments made during a pursuit.</p>
</div>
<div class="executive-track-grid">
<article data-reveal=""><span class="index">01</span><h3>Federal Growth &amp; Capture</h3><p>Government acquisition, agency and program mapping, market entry, contract vehicles, opportunity qualification, capture governance, partner strategy, pricing, proposal leadership, and transition to execution.</p></article>
<article data-reveal=""><span class="index">02</span><h3>Enterprise Growth &amp; Sales Operations</h3><p>Global sales operations, CRM and ERP integration, pipeline and forecast discipline, executive business reviews, KPI reporting, sales enablement, commercial governance, and operating cadence.</p></article>
<article data-reveal=""><span class="index">03</span><h3>Complex Programs &amp; Execution</h3><p>Cross-functional program governance, cost and resource models, infrastructure and site readiness, international implementation, testing, acceptance, recovery, customer handoff, and follow-on growth.</p></article>
</div>
<p class="executive-background-link"><a class="text-link text-link-large" href="experience.html#career-evidence">Review selected prior-role evidence <svg aria-hidden="true" class="icon-arrow" viewbox="0 0 18 18"><path d="M3 9h11M10 4l5 5-5 5"></path></svg></a></p>
</div>
</section>
{ABOUT_END}'''


EXPERIENCE_BLOCK = f'''{EXPERIENCE_START}
<section aria-labelledby="career-evidence-title" class="section career-outcomes-section surface-slate" id="career-evidence">
<div class="container">
<div class="career-outcomes-heading" data-reveal="">
<div><p class="eyebrow">Selected prior-role evidence</p><h2 id="career-evidence-title">Scale, operating discipline, and commercial consequence.</h2></div>
<p class="lead">The record spans growth systems, capture portfolios, and programs where opportunity quality, commercial commitments, and delivery performance had measurable consequences.</p>
</div>
<div class="career-outcome-grid">
<article class="career-outcome-card" data-reveal="">
<span class="index">01</span><p class="card-kicker">Growth operations</p><h3>Global sales-operations transformation</h3>
<p>Led 14 direct reports across five regions supporting more than $1 billion in annual opportunity portfolios and more than $1.5 billion in annual proposal and quotation activity. Rebuilt Salesforce and integrated CRM with ERP, increasing bid throughput from four to 20 per month while reducing quotation labor by 50% and annual cost by more than $200,000.</p>
<ul class="outcome-metrics"><li><strong>$1B+</strong><span>annual opportunity portfolios</span></li><li><strong>$1.5B+</strong><span>annual proposal and quotation activity</span></li><li><strong>4 → 20</strong><span>bids per month</span></li></ul>
</article>
<article class="career-outcome-card" data-reveal="">
<span class="index">02</span><p class="card-kicker">Federal capture</p><h3>Portfolio and pursuit governance</h3>
<p>Expanded a strategic pipeline beyond $600 million and captured a $6.6 million U.S. Air Force task order while leading qualification, customer strategy, teaming, pricing, proposal development, risk, executive capture gates, and transition planning.</p>
<ul class="outcome-metrics"><li><strong>$600M+</strong><span>strategic pipeline</span></li><li><strong>$6.6M</strong><span>U.S. Air Force task order</span></li><li><strong>$2M</strong><span>annual bid-and-proposal investment</span></li></ul>
</article>
<article class="career-outcome-card" data-reveal="">
<span class="index">03</span><p class="card-kicker">International growth &amp; delivery</p><h3>Commercial strategy carried into execution</h3>
<p>Aligned account development, technical solutioning, commercial planning, partner management, and program execution during annual business expansion from approximately $3 million to more than $50 million. Served as sales-technical and program-management bid lead contributing to a $150 million award.</p>
<ul class="outcome-metrics"><li><strong>$3M → $50M+</strong><span>annual business expansion</span></li><li><strong>$150M</strong><span>award contribution as sales-technical and program-management bid lead</span></li><li><strong>8 countries</strong><span>cross-functional program coordination</span></li></ul>
</article>
</div>
<p class="evidence-note">Selected prior-role scope and outcomes; these are not Lochlann client results.</p>
</div>
</section>
{EXPERIENCE_END}'''


PROOF_GRID = '''<div class="experience-proof-grid" data-reveal="">
<article>
<strong>25+</strong>
<span>Years across government and industry</span>
</article>
<article>
<strong>$1B+</strong>
<span>Annual opportunity portfolios</span>
</article>
<article>
<strong>14</strong>
<span>Direct reports across five global regions</span>
</article>
<article>
<strong>U.S. + International</strong>
<span>Customers, partners, teams, and sites</span>
</article>
</div>'''


README_TEXT = '''# Lochlann Strategies v17.4.0 — Executive Career Evidence

This release starts from v17.3.0 and makes Michael Maglothin’s executive scale, role progression, sales-operations leadership, federal capture record, and complex-program experience easier to verify without changing Lochlann’s company-first positioning.

## v17.4.0 update

- Preserves “Choose the right work. Win it. Deliver it.” and the company-first Home hierarchy.
- Changes the Home secondary career link to “View Michael’s Executive Background.”
- Adds a concise, recruiter- and buyer-usable career chronology to About.
- Keeps the 2019–2026 employer anonymous on the public site while retaining the role and relevant scope.
- Adds three evidence tracks: Federal Growth & Capture, Enterprise Growth & Sales Operations, and Complex Programs & Execution.
- Replaces generic Experience proof with visible executive-scale evidence.
- Adds three representative prior-role outcome modules with exact metric categories and attribution.
- States directly that prior-role scope and outcomes are not Lochlann client results.
- Adds no public résumé, job-seeking language, fabricated testimonial, or Lochlann client outcome.

## Preserved

- Dark navy and gold visual system, crest, imagery, fixed navigation, page architecture, and responsive behavior.
- `assets/lochlann-v17.2.2.css?v=17.2.2` as the unchanged base stylesheet.
- `assets/lochlann-v17.2.1.js?v=17.2.1` as the unchanged behavior layer.
- Current capabilities, engagement model, contact path, name-search SEO, and linked Person/Organization schema.
- The v17.2.1 removal of the circular operating map.

## Deployment

Upload the contents of the generated `lochlann-site-v17.4.0-executive-career-evidence.zip` to the existing GitHub Pages repository root in one commit, replacing prior files. Preserve any repository-only `CNAME` file.

No build process, package manager, external font service, JavaScript framework, or third-party runtime dependency is required.
'''


CHANGELOG_TEXT = '''# Lochlann Strategies — v17.4.0 Change Log

**Release date:** August 18, 2026  
**Baseline:** v17.3.0

## Implemented

- Preserved the company-first Home page and primary hero message.
- Changed the Home career CTA from “About Michael Maglothin” to “View Michael’s Executive Background,” linking directly to the new chronology.
- Added a six-stage career chronology to About.
- Identified the 2019–2026 role as “Global security-technology company,” preserving the decision not to name S2 Global on the public site.
- Added Federal Growth & Capture, Enterprise Growth & Sales Operations, and Complex Programs & Execution as distinct executive evidence tracks.
- Replaced the generic Experience proof strip with 25+ years, $1B+ annual opportunity portfolios, 14 direct reports across five regions, and U.S./international scope.
- Added selected prior-role evidence for global sales operations, federal capture, and international growth and delivery.
- Preserved exact distinctions among opportunity portfolios, pipeline, proposal/quotation activity, annual business, awards, B&P investment, and cost reduction.
- Added a supplemental, cache-versioned stylesheet; no existing CSS or JavaScript file was modified.
- Removed duplicate “Government requirements and acquisition” entries in structured-data knowledge lists and added global sales operations/CRM governance.

## Deliberately not added

- No résumé download.
- No statement that Michael is seeking employment.
- No client testimonial, Lochlann case study, or Lochlann outcome unsupported by the record.
- No restoration of S2 Global by name.
- No visual redesign, additional imagery, animation, or decorative content.
'''


DEPLOY_TEXT = '''LOCHLANN STRATEGIES v17.4.0 — DEPLOYMENT

1. Run apply-v17.4.0.command and select the current local Lochlann repository folder.
2. The patch creates a timestamped _rollback-v17.4.0-* folder inside that local repository.
3. The patch validates the updated files and creates:
   lochlann-site-v17.4.0-executive-career-evidence.zip
4. Open that generated ZIP and upload its CONTENTS to the GitHub repository root in one commit.
5. Preserve any repository-only CNAME file.
6. After GitHub Pages publishes, verify Home, About, and Experience on desktop and iPhone Safari.

The patch does not modify the v17.2.2 base CSS or v17.2.1 JavaScript.
'''


class ReferenceCollector(HTMLParser):
    """Collect local src/href references and basic landmark counts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []
        self.start_counts: dict[str, int] = {}
        self.end_counts: dict[str, int] = {}
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.start_counts[tag] = self.start_counts.get(tag, 0) + 1
        attr_map = dict(attrs)
        if attr_map.get("id"):
            self.ids.append(attr_map["id"] or "")
        for name in ("src", "href"):
            value = attr_map.get(name)
            if value:
                self.references.append(value)

    def handle_endtag(self, tag: str) -> None:
        self.end_counts[tag] = self.end_counts.get(tag, 0) + 1


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def remove_marker_block(text: str, start: str, end: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end) + r"\s*", re.DOTALL)
    return pattern.sub("", text)


def add_stylesheet(text: str) -> str:
    if STYLE_LINK in text:
        return text
    pattern = re.compile(r'(<link href="assets/lochlann-v17\.2\.2\.css\?v=17\.2\.2" rel="stylesheet"/>)')
    updated, count = pattern.subn(r"\1\n" + STYLE_LINK, text, count=1)
    if count != 1:
        raise PatchError("Could not locate the v17.2.2 base stylesheet link.")
    return updated


def insert_before(text: str, anchor: str, block: str, label: str) -> str:
    if text.count(anchor) != 1:
        raise PatchError(f"Expected one {label} anchor; found {text.count(anchor)}.")
    return text.replace(anchor, block + "\n" + anchor, 1)


def update_knowledge_lists(text: str) -> str:
    pattern = re.compile(
        r'(?P<indent>[ \t]*)"Government requirements and acquisition",\s*'
        r'"Federal, defense, and security markets",\s*'
        r'"Government requirements and acquisition",\s*'
        r'"Growth strategy and operations",'
    )

    def replacement(match: re.Match[str]) -> str:
        indent = match.group("indent")
        return (
            f'{indent}"Government requirements and acquisition",\n'
            f'{indent}"Federal, defense, and security markets",\n'
            f'{indent}"Growth strategy and operations",\n'
            f'{indent}"Global sales operations and CRM governance",'
        )

    return pattern.sub(replacement, text)


def patch_index(text: str) -> str:
    cta_pattern = re.compile(
        r'<a class="button" href="about\.html(?:#executive-background)?">\s*'
        r'<span>(?:About Michael Maglothin|View Michael’s Executive Background)</span>'
    )
    replacement = (
        '<a class="button" href="about.html#executive-background">'
        '<span>View Michael’s Executive Background</span>'
    )
    text, count = cta_pattern.subn(replacement, text, count=1)
    if count != 1:
        raise PatchError("Could not locate the Home career CTA.")
    return update_knowledge_lists(text)


def patch_about(text: str) -> str:
    text = remove_marker_block(text, ABOUT_START, ABOUT_END)
    text = add_stylesheet(text)
    old_meta_description = (
        "Michael Maglothin leads Lochlann Strategies with 25+ years across government acquisition, "
        "growth and capture, partner ecosystems, and complex delivery."
    )
    old_schema_description = (
        "Michael Maglothin is the founder and principal of Lochlann Strategies, advising defense, "
        "security, infrastructure, and operational-technology organizations on growth, capture, "
        "partnerships, and complex delivery."
    )
    new_description = (
        "Michael Maglothin is Founder and Principal of Lochlann Strategies, with 25+ years across "
        "government acquisition, federal and international growth, capture, sales operations, "
        "partnerships, and complex program delivery."
    )
    matched = False
    for old_description in (old_meta_description, old_schema_description):
        if old_description in text:
            text = text.replace(old_description, new_description)
            matched = True
    if not matched and new_description not in text:
        raise PatchError("About metadata did not match the v17.3.0 baseline.")
    text = insert_before(
        text,
        '<section class="section orientation-feature surface-deep">',
        ABOUT_BLOCK,
        "About orientation-feature",
    )
    return update_knowledge_lists(text)


def patch_experience(text: str) -> str:
    text = remove_marker_block(text, EXPERIENCE_START, EXPERIENCE_END)
    text = add_stylesheet(text)
    old_description = (
        "Michael Maglothin’s 25+ years across defense, national security, growth and capture, "
        "partner ecosystems, operational technology, and international delivery."
    )
    new_description = (
        "Michael Maglothin’s 25+ years across government acquisition, $1B+ opportunity portfolios, "
        "federal capture, global sales operations, partner ecosystems, and complex U.S. and "
        "international program delivery."
    )
    if old_description in text:
        text = text.replace(old_description, new_description)
    elif new_description not in text:
        raise PatchError("Experience metadata did not match the v17.3.0 baseline.")

    proof_pattern = re.compile(
        r'<div class="experience-proof-grid" data-reveal="">.*?</div>\s*'
        r'(?=<p class="evidence-note">)',
        re.DOTALL,
    )
    text, count = proof_pattern.subn(PROOF_GRID + "\n", text, count=1)
    if count != 1:
        raise PatchError("Could not locate the Experience proof grid.")

    hero_link_pattern = re.compile(
        r'(<a class="button" href=")#(?:lifecycle|career-evidence)(">\s*<span>)'
        r'(?:Follow the work|See selected evidence)(</span>)'
    )
    text, count = hero_link_pattern.subn(
        r'\1#career-evidence\2See selected evidence\3', text, count=1
    )
    if count != 1:
        raise PatchError("Could not locate the Experience hero action.")

    text = insert_before(
        text,
        '<section class="section lifecycle-section surface-navy" id="lifecycle">',
        EXPERIENCE_BLOCK,
        "Experience lifecycle",
    )
    return update_knowledge_lists(text)


def validate_json_ld(name: str, text: str, errors: list[str]) -> None:
    scripts = re.findall(
        r'<script\s+type="application/ld\+json">(.*?)</script>', text, flags=re.DOTALL
    )
    if not scripts:
        errors.append(f"{name}: no JSON-LD block found")
        return
    for index, script in enumerate(scripts, start=1):
        try:
            json.loads(script)
        except json.JSONDecodeError as exc:
            errors.append(f"{name}: JSON-LD block {index} is invalid: {exc}")


def validate_html(name: str, text: str, repo: Path, errors: list[str]) -> None:
    parser = ReferenceCollector()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # pragma: no cover - defensive
        errors.append(f"{name}: HTML parser error: {exc}")
        return

    for tag in ("html", "head", "body", "main"):
        if parser.start_counts.get(tag, 0) != 1:
            errors.append(f"{name}: expected one <{tag}>; found {parser.start_counts.get(tag, 0)}")
        if parser.end_counts.get(tag, 0) != 1:
            errors.append(f"{name}: expected one </{tag}>; found {parser.end_counts.get(tag, 0)}")
    if parser.start_counts.get("h1", 0) != 1:
        errors.append(f"{name}: expected one h1; found {parser.start_counts.get('h1', 0)}")

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        errors.append(f"{name}: duplicate IDs: {', '.join(duplicates)}")

    for reference in parser.references:
        if (
            reference.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#"))
            or reference.startswith("javascript:")
        ):
            continue
        clean = reference.split("#", 1)[0].split("?", 1)[0]
        if not clean:
            continue
        target = repo / clean
        if not target.exists():
            errors.append(f"{name}: missing local reference {clean}")

    validate_json_ld(name, text, errors)


def validate_site(repo: Path) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    data: dict[str, object] = {}
    texts: dict[str, str] = {}
    for name in ("index.html", "about.html", "experience.html"):
        path = repo / name
        if not path.exists():
            errors.append(f"Missing required file: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        validate_html(name, text, repo, errors)

    combined = "\n".join(texts.values())
    required_fragments = [
        "View Michael’s Executive Background",
        'id="executive-background"',
        'id="career-evidence"',
        "$1B+",
        "$1.5B+",
        "$600M+",
        "$2M",
        "4 → 20",
        "50%",
        "$200,000",
        "$3M → $50M+",
        "$150M",
        "Selected prior-role scope and outcomes; these are not Lochlann client results.",
        "Global sales operations and CRM governance",
    ]
    for fragment in required_fragments:
        if fragment not in combined:
            errors.append(f"Required content missing: {fragment}")

    if re.search(r"\bS2\s+Global\b", combined, flags=re.IGNORECASE):
        errors.append("Public HTML contains the prohibited employer name S2 Global.")

    for name, marker in (("about.html", ABOUT_START), ("experience.html", EXPERIENCE_START)):
        if texts.get(name, "").count(marker) != 1:
            errors.append(f"{name}: expected one v17.4.0 marker")
        if texts.get(name, "").count(STYLE_LINK) != 1:
            errors.append(f"{name}: expected one supplemental stylesheet link")

    css_path = repo / "assets" / STYLE_NAME
    if not css_path.exists():
        errors.append(f"Missing supplemental stylesheet: assets/{STYLE_NAME}")
    else:
        css_text = css_path.read_text(encoding="utf-8")
        if css_text.count("{") != css_text.count("}"):
            errors.append("Supplemental stylesheet has unbalanced braces.")
        data["supplemental_css_bytes"] = css_path.stat().st_size

    data.update(
        {
            "version": VERSION,
            "release_date": RELEASE_DATE,
            "pages_checked": sorted(texts),
            "required_content_checks": len(required_fragments),
            "errors": errors,
            "passed": not errors,
        }
    )
    return errors, data


def write_release_files(repo: Path) -> None:
    (repo / "README.md").write_text(README_TEXT, encoding="utf-8")
    (repo / f"CHANGELOG-v{VERSION}.md").write_text(CHANGELOG_TEXT, encoding="utf-8")
    (repo / f"DEPLOY-v{VERSION}.txt").write_text(DEPLOY_TEXT, encoding="utf-8")


def write_test_results(repo: Path, results: dict[str, object]) -> None:
    json_path = repo / f"test-results-v{VERSION}.json"
    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    status = "PASS" if results.get("passed") else "FAIL"
    errors = results.get("errors") or []
    error_lines = "\n".join(f"- {item}" for item in errors) if errors else "- None"
    report = f'''# Lochlann Strategies v{VERSION} Test Report

**Status:** {status}  
**Date:** August 18, 2026

## Scope

- Required page and landmark checks for Home, About, and Experience.
- JSON-LD parsing.
- Local `src` and `href` reference validation.
- Duplicate-ID checks.
- Supplemental CSS existence and brace balance.
- Required chronology, metrics, attribution language, and structured-data terms.
- Verification that “S2 Global” is absent from public HTML.

## Errors

{error_lines}

## Limitation

The patch performs deterministic static validation against the local repository. Final deployment should still be reviewed in desktop and iPhone Safari after GitHub Pages publishes.
'''
    (repo / f"TEST_REPORT-v{VERSION}.md").write_text(report, encoding="utf-8")


def write_hashes(repo: Path) -> None:
    names = [
        "index.html",
        "about.html",
        "experience.html",
        "README.md",
        f"CHANGELOG-v{VERSION}.md",
        f"DEPLOY-v{VERSION}.txt",
        f"TEST_REPORT-v{VERSION}.md",
        f"test-results-v{VERSION}.json",
        f"assets/{STYLE_NAME}",
    ]
    lines: list[str] = []
    for name in names:
        path = repo / name
        if path.exists():
            lines.append(f"{sha256(path)}  {name}")
    (repo / f"SHA256SUMS-v{VERSION}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def should_include(path: Path, repo: Path) -> bool:
    relative = path.relative_to(repo)
    parts = relative.parts
    if not parts:
        return False
    if parts[0] in {".git", ".github"}:
        return False
    if parts[0].startswith("_rollback-v17.4.0-"):
        return False
    if path.name == ".DS_Store" or path.name.endswith("~"):
        return False
    if path.suffix.lower() in {".zip", ".sha256"}:
        return False
    if path.name in {"apply-v17.4.0.py", "apply-v17.4.0.command"}:
        return False
    return path.is_file()


def create_deployment_zip(repo: Path) -> Path:
    output = repo.parent / "lochlann-site-v17.4.0-executive-career-evidence.zip"
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(repo.rglob("*")):
            if should_include(path, repo):
                archive.write(path, path.relative_to(repo).as_posix())
    return output


def copy_with_parents(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def apply_patch(repo: Path, make_zip: bool) -> tuple[Path | None, Path]:
    repo = repo.expanduser().resolve()
    required = [repo / "index.html", repo / "about.html", repo / "experience.html", repo / "assets"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise PatchError("Selected folder is not the current Lochlann repository. Missing: " + ", ".join(missing))

    source_css = Path(__file__).resolve().parent / "assets" / STYLE_NAME
    if not source_css.exists():
        raise PatchError(f"Patch package is missing assets/{STYLE_NAME}")

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup = repo / f"_rollback-v17.4.0-{timestamp}"
    backup.mkdir(parents=True, exist_ok=False)

    tracked_names = [
        "index.html",
        "about.html",
        "experience.html",
        "README.md",
        f"CHANGELOG-v{VERSION}.md",
        f"DEPLOY-v{VERSION}.txt",
        f"TEST_REPORT-v{VERSION}.md",
        f"test-results-v{VERSION}.json",
        f"SHA256SUMS-v{VERSION}.txt",
        f"assets/{STYLE_NAME}",
    ]
    preexisting: set[str] = set()
    for name in tracked_names:
        source = repo / name
        if source.exists():
            preexisting.add(name)
            copy_with_parents(source, backup / name)

    try:
        index_text = patch_index((repo / "index.html").read_text(encoding="utf-8"))
        about_text = patch_about((repo / "about.html").read_text(encoding="utf-8"))
        experience_text = patch_experience((repo / "experience.html").read_text(encoding="utf-8"))

        (repo / "index.html").write_text(index_text, encoding="utf-8")
        (repo / "about.html").write_text(about_text, encoding="utf-8")
        (repo / "experience.html").write_text(experience_text, encoding="utf-8")
        copy_with_parents(source_css, repo / "assets" / STYLE_NAME)
        write_release_files(repo)

        errors, results = validate_site(repo)
        write_test_results(repo, results)
        if errors:
            raise PatchError("Validation failed:\n- " + "\n- ".join(errors))
        write_hashes(repo)
        deployment_zip = create_deployment_zip(repo) if make_zip else None
        return deployment_zip, backup
    except Exception:
        for name in tracked_names:
            target = repo / name
            backup_file = backup / name
            if name in preexisting and backup_file.exists():
                copy_with_parents(backup_file, target)
            elif target.exists():
                target.unlink()
        raise


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply the Lochlann Strategies v17.4.0 executive-evidence patch."
    )
    parser.add_argument("repo", type=Path, help="Path to the current Lochlann repository folder")
    parser.add_argument("--no-zip", action="store_true", help="Apply and validate without creating a deployment ZIP")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        deployment_zip, backup = apply_patch(args.repo, make_zip=not args.no_zip)
    except PatchError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # pragma: no cover - defensive
        print(f"UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 3

    print(f"Lochlann Strategies v{VERSION} applied successfully.")
    print(f"Rollback backup: {backup}")
    if deployment_zip:
        print(f"Deployment ZIP: {deployment_zip}")
    print(f"Validation report: {args.repo.resolve() / f'TEST_REPORT-v{VERSION}.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
