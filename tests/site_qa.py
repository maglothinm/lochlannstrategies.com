#!/usr/bin/env python3
"""Static and Chromium QA for Lochlann Strategies.

Runs from the repository root. Browser cases exercise desktop and mobile
rendering without third-party sites or user data.
"""
from __future__ import annotations

from datetime import datetime
from functools import partial
from html import unescape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import re
import threading
import xml.etree.ElementTree as ET

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "qa-artifacts"
PAGES = [
    "index.html", "services.html", "engagements.html",
    "experience.html", "about.html", "contact.html", "404.html",
]
VIEWPORTS = {"desktop": (1440, 1000), "mobile": (390, 844)}
QA_DATE = "2026-10-14"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def metadata(html: str, key: str) -> str | None:
    for tag in re.findall(r"<meta\b[^>]*>", html):
        if f'name="{key}"' in tag or f'property="{key}"' in tag:
            match = re.search(r'content="([^"]*)"', tag)
            return unescape(match.group(1)) if match else None
    return None


def validate_static() -> dict:
    page_ids = {}
    contents = {}
    for path in PAGES:
        html = (ROOT / path).read_text(encoding="utf-8")
        contents[path] = html
        require(len(re.findall(r"<h1\b", html)) == 1, f"{path}: expected one H1")
        require(len(re.findall(r"<main\b", html)) == 1, f"{path}: expected one main")
        require(len(re.findall(r"</main>", html)) == 1, f"{path}: missing closing main")
        for name in ("section", "article", "figure", "aside"):
            require(
                len(re.findall(rf"<{name}\b", html)) == len(re.findall(rf"</{name}>", html)),
                f"{path}: unbalanced {name}"
            )
        ids = re.findall(r'\bid="([^"]+)"', html)
        require(len(ids) == len(set(ids)), f"{path}: duplicate HTML ID")
        page_ids[path] = set(ids)
        jsonld = re.findall(
            r'<script type="application/ld\+json">([\s\S]*?)</script>', html
        )
        require(jsonld, f"{path}: no JSON-LD")
        for raw in jsonld:
            data = json.loads(raw)
            graph = data.get("@graph", [data])
            for item in graph:
                stamp = item.get("dateModified")
                if stamp:
                    require(
                        bool(re.fullmatch(
                            r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:Z|[+-]\d\d:\d\d)", stamp
                        )),
                        f"{path}: dateModified must be ISO 8601 date-time with timezone: {stamp}",
                    )
                    value = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
                    require(value.tzinfo is not None, f"{path}: naive dateModified")
                    if path in {"index.html", "about.html", "experience.html"}:
                        require(value.date().isoformat() == QA_DATE,
                                f"{path}: stale dateModified")
        require(bool(metadata(html, "og:image")), f"{path}: missing Open Graph image")
        require(bool(metadata(html, "twitter:card")), f"{path}: missing Twitter card")
        require('rel="canonical"' in html, f"{path}: canonical missing")

    for path, html in contents.items():
        refs = re.findall(r'\b(?:href|src)="([^"]+)"', html)
        for srcset in re.findall(r'\bsrcset="([^"]+)"', html):
            refs.extend(part.strip().split()[0] for part in srcset.split(","))
        for ref in refs:
            if not ref or re.match(r"^(https?:|mailto:|tel:|data:|javascript:|//)", ref):
                continue
            relative, _, fragment = ref.partition("#")
            pathname = relative.split("?")[0].lstrip("/")
            target = (ROOT / pathname) if pathname else (ROOT / path)
            require(target.is_file(), f"{path}: broken reference {ref}")
            if fragment and pathname.endswith(".html"):
                require(fragment in page_ids.get(pathname, set()),
                        f"{path}: missing target fragment {ref}")
            if fragment and not pathname:
                require(fragment in page_ids[path], f"{path}: missing local anchor {ref}")

    home = contents["index.html"]
    about = contents["about.html"]
    exp = contents["experience.html"]
    require("Success delivery" not in home and "spans across" not in home,
            "Home: outdated hero copy")
    require("Each engagement is shaped around your priorities, team, and schedule." in home,
            "Home: approved hero wording missing")
    title = unescape(re.search(r"<title>([^<]+)</title>", about).group(1))
    require(title == "Michael Maglothin | Executive Growth & Capture Leadership",
            "About: SEO title mismatch")
    require(metadata(about, "og:title") == title, "About: Open Graph title mismatch")
    require(metadata(about, "twitter:title") == title,
            "About: Twitter title mismatch")
    require("Founder &amp; Principal" in about, "About: founder title removed")
    require(about.count("<blockquote>") == 1, "About: expected one executive quote")
    require(exp.count("<blockquote>") == 3, "Experience: expected three quotes")
    require("Additional perspectives" not in exp, "Experience: secondary quotes remain")
    require("They do not describe Lochlann client engagements" in exp,
            "Experience: prior-role disclaimer missing")
    start = exp.index('id="professional-perspectives"')
    end = exp.index('id="customer-footprint"', start)
    segment = exp[start:end]
    for forbidden in (
        "General Dynamics", "Honeywell", "Jonathan Fleming", "Red Millander",
        "Derrick Nixon", "Steve Coughlan", "Jeff Hassannia", "Larry Cassenti",
        "Derrell James", "Former ", "former ",
    ):
        require(forbidden not in segment,
                f"Experience endorsement section reveals {forbidden!r}")
    for phrase in (
        "Senior Director</span><span class=\"endorsement-context\">· Security Solutions",
        "Senior Director</span><span class=\"endorsement-context\">· Business Development, Security Technology",
        "Vice President</span><span class=\"endorsement-context\">· Secure Network Solutions",
    ):
        require(phrase in segment, f"Experience: missing attribution {phrase}")
    require("· Global Security Technology" in about,
            "About: missing anonymous company-president attribution")

    sitemap = ET.parse(ROOT / "sitemap.xml")
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    mod = {
        entry.findtext(f"{ns}loc"): entry.findtext(f"{ns}lastmod")
        for entry in sitemap.getroot().findall(f"{ns}url")
    }
    for tail in ("", "about.html", "experience.html"):
        url = "https://lochlannstrategies.com/" + tail
        require(mod.get(url) == QA_DATE,
                f"Sitemap stale/missing modification date: {url}")

    styles = set()
    for html in contents.values():
        for href in re.findall(r'<link href="([^"]+\.css(?:\?[^"]*)?)" rel="stylesheet"', html):
            styles.add(href.split("?")[0])
    for path in styles:
        raw = (ROOT / path).read_text(encoding="utf-8")
        require(raw.count("{") == raw.count("}"), f"{path}: unbalanced CSS")
    require("assets/lochlann-endorsements-v17.5.3.css" in styles,
            "Endorsement stylesheet missing")
    return {
        "pages": len(PAGES),
        "local_references": "PASS",
        "JSON-LD": "PASS",
        "dateModified": "PASS",
        "sitemap": "PASS",
        "quotes": {"about": 1, "experience": 3},
        "stylesheets_checked": len(styles),
    }


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args) -> None:
        return


def validate_browser() -> list[dict]:
    cases = []
    handler = partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    runner = threading.Thread(target=server.serve_forever, daemon=True)
    runner.start()
    origin = f"http://127.0.0.1:{server.server_port}"
    shots = OUT / "screenshots"
    shots.mkdir(parents=True, exist_ok=True)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            try:
                for viewport_name, (width, height) in VIEWPORTS.items():
                    context = browser.new_context(
                        viewport={"width": width, "height": height},
                        device_scale_factor=1,
                        reduced_motion="reduce",
                    )
                    try:
                        for filename in PAGES:
                            page = context.new_page()
                            errors: list[str] = []
                            page.on("pageerror", lambda e: errors.append(str(e)))
                            page.on(
                                "console",
                                lambda msg: errors.append(msg.text) if msg.type == "error" else None
                            )
                            page.on(
                                "requestfailed",
                                lambda req: errors.append(f"Request failed: {req.url}")
                                if req.url.startswith(origin) else None,
                            )
                            response = page.goto(
                                f"{origin}/{filename}", wait_until="load", timeout=30000
                            )
                            require(response is not None and response.status == 200,
                                    f"{filename}/{viewport_name}: HTTP failure")
                            require(page.locator("main").count() == 1,
                                    f"{filename}/{viewport_name}: no main")
                            require(page.locator("h1").count() == 1,
                                    f"{filename}/{viewport_name}: H1 count")
                            page.wait_for_timeout(100)
                            overflow = page.evaluate(
                                "document.documentElement.scrollWidth - window.innerWidth"
                            )
                            require(overflow <= 2,
                                    f"{filename}/{viewport_name}: overflow {overflow}px")
                            if filename in ("about.html", "experience.html"):
                                quote_count = page.locator(".endorsement-quote").count()
                                expected = 1 if filename == "about.html" else 3
                                require(quote_count == expected,
                                        f"{filename}/{viewport_name}: {quote_count} quotes")
                                for card in page.locator(".endorsement-quote").all():
                                    box = card.bounding_box()
                                    require(box is not None,
                                            f"{filename}/{viewport_name}: quote not rendered")
                                    require(box["x"] >= -2 and box["x"] + box["width"] <= width + 2,
                                            f"{filename}/{viewport_name}: quote clipped")
                                    own_overflow = card.evaluate(
                                        "node => node.scrollWidth - node.clientWidth"
                                    )
                                    require(own_overflow <= 2,
                                            f"{filename}/{viewport_name}: quote text clipped")
                                if filename == "experience.html":
                                    columns = page.locator(".endorsement-quote-grid").first.evaluate(
                                        "node => getComputedStyle(node).gridTemplateColumns.split(' ').length"
                                    )
                                    expected_cols = 1 if viewport_name == "mobile" else 3
                                    require(columns == expected_cols,
                                            f"{filename}/{viewport_name}: grid columns {columns}")
                            if viewport_name == "mobile":
                                toggle = page.locator("[data-menu-toggle]")
                                if toggle.count() and toggle.is_visible():
                                    toggle.click()
                                    require(page.locator("[data-mobile-menu]").is_visible(),
                                            f"{filename}: mobile nav failed to open")
                                    page.keyboard.press("Escape")
                                    # Some releases only close on toggle click.
                                    if page.locator("[data-mobile-menu]").is_visible():
                                        toggle.click()
                                    require(not page.locator("[data-mobile-menu]").is_visible(),
                                            f"{filename}: mobile nav failed to close")
                            require(not errors, f"{filename}/{viewport_name}: browser errors: {errors}")
                            if filename in ("index.html", "about.html", "experience.html"):
                                path = shots / f"{filename.removesuffix('.html')}-{viewport_name}.png"
                                page.screenshot(path=str(path), full_page=True,
                                                animations="disabled")
                            cases.append({
                                "page": filename, "viewport": viewport_name,
                                "http": 200, "horizontal_overflow_px": overflow,
                                "console_errors": len(errors), "pass": True,
                            })
                            page.close()
                    finally:
                        context.close()
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return cases


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    result: dict = {"release": "17.5.4", "static": {}, "browser": [], "pass": False}
    try:
        result["static"] = validate_static()
        result["browser"] = validate_browser()
        result["pass"] = True
        print(f"PASS: static checks; {len(result['browser'])} responsive browser cases.")
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        print(f"FAIL: {result['error']}")
        raise
    finally:
        (OUT / "site-qa-results.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
