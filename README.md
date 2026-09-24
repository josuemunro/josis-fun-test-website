# Kererū Kettle Co. — a FlowSearch test site

A fictional Wellington tea and kettle shop, generated as plain static HTML so the
FlowSearch crawler has something realistic to chew on. About 100 pages: products,
services, blog posts, help articles, an FAQ, legal pages, and a handful of
deliberately awkward pages (orphans, missing metadata, noindex).

No JavaScript is needed to read any content. The only scripts are the FlowSearch
widget (every page) and results script (`/search/` only), loaded from
www.flowsearch.io. Live site: https://josis-fun-test-website.netlify.app

## Build

```bash
python3 build.py        # writes ./dist (Python 3.8+, no dependencies)
python3 -m http.server -d dist 8000   # preview at http://localhost:8000
```

The build prints the page count and the list of edge-case pages.

## Deploy on Netlify

The Netlify site `josis-fun-test-website` is linked to this repo and builds on
every push to `main` using the command and publish directory in `netlify.toml`.
`SITE_URL` is picked up from Netlify's built-in `URL` variable, so the sitemap
and canonical links point at the real deploy.

The FlowSearch verification token, script origin and widget key are committed
as defaults near the top of `build.py`. The widget key is a public key that
ends up in the page HTML anyway. Environment variables override the defaults:

| Variable | Purpose |
| --- | --- |
| `FLOWSEARCH_VERIFICATION_TOKEN` | Fills the `flowsearch-site-verification` meta tag. |
| `FLOWSEARCH_APP_URL` | Origin serving `widget.js` and `results.js`. |
| `FLOWSEARCH_API_KEY` | The website's `fs_...` widget key. Set both this and the origin to empty to emit placeholder comments instead of script tags. |
| `SITE_URL` | Override the canonical origin. |

Note: a Netlify site is HTTPS, so browsers block a widget script loaded from a
plain `http://localhost:3000`. To test the widget against a local FlowSearch app,
expose it over HTTPS (ngrok, Cloudflare tunnel) or use the deployed app.

## What the site exercises

- `sitemap.xml` at the root with `lastmod`, and a permissive `robots.txt`.
- `<title>`, `<meta name="description">` and `<h1>` on nearly every page.
- JSON-LD: `Product`, `BlogPosting`, `Service`, `Organization`, and `FAQPage` on `/faq/`.
- Content categories the crawler recognises from URL paths: `/products/`, `/services/`, `/blog/`, `/help/`, `/about/`.
- Shared vocabulary across sections (oolong, steep, temperature, descale, gooseneck, chai) so ranking has to work.
- Search forms with `data-fs-search` / `data-fs-input` in the header and on the home page.
- `/search/` with the full `results.js` markup (results template, count, query, loading, empty, error, pagination, summary).

### Deliberate edge cases

| Page | What is odd about it |
| --- | --- |
| `/products/mystery-box/` | Linked and in the sitemap, but no `<h1>`. |
| `/blog/untitled-draft/` | Linked from the blog index, but no `<title>`, description or `<h1>`. |
| `/help/legacy-brewing-chart/` | Orphan (sitemap only), no description, no `<h1>`. |
| `/products/discontinued-lemon-verbena/` | Orphan: in the sitemap, linked from nowhere. |
| `/blog/unlisted-staff-picks/` | Orphan blog post, sitemap only. |
| `/secret-menu/` | Orphan, sitemap only. |
| `/help/internal-notes/` | In the sitemap, unlinked, `noindex` meta tag. |
| `/easter-egg/` | Linked from `/about/team/` but missing from the sitemap. |
| `/search/` | `noindex`, not in the sitemap, results page for the hosted flow. |
| `/404.html` | Netlify's custom 404. |

## Layout

```
build.py            generator and HTML layout
model.py            Page dataclass and small HTML helpers
content/products.py teas, kettles, accessories
content/blog.py     blog posts
content/help_articles.py  help centre
content/pages.py    home, about, services, FAQ, contact, search, legal, oddities
static/style.css    copied into dist/
netlify.toml        build settings
```
