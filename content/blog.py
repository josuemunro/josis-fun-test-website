"""Blog posts. Several overlap in vocabulary with help articles and products on
purpose (descaling, water temperature, oolong, chai) so ranking is testable."""
from model import Page, p, ul, ol, related, card_list, link, esc
from content.products import BY_SLUG as BY_SLUG_P, product_url


def _post(slug, title, description, date, tags, paras, products=(), next_posts=(), extra_html=""):
    return dict(slug=slug, title=title, description=description, date=date, tags=tags,
                paras=paras, products=products, next_posts=next_posts, extra_html=extra_html)


POSTS = [
    _post(
        "how-to-steep-oolong-properly", "How to steep oolong properly (and why you have been under-leafing it)",
        "A practical guide to brewing oolong tea gongfu-style: leaf ratio, water temperature, steep times and how many infusions to expect.",
        "2026-09-14", ["brewing", "oolong"],
        [
            "The most common oolong complaint we hear at the counter is that it tastes of nothing. Nine times out of ten the fix is the same: more leaf, less water, shorter steeps. Oolong is not a one-teaspoon-per-mug tea. It is a six-grams-in-a-small-pot tea.",
            "Start with a 150 ml pot or gaiwan, warm it with hot water, and add 6 grams of rolled oolong, which looks like far too much. Pour water at about 85 °C for a light oolong like Milford Mist, or 95 °C for a roasted one like Midnight. Steep for 45 seconds, pour everything out into a jug, and drink from there.",
            "Each following steep gets a little longer: 60 seconds, 75, 90, two minutes. The leaves will have fully opened by the third steep and the flavour will shift as you go, from floral to creamy to sweet. Six or seven infusions is normal. Stop when it tastes thin.",
            "A variable temperature kettle with a hold function makes this dramatically easier, because you are not re-boiling and waiting between every steep. That is roughly why we built one.",
        ],
        products=["milford-mist-oolong", "midnight-oolong-roast", "gooseneck-kettle-pro", "ceramic-teapot-600"],
        next_posts=["water-temperature-guide", "tasting-notes-vocabulary"],
    ),
    _post(
        "water-temperature-guide", "The water temperature guide: one chart for every tea we sell",
        "Green, white, oolong, black and herbal teas all want different water temperatures. Here is the chart, and why it matters.",
        "2026-09-07", ["brewing", "temperature"],
        [
            "Water temperature is the single biggest lever you have over how a tea tastes. Too hot and green tea turns bitter, white tea goes flat, and delicate oolong loses its perfume. Too cool and black tea tastes like coloured water.",
            "Here is the chart we print on the back of the brew thermometer: green tea 70 to 80 °C, white tea 75 to 85 °C, light oolong 85 °C, roasted oolong and black tea 90 to 95 °C, herbal and fruit tisanes a full 100 °C boil.",
            "If your kettle only boils, let it sit with the lid open. Roughly speaking, boiled water in a metal kettle drops to about 90 °C after one minute, 85 °C after two, and 80 °C after three to four. Or you can just measure it. The help centre has a fuller version of this in the brewing guides.",
        ],
        products=["gooseneck-kettle-pro", "brew-thermometer", "zealandia-green", "harbour-fog-white"],
        next_posts=["how-to-steep-oolong-properly", "why-gooseneck-kettles"],
    ),
    _post(
        "why-gooseneck-kettles", "Why gooseneck kettles? A slightly defensive explanation",
        "What a gooseneck spout actually does for tea and pour-over coffee, and when you genuinely do not need one.",
        "2026-08-30", ["kettles", "gear"],
        [
            "We get asked whether a gooseneck kettle is a gimmick. Honest answer: sometimes. If you make a big pot of breakfast tea every morning, you do not need one. A normal kettle pours water into a teapot perfectly well.",
            "A gooseneck earns its place when you are pouring into something small or when the pour itself matters. Small teapots and gaiwans overflow with a wide spout. Pour-over coffee needs a slow, steady stream. And a gooseneck lets you pour down the side of the pot so you are not blasting delicate leaves.",
            "Ours come in two versions: the Pro with a variable temperature base, and the Lite that just boils. If you brew green, white or oolong tea, the temperature control is the more important feature. If you brew black tea and coffee, the Lite plus a thermometer covers it.",
        ],
        products=["gooseneck-kettle-pro", "gooseneck-kettle-lite", "brew-thermometer"],
        next_posts=["water-temperature-guide", "descale-your-kettle"],
    ),
    _post(
        "history-of-tea-in-wellington", "A short history of tea in Wellington",
        "From the clipper ships on Lambton Quay to the tea rooms of the 1950s to the specialty tea shops of today.",
        "2026-08-22", ["wellington", "history"],
        [
            "Tea arrived in Wellington with the first European settlers in 1840 and never really left. By the 1860s tea merchants lined Lambton Quay, importing chests from Ceylon and China and blending them in back rooms with a heavy hand of Assam to suit the local taste for strong, milky cups.",
            "The twentieth century was the age of the tea room. Kirkcaldie and Stains had one, the DIC had one, and the Wellington railway station had a tea kiosk that served thousands of cups a day to commuters heading over the hill. The national tea break was enshrined in employment law.",
            "Specialty tea, the loose leaf, single-origin, mind-the-temperature kind, arrived in the 2000s alongside the coffee scene it borrowed most of its ideas from. We opened our first stall on Cuba Street in 2022, which felt late until we looked at the history and realised we were just the latest merchants on a very old street.",
        ],
        products=["wellington-breakfast", "cuba-street-chai"],
        next_posts=["our-first-year", "behind-the-blend-wellington-breakfast"],
    ),
    _post(
        "tea-vs-coffee-caffeine", "Tea vs coffee: how much caffeine is actually in your cup?",
        "Real numbers on caffeine in black, green, white, oolong and herbal tea compared with coffee, and why the leaf is only half the story.",
        "2026-08-15", ["caffeine", "science"],
        [
            "A cup of filter coffee contains somewhere around 90 to 140 mg of caffeine. A cup of black tea is closer to 40 to 70 mg, green tea 20 to 45 mg, white and oolong somewhere in between, and herbal tisanes zero, because they are not made from the tea plant at all.",
            "But the leaf is only half the story. Caffeine extraction depends on water temperature, steep time and leaf quantity. A strong, boiling, five minute Wellington Breakfast will have more caffeine than a cool, ninety second Zealandia Green, but a long-steeped green tea can overtake a short black one.",
            "The idea that white tea is lowest in caffeine because it is least processed is a myth; buds are actually caffeine-rich. Genmaicha is genuinely lower because half the weight is rice. If you want zero, choose the herbal shelf. We have a caffeine chart in the help centre if you want the table.",
        ],
        products=["genmaicha-toasted-rice", "wellington-breakfast", "sleepy-tui-blend"],
        next_posts=["tea-and-sleep", "what-is-white-tea"],
    ),
    _post(
        "cold-brew-tea-summer", "Cold brew tea for a Wellington summer (all three days of it)",
        "How to cold brew loose leaf tea overnight in the fridge, which teas work best, and a few combinations to try.",
        "2026-08-08", ["brewing", "summer", "cold brew"],
        [
            "Cold brewing is the laziest way to make excellent tea. Put leaf in cold water, put it in the fridge, go to bed. In the morning you have a smooth, sweet, low-bitterness tea with no ice dilution and no effort.",
            "Ratios: about 10 grams of leaf per litre of cold water for eight to twelve hours. Green tea and white tea come out remarkably sweet, because the compounds that make them bitter need heat to extract. Fruit tisanes like Pōhutukawa Berry are the crowd favourite. Black tea works but can go cloudy; Earl Grey is the exception and makes a superb base for iced lemonade.",
            "Strain, keep in the fridge for up to three days, and serve over ice with something green in the glass so it looks like you tried.",
        ],
        products=["pohutukawa-berry", "zealandia-green", "southerly-earl-grey"],
        next_posts=["iced-earl-grey-lemonade", "water-temperature-guide"],
    ),
    _post(
        "kawakawa-the-native-leaf", "Kawakawa: the native leaf with holes in it",
        "About kawakawa, the peppery New Zealand shrub in our Kawakawa Mint blend, how it is harvested and what it tastes like.",
        "2026-08-01", ["ingredients", "aotearoa"],
        [
            "Kawakawa (Piper excelsum) is a shrub of the pepper family found in lowland forest across the North Island. Its heart-shaped leaves are famously full of holes chewed by the kawakawa looper caterpillar, and there is a long-held view that the holiest leaves are the most potent.",
            "In rongoā Māori, kawakawa has been used for generations as a tonic and for skin. As a tea, the flavour is peppery, faintly bitter and green, which is why we pair it with peppermint rather than serve it alone.",
            "Our leaf comes from a whānau trust in the Wairarapa under a harvesting agreement that limits how much is taken from each plant. If you want to try it neat, we are happy to send a sample with any order; just ask in the order notes.",
        ],
        products=["kawakawa-mint", "peppermint-tidal"],
        next_posts=["tea-for-people-who-hate-tea", "our-first-year"],
    ),
    _post(
        "descale-your-kettle", "Descale your kettle. Yes, now. It takes ten minutes.",
        "Why limescale builds up in kettles, how it affects taste and boil time, and the citric acid method we recommend.",
        "2026-07-25", ["kettles", "maintenance"],
        [
            "If you live in a hard water area, and parts of the Wellington region are surprisingly hard, your kettle is quietly growing a crust of calcium carbonate. It slows the boil, makes the element work harder, flakes into your cup and, in a variable temperature kettle, throws off the temperature sensor.",
            "The method: add one tablespoon of citric acid, or a half-and-half mix of white vinegar and water, to a kettle of water. Boil it, let it sit for twenty minutes, pour it out, rinse twice and boil a fresh kettle of plain water. Done. Citric acid smells of nothing, which is why we prefer it to vinegar.",
            "Do it monthly with hard water, every three months with soft. The help centre has the same instructions written as steps, plus what to do if the glass kettle has clouded.",
        ],
        products=["gooseneck-kettle-pro", "cordless-glass-kettle"],
        next_posts=["why-gooseneck-kettles", "tea-storage-mistakes"],
    ),
    _post(
        "our-first-year", "Our first year: a stall, a kettle and a very bad website",
        "How Kererū Kettle Co. went from a Cuba Street market stall to a Petone warehouse, and what we got wrong on the way.",
        "2026-07-18", ["company", "story"],
        [
            "We started in 2022 with a folding table at the Cuba Street market, one Stovetop Classic kettle borrowed from a flatmate, and four teas. The first weekend we sold eleven pouches and gave away about forty cups. The second weekend it rained sideways and we sold three.",
            "By the end of that year we had a permanent stall, a subscription list of about ninety people, and the beginnings of the kettle. We also had a website that took eleven seconds to load and had no search at all, so anyone looking for the oolong found the chamomile.",
            "Three years on there is a warehouse in Petone, a small café on the corner, a wholesale list, and a website with search that works. Mostly. The post about a day at the warehouse covers what the operation looks like now.",
        ],
        products=["stovetop-classic-kettle", "wellington-breakfast"],
        next_posts=["a-day-at-the-warehouse", "history-of-tea-in-wellington"],
    ),
    _post(
        "tea-and-sleep", "Tea and sleep: what the evidence says about chamomile, valerian and the rest",
        "A sceptical but affectionate look at bedtime teas. Chamomile, valerian, lemon balm and lavender, and whether any of it helps.",
        "2026-07-11", ["science", "herbal"],
        [
            "We sell a bedtime blend, so we have an interest here. Still, the honest summary is: the evidence for herbal sleep teas is modest. Chamomile has a couple of small trials showing slightly better sleep quality. Valerian has more trials and a mixed picture. Lemon balm and lavender mostly show up as reducing anxiety, which is sleep-adjacent.",
            "What nearly every study agrees on is that a warm, caffeine-free drink as part of a wind-down routine helps people fall asleep. The ritual is doing a lot of the work. We think that is fine. A ritual you enjoy is not a placebo, it is a ritual.",
            "The practical advice: avoid caffeine after early afternoon, which rules out black, green, white and oolong. Chamomile, peppermint and Sleepy Tūī are all safe. Steep it long and drink it slowly.",
        ],
        products=["sleepy-tui-blend", "golden-bay-chamomile", "peppermint-tidal"],
        next_posts=["tea-vs-coffee-caffeine", "tea-for-people-who-hate-tea"],
    ),
    _post(
        "pairing-tea-with-cheese", "Pairing tea with cheese, which is a real thing we do at workshops",
        "Smoked tea with cheddar, oolong with brie, Earl Grey with blue: a starter guide to tea and cheese pairing.",
        "2026-07-04", ["pairing", "workshops"],
        [
            "Wine and cheese is the classic, but tea has tannins, sweetness and aromatics too, and it does not leave you asleep by three in the afternoon. We run a tea and cheese evening at the café every couple of months and these are the pairings that survive.",
            "Mānuka Smoked Lapsang with an aged cheddar is the one that makes people gasp. Milford Mist Oolong with a soft brie or camembert: the creaminess in both lines up. Southerly Earl Grey with a blue cheese, where the bergamot cuts the funk. Genmaicha with a salty halloumi, and Pōhutukawa Berry with a fresh goat cheese for something like a fruit-and-cheese plate in a cup.",
            "Serve the tea slightly cooler than you would drink it normally so the flavours do not scald past the cheese. And use a small cup; it is a tasting, not a session.",
        ],
        products=["manuka-smoked-lapsang", "milford-mist-oolong", "southerly-earl-grey", "tasting-flight-set"],
        next_posts=["smoky-teas-explained", "workshop-recap-winter"],
    ),
    _post(
        "what-is-white-tea", "What is white tea, and why does it cost so much?",
        "Silver needle, white peony and the minimal processing that makes white tea delicate, expensive and worth it.",
        "2026-06-27", ["tea types", "white tea"],
        [
            "White tea is the least processed of the true teas. The buds and young leaves are picked, withered in the sun or a warm room, and dried. No rolling, no pan-firing, no oxidation on purpose. What you get is a pale, sweet, hay-and-melon cup that tastes like the leaf itself.",
            "Silver needle, which is what Harbour Fog is, uses only the unopened buds, picked over a few days in early spring. That is the reason for the price: a kilo of finished silver needle is a lot of very small buds picked by hand at exactly the right moment.",
            "Brew it cool, around 80 °C, and long, four to five minutes. The buds float, then slowly sink. Re-steep at least twice.",
        ],
        products=["harbour-fog-white", "glass-teapot-with-infuser"],
        next_posts=["water-temperature-guide", "tasting-notes-vocabulary"],
    ),
    _post(
        "behind-the-blend-wellington-breakfast", "Behind the blend: Wellington Breakfast",
        "How we built our flagship breakfast tea, why it is two thirds Assam, and the version that did not make it.",
        "2026-06-20", ["blends", "black tea"],
        [
            "Every breakfast tea is a regional argument. English Breakfast is a Ceylon-heavy blend, Irish Breakfast leans on Assam, Scottish is heavier still. We wanted something that could take Wellington milk, Wellington weather and a Wellington commute, which meant leaning towards the Assam end.",
            "The final blend is two parts second-flush Assam for malt and body, one part Dimbula Ceylon for brightness and a clean finish. We tried a version with a little Kenyan tea for colour and it was fine, but it tasted like a supermarket bag. We tried a version with a touch of lapsang and it was excellent but not a breakfast tea.",
            "Brew it hot, three to four minutes, and it will forgive almost anything, including being forgotten on the bench while you find your keys.",
        ],
        products=["wellington-breakfast", "the-big-brew-kettle"],
        next_posts=["history-of-tea-in-wellington", "chai-at-home"],
    ),
    _post(
        "smoky-teas-explained", "Smoky teas explained: lapsang, mānuka and why ours is not made over pine",
        "The history of lapsang souchong, how tea gets smoked, and the mānuka wood smokehouse behind our warehouse.",
        "2026-06-13", ["tea types", "smoked"],
        [
            "Lapsang souchong is the original smoked tea, from the Wuyi mountains in Fujian, traditionally dried over pinewood fires. The story is that a passing army delayed the harvest and the farmers dried the leaves fast over fire to get them to market. Whether or not that is true, it produced a tea that tastes like a campfire.",
            "We smoke ours over mānuka rather than pine. Mānuka smoke is sweeter and rounder, closer to the smoke you get on a good New Zealand bacon, and it plays nicer with a honeyed Yunnan leaf. The smokehouse is a converted shipping container behind the Petone warehouse and it makes the whole street smell fantastic on smoking days.",
            "If you have only ever had a harsh, tarry lapsang, ours may surprise you. If you loved the harsh, tarry one, ours may disappoint you. We can live with either.",
        ],
        products=["manuka-smoked-lapsang", "cuba-street-chai"],
        next_posts=["pairing-tea-with-cheese", "behind-the-blend-wellington-breakfast"],
    ),
    _post(
        "tasting-notes-vocabulary", "A tasting vocabulary for tea, so you can stop saying 'nice'",
        "The words we use in workshops to describe tea: body, astringency, finish, and the flavour families from grassy to malty.",
        "2026-06-06", ["tasting", "workshops"],
        [
            "Everyone can taste the difference between green tea and black tea. Putting it into words is the hard bit, and having words makes you notice more. These are the ones we teach.",
            "Body is weight in the mouth: watery, light, medium, full. Astringency is the drying, puckering feeling on your gums, from tannins; black tea has a lot, white tea has little. Finish is how long the flavour hangs around after you swallow. Sweetness, bitterness and umami are the three tastes that show up most.",
            "Then the flavour families: vegetal (grass, spinach, seaweed) for greens; floral (orchid, honeysuckle) for light oolongs; fruity (stone fruit, dried plum); malty and toasty for blacks; smoky, obviously; and earthy or woody for aged and roasted teas. Say 'creamy floral with a long sweet finish' about Milford Mist and you will sound like you know what you are doing, because you will.",
        ],
        products=["tasting-flight-set", "milford-mist-oolong"],
        next_posts=["how-to-steep-oolong-properly", "what-is-white-tea"],
    ),
    _post(
        "reusable-tea-bags-vs-loose-leaf", "Reusable tea bags vs loose leaf vs the infuser basket",
        "The pros and cons of cotton tea bags, infuser baskets, tea balls and just putting the leaves in the pot.",
        "2026-05-30", ["gear", "brewing"],
        [
            "We sell loose leaf only, so people ask what to actually brew it in. The options, roughly ranked: an infuser basket in a teapot, the leaves loose in the pot with a strainer when pouring, a cotton reusable bag, and, last, the little metal tea ball.",
            "The tea ball is last because leaves need room to expand. Rolled oolong triples in size; crammed in a ball it never opens and never tastes right. A big basket infuser, like the one in our ceramic teapot, gives the leaf space and lifts out cleanly to stop the steep.",
            "Loose in the pot is how most of the world does it and it makes the best tea, at the cost of a strainer and a slightly messier sink. Cotton bags are fine for herbals and for travel.",
        ],
        products=["ceramic-teapot-600", "glass-teapot-with-infuser", "travel-kettle-mini"],
        next_posts=["tea-storage-mistakes", "how-to-steep-oolong-properly"],
    ),
    _post(
        "chai-at-home", "Chai at home: the stovetop method",
        "How to make proper masala chai on the stovetop with our Cuba Street Chai blend: simmer, add milk, simmer again.",
        "2026-05-23", ["recipes", "chai"],
        [
            "Steeping chai in a teapot makes a spiced black tea. Simmering it on the stove makes chai. The difference is that the milk and the long, low heat pull the spices out in a way hot water on its own does not.",
            "For two cups: put 300 ml of water and two heaped teaspoons of Cuba Street Chai in a small pot, bring to a boil and simmer for three minutes. Add 200 ml of whole milk and sugar to taste, bring back to just under a boil, and simmer another two minutes. Strain into cups.",
            "Add a slice of fresh ginger with the water if you like it hotter. Oat milk works; almond milk splits. The Stovetop Classic kettle is what we use at the café for this because it is enamelled and does not mind milk.",
        ],
        products=["cuba-street-chai", "stovetop-classic-kettle"],
        next_posts=["behind-the-blend-wellington-breakfast", "iced-earl-grey-lemonade"],
    ),
    _post(
        "workshop-recap-winter", "Workshop recap: the winter tasting series",
        "What happened at our four winter tasting workshops, the teas people liked most, and the surprise winner nobody expected.",
        "2026-05-16", ["workshops", "events"],
        [
            "We ran four workshops over June and July at the Petone café: an introduction to tasting, an oolong deep dive, a tea and cheese night, and a kettle clinic where people brought their broken kettles and we mostly descaled them.",
            "Across about ninety attendees the most-liked tea was, again, Milford Mist Oolong. The surprise was Genmaicha, which came second overall, mostly because people had never tried it and liked the popcorn thing. The lapsang split the room exactly as it always does.",
            "The next series starts in October. Tickets are on the workshops page, and the Tasting Flight Set is the take-home version if you cannot make it to Petone.",
        ],
        products=["milford-mist-oolong", "genmaicha-toasted-rice", "tasting-flight-set"],
        next_posts=["pairing-tea-with-cheese", "tasting-notes-vocabulary"],
    ),
    _post(
        "tea-storage-mistakes", "Five tea storage mistakes we see all the time",
        "Light, air, moisture, heat and strong smells: the five ways tea goes stale, and the tins that stop it.",
        "2026-05-09", ["storage", "gear"],
        [
            "Tea does not go off, exactly, but it does go flat. Loose leaf kept badly loses its aroma in a couple of months; kept well it lasts a year or more. The enemies are light, air, moisture, heat and strong smells, and here is how people let each one in.",
            "One: leaving it in the paper pouch. Our pouches are resealable but they are not airtight. Two: a glass jar on a sunny shelf, which looks lovely and cooks the tea. Three: the cupboard above the stove, where it is warm and damp. Four: next to the coffee or the spices, because tea absorbs smells beautifully, which is how Earl Grey gets made and how your green tea ends up tasting of cumin. Five: the fridge, unless it is sealed properly, for the same reason.",
            "The fix is a tin with a good lid in a cool, dark cupboard. That is what the caddy trio is for. The help centre has a note on best-before dates and what they actually mean for tea.",
        ],
        products=["tin-caddy-trio", "southerly-earl-grey"],
        next_posts=["reusable-tea-bags-vs-loose-leaf", "descale-your-kettle"],
    ),
    _post(
        "iced-earl-grey-lemonade", "Iced Earl Grey lemonade",
        "A recipe for iced Earl Grey lemonade: cold brew the tea, add lemon and a little sugar, serve over ice.",
        "2026-05-02", ["recipes", "summer"],
        [
            "This is the drink that sells out at the café every warm weekend, and it is embarrassingly easy. Cold brew Southerly Earl Grey at 10 grams per litre overnight. Make a simple syrup with equal parts sugar and water. Juice some lemons.",
            "To serve: fill a glass with ice, pour in two thirds Earl Grey, add the juice of half a lemon and a tablespoon of syrup, top with soda water if you like fizz. Stir. The bergamot and the lemon are natural friends.",
            "It also works with Pōhutukawa Berry for a pink version, which children and adults respond to in equal measure.",
        ],
        products=["southerly-earl-grey", "pohutukawa-berry"],
        next_posts=["cold-brew-tea-summer", "chai-at-home"],
    ),
    _post(
        "subscription-box-september-unboxing", "What was in the September subscription box",
        "This month's Kererū subscription box: Milford Mist Oolong, Genmaicha, a new limited chamomile and a brewing card.",
        "2026-09-02", ["subscription", "unboxing"],
        [
            "September's box went out on the first of the month. Inside: a 50 g pouch of Milford Mist Oolong, a 50 g pouch of Genmaicha, a 30 g taster of a limited chamomile and lemon balm blend we are trialling, and the brewing card for oolong that also lives in the help centre.",
            "The theme was 'spring, allegedly', on the grounds that Wellington in September is technically spring. Feedback on the chamomile blend decides whether it goes into the range. Email us or reply to the box email.",
            "If you are not a subscriber, the subscription page explains how it works: choose a size, choose a caffeine preference, pause whenever.",
        ],
        products=["milford-mist-oolong", "genmaicha-toasted-rice", "golden-bay-chamomile"],
        next_posts=["how-to-steep-oolong-properly", "our-first-year"],
    ),
    _post(
        "wellington-wind-and-warm-cups", "On Wellington wind and the case for a warm cup",
        "A short, slightly sentimental essay about living in the windiest city in the world and why a kettle is a form of shelter.",
        "2026-04-25", ["wellington", "essay"],
        [
            "Wellington averages 173 days a year with gusts over 60 km/h. That is not a boast; it is a warning. It is also, we think, why this is such a good tea city. Coffee is for the morning rush. Tea is for the moment you get inside, shut the door, and hear the wind hit the window instead of you.",
            "There is a particular kind of afternoon in July when the southerly comes straight up the harbour, the rain goes horizontal, and the only reasonable response is to put the kettle on. Every Wellingtonian knows it. Most of them reach for a breakfast tea; the brave ones reach for the lapsang.",
            "We named the company after the kererū because it is a big, slightly ridiculous bird that sits in the trees through all of it, looking unbothered. That is the goal.",
        ],
        products=["wellington-breakfast", "manuka-smoked-lapsang"],
        next_posts=["history-of-tea-in-wellington", "our-first-year"],
    ),
    _post(
        "a-day-at-the-warehouse", "A day at the Petone warehouse",
        "What actually happens at Kererū Kettle Co. between an order arriving and a box leaving: blending, packing, smoking, kettle testing.",
        "2026-04-18", ["company", "behind the scenes"],
        [
            "The warehouse is a former panel beater's on a side street in Petone, and on a normal Tuesday it goes like this. Seven in the morning: the overnight orders print. Two people pack while a third weighs and seals pouches from the blending bins. Anything ordered before noon ships the same day.",
            "Mid-morning is blending. Wellington Breakfast is made in 20 kilo batches in a tumble mixer, chai is made in 10 kilo batches by hand because the spices bruise. Once a fortnight the smokehouse runs and nobody gets anything else done because everyone is standing outside sniffing.",
            "Afternoons are kettles. Every Gooseneck Pro is boiled and temperature-checked before it goes out, which is slow but means we have had eleven warranty returns in two years. Then the courier, then the café for a cup of whatever went slightly wrong in blending.",
        ],
        products=["gooseneck-kettle-pro", "wellington-breakfast", "cuba-street-chai"],
        next_posts=["our-first-year", "smoky-teas-explained"],
    ),
    _post(
        "tea-for-people-who-hate-tea", "Tea for people who hate tea",
        "If you think tea tastes like hot water and sadness, you have been drinking bad tea badly. Here is where to start.",
        "2026-04-11", ["beginners"],
        [
            "Most people who say they hate tea have had two experiences: a supermarket bag left in boiling water for a minute, and a herbal tea that promised strawberries and delivered warm disappointment. Neither is tea's fault.",
            "Where to start, depending on what you do like. Coffee drinkers: Wellington Breakfast, brewed strong, with milk, or Midnight Oolong Roast, which tastes like cocoa. Wine drinkers: Milford Mist Oolong, which has more going on in the glass than most pinot gris. Whisky drinkers: the lapsang, obviously. People who like juice: Pōhutukawa Berry, cold brewed.",
            "And use enough leaf. The single biggest fix for 'tastes like nothing' is more tea in the pot. The help centre has a guide to how much per cup.",
        ],
        products=["midnight-oolong-roast", "milford-mist-oolong", "pohutukawa-berry"],
        next_posts=["tasting-notes-vocabulary", "tea-vs-coffee-caffeine"],
    ),
]

BY_SLUG = {d["slug"]: d for d in POSTS}


def post_url(slug: str) -> str:
    return "/blog/{}/".format(slug)


def _jsonld(d: dict) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": d["title"],
        "description": d["description"],
        "datePublished": d["date"],
        "author": {"@type": "Organization", "name": "Kererū Kettle Co."},
        "keywords": ", ".join(d["tags"]),
    }


def _post_page(d: dict) -> Page:
    body = ['<p class="meta">Published {} · {}</p>'.format(esc(d["date"]), esc(", ".join(d["tags"])))]
    body.append("<article>" + p(*d["paras"]) + d.get("extra_html", "") + "</article>")
    body.append(related("Mentioned in this post", [(product_url(s), BY_SLUG_P[s]["name"]) for s in d["products"] if s in BY_SLUG_P]))
    body.append(related("Read next", [(post_url(s), BY_SLUG[s]["title"]) for s in d["next_posts"] if s in BY_SLUG]))
    return Page(
        path=post_url(d["slug"]),
        title="{} | Kererū Kettle Co. blog".format(d["title"]),
        description=d["description"],
        h1=d["title"],
        body="".join(body),
        section="blog",
        jsonld=_jsonld(d),
        lastmod=d["date"],
    )


def _index_page() -> Page:
    posts = sorted(POSTS, key=lambda d: d["date"], reverse=True)
    parts = [p("Brewing guides, kettle opinions, Wellington history and the occasional recipe. New posts most weeks, wind permitting.")]
    parts.append(card_list([(post_url(d["slug"]), d["title"], d["description"]) for d in posts]))
    parts.append("<h2>Drafts and oddities</h2>")
    parts.append(ul([link("/blog/untitled-draft/", "An untitled draft that escaped")]))
    return Page(
        path="/blog/",
        title="Blog | Kererū Kettle Co.",
        description="Brewing guides, kettle opinions, Wellington tea history and recipes from the Kererū Kettle Co. team.",
        h1="The Kererū blog",
        body="".join(parts),
        section="blog",
        lastmod="2026-09-14",
    )


def _untitled_draft() -> Page:
    # No <title>, no meta description, no <h1>.
    body = "<article>" + p(
        "this is the draft about the new chamomile blend that i started on the train and never finished. notes so far: lemon balm ratio too high at 30 percent, try 20. the valerian version is definitely out, it smelled like socks.",
        "todo: ask the wairarapa growers about lemon balm. todo: photos. todo: title.",
    ) + "</article>" + related("Related", [(post_url("tea-and-sleep"), "Tea and sleep"), (product_url("sleepy-tui-blend"), "Sleepy Tūī Blend")])
    return Page(
        path="/blog/untitled-draft/",
        title="", description="", h1="",
        body=body,
        section="blog",
        omit_title=True, omit_description=True, omit_h1=True,
        lastmod="2026-09-03",
        test_note="Linked from the blog index, in the sitemap, but has no title, meta description or h1.",
    )


def _unlisted_staff_picks() -> Page:
    # Orphan: in the sitemap, linked from nowhere.
    body = "<article>" + p(
        "This is the unlisted staff picks page we send to the newsletter and never linked from the site. Each person on the team names the tea they would take to a desert island with a kettle.",
        "Ana: Milford Mist Oolong, no contest. Tama: the lapsang, because the island will need a campfire anyway. Priya: Genmaicha, for breakfast, lunch and dinner. Josh: Wellington Breakfast, because he is a simple man with a large mug.",
    ) + "</article>" + related("Their picks", [(product_url(s), BY_SLUG_P[s]["name"]) for s in ("milford-mist-oolong", "manuka-smoked-lapsang", "genmaicha-toasted-rice", "wellington-breakfast")])
    return Page(
        path="/blog/unlisted-staff-picks/",
        title="Staff picks (unlisted) | Kererū Kettle Co. blog",
        description="The team's desert island teas. An unlisted page for newsletter readers.",
        h1="Staff picks: desert island teas",
        body=body,
        section="blog",
        jsonld=_jsonld(dict(title="Staff picks", description="Desert island teas", date="2026-08-05", tags=["staff picks"])),
        lastmod="2026-08-05",
        test_note="Orphan blog post: in the sitemap but no internal links point to it.",
    )


def pages():
    out = [_index_page()]
    out.extend(_post_page(d) for d in POSTS)
    out.append(_untitled_draft())
    out.append(_unlisted_staff_picks())
    return out
