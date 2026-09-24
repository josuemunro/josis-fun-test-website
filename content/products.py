"""Products: teas, kettles and accessories. Shared vocabulary (steep, oolong,
gooseneck, temperature) is deliberate so ranking has to do some work."""
from model import Page, p, table, related, card_list, link, esc, ul

# (slug, name, category, price, tagline, paragraphs, specs, steep, related)
TEAS = [
    dict(
        slug="wellington-breakfast", name="Wellington Breakfast", price=14.50,
        tagline="A brisk, malty black blend built to stand up to a southerly.",
        paras=[
            "Wellington Breakfast is our flagship black tea: a blend of Assam and Sri Lankan Dimbula leaf that brews strong, coppery and malty. It was designed for mornings when the wind is doing forty knots on the harbour and you need a cup that argues back.",
            "It takes milk happily, holds up to a second steep, and is the tea we hand to anyone who says they only drink coffee. Most of our subscription boxes start with a pouch of this one.",
        ],
        specs=[("Type", "Black tea blend"), ("Origin", "Assam, India and Dimbula, Sri Lanka"), ("Pack size", "100 g loose leaf"), ("Caffeine", "High"), ("Tasting notes", "Malt, toast, honeyed stone fruit")],
        steep=("95 °C", "3 to 4 minutes", "3 g per 250 ml"),
        rel=["southerly-earl-grey", "cuba-street-chai", "gooseneck-kettle-pro"],
    ),
    dict(
        slug="southerly-earl-grey", name="Southerly Earl Grey", price=15.00,
        tagline="Bergamot-scented black tea with a squeeze of Kāpiti lemon peel.",
        paras=[
            "Our Earl Grey uses a Ceylon black base and real cold-pressed bergamot oil, rather than the synthetic stuff that makes a lot of Earl Greys smell like bathroom cleaner. We finish it with dried lemon peel from a grower on the Kāpiti coast.",
            "Steep it a touch cooler than a breakfast tea and it stays bright rather than bitter. It also makes an excellent iced Earl Grey lemonade in summer, which we have written about on the blog more than once.",
        ],
        specs=[("Type", "Flavoured black tea"), ("Origin", "Sri Lanka"), ("Pack size", "100 g loose leaf"), ("Caffeine", "Medium to high"), ("Tasting notes", "Bergamot, citrus, light malt")],
        steep=("90 °C", "3 minutes", "2.5 g per 250 ml"),
        rel=["wellington-breakfast", "harbour-fog-white", "glass-teapot-with-infuser"],
    ),
    dict(
        slug="zealandia-green", name="Zealandia Green", price=16.00,
        tagline="A grassy, sweet sencha-style green tea that forgives a hot kettle.",
        paras=[
            "Zealandia Green is a steamed green tea from Shizuoka with a bright, vegetal character and a sweetness that shows up if you keep the water temperature down. It is the tea we use in workshops to teach why temperature matters.",
            "Steeped at 95 °C it turns bitter and astringent; steeped at 75 °C it is soft, sweet and a little like fresh peas. Same leaf, different kettle setting. If you own a variable temperature gooseneck kettle, this is the tea to try first.",
        ],
        specs=[("Type", "Green tea"), ("Origin", "Shizuoka, Japan"), ("Pack size", "80 g loose leaf"), ("Caffeine", "Medium"), ("Tasting notes", "Fresh grass, sweet pea, seaweed")],
        steep=("75 °C", "90 seconds", "3 g per 200 ml"),
        rel=["genmaicha-toasted-rice", "gooseneck-kettle-pro", "brew-thermometer"],
    ),
    dict(
        slug="milford-mist-oolong", name="Milford Mist Oolong", price=19.50,
        tagline="A lightly oxidised high-mountain oolong: floral, creamy, endlessly re-steepable.",
        paras=[
            "Milford Mist is a Taiwanese high-mountain oolong from around 1,600 metres. The rolled leaves unfurl over several steeps and give up a creamy, orchid-like cup with a long sweet finish. It is the tea most likely to convert a green tea drinker to oolong.",
            "Oolong rewards patience. Use a small pot, a lot of leaf, and short steeps that get a little longer each time. Six or seven infusions from one measure is normal. Our oolong brewing guide walks through the whole thing.",
        ],
        specs=[("Type", "Oolong, lightly oxidised"), ("Origin", "Nantou, Taiwan"), ("Pack size", "60 g loose leaf"), ("Caffeine", "Medium"), ("Tasting notes", "Orchid, cream, cut grass")],
        steep=("85 °C", "45 seconds, then add 15 seconds each steep", "6 g per 150 ml"),
        rel=["midnight-oolong-roast", "ceramic-teapot-600", "tasting-flight-set"],
    ),
    dict(
        slug="golden-bay-chamomile", name="Golden Bay Chamomile", price=12.00,
        tagline="Whole chamomile flowers, honey-sweet and caffeine free.",
        paras=[
            "Whole-flower chamomile, not the dusty fannings that end up in most bags. The flowers are big, gold and apple-scented, and they brew a clear, honeyed cup with no bitterness even if you forget the pot for ten minutes.",
            "Caffeine free, so it is the base for our Sleepy Tūī blend and a regular in the evening section of the subscription box.",
        ],
        specs=[("Type", "Herbal tisane"), ("Origin", "Egypt"), ("Pack size", "50 g whole flowers"), ("Caffeine", "None"), ("Tasting notes", "Apple, honey, hay")],
        steep=("100 °C", "5 to 7 minutes", "2 g per 250 ml"),
        rel=["sleepy-tui-blend", "peppermint-tidal", "tin-caddy-trio"],
    ),
    dict(
        slug="kawakawa-mint", name="Kawakawa Mint", price=13.50,
        tagline="Native kawakawa leaf with peppermint: peppery, cooling, a little bit Aotearoa.",
        paras=[
            "Kawakawa is a native New Zealand shrub with heart-shaped leaves and a peppery, slightly bitter flavour that has been used in rongoā Māori for generations. We blend dried kawakawa with peppermint so the pepper sits behind a cool minty front.",
            "Our kawakawa is wild-harvested under agreement with a whānau trust in the Wairarapa, and we buy only the leaves the caterpillars have already had a go at, because those are said to be the best ones.",
        ],
        specs=[("Type", "Herbal tisane"), ("Origin", "Wairarapa, New Zealand"), ("Pack size", "40 g"), ("Caffeine", "None"), ("Tasting notes", "Pepper, mint, green leaf")],
        steep=("100 °C", "5 minutes", "2 g per 250 ml"),
        rel=["peppermint-tidal", "pohutukawa-berry", "golden-bay-chamomile"],
    ),
    dict(
        slug="manuka-smoked-lapsang", name="Mānuka Smoked Lapsang", price=17.00,
        tagline="A lapsang-style black tea smoked over mānuka wood in Petone.",
        paras=[
            "Traditional lapsang souchong is smoked over pine. Ours is a Yunnan black leaf that we cold-smoke over mānuka in a converted smokehouse behind our Petone warehouse. The result is smoky and sweet rather than tarry, with a bacon-and-honey thing going on that people either adore or flee from.",
            "It is a polarising tea and we love it for that. Try it with cheddar, or use it as the base for a smoky chai.",
        ],
        specs=[("Type", "Smoked black tea"), ("Origin", "Yunnan leaf, smoked in Petone"), ("Pack size", "80 g loose leaf"), ("Caffeine", "Medium to high"), ("Tasting notes", "Mānuka smoke, honey, dried fig")],
        steep=("95 °C", "3 minutes", "3 g per 250 ml"),
        rel=["wellington-breakfast", "cuba-street-chai", "stovetop-classic-kettle"],
    ),
    dict(
        slug="cuba-street-chai", name="Cuba Street Chai", price=15.50,
        tagline="Whole-spice masala chai with cardamom, ginger and black pepper.",
        paras=[
            "Named after the street where our first café stall stood, Cuba Street Chai is an Assam base with cracked cardamom, dried ginger, cinnamon quill, clove and black pepper. There is no sugar in the blend; add your own, or do not.",
            "Simmer it in milk on the stovetop for the proper thing, or steep it hot and strong in a pot for a quicker cup. The chai-at-home post on our blog has the stovetop method.",
        ],
        specs=[("Type", "Spiced black tea"), ("Origin", "Assam leaf, spices from Kerala"), ("Pack size", "100 g"), ("Caffeine", "Medium to high"), ("Tasting notes", "Cardamom, ginger, warm pepper")],
        steep=("100 °C", "5 minutes, or simmer in milk", "4 g per 250 ml"),
        rel=["wellington-breakfast", "manuka-smoked-lapsang", "stovetop-classic-kettle"],
    ),
    dict(
        slug="harbour-fog-white", name="Harbour Fog White", price=21.00,
        tagline="Silver needle white tea: delicate, downy buds and a whisper of melon.",
        paras=[
            "Harbour Fog is a Bai Hao Yin Zhen, or silver needle, made only from unopened buds covered in fine white down. It is the least processed tea we sell and the most delicate: pale gold in the cup, with notes of honeydew melon and fresh hay.",
            "White tea wants cool water and a long steep. Go too hot and you cook the buds; go too short and you get warm water. Our white tea brewing guide has the numbers.",
        ],
        specs=[("Type", "White tea"), ("Origin", "Fujian, China"), ("Pack size", "50 g"), ("Caffeine", "Low to medium"), ("Tasting notes", "Melon, hay, white flowers")],
        steep=("80 °C", "4 to 5 minutes", "4 g per 250 ml"),
        rel=["zealandia-green", "milford-mist-oolong", "glass-teapot-with-infuser"],
    ),
    dict(
        slug="pohutukawa-berry", name="Pōhutukawa Berry", price=13.00,
        tagline="Hibiscus, rosehip and blackcurrant: a bright red summer cup, hot or iced.",
        paras=[
            "Pōhutukawa Berry is a fruit tisane that brews the same colour as the tree's Christmas flowers. Hibiscus and rosehip give it tartness, dried blackcurrant and apple give it sweetness, and there is no caffeine anywhere in it.",
            "It is our most popular cold brew. Drop a spoonful in a bottle of cold water, leave it in the fridge overnight, and it is ready by breakfast.",
        ],
        specs=[("Type", "Fruit tisane"), ("Origin", "Blend"), ("Pack size", "80 g"), ("Caffeine", "None"), ("Tasting notes", "Blackcurrant, hibiscus, apple")],
        steep=("100 °C", "6 minutes, or cold brew 8 hours", "3 g per 250 ml"),
        rel=["kawakawa-mint", "peppermint-tidal", "travel-kettle-mini"],
    ),
    dict(
        slug="midnight-oolong-roast", name="Midnight Oolong Roast", price=18.50,
        tagline="A dark, charcoal-roasted oolong with cocoa and toasted grain.",
        paras=[
            "If Milford Mist is the bright, floral side of oolong, Midnight is the other end: a heavily oxidised Tieguanyin-style leaf roasted over charcoal until it tastes of cocoa, toasted barley and a little dried plum. It brews dark amber and drinks like a cross between a black tea and a hot chocolate.",
            "Roasted oolong is forgiving. It does not mind boiling water and it re-steeps well, which makes it a good first oolong for people who find the green ones fussy.",
        ],
        specs=[("Type", "Oolong, heavily roasted"), ("Origin", "Anxi, China"), ("Pack size", "60 g"), ("Caffeine", "Medium"), ("Tasting notes", "Cocoa, toasted barley, dried plum")],
        steep=("95 °C", "1 minute, then add 20 seconds each steep", "5 g per 150 ml"),
        rel=["milford-mist-oolong", "ceramic-teapot-600", "manuka-smoked-lapsang"],
    ),
    dict(
        slug="genmaicha-toasted-rice", name="Genmaicha Toasted Rice", price=14.00,
        tagline="Green tea with toasted brown rice: nutty, savoury, low in caffeine.",
        paras=[
            "Genmaicha is bancha green tea mixed with toasted and popped brown rice. The rice gives it a savoury, popcorn-like flavour and dilutes the caffeine, so it is the green tea we suggest for the afternoon.",
            "It is also about the most relaxed green tea to brew. Slightly hot water is fine, slightly long steeps are fine. It makes a great pairing with anything salty.",
        ],
        specs=[("Type", "Green tea with rice"), ("Origin", "Kagoshima, Japan"), ("Pack size", "100 g"), ("Caffeine", "Low"), ("Tasting notes", "Toasted rice, popcorn, mild grass")],
        steep=("85 °C", "2 minutes", "3 g per 250 ml"),
        rel=["zealandia-green", "harbour-fog-white", "tea-timer-hourglass"],
    ),
    dict(
        slug="peppermint-tidal", name="Peppermint Tidal", price=11.50,
        tagline="Just peppermint. Big cut leaf, very cold on the tongue.",
        paras=[
            "Sometimes you want one thing done well. Peppermint Tidal is a single-origin Tasmanian peppermint with an unusually high menthol content, cut coarse so it does not turn to dust in the tin.",
            "It is caffeine free, great after dinner, and the peppermint half of our Kawakawa Mint blend.",
        ],
        specs=[("Type", "Herbal tisane"), ("Origin", "Tasmania, Australia"), ("Pack size", "50 g"), ("Caffeine", "None"), ("Tasting notes", "Menthol, sweet mint, cool finish")],
        steep=("100 °C", "5 minutes", "2 g per 250 ml"),
        rel=["kawakawa-mint", "golden-bay-chamomile", "sleepy-tui-blend"],
    ),
    dict(
        slug="sleepy-tui-blend", name="Sleepy Tūī Blend", price=13.50,
        tagline="Chamomile, lemon balm, lavender and a pinch of valerian for the end of the day.",
        paras=[
            "Sleepy Tūī is our bedtime blend. Golden Bay chamomile does the heavy lifting, lemon balm and a little lavender round it out, and a small measure of valerian root gives it an earthy base. There is no caffeine in it and, we are told, it works.",
            "We wrote a blog post about tea and sleep that goes into what the evidence actually says, which is: less than the packaging usually claims, but chamomile is nice regardless.",
        ],
        specs=[("Type", "Herbal tisane"), ("Origin", "Blend"), ("Pack size", "50 g"), ("Caffeine", "None"), ("Tasting notes", "Chamomile, lemon, soft lavender")],
        steep=("100 °C", "7 minutes", "2.5 g per 250 ml"),
        rel=["golden-bay-chamomile", "peppermint-tidal", "ceramic-teapot-600"],
    ),
]

KETTLES = [
    dict(
        slug="gooseneck-kettle-pro", name="Gooseneck Kettle Pro", price=189.00,
        tagline="Our variable temperature gooseneck kettle with five presets and a hold function.",
        paras=[
            "The Gooseneck Kettle Pro is the kettle we designed because we could not find one we liked. It has a slow, controllable gooseneck spout for pour-over and small teapots, a 0.9 litre stainless body, and a variable temperature base with presets for green, white, oolong, black and boiling.",
            "Set 75 °C for Zealandia Green, 85 °C for Milford Mist Oolong, or dial anything from 40 °C to 100 °C in one degree steps. The hold function keeps the water at temperature for up to an hour, which is exactly what a long oolong session needs.",
            "It comes with a two year warranty. The help centre has setup instructions, a list of the temperature presets, and what the error codes mean if it ever throws one.",
        ],
        specs=[("Capacity", "0.9 litres"), ("Power", "1200 W"), ("Temperature range", "40 to 100 °C, 1 °C steps"), ("Presets", "Green 75, White 80, Oolong 85, Black 95, Boil 100"), ("Hold", "60 minutes"), ("Body", "304 stainless steel"), ("Warranty", "2 years")],
        steep=None,
        rel=["gooseneck-kettle-lite", "brew-thermometer", "zealandia-green"],
    ),
    dict(
        slug="gooseneck-kettle-lite", name="Gooseneck Kettle Lite", price=119.00,
        tagline="The same gooseneck spout without the variable temperature base. Boils, and that is it.",
        paras=[
            "The Lite is for people who want the pour control of a gooseneck kettle but do not need the temperature presets. It boils to 100 °C and switches off. Pair it with a brew thermometer, or just let the water sit for a minute or two before pouring green tea.",
            "Same 0.9 litre stainless body and lid as the Pro, same two year warranty, about two thirds the price.",
        ],
        specs=[("Capacity", "0.9 litres"), ("Power", "1200 W"), ("Temperature", "Boil only"), ("Body", "304 stainless steel"), ("Warranty", "2 years")],
        steep=None,
        rel=["gooseneck-kettle-pro", "brew-thermometer", "cordless-glass-kettle"],
    ),
    dict(
        slug="stovetop-classic-kettle", name="Stovetop Classic Kettle", price=95.00,
        tagline="A 1.7 litre enamelled steel whistling kettle that works on gas, induction and campfires.",
        paras=[
            "No electronics, no presets, no error codes. The Stovetop Classic is enamelled steel with a whistling lid, a heat-proof handle and a flat base that works on induction. It is the kettle we use at the café for chai, because you can simmer milk in it without anything complaining.",
            "Available in harbour blue and kererū green.",
        ],
        specs=[("Capacity", "1.7 litres"), ("Hob compatibility", "Gas, electric, induction, open fire"), ("Body", "Enamelled carbon steel"), ("Colours", "Harbour blue, kererū green"), ("Warranty", "5 years")],
        steep=None,
        rel=["cuba-street-chai", "the-big-brew-kettle", "manuka-smoked-lapsang"],
    ),
    dict(
        slug="travel-kettle-mini", name="Travel Kettle Mini", price=59.00,
        tagline="A 0.5 litre collapsible silicone kettle for hotel rooms, campervans and the office.",
        paras=[
            "The Travel Kettle Mini folds down to the height of a coffee mug. It boils half a litre in under three minutes on 110 or 240 volts, so it works in the campervan, the office kitchen and the sort of hotel where the kettle has been missing since 2019.",
            "It is boil-only. For green tea on the road, boil, wait two minutes, pour.",
        ],
        specs=[("Capacity", "0.5 litres"), ("Power", "800 W, dual voltage"), ("Collapsed height", "9 cm"), ("Body", "Food-grade silicone and stainless base"), ("Warranty", "1 year")],
        steep=None,
        rel=["pohutukawa-berry", "tin-caddy-trio", "gooseneck-kettle-lite"],
    ),
    dict(
        slug="the-big-brew-kettle", name="The Big Brew Kettle", price=249.00,
        tagline="A 5 litre commercial urn-style kettle with a tap, for offices, events and very large families.",
        paras=[
            "The Big Brew is what we send out with our corporate tea service and workshop kits. It holds five litres, keeps them hot, and dispenses through a tap so nobody has to lift it. It is the reason we can run a workshop for thirty people with one power point.",
            "Not a gooseneck, not delicate, not pretty. Extremely useful.",
        ],
        specs=[("Capacity", "5 litres"), ("Power", "2200 W"), ("Keep warm", "Yes, thermostat"), ("Body", "Stainless steel, insulated"), ("Warranty", "2 years")],
        steep=None,
        rel=["stovetop-classic-kettle", "wellington-breakfast", "cuba-street-chai"],
    ),
    dict(
        slug="cordless-glass-kettle", name="Cordless Glass Kettle", price=79.00,
        tagline="A 1.5 litre borosilicate glass kettle with a blue light you can turn off.",
        paras=[
            "A glass kettle mostly so you can watch it. Borosilicate body, stainless lid and base, 1.5 litre capacity, and a blue boiling light that has an off switch because we asked customers and they were unanimous.",
            "Boil only. Descale it monthly if your water is hard or the glass will cloud, which the help centre explains how to fix.",
        ],
        specs=[("Capacity", "1.5 litres"), ("Power", "2000 W"), ("Body", "Borosilicate glass, stainless steel"), ("Warranty", "2 years")],
        steep=None,
        rel=["gooseneck-kettle-lite", "glass-teapot-with-infuser", "brew-thermometer"],
    ),
]

ACCESSORIES = [
    dict(
        slug="ceramic-teapot-600", name="Ceramic Teapot 600", price=68.00,
        tagline="A 600 ml stoneware teapot with a removable steel infuser, thrown in Whanganui.",
        paras=[
            "Our house teapot, made for us by a potter in Whanganui. It holds 600 millilitres, or about two large cups, and comes with a fine stainless infuser basket that lifts out so you can stop the steep exactly when you want to.",
            "Thick walls keep oolong warm across a long session. Glazed in the same harbour blue as the stovetop kettle.",
        ],
        specs=[("Capacity", "600 ml"), ("Material", "Stoneware, stainless infuser"), ("Dishwasher safe", "Yes, body only"), ("Made in", "Whanganui, New Zealand")],
        steep=None,
        rel=["milford-mist-oolong", "midnight-oolong-roast", "tea-timer-hourglass"],
    ),
    dict(
        slug="glass-teapot-with-infuser", name="Glass Teapot with Infuser", price=42.00,
        tagline="An 800 ml borosilicate teapot so you can watch the leaves unfurl.",
        paras=[
            "Clear glass, 800 millilitres, with a glass infuser tube and a bamboo lid. It is the teapot we use for white tea and Earl Grey in the café because the colour of the liquor is half the pleasure.",
            "It is not the pot for keeping tea hot for an hour. It is the pot for watching a silver needle bud slowly stand up.",
        ],
        specs=[("Capacity", "800 ml"), ("Material", "Borosilicate glass, bamboo lid"), ("Dishwasher safe", "Glass only")],
        steep=None,
        rel=["harbour-fog-white", "southerly-earl-grey", "cordless-glass-kettle"],
    ),
    dict(
        slug="tea-timer-hourglass", name="Tea Timer Hourglass", price=24.00,
        tagline="A three-in-one sand timer: one, three and five minutes, no batteries.",
        paras=[
            "Three glass hourglasses in a wooden frame, timed to one, three and five minutes. One minute for oolong steeps, three for black tea, five for herbals. It is charming, silent and never needs charging, which is more than we can say for the app we tried to build once.",
        ],
        specs=[("Timings", "1, 3 and 5 minutes"), ("Material", "Glass, beech wood"), ("Size", "9 cm x 9 cm x 8 cm")],
        steep=None,
        rel=["genmaicha-toasted-rice", "ceramic-teapot-600", "brew-thermometer"],
    ),
    dict(
        slug="brew-thermometer", name="Brew Thermometer", price=29.00,
        tagline="A fast digital probe thermometer for kettles that only know how to boil.",
        paras=[
            "If your kettle does not have temperature control, a thermometer is the next best thing. This one reads in about two seconds, clips onto the side of a kettle or teapot, and has a little printed chart on the back with the steep temperatures for green, white, oolong and black tea.",
            "Pairs with the Gooseneck Kettle Lite to make a budget version of the Pro.",
        ],
        specs=[("Range", "-10 to 120 °C"), ("Response", "About 2 seconds"), ("Battery", "CR2032, included")],
        steep=None,
        rel=["gooseneck-kettle-lite", "zealandia-green", "harbour-fog-white"],
    ),
    dict(
        slug="tin-caddy-trio", name="Tin Caddy Trio", price=32.00,
        tagline="Three airtight 100 g tea tins in kererū colours: green, purple and white.",
        paras=[
            "Tea's enemies are light, air, moisture and strong smells. These tins deal with the first three. Three 100 gram tins with double lids, coloured like the bird: bush green, breast purple, belly white.",
            "Our tea storage post on the blog covers the mistakes we see most, and step one is always: get it out of the paper pouch.",
        ],
        specs=[("Capacity", "3 x 100 g"), ("Material", "Tinplate, double lid"), ("Colours", "Green, purple, white")],
        steep=None,
        rel=["golden-bay-chamomile", "travel-kettle-mini", "tasting-flight-set"],
    ),
    dict(
        slug="tasting-flight-set", name="Tasting Flight Set", price=85.00,
        tagline="Six 20 g teas, a tasting cup, a timer and our notes booklet. The workshop in a box.",
        paras=[
            "The Tasting Flight Set is the home version of our tasting workshop. You get six 20 gram pouches spanning white, green, oolong, black, smoked and herbal, a porcelain tasting cup and lid, a one minute timer, and the tasting notes booklet we use in class.",
            "It is the gift we sell most of in December and the thing we send to every corporate tea service client before their first session.",
        ],
        specs=[("Teas", "Harbour Fog White, Zealandia Green, Milford Mist Oolong, Wellington Breakfast, Mānuka Smoked Lapsang, Kawakawa Mint"), ("Includes", "Tasting cup and lid, 1 minute timer, notes booklet"), ("Pack size", "6 x 20 g")],
        steep=None,
        rel=["milford-mist-oolong", "tin-caddy-trio", "ceramic-teapot-600"],
    ),
]

ALL_PRODUCTS = [dict(d, cat="tea") for d in TEAS] + [dict(d, cat="kettle") for d in KETTLES] + [dict(d, cat="accessory") for d in ACCESSORIES]
BY_SLUG = {d["slug"]: d for d in ALL_PRODUCTS}

CATEGORY_LABEL = {"tea": "Loose leaf tea", "kettle": "Kettles", "accessory": "Teaware and accessories"}


def product_url(slug: str) -> str:
    return "/products/{}/".format(slug)


def _jsonld(d: dict) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": d["name"],
        "description": d["tagline"],
        "brand": {"@type": "Brand", "name": "Kererū Kettle Co."},
        "offers": {"@type": "Offer", "priceCurrency": "NZD", "price": "{:.2f}".format(d["price"]), "availability": "https://schema.org/InStock"},
    }


def _product_page(d: dict) -> Page:
    body = ['<p class="tagline">{}</p>'.format(esc(d["tagline"]))]
    body.append('<p class="price">NZ${:.2f}</p>'.format(d["price"]))
    body.append(p(*d["paras"]))
    if d.get("steep"):
        temp, time, dose = d["steep"]
        body.append(
            '<div class="brewbox"><h2>Brew it right</h2>'
            '<dl><dt>Water temperature</dt><dd>{}</dd><dt>Steep time</dt><dd>{}</dd><dt>Leaf</dt><dd>{}</dd></dl></div>'.format(esc(temp), esc(time), esc(dose))
        )
    body.append("<h2>Details</h2>")
    body.append(table(d["specs"]))
    rel_links = [(product_url(s), BY_SLUG[s]["name"]) for s in d["rel"] if s in BY_SLUG]
    body.append(related("You might also like", rel_links))
    body.append(related("Helpful reading", [("/help/", "Help centre"), ("/help/how-much-tea-per-cup/", "How much tea per cup?"), ("/services/subscription/", "Get it monthly with a subscription")]))
    return Page(
        path=product_url(d["slug"]),
        title="{} | {}".format(d["name"], CATEGORY_LABEL[d["cat"]]),
        description=d["tagline"],
        h1=d["name"],
        body="".join(body),
        section="products",
        jsonld=_jsonld(d),
        lastmod="2026-08-18",
    )


def _index_page() -> Page:
    parts = [p("Everything we sell fits in a kettle, a teapot or a tin. Teas are sold loose leaf in resealable pouches; kettles ship with a two year warranty and a very earnest manual.")]
    for cat in ("tea", "kettle", "accessory"):
        items = [d for d in ALL_PRODUCTS if d["cat"] == cat]
        parts.append("<h2>{}</h2>".format(esc(CATEGORY_LABEL[cat])))
        parts.append(card_list([(product_url(d["slug"]), d["name"], d["tagline"]) for d in items]))
    parts.append("<h2>Odds and ends</h2>")
    parts.append(ul([link("/products/mystery-box/", "The Mystery Box"), link("/products/", "Full catalogue (this page)")]))
    return Page(
        path="/products/",
        title="Teas, kettles and teaware | Kererū Kettle Co.",
        description="Browse loose leaf teas, gooseneck and stovetop kettles, teapots and accessories from Kererū Kettle Co. in Wellington.",
        h1="Teas, kettles and teaware",
        body="".join(parts),
        section="products",
        lastmod="2026-09-10",
    )


def _mystery_box() -> Page:
    # Deliberately has no <h1>.
    body = (
        '<p class="tagline">A 100 g surprise. Could be oolong. Could be chamomile. Could be the lapsang, in which case sorry.</p>'
        '<p class="price">NZ$20.00</p>'
        + p(
            "The Mystery Box is whatever we have too much of this month, packed into a tin from the caddy trio and posted with a handwritten note. It is always a full-size pouch and it is always at least NZ$25 worth of tea, which is how we justify the name.",
            "You cannot choose. That is the whole point. You can, however, tell us if you cannot drink caffeine and we will steer accordingly.",
        )
        + related("Or choose for yourself", [(product_url("tin-caddy-trio"), "Tin Caddy Trio"), ("/products/", "Full catalogue")])
    )
    return Page(
        path="/products/mystery-box/",
        title="The Mystery Box | Kererū Kettle Co.",
        description="A surprise 100 g tin of whichever tea we have too much of this month.",
        h1="The Mystery Box",
        body=body,
        section="products",
        omit_h1=True,
        test_note="Linked, in the sitemap, but has no h1 element.",
    )


def _discontinued() -> Page:
    # Orphan: in the sitemap, linked from nowhere.
    body = (
        '<p class="tagline">Discontinued in 2025. This page stays up for the search engines and the sentimental.</p>'
        + p(
            "Lemon Verbena was a single-ingredient tisane we sold for two years before our grower in Nelson retired. It was lemony, bright and caffeine free, and we have not found a replacement that tastes as good.",
            "If you are looking for something similar, Peppermint Tidal or Golden Bay Chamomile are the closest we have. If you are our old grower reading this: please come back.",
        )
        + related("Still available", [(product_url("peppermint-tidal"), "Peppermint Tidal"), (product_url("golden-bay-chamomile"), "Golden Bay Chamomile")])
    )
    return Page(
        path="/products/discontinued-lemon-verbena/",
        title="Lemon Verbena (discontinued) | Kererū Kettle Co.",
        description="Our discontinued lemon verbena tisane. No longer for sale, page kept for reference.",
        h1="Lemon Verbena (discontinued)",
        body=body,
        section="products",
        lastmod="2025-11-02",
        test_note="Orphan page: in the sitemap but no internal links point to it.",
    )


def pages():
    out = [_index_page()]
    out.extend(_product_page(d) for d in ALL_PRODUCTS)
    out.append(_mystery_box())
    out.append(_discontinued())
    return out


# Exposed for other modules to link to.
ORPHAN_SLUGS = {"discontinued-lemon-verbena"}
