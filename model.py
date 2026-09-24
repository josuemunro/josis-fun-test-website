"""Shared page model and tiny HTML helpers for the Kererū Kettle Co. test site."""
from dataclasses import dataclass, field
from html import escape
from typing import Dict, List, Optional, Sequence, Tuple


@dataclass
class Page:
    path: str                      # e.g. "/products/wellington-breakfast/"
    title: str
    description: str
    h1: str
    body: str                      # inner HTML of <main>
    section: str = ""              # which nav item to highlight
    jsonld: Optional[dict] = None
    in_sitemap: bool = True        # False = linked but missing from sitemap
    omit_title: bool = False       # deliberately broken metadata for testing
    omit_description: bool = False
    omit_h1: bool = False
    noindex: bool = False
    lastmod: str = "2026-09-01"
    test_note: str = ""            # why this page exists; surfaced in the README


def esc(text: str) -> str:
    return escape(text, quote=True)


def p(*paragraphs: str) -> str:
    return "".join("<p>{}</p>".format(t) for t in paragraphs)


def ul(items: Sequence[str]) -> str:
    return "<ul>" + "".join("<li>{}</li>".format(i) for i in items) + "</ul>"


def ol(items: Sequence[str]) -> str:
    return "<ol>" + "".join("<li>{}</li>".format(i) for i in items) + "</ol>"


def link(href: str, text: str) -> str:
    return '<a href="{}">{}</a>'.format(href, esc(text))


def table(rows: Sequence[Tuple[str, str]], caption: str = "") -> str:
    out = ["<table class=\"specs\">"]
    if caption:
        out.append("<caption>{}</caption>".format(esc(caption)))
    for k, v in rows:
        out.append("<tr><th scope=\"row\">{}</th><td>{}</td></tr>".format(esc(k), esc(v)))
    out.append("</table>")
    return "".join(out)


def card_list(cards: Sequence[Tuple[str, str, str]]) -> str:
    """cards = [(href, title, blurb)] -> a grid of link cards."""
    out = ['<div class="cards">']
    for href, title, blurb in cards:
        out.append(
            '<a class="card" href="{}"><strong>{}</strong><span>{}</span></a>'.format(
                href, esc(title), esc(blurb)
            )
        )
    out.append("</div>")
    return "".join(out)


def related(title: str, links: Sequence[Tuple[str, str]]) -> str:
    if not links:
        return ""
    return '<aside class="related"><h2>{}</h2>{}</aside>'.format(
        esc(title), ul([link(h, t) for h, t in links])
    )
