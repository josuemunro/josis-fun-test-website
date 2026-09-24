"""Everything that is not a product, post or help article: home, about,
services, FAQ, contact, legal, the search results page and the oddities."""
import json
from model import Page, p, ul, ol, table, related, card_list, link, esc
from content.products import ALL_PRODUCTS, BY_SLUG as PRODUCTS, product_url
from content.blog import POSTS, post_url
from content.help_articles import ARTICLES, help_url

SEARCH_FORM = (
    '<form class="search hero-search" data-fs-search action="/search/" method="get" role="search">'
    '<label class="visually-hidden" for="hero-q">Search the site</label>'
    '<input id="hero-q" data-fs-input type="search" name="q" placeholder="Try &quot;oolong&quot;, &quot;descale&quot; or &quot;shipping&quot;" autocomplete="off">'
    '<button data-fs-submit type="submit">Search</button>'
    '</form>'
)


def _home() -> Page:
    featured = ["milford-mist-oolong", "wellington-breakfast", "gooseneck-kettle-pro", "kawakawa-mint", "tasting-flight-set", "cuba-street-chai"]
    latest = sorted(POSTS, key=lambda d: d["date"], reverse=True)[:4]
    body = [
        '<p class="tagline">Loose leaf tea and very good kettles from a windy corner of Wellington.</p>',
        SEARCH_FORM,
        "<h2>Featured</h2>",
        card_list([(product_url(s), PRODUCTS[s]["name"], PRODUCTS[s]["tagline"]) for s in featured]),
        "<h2>What we do</h2>",
        card_list([
            ("/services/subscription/", "Tea subscription", "A box of two or three teas every month, chosen by us, paused by you whenever."),
            ("/services/workshops/", "Tasting workshops", "Two hours, six teas, one very enthusiastic host, at the Petone café."),
            ("/services/corporate-tea-service/", "Corporate tea service", "Good tea for offices, with a Big Brew kettle and a monthly restock."),
            ("/services/kettle-repairs/", "Kettle repairs", "We fix our kettles, and most other people's, at the warehouse."),
        ]),
        "<h2>From the blog</h2>",
        card_list([(post_url(d["slug"]), d["title"], d["description"]) for d in latest]),
        "<h2>Popular help articles</h2>",
        ul([link(help_url(s), dict((a["slug"], a["title"]) for a in ARTICLES)[s]) for s in ("brewing-guide-oolong", "descaling-your-kettle", "shipping-times-nz", "kettle-error-codes", "pause-or-skip-a-box")]),
    ]
    return Page(
        path="/",
        title="Kererū Kettle Co. | Loose leaf tea and kettles, Wellington",
        description="Kererū Kettle Co. sells loose leaf tea, gooseneck and stovetop kettles and teaware from Petone, Wellington. Subscriptions, workshops and a help centre that actually helps.",
        h1="Kererū Kettle Co.",
        body="".join(body),
        section="home",
        jsonld={"@context": "https://schema.org", "@type": "Organization", "name": "Kererū Kettle Co.", "url": "/", "address": {"@type": "PostalAddress", "addressLocality": "Petone", "addressRegion": "Wellington", "addressCountry": "NZ"}},
        lastmod="2026-09-20",
    )


def _about() -> Page:
    body = p(
        "Kererū Kettle Co. started in 2022 as a folding table at the Cuba Street market with four teas and a borrowed kettle. Today we blend, pack and smoke tea in a former panel beater's in Petone, run a small café on the corner, and make a gooseneck kettle we are unreasonably proud of.",
        "We are named after the kererū, the native wood pigeon, because it is large, slightly ridiculous, and sits calmly in the trees through the worst weather Wellington can produce. We aspire to that.",
        "We sell about thirty things and we would rather sell those well than sell three hundred badly. Every tea is tasted every batch. Every kettle is boiled and temperature-checked before it ships. Every order before noon leaves the same day.",
    ) + card_list([
        ("/about/team/", "The team", "Six people, one dog, an alarming number of teapots."),
        ("/about/sustainability/", "Sustainability", "Compostable pouches, direct-trade leaf, and a kettle designed to be repaired."),
        ("/contact/", "Contact", "Email, phone, or come to the café in Petone."),
    ])
    return Page(path="/about/", title="About Kererū Kettle Co.", description="Who we are, how we started at the Cuba Street market, and why we are named after a pigeon.", h1="About us", body=body, section="about", lastmod="2026-07-01")


def _team() -> Page:
    body = p("Six of us, plus Biscuit the warehouse dog, who is not allowed near the smokehouse.") + table([
        ("Ana Reyes", "Founder, blender, oolong evangelist"),
        ("Tama Walker", "Founder, kettle engineer, smokehouse operator"),
        ("Priya Nair", "Café and workshops"),
        ("Josh Mackie", "Warehouse and shipping"),
        ("Lena Kruger", "Wholesale and corporate"),
        ("Sam Ihaka", "Website, photos, and the person who wrote this page"),
        ("Biscuit", "Morale"),
    ]) + p("Sam would like you to know that the site has an " + link("/easter-egg/", "easter egg") + ", which is not in the sitemap, and that nobody else on the team knows about it.")
    return Page(path="/about/team/", title="The team | Kererū Kettle Co.", description="Meet the six people and one dog behind Kererū Kettle Co. in Petone, Wellington.", h1="The team", body=body, section="about", lastmod="2026-07-01")


def _sustainability() -> Page:
    body = p(
        "Our pouches are home-compostable kraft and PLA, and the tins are steel, which is recycled essentially everywhere. We buy leaf directly from growers where we can, which currently means our Taiwanese oolong, our Japanese greens and the kawakawa; the rest comes through a single importer in Auckland who visits the gardens.",
        "The Gooseneck Kettle Pro was designed to be repaired. The element, the base controller and the lid are all replaceable parts and we stock them. We would rather fix a kettle than replace it, which is the opposite of how most small appliances are built, and we think that is a bit mad.",
        "We are not carbon neutral and we are not going to pretend we are by buying offsets. We are working on it. This page gets updated when there is something real to say.",
    ) + related("Related", [("/services/kettle-repairs/", "Kettle repairs"), (product_url("gooseneck-kettle-pro"), "Gooseneck Kettle Pro"), ("/blog/kawakawa-the-native-leaf/", "Kawakawa: the native leaf")])
    return Page(path="/about/sustainability/", title="Sustainability | Kererū Kettle Co.", description="Compostable packaging, direct-trade tea and a kettle built to be repaired. What we do and what we have not done yet.", h1="Sustainability", body=body, section="about", lastmod="2026-06-15")


def _contact() -> Page:
    body = p("Email is best. We answer within one business day, usually faster, unless the smokehouse is running.") + table([
        ("Email", "hello@kererukettle.example"),
        ("Phone", "04 555 0142 (weekdays 9 to 5)"),
        ("Café and warehouse", "14 Sydney Street, Petone, Lower Hutt 5012"),
        ("Café hours", "Tuesday to Sunday, 8 am to 3 pm"),
        ("Wholesale enquiries", "wholesale@kererukettle.example"),
        ("Press", "press@kererukettle.example"),
    ]) + p("For order problems, include your order number. For kettle problems, include a photo of the serial label under the base and any error code on the display.") + related("Before you email", [("/faq/", "Frequently asked questions"), ("/help/track-your-order/", "Track your order"), ("/help/kettle-error-codes/", "Kettle error codes")])
    return Page(path="/contact/", title="Contact | Kererū Kettle Co.", description="Email, phone and address for Kererū Kettle Co. in Petone, Wellington, plus café opening hours.", h1="Contact us", body=body, section="contact", lastmod="2026-08-01")


FAQS = [
    ("Do you sell tea bags?", "No. Everything is loose leaf. We think it tastes better, it is cheaper per cup, and it lets the leaf expand properly. The help centre has a guide to brewing without bags."),
    ("How long does shipping take?", "Orders before noon on a weekday ship the same day from Petone. Wellington next day, the rest of the North Island one to two days, South Island two to three. Rural adds a day or two."),
    ("Do you ship overseas?", "Tea and teaware to Australia, the UK, US, Canada, Singapore and Japan. Kettles to Australia only, because of plugs and voltage."),
    ("Can I pause my subscription?", "Yes, any time, from your account. Skip a month or pause indefinitely. Changes before the 25th apply to the next box."),
    ("What temperature should I brew green tea at?", "70 to 80 °C. Boiling water makes green tea bitter. The Gooseneck Kettle Pro has a Green preset at 75 °C; otherwise boil and wait three minutes."),
    ("How do I descale my kettle?", "A tablespoon of citric acid in a full kettle, boil, stand twenty minutes, rinse twice. Monthly in hard water areas. The help centre has the full steps."),
    ("What does error E2 on the kettle mean?", "Temperature sensor out of range, almost always limescale. Descale, unplug the base for a minute, and try again."),
    ("Is white tea low in caffeine?", "Not especially. Buds are caffeine-rich. Genmaicha is genuinely lower because half of it is rice, and herbals have none at all."),
    ("Do you do wholesale?", "Yes, for cafés, restaurants and shops. Minimum order is 2 kg of tea or six kettles. Email wholesale@kererukettle.example."),
    ("Where is the café?", "14 Sydney Street, Petone. Tuesday to Sunday, 8 am to 3 pm. The warehouse is out the back and you can usually smell whether the smokehouse is on."),
    ("What is the Mystery Box?", "A full-size tin of whatever tea we have too much of, for NZ$20. You cannot choose, but you can tell us if you need caffeine free."),
    ("Can I visit the smokehouse?", "Only during workshops, and only if the wind is in the right direction."),
]


def _faq() -> Page:
    body = [p("The questions we get most, answered briefly. Longer answers live in the " + link("/help/", "help centre") + ".")]
    for q, a in FAQS:
        body.append("<details><summary>{}</summary><p>{}</p></details>".format(esc(q), esc(a)))
    jsonld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS
    ]}
    return Page(path="/faq/", title="FAQ | Kererū Kettle Co.", description="Quick answers about shipping, subscriptions, brewing temperatures, descaling, caffeine, wholesale and the café.", h1="Frequently asked questions", body="".join(body), section="help", jsonld=jsonld, lastmod="2026-08-20")


SERVICES = [
    dict(slug="subscription", name="Tea subscription", tagline="Two or three teas a month, chosen by us, paused by you.",
         paras=["Every month we pick two or three teas, pack them with a brewing card and a note about why we chose them, and post them on the first. Small boxes are two 50 g pouches, standard is three, large is three 100 g pouches. Choose a caffeine preference: everything, low caffeine, or caffeine free.",
                "Pause, skip or cancel from your account at any time, with no fees. Subscribers get 10 percent off everything else on the site and first go at limited teas. The September box had Milford Mist Oolong, Genmaicha and a trial chamomile blend."],
         rows=[("Small", "NZ$24 per month, 2 x 50 g"), ("Standard", "NZ$34 per month, 3 x 50 g"), ("Large", "NZ$58 per month, 3 x 100 g"), ("Shipping", "Free within New Zealand")],
         links=[("/help/manage-your-subscription/", "Manage your subscription"), ("/help/pause-or-skip-a-box/", "Pause or skip a box"), ("/blog/subscription-box-september-unboxing/", "September box unboxing")]),
    dict(slug="workshops", name="Tasting workshops", tagline="Two hours, six teas, at the Petone café.",
         paras=["Our workshops run monthly at the café for up to sixteen people. The introduction to tasting covers white, green, oolong, black, smoked and herbal, with the vocabulary to describe them. The oolong deep dive does six oolongs gongfu-style. The tea and cheese night is exactly what it sounds like. The kettle clinic is free and you bring your broken kettle.",
                "Tickets are NZ$45 and include tea, a 20 g pouch of your favourite to take home, and a discount code. The next series starts in October."],
         rows=[("Introduction to tasting", "NZ$45, monthly"), ("Oolong deep dive", "NZ$45, every second month"), ("Tea and cheese", "NZ$55, every second month"), ("Kettle clinic", "Free, quarterly")],
         links=[("/blog/workshop-recap-winter/", "Winter workshop recap"), ("/blog/tasting-notes-vocabulary/", "A tasting vocabulary"), (product_url("tasting-flight-set"), "Tasting Flight Set, the take-home version")]),
    dict(slug="corporate-tea-service", name="Corporate tea service", tagline="Good tea for offices, with the kettle to make it.",
         paras=["We supply offices around Wellington with a Big Brew kettle or a Gooseneck Pro, a set of tins, and a monthly restock of three to five teas chosen with your team. It starts with a tasting session at your office so people actually choose things they will drink, rather than the chamomile nobody touches.",
                "Plans start at NZ$120 a month for up to 20 people. Kettles are on loan and maintained by us, including descaling."],
         rows=[("Up to 20 people", "NZ$120 per month"), ("Up to 50 people", "NZ$260 per month"), ("Larger", "Ask us"), ("Includes", "Kettle on loan, tins, monthly restock, tasting session")],
         links=[(product_url("the-big-brew-kettle"), "The Big Brew Kettle"), ("/services/wholesale/", "Wholesale"), ("/contact/", "Contact us")]),
    dict(slug="wholesale", name="Wholesale", tagline="Tea and kettles for cafés, restaurants and shops.",
         paras=["We supply about forty cafés and shops around New Zealand. Tea is available in 500 g and 1 kg foil bags or in our retail pouches with your choice of shelf display. Kettles are available in cartons of six. Minimum first order is 2 kg of tea or six kettles; reorders have no minimum.",
                "We provide brewing cards, staff training at the café or over video, and a listing on our stockists page. Email wholesale@kererukettle.example for the price list."],
         rows=[("Minimum first order", "2 kg tea or 6 kettles"), ("Lead time", "3 business days"), ("Training", "Included")],
         links=[("/services/corporate-tea-service/", "Corporate tea service"), ("/help/international-shipping/", "International shipping"), ("/contact/", "Contact")]),
    dict(slug="cafe", name="The Kererū Corner café", tagline="A small café at the front of the warehouse in Petone.",
         paras=["Eight tables, every tea on the menu, chai off the stovetop, iced Earl Grey lemonade in summer, and whatever the blending room got slightly wrong that morning as the daily special. Toasties. No coffee, sorry, there are four excellent cafés within a hundred metres.",
                "Open Tuesday to Sunday, 8 am to 3 pm, at 14 Sydney Street, Petone. Workshops run here in the evenings."],
         rows=[("Address", "14 Sydney Street, Petone"), ("Hours", "Tuesday to Sunday, 8 am to 3 pm"), ("Coffee", "No")],
         links=[("/services/workshops/", "Workshops"), ("/blog/iced-earl-grey-lemonade/", "Iced Earl Grey lemonade"), ("/blog/chai-at-home/", "Chai at home")]),
    dict(slug="kettle-repairs", name="Kettle repairs", tagline="We fix our kettles under warranty, and most kettles out of it.",
         paras=["Every part of the Gooseneck Kettle Pro is replaceable and we stock all of them. Within the two year warranty, repairs are free. Outside it, a new element is NZ$35 fitted and a new base controller is NZ$55. We will also have a look at other brands' kettles at the quarterly kettle clinic; usually the answer is descaling.",
                "Drop kettles at the café or post them to the warehouse. Turnaround is about a week."],
         rows=[("Element replacement", "NZ$35 fitted"), ("Base controller", "NZ$55 fitted"), ("Lid or gasket", "NZ$15"), ("Descale and check", "NZ$20, or free at a kettle clinic")],
         links=[("/help/warranty/", "Warranty"), ("/help/kettle-not-turning-on/", "Kettle will not turn on"), ("/about/sustainability/", "Why we repair kettles")]),
]


def _service_pages():
    out = [Page(
        path="/services/", title="Services | Kererū Kettle Co.",
        description="Tea subscriptions, tasting workshops, corporate tea service, wholesale, the Petone café and kettle repairs.",
        h1="Services", section="services", lastmod="2026-07-20",
        body=p("Beyond the shop: things we do for people, offices and cafés.") + card_list([("/services/{}/".format(s["slug"]), s["name"], s["tagline"]) for s in SERVICES]),
    )]
    for s in SERVICES:
        body = '<p class="tagline">{}</p>'.format(esc(s["tagline"])) + p(*s["paras"]) + "<h2>At a glance</h2>" + table(s["rows"]) + related("Related", s["links"])
        out.append(Page(
            path="/services/{}/".format(s["slug"]), title="{} | Kererū Kettle Co.".format(s["name"]),
            description=s["tagline"] + " " + s["paras"][0][:120].rsplit(" ", 1)[0] + ".",
            h1=s["name"], body=body, section="services", lastmod="2026-07-20",
            jsonld={"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["tagline"], "provider": {"@type": "Organization", "name": "Kererū Kettle Co."}},
        ))
    return out


def _search_page() -> Page:
    body = (
        '<form class="search" data-fs-search action="/search/" method="get" role="search">'
        '<label class="visually-hidden" for="q">Search</label>'
        '<input id="q" data-fs-input type="search" name="q" placeholder="Search teas, kettles, help articles…" autocomplete="off">'
        '<button data-fs-submit type="submit">Search</button></form>'
        '<p class="meta" data-fs-count-wrap>Showing <span data-fs-count>0</span> results for “<span data-fs-query></span>”</p>'
        '<div class="fs-summary" data-fs-summary style="display:none"></div>'
        '<div class="state" data-fs-loading style="display:none">Searching…</div>'
        '<div class="state" data-fs-empty style="display:none">No results. Try a different word, or browse the <a href="/help/">help centre</a>.</div>'
        '<div class="state" data-fs-error style="display:none">Search is not available right now. <span data-fs-error-message></span></div>'
        '<div class="results" data-fs-results>'
        '<article class="result" data-fs-result>'
        '<h2><a data-fs-url data-fs-title href="#"></a></h2>'
        '<p data-fs-snippet></p>'
        '<small class="result-meta"><span data-fs-category></span> · <span data-fs-url></span></small>'
        '</article>'
        '</div>'
        '<nav class="pagination" data-fs-pagination aria-label="Search results pages"></nav>'
        '<noscript><p>Search results need JavaScript and the FlowSearch results script. Without them, try the <a href="/help/">help centre</a> or the <a href="/products/">catalogue</a>.</p></noscript>'
    )
    return Page(
        path="/search/", title="Search | Kererū Kettle Co.",
        description="Search Kererū Kettle Co. for teas, kettles, blog posts and help articles.",
        h1="Search results", body=body, section="search", noindex=True, in_sitemap=False, lastmod="2026-09-20",
        test_note="Results page for the hosted results.js flow. Marked noindex and left out of the sitemap, as a real site would.",
    )


def _legal():
    privacy = Page(path="/privacy/", title="Privacy policy | Kererū Kettle Co.", description="What personal information Kererū Kettle Co. collects, why, and how to ask us to delete it.", h1="Privacy policy", section="legal", lastmod="2026-03-01",
                   body=p("We collect your name, email, delivery address and order history so we can send you tea. We use a payment processor and never see your full card number. We use a site search provider that records what people search for so we can make the search better, and an email provider for order confirmations and, if you opt in, the newsletter.",
                          "We do not sell your data. We do not run advertising. To see or delete what we hold, email hello@kererukettle.example and we will do it within ten business days. This policy is governed by the New Zealand Privacy Act 2020."))
    terms = Page(path="/terms/", title="Terms of sale | Kererū Kettle Co.", description="Terms of sale for orders from Kererū Kettle Co.: pricing, returns, warranty, subscriptions and the Consumer Guarantees Act.", h1="Terms of sale", section="legal", lastmod="2026-03-01",
                 body=p("All prices are in New Zealand dollars and include GST. Orders are accepted when we send the shipping confirmation. Unopened goods may be returned within 30 days; kettles are covered by the warranty described in the help centre. Subscriptions renew monthly on the first and can be cancelled from your account before the 25th.",
                        "Nothing in these terms limits your rights under the Consumer Guarantees Act 1993. If something is wrong, tell us and we will fix it.") + related("See also", [("/help/returns-and-exchanges/", "Returns and exchanges"), ("/help/warranty/", "Warranty"), ("/shipping-policy/", "Shipping policy")]))
    shipping = Page(path="/shipping-policy/", title="Shipping policy | Kererū Kettle Co.", description="Shipping costs, carriers, same-day dispatch cut-off and international shipping rules for Kererū Kettle Co. orders.", h1="Shipping policy", section="legal", lastmod="2026-03-01",
                    body=p("We ship from Petone with NZ Post and Aramex. Orders placed before 12 noon on a business day are dispatched the same day. Shipping within New Zealand is NZ$6.50, free over NZ$60. Rural delivery adds NZ$4. International rates are calculated at checkout by weight and destination; duties and taxes are the customer's responsibility.",
                           "If a parcel is lost or damaged in transit, we replace it. Contact us within 14 days of the expected delivery date.") + related("Help articles", [("/help/shipping-times-nz/", "Shipping times within New Zealand"), ("/help/international-shipping/", "International shipping"), ("/help/track-your-order/", "Track your order")]))
    return [privacy, terms, shipping]


def _not_found() -> Page:
    return Page(path="/404.html", title="Page not found | Kererū Kettle Co.", description="That page has gone the way of the lemon verbena.", h1="Page not found", section="", in_sitemap=False, noindex=True, lastmod="2026-01-01",
                body=p("That page has gone the way of the lemon verbena. Try the search box above, the " + link("/products/", "catalogue") + " or the " + link("/help/", "help centre") + "."))


def _easter_egg() -> Page:
    return Page(path="/easter-egg/", title="You found the easter egg | Kererū Kettle Co.", description="A hidden page about Biscuit the warehouse dog. Not in the sitemap.", h1="You found it", section="", in_sitemap=False, lastmod="2026-05-05",
                body=p("This page is linked from the team page and nowhere else, and it is deliberately missing from the sitemap. It exists to see whether the crawler follows links it was not told about.",
                       "Biscuit is a seven year old huntaway cross who joined the company in 2023 after wandering into the warehouse during a smokehouse run and refusing to leave. Biscuit's favourite tea is none of them. Biscuit's favourite thing is the courier.") + related("Back to reality", [("/about/team/", "The team"), ("/", "Home")]),
                test_note="Linked from the team page but deliberately left out of the sitemap.")


def _secret_menu() -> Page:
    return Page(path="/secret-menu/", title="The café secret menu | Kererū Kettle Co.", description="Off-menu drinks at the Kererū Corner café: the smoky chai, the oolong affogato and the double Earl Grey lemonade.", h1="The secret menu", section="", lastmod="2026-06-10",
                body=p("There is a secret menu at the café. It is not on the board and this page is not linked from anywhere on the site, so if you are reading it, someone told you or you found the sitemap.",
                       "The smoky chai: Cuba Street Chai simmered with a pinch of Mānuka Smoked Lapsang. The oolong affogato: a scoop of vanilla ice cream with a shot of very strong Midnight Oolong Roast poured over. The double: iced Earl Grey lemonade with a second cold brew of Pōhutukawa Berry floated on top. Ask for them by name.") + related("Ingredients", [(product_url("cuba-street-chai"), "Cuba Street Chai"), (product_url("manuka-smoked-lapsang"), "Mānuka Smoked Lapsang"), (product_url("midnight-oolong-roast"), "Midnight Oolong Roast")]),
                test_note="Orphan page: in the sitemap, linked from nowhere.")


def pages():
    out = [_home(), _about(), _team(), _sustainability(), _contact(), _faq(), _search_page()]
    out.extend(_service_pages())
    out.extend(_legal())
    out.extend([_not_found(), _easter_egg(), _secret_menu()])
    return out
