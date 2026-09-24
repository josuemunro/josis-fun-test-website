"""Help centre articles, grouped by category. Some overlap with blog posts on
purpose (descaling, temperatures, caffeine) so search ranking has to choose."""
from model import Page, p, ul, ol, table, related, card_list, link, esc
from content.products import BY_SLUG as PRODUCTS, product_url

CATEGORIES = [
    ("brewing", "Brewing guides"),
    ("orders", "Orders and shipping"),
    ("subscriptions", "Subscriptions"),
    ("kettles", "Kettles and troubleshooting"),
    ("account", "Account and gift cards"),
]


def _a(slug, title, description, cat, paras, steps=None, rows=None, products=(), see_also=()):
    return dict(slug=slug, title=title, description=description, cat=cat, paras=paras,
                steps=steps or [], rows=rows or [], products=products, see_also=see_also)


ARTICLES = [
    # Brewing
    _a("brewing-guide-black-tea", "Brewing guide: black tea",
       "How to brew loose leaf black tea: 95 °C water, 3 to 4 minutes, 3 grams per cup. Includes milk and re-steeping notes.",
       "brewing",
       ["Black tea is the most forgiving of the true teas. It wants hot water, a few minutes, and a decent amount of leaf. It takes milk, sugar, lemon or nothing at all."],
       steps=["Boil the kettle, or set it to 95 °C.", "Add 3 g of leaf (about one heaped teaspoon) per 250 ml cup to a warmed pot.", "Pour, cover and steep for 3 to 4 minutes. Longer is stronger, and past 5 minutes it turns astringent.", "Pour through a strainer or lift out the infuser. Add milk if you like."],
       rows=[("Water", "95 °C"), ("Time", "3 to 4 minutes"), ("Leaf", "3 g per 250 ml"), ("Re-steeps", "1 to 2")],
       products=["wellington-breakfast", "southerly-earl-grey", "manuka-smoked-lapsang"],
       see_also=[("/help/how-much-tea-per-cup/", "How much tea per cup?"), ("/blog/water-temperature-guide/", "The water temperature guide")]),
    _a("brewing-guide-green-tea", "Brewing guide: green tea",
       "How to brew green tea without bitterness: 70 to 80 °C water, 1 to 2 minutes, and why boiling water ruins it.",
       "brewing",
       ["Green tea gets bitter for one reason: the water was too hot. Steamed Japanese greens like Zealandia Green want 70 to 80 °C; pan-fired Chinese greens tolerate a little more. If your kettle only boils, leave the lid open for three minutes before pouring."],
       steps=["Heat water to 75 °C, or boil and wait three to four minutes.", "Add 3 g of leaf per 200 ml to a warmed pot.", "Steep 60 to 90 seconds for the first infusion.", "Pour out completely so the leaves stop brewing. Re-steep two or three times, adding 30 seconds each time."],
       rows=[("Water", "70 to 80 °C"), ("Time", "60 to 90 seconds"), ("Leaf", "3 g per 200 ml"), ("Re-steeps", "2 to 3")],
       products=["zealandia-green", "genmaicha-toasted-rice", "gooseneck-kettle-pro"],
       see_also=[("/help/kettle-temperature-presets/", "Kettle temperature presets"), ("/blog/water-temperature-guide/", "The water temperature guide")]),
    _a("brewing-guide-oolong", "Brewing guide: oolong",
       "Brew oolong tea gongfu-style: 5 to 6 grams in a 150 ml pot, 85 to 95 °C, short steeps that lengthen with each infusion.",
       "brewing",
       ["Oolong is best brewed with lots of leaf, little water and short, repeated steeps. This is the gongfu method and it is where oolong shows off. You can also brew it western-style in a big pot, using 3 g per 250 ml for three minutes, but you will get fewer, flatter infusions."],
       steps=["Warm a 150 ml pot or gaiwan with hot water and discard.", "Add 5 to 6 g of leaf. It will look like too much; it is not.", "Pour water at 85 °C for light oolongs (Milford Mist) or 95 °C for roasted (Midnight).", "Steep 45 seconds, then pour everything out into a jug or cups.", "Repeat, adding 15 to 20 seconds each steep. Expect six or more infusions."],
       rows=[("Water", "85 °C light, 95 °C roasted"), ("Time", "45 seconds, then longer each steep"), ("Leaf", "6 g per 150 ml"), ("Re-steeps", "5 to 8")],
       products=["milford-mist-oolong", "midnight-oolong-roast", "ceramic-teapot-600"],
       see_also=[("/blog/how-to-steep-oolong-properly/", "How to steep oolong properly"), ("/help/kettle-temperature-presets/", "Kettle temperature presets")]),
    _a("brewing-guide-herbal", "Brewing guide: herbal and fruit tisanes",
       "Chamomile, peppermint, kawakawa and fruit blends want boiling water and a long steep of 5 to 7 minutes. Here is how.",
       "brewing",
       ["Herbal and fruit tisanes are not made from the tea plant, so they do not go bitter with heat or time. Use boiling water and steep long. If anything, most people under-steep them."],
       steps=["Boil the kettle.", "Add 2 to 3 g per 250 ml, a generous teaspoon, to a pot or infuser.", "Steep 5 to 7 minutes, covered, so the aromatics do not escape.", "Fruit blends can go longer and also cold brew well overnight."],
       rows=[("Water", "100 °C"), ("Time", "5 to 7 minutes"), ("Leaf", "2 to 3 g per 250 ml"), ("Re-steeps", "1")],
       products=["golden-bay-chamomile", "kawakawa-mint", "pohutukawa-berry", "sleepy-tui-blend"],
       see_also=[("/blog/cold-brew-tea-summer/", "Cold brew tea for summer"), ("/blog/tea-and-sleep/", "Tea and sleep")]),
    _a("brewing-guide-white-tea", "Brewing guide: white tea",
       "How to brew silver needle white tea: 80 °C water, 4 to 5 minutes, and more leaf than you expect because the buds are light.",
       "brewing",
       ["White tea is delicate and light, in both flavour and weight. Buds are fluffy, so a 'teaspoon' is barely anything; weigh it if you can. Water should be well below boiling and the steep should be long."],
       steps=["Heat water to 80 °C.", "Add 4 g per 250 ml, which looks like a small handful of buds.", "Steep 4 to 5 minutes.", "Re-steep twice, adding a minute each time."],
       rows=[("Water", "80 °C"), ("Time", "4 to 5 minutes"), ("Leaf", "4 g per 250 ml"), ("Re-steeps", "2 to 3")],
       products=["harbour-fog-white", "glass-teapot-with-infuser", "brew-thermometer"],
       see_also=[("/blog/what-is-white-tea/", "What is white tea?")]),
    _a("how-much-tea-per-cup", "How much tea per cup?",
       "A quick reference for grams and teaspoons of loose leaf tea per cup, by tea type, and why weighing beats spooning.",
       "brewing",
       ["The honest answer is 'weigh it', because a teaspoon of rolled oolong weighs three times as much as a teaspoon of fluffy white tea. A cheap kitchen scale that reads to 0.1 g is the best tea gadget you can buy after a kettle. Failing that, use this table."],
       rows=[("Black tea", "3 g, about 1 heaped teaspoon per 250 ml"), ("Green tea", "3 g, about 1 heaped teaspoon per 200 ml"), ("Oolong (rolled)", "6 g per 150 ml gongfu, or 3 g per 250 ml western"), ("White tea", "4 g, about 2 heaped teaspoons per 250 ml"), ("Herbal", "2 to 3 g, 1 generous teaspoon per 250 ml"), ("Chai (simmered)", "4 g per 250 ml")],
       products=["tasting-flight-set", "tea-timer-hourglass"],
       see_also=[("/blog/tea-for-people-who-hate-tea/", "Tea for people who hate tea")]),
    _a("caffeine-content-chart", "Caffeine content chart",
       "Approximate caffeine per 250 ml cup for every tea type we sell, from black tea down to caffeine-free herbals.",
       "brewing",
       ["These are typical ranges for a standard brew. Longer, hotter and stronger all push the number up. Herbal and fruit tisanes contain no caffeine at all."],
       rows=[("Black tea (Wellington Breakfast, Earl Grey, Lapsang, Chai)", "40 to 70 mg"), ("Oolong (Milford Mist, Midnight Roast)", "30 to 50 mg"), ("Green tea (Zealandia Green)", "20 to 45 mg"), ("White tea (Harbour Fog)", "20 to 40 mg"), ("Genmaicha", "10 to 25 mg"), ("Herbal and fruit (Chamomile, Peppermint, Kawakawa Mint, Pōhutukawa Berry, Sleepy Tūī)", "0 mg"), ("Filter coffee, for comparison", "90 to 140 mg")],
       products=["genmaicha-toasted-rice", "sleepy-tui-blend"],
       see_also=[("/blog/tea-vs-coffee-caffeine/", "Tea vs coffee: how much caffeine?")]),
    _a("cleaning-your-teapot", "Cleaning your teapot and infuser",
       "How to clean stoneware and glass teapots and stainless infusers without soap, and how to shift tannin stains with bicarb.",
       "brewing",
       ["Rinse with hot water after every use and let it air dry with the lid off. Avoid dish soap on unglazed stoneware; it soaks in and you will taste it. For tannin stains, make a paste of bicarbonate of soda and water, rub, rinse. Stainless infusers can go in the dishwasher; bamboo lids cannot."],
       products=["ceramic-teapot-600", "glass-teapot-with-infuser"],
       see_also=[("/help/descaling-your-kettle/", "Descaling your kettle")]),
    _a("tea-freshness-and-best-before", "Tea freshness and best-before dates",
       "What the best-before date on our pouches means, how long each tea type stays fresh, and how to tell when tea has gone flat.",
       "brewing",
       ["Every pouch is stamped with a best-before date 18 months from packing. Tea does not become unsafe after that; it becomes boring. Green and white teas fade fastest, in six to nine months once opened. Black and roasted oolong last a year or more. Herbals lose their aroma before their flavour.",
        "The test: open the tin and sniff. If it smells of nothing, it will taste of nothing. Store in a sealed tin, away from light, heat and the spice rack."],
       products=["tin-caddy-trio"],
       see_also=[("/blog/tea-storage-mistakes/", "Five tea storage mistakes")]),
    # Orders and shipping
    _a("shipping-times-nz", "Shipping times within New Zealand",
       "Orders placed before noon ship the same day from Petone. North Island 1 to 2 days, South Island 2 to 3 days, rural add a day.",
       "orders",
       ["We ship from our Petone warehouse with NZ Post and Aramex. Orders placed before 12 noon on a weekday leave the same day. Weekend orders ship Monday."],
       rows=[("Wellington region", "Next business day"), ("Rest of North Island", "1 to 2 business days"), ("South Island", "2 to 3 business days"), ("Rural delivery", "Add 1 to 2 days"), ("Free shipping", "Orders over NZ$60")],
       products=["wellington-breakfast"],
       see_also=[("/help/track-your-order/", "Track your order"), ("/shipping-policy/", "Shipping policy")]),
    _a("international-shipping", "International shipping",
       "We ship tea and teaware to Australia and a short list of other countries. Kettles ship to Australia only. Duties are the customer's responsibility.",
       "orders",
       ["Tea and teaware ship to Australia, the UK, the US, Canada, Singapore and Japan. Kettles ship to Australia only, because of plug and voltage rules. International orders take 5 to 12 business days and are tracked.",
        "Import duties and taxes are charged by your country, not by us, and are your responsibility. Australia is duty free under the trans-Tasman agreement for orders under AU$1,000."],
       products=["tasting-flight-set", "tin-caddy-trio"],
       see_also=[("/help/shipping-times-nz/", "Shipping within New Zealand"), ("/shipping-policy/", "Shipping policy")]),
    _a("returns-and-exchanges", "Returns and exchanges",
       "Unopened tea and teaware can be returned within 30 days. Kettles are covered by warranty. Opened tea you did not like: tell us, we will sort it.",
       "orders",
       ["Unopened tea and teaware can be returned for a refund or exchange within 30 days of delivery. Kettle faults are handled under warranty rather than as returns.",
        "If you opened a tea and genuinely did not like it, email us. We would rather swap it for something you will drink than have you push through a pouch of lapsang out of politeness."],
       steps=["Email hello@kererukettle.example with your order number.", "We send a return label for NZ orders.", "Refunds go back to the original payment method within five business days of the parcel arriving."],
       see_also=[("/help/warranty/", "Kettle warranty"), ("/terms/", "Terms of sale")]),
    _a("track-your-order", "Track your order",
       "Find your tracking number in the shipping confirmation email, or log in to your account to see order status and tracking links.",
       "orders",
       ["When your order ships you get an email with a tracking link. You can also log in to your account and open the order from the orders page. If the tracking has not updated in three business days, get in touch and we will chase the courier."],
       see_also=[("/help/shipping-times-nz/", "Shipping times"), ("/help/account-and-password/", "Account and password help")]),
    _a("gift-cards", "Gift cards",
       "Digital gift cards from NZ$20 to NZ$500, emailed instantly or scheduled for a date. Valid three years, usable on anything including subscriptions.",
       "account",
       ["Gift cards are digital and arrive by email, either immediately or on a date you choose. They are valid for three years and work on everything on the site, including subscriptions and workshop tickets. Balances can be checked on the account page."],
       products=["tasting-flight-set", "gooseneck-kettle-pro"],
       see_also=[("/services/subscription/", "Tea subscription"), ("/services/workshops/", "Workshops")]),
    # Subscriptions
    _a("manage-your-subscription", "Manage your subscription",
       "Change your box size, caffeine preference, delivery address or payment method from the subscription page in your account.",
       "subscriptions",
       ["Everything about your subscription lives on the subscription page of your account: box size (small, standard, large), caffeine preference (everything, low caffeine, caffeine free), delivery address, payment card and next ship date. Changes made before the 25th of the month apply to the next box."],
       steps=["Log in and open Account, then Subscription.", "Change the setting you need and press Save.", "You will get a confirmation email. If you do not, the change did not save."],
       see_also=[("/help/pause-or-skip-a-box/", "Pause or skip a box"), ("/services/subscription/", "About the subscription")]),
    _a("pause-or-skip-a-box", "Pause or skip a box",
       "Skip a single month or pause your subscription indefinitely from your account. No fees, no phone calls, no guilt.",
       "subscriptions",
       ["Skip a month if you are away or drowning in tea. Pause if you want to stop for longer. Both are on the subscription page and take effect immediately as long as you do it before the 25th. Paused subscriptions keep your price and preferences and can be resumed any time."],
       see_also=[("/help/manage-your-subscription/", "Manage your subscription"), ("/blog/subscription-box-september-unboxing/", "What was in the September box")]),
    # Kettles
    _a("gooseneck-kettle-setup", "Gooseneck Kettle Pro: setup and first boil",
       "Unbox, rinse, run two boil cycles and set your first temperature preset. Setup for the Gooseneck Kettle Pro takes about ten minutes.",
       "kettles",
       ["Before your first cup, rinse the kettle, run two full boils with plain water and discard them. This clears any residue from manufacturing. Then set a preset and you are away."],
       steps=["Remove the kettle and base from the box and take the sticker off the lid.", "Rinse the inside and fill to the MAX line.", "Place on the base, press the power button and let it boil. Discard the water. Repeat.", "Press the preset button to cycle through Green (75), White (80), Oolong (85), Black (95) and Boil (100).", "Press and hold the Hold button to keep the water at temperature for up to 60 minutes."],
       products=["gooseneck-kettle-pro"],
       see_also=[("/help/kettle-temperature-presets/", "Temperature presets explained"), ("/help/kettle-error-codes/", "Error codes")]),
    _a("kettle-temperature-presets", "Kettle temperature presets explained",
       "What each preset on the Gooseneck Kettle Pro is for: Green 75 °C, White 80 °C, Oolong 85 °C, Black 95 °C, Boil 100 °C, and how to set a custom temperature.",
       "kettles",
       ["The five presets match our brewing guides. Green at 75 °C keeps sencha sweet. White at 80 °C suits silver needle. Oolong at 85 °C is for light, floral oolongs; use Black or Boil for roasted ones. Black at 95 °C is for breakfast teas and Earl Grey. Boil is for herbals, chai and coffee.",
        "To set a custom temperature, turn the dial on the base. It moves in one degree steps from 40 to 100 °C. The last custom temperature is remembered until you unplug the base."],
       rows=[("Green", "75 °C"), ("White", "80 °C"), ("Oolong", "85 °C"), ("Black", "95 °C"), ("Boil", "100 °C"), ("Custom", "40 to 100 °C in 1 °C steps")],
       products=["gooseneck-kettle-pro", "zealandia-green", "milford-mist-oolong"],
       see_also=[("/blog/water-temperature-guide/", "The water temperature guide"), ("/help/gooseneck-kettle-setup/", "Setup and first boil")]),
    _a("descaling-your-kettle", "Descaling your kettle",
       "Step-by-step descaling with citric acid or vinegar for all our kettles, how often to do it, and fixing a clouded glass kettle.",
       "kettles",
       ["Limescale slows boiling, flakes into your cup and can confuse the temperature sensor in the Gooseneck Pro. Descale monthly in hard water areas, every three months otherwise. Citric acid is our preference because it leaves no smell."],
       steps=["Fill the kettle to MAX with water and add 1 tablespoon of citric acid, or use half water, half white vinegar.", "Boil, then leave to stand for 20 minutes.", "Pour out and rinse twice.", "Boil a fresh kettle of plain water and discard it.", "For a clouded glass kettle, repeat once and wipe the inside with a soft cloth while warm."],
       products=["gooseneck-kettle-pro", "cordless-glass-kettle", "stovetop-classic-kettle"],
       see_also=[("/blog/descale-your-kettle/", "Descale your kettle. Yes, now."), ("/help/kettle-error-codes/", "Error codes")]),
    _a("kettle-not-turning-on", "My kettle will not turn on",
       "Troubleshooting a kettle that does not power on: base contact, boil-dry cutout, the reset procedure, and when to claim warranty.",
       "kettles",
       ["Most 'dead' kettles are not dead. Work through these in order before contacting us."],
       steps=["Check the kettle is seated fully on the base; lift and replace it.", "Try a different power point.", "If the kettle boiled dry, the safety cutout has tripped. Let it cool for 15 minutes with the lid open, then try again.", "For the Gooseneck Pro, unplug the base for one minute to reset the controller.", "If none of that works, email us your order number and a photo of the serial label under the base. If it is within two years, it is covered."],
       products=["gooseneck-kettle-pro", "gooseneck-kettle-lite", "cordless-glass-kettle"],
       see_also=[("/help/warranty/", "Warranty"), ("/help/kettle-error-codes/", "Error codes")]),
    _a("kettle-error-codes", "Gooseneck Kettle Pro error codes",
       "What E1, E2, E3 and E4 mean on the Gooseneck Kettle Pro display and how to fix each one.",
       "kettles",
       ["The Pro shows an error code on the base display when something is wrong. These are the four you can see."],
       rows=[("E1", "No water detected, or boil-dry. Fill the kettle and let it cool."), ("E2", "Temperature sensor out of range. Usually limescale on the sensor; descale and reset."), ("E3", "Kettle removed from base mid-cycle. Replace it and press start."), ("E4", "Controller fault. Unplug for one minute. If it persists, contact us for a warranty replacement.")],
       products=["gooseneck-kettle-pro"],
       see_also=[("/help/descaling-your-kettle/", "Descaling"), ("/help/kettle-not-turning-on/", "Kettle will not turn on")]),
    _a("warranty", "Kettle and teaware warranty",
       "Electric kettles are covered for two years, the Stovetop Classic for five, teaware for one year against manufacturing faults. How to claim.",
       "kettles",
       ["Gooseneck Pro, Gooseneck Lite, Cordless Glass and Big Brew kettles: two years. Travel Kettle Mini: one year. Stovetop Classic: five years, because there is nothing in it to break. Teapots and accessories: one year against manufacturing faults. The warranty covers faults, not drops, and not limescale damage from never descaling, which we can tell.",
        "To claim, email your order number, a description and a photo. We usually replace rather than repair, and we pay the return shipping within New Zealand."],
       products=["gooseneck-kettle-pro", "stovetop-classic-kettle", "ceramic-teapot-600"],
       see_also=[("/help/returns-and-exchanges/", "Returns and exchanges"), ("/services/kettle-repairs/", "Out-of-warranty repairs")]),
    # Account
    _a("account-and-password", "Account and password help",
       "Reset your password, change your email, update addresses and delete your account from the account page.",
       "account",
       ["Use the 'Forgot password' link on the login page to get a reset email. If it does not arrive within five minutes, check spam, then try again with the email address you ordered with, which may not be the one you think. Email and address changes are on the account page. To delete your account entirely, email us and we will do it within two business days."],
       see_also=[("/help/track-your-order/", "Track your order"), ("/privacy/", "Privacy policy")]),
]

BY_SLUG = {d["slug"]: d for d in ARTICLES}


def help_url(slug: str) -> str:
    return "/help/{}/".format(slug)


def _article_page(d: dict) -> Page:
    cat_label = dict(CATEGORIES)[d["cat"]]
    body = ['<p class="meta">Help centre · {}</p>'.format(esc(cat_label))]
    body.append("<article>" + p(*d["paras"]))
    if d["steps"]:
        body.append("<h2>Steps</h2>" + ol(d["steps"]))
    if d["rows"]:
        body.append("<h2>At a glance</h2>" + table(d["rows"]))
    body.append("</article>")
    body.append(related("Products mentioned", [(product_url(s), PRODUCTS[s]["name"]) for s in d["products"] if s in PRODUCTS]))
    body.append(related("See also", list(d["see_also"])))
    return Page(
        path=help_url(d["slug"]),
        title="{} | Help centre".format(d["title"]),
        description=d["description"],
        h1=d["title"],
        body="".join(body),
        section="help",
        lastmod="2026-08-25",
    )


def _index_page() -> Page:
    parts = [p("Short, practical answers. If yours is not here, the FAQ has the quick ones and the contact page has a human.")]
    for key, label in CATEGORIES:
        items = [d for d in ARTICLES if d["cat"] == key]
        parts.append("<h2>{}</h2>".format(esc(label)))
        parts.append(card_list([(help_url(d["slug"]), d["title"], d["description"]) for d in items]))
    return Page(
        path="/help/",
        title="Help centre | Kererū Kettle Co.",
        description="Brewing guides, shipping, subscriptions, kettle troubleshooting and account help from Kererū Kettle Co.",
        h1="Help centre",
        body="".join(parts),
        section="help",
        lastmod="2026-08-25",
    )


def _legacy_chart() -> Page:
    # Orphan, no meta description, no h1.
    body = "<article>" + p("Old brewing chart from the 2023 stall days. Kept because it is linked from some printed cards that are still floating around Wellington.") + table([
        ("Black", "boiling, 3 min"), ("Green", "hot not boiling, 1 min"), ("Oolong", "hot, short and often"), ("Herbal", "boiling, ages"),
    ]) + p("For the current version see the brewing guides in the help centre.") + "</article>"
    return Page(
        path="/help/legacy-brewing-chart/",
        title="Legacy brewing chart | Help centre",
        description="", h1="Legacy brewing chart",
        body=body, section="help",
        omit_description=True, omit_h1=True,
        lastmod="2023-11-10",
        test_note="Orphan help page (sitemap only) with no meta description and no h1.",
    )


def _internal_notes() -> Page:
    # noindex, in sitemap, unlinked.
    body = "<article>" + p(
        "Internal packing notes. Chai bins are the blue ones. Lapsang is stored in the smokehouse annex, not the main room, because everything near it starts to taste of smoke. Do not put the Genmaicha next to the Earl Grey.",
        "This page has a noindex meta tag. If it turns up in search results, the crawler is ignoring robots meta.",
    ) + "</article>"
    return Page(
        path="/help/internal-notes/",
        title="Internal packing notes | Help centre",
        description="Internal warehouse packing notes. Marked noindex.",
        h1="Internal packing notes",
        body=body, section="help",
        noindex=True,
        lastmod="2026-06-01",
        test_note="In the sitemap, unlinked, and carries a robots noindex meta tag.",
    )


def pages():
    out = [_index_page()]
    out.extend(_article_page(d) for d in ARTICLES)
    out.append(_legacy_chart())
    out.append(_internal_notes())
    return out
