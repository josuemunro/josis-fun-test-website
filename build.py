#!/usr/bin/env python3
"""Build the Kererū Kettle Co. test site into ./dist.

Plain Python 3.8+, no dependencies. Run `python3 build.py`.

Environment variables (all optional):
  SITE_URL                        Canonical origin used in sitemap.xml and
                                  canonical links. Falls back to Netlify's URL.
  FLOWSEARCH_VERIFICATION_TOKEN   Value for the flowsearch-site-verification
                                  meta tag. Defaults to the placeholder TOKEN.
  FLOWSEARCH_APP_URL              Origin that serves widget.js and results.js,
                                  e.g. https://app.flowsearch.example
  FLOWSEARCH_API_KEY              The website's fs_... key. When both this and
                                  FLOWSEARCH_APP_URL are set the widget and
                                  results scripts are emitted; otherwise an
                                  HTML comment placeholder is left in place.
"""
import json
import os
import shutil
from html import escape
from pathlib import Path
from typing import List

from model import Page
from content import products, blog, help_articles, pages as misc

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
STATIC = ROOT / "static"

SITE_URL = (os.environ.get("SITE_URL") or os.environ.get("URL") or "https://josis-fun-test-website.netlify.app").rstrip("/")
FS_TOKEN = os.environ.get("FLOWSEARCH_VERIFICATION_TOKEN", "b0a95fb2-8eed-450b-8819-4616b191d08c")
FS_APP_URL = os.environ.get("FLOWSEARCH_APP_URL", "https://www.flowsearch.io").rstrip("/")
FS_API_KEY = os.environ.get("FLOWSEARCH_API_KEY", "fs_your_key_here")

NAV = [
    ("products", "/products/", "Teas & kettles"),
    ("services", "/services/", "Services"),
    ("blog", "/blog/", "Blog"),
    ("help", "/help/", "Help"),
    ("about", "/about/", "About"),
    ("contact", "/contact/", "Contact"),
]


def header(active: str) -> str:
    items = []
    for key, href, label in NAV:
        cls = ' class="active"' if key == active else ""
        items.append('<li><a href="{}"{}>{}</a></li>'.format(href, cls, escape(label)))
    return (
        '<header class="site-header">'
        '<a class="brand" href="/"><span class="bird" aria-hidden="true">🐦</span> Kererū Kettle Co.</a>'
        '<nav class="site-nav" aria-label="Main"><ul>{}</ul></nav>'
        '<form class="search header-search" data-fs-search action="/search/" method="get" role="search">'
        '<label class="visually-hidden" for="header-q">Search</label>'
        '<input id="header-q" data-fs-input type="search" name="q" placeholder="Search…" autocomplete="off">'
        '<button data-fs-submit type="submit">Go</button>'
        '</form>'
        '</header>'
    ).format("".join(items))


FOOTER = (
    '<footer class="site-footer">'
    '<p>Kererū Kettle Co. · 14 Sydney Street, Petone, Wellington · A fictional company built as a FlowSearch test site.</p>'
    '<ul><li><a href="/faq/">FAQ</a></li><li><a href="/shipping-policy/">Shipping</a></li><li><a href="/privacy/">Privacy</a></li>'
    '<li><a href="/terms/">Terms</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul>'
    '</footer>'
)


def flowsearch_head() -> str:
    return (
        "\n<!-- FlowSearch site verification. Replace TOKEN with the token from the FlowSearch dashboard,\n"
        "     or set FLOWSEARCH_VERIFICATION_TOKEN in the build environment. -->\n"
        '<meta name="flowsearch-site-verification" content="{}">\n'.format(escape(FS_TOKEN))
    )


def flowsearch_widget() -> str:
    if FS_APP_URL and FS_API_KEY:
        return (
            '<script src="{}/widget.js" data-key="{}" data-results-page="/search/" data-live="true"></script>\n'
            .format(FS_APP_URL, escape(FS_API_KEY))
        )
    return (
        "<!-- FlowSearch widget placeholder. After onboarding, drop the tag here or set FLOWSEARCH_APP_URL and FLOWSEARCH_API_KEY:\n"
        '     <script src="https://YOUR-FLOWSEARCH-APP/widget.js" data-key="fs_xxxxx" data-results-page="/search/" data-live="true"></script> -->\n'
    )


def flowsearch_results() -> str:
    if FS_APP_URL and FS_API_KEY:
        return '<script src="{}/results.js" data-key="{}" data-summary="true"></script>\n'.format(FS_APP_URL, escape(FS_API_KEY))
    return (
        "<!-- FlowSearch results placeholder. After onboarding, drop the tag here or set FLOWSEARCH_APP_URL and FLOWSEARCH_API_KEY:\n"
        '     <script src="https://YOUR-FLOWSEARCH-APP/results.js" data-key="fs_xxxxx" data-summary="true"></script> -->\n'
    )


def render(page: Page) -> str:
    head = ['<!doctype html>', '<html lang="en">', "<head>", '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">']
    if not page.omit_title:
        head.append("<title>{}</title>".format(escape(page.title)))
    if not page.omit_description:
        head.append('<meta name="description" content="{}">'.format(escape(page.description)))
    if page.noindex:
        head.append('<meta name="robots" content="noindex">')
    if page.path != "/404.html":
        head.append('<link rel="canonical" href="{}{}">'.format(SITE_URL, page.path))
    head.append(flowsearch_head())
    head.append('<link rel="stylesheet" href="/style.css">')
    if page.jsonld:
        data = dict(page.jsonld)
        if data.get("url") == "/":
            data["url"] = SITE_URL + "/"
        head.append('<script type="application/ld+json">{}</script>'.format(json.dumps(data, ensure_ascii=False)))
    head.append("</head>")

    h1 = "" if page.omit_h1 else "<h1>{}</h1>".format(escape(page.h1))
    body = [
        "<body>",
        '<a class="skip" href="#main">Skip to content</a>',
        header(page.section),
        '<main id="main" class="content">', h1, page.body, "</main>",
        FOOTER,
        flowsearch_widget(),
    ]
    if page.path == "/search/":
        body.append(flowsearch_results())
    body.append("</body></html>")
    return "\n".join(head) + "\n" + "\n".join(body)


def out_path(page: Page) -> Path:
    if page.path == "/404.html":
        return DIST / "404.html"
    rel = page.path.strip("/")
    return (DIST / rel / "index.html") if rel else (DIST / "index.html")


def sitemap(all_pages: List[Page]) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pg in all_pages:
        if not pg.in_sitemap:
            continue
        lines.append("  <url><loc>{}{}</loc><lastmod>{}</lastmod></url>".format(SITE_URL, escape(pg.path), pg.lastmod))
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def robots() -> str:
    return "User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE_URL)


def main() -> None:
    all_pages = misc.pages() + products.pages() + blog.pages() + help_articles.pages()
    seen = set()
    for pg in all_pages:
        if pg.path in seen:
            raise SystemExit("duplicate path: " + pg.path)
        seen.add(pg.path)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for pg in all_pages:
        target = out_path(pg)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(pg), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(sitemap(all_pages), encoding="utf-8")
    (DIST / "robots.txt").write_text(robots(), encoding="utf-8")
    for f in STATIC.iterdir():
        shutil.copy(f, DIST / f.name)

    in_map = sum(1 for pg in all_pages if pg.in_sitemap)
    print("Built {} pages ({} in sitemap) to {}".format(len(all_pages), in_map, DIST))
    print("Site URL: {}".format(SITE_URL))
    print("FlowSearch scripts: {}".format("emitted" if (FS_APP_URL and FS_API_KEY) else "placeholder comments only"))
    print("\nDeliberate edge cases:")
    for pg in all_pages:
        if pg.test_note:
            print("  {:<40} {}".format(pg.path, pg.test_note))


if __name__ == "__main__":
    main()
