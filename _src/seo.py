"""SEO: názvy stránek, popisy pro vyhledávače, strukturovaná data (schema.org) a časté otázky."""
import json

SITE = "https://lenkarekha.com/"

# stránka: (title, description)
META = {
    "index.html": ("Jóga Přerov a Olomouc, dech a freediving | Lenka Rekha",
                   "Lekce jógy, jógové terapie a pránájámy v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech. Intuitivní masáž, workshopy, kurz freedivingu na suchu a retreat na Bali."),
    "pohyb.html": ("Jóga Přerov, Olomouc, Lipník: jógová terapie a hravá flow | Lenka Rekha",
                   "Skupinové lekce jógy v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech, 200–300 Kč. Integrovaná jógová terapie pro všechny, hravá flow, individuální lekce a jóga pro firmy."),
    "dech.html": ("Pránájáma a dechové techniky Přerov, workshop Flow State Reset | Lenka Rekha",
                  "Pránájáma a dechové techniky ve studiu Sangha v Přerově. Tříhodinový workshop Flow State Reset: pohyb a dech pro zklidnění nervového systému."),
    "dotek.html": ("Intuitivní masáž Přerov | Lenka Rekha",
                   "Intuitivní masáž v Přerově: sportovní masáž, aromaterapie, dech a prvky thajské masáže. Záda, šíje, hlava, hrudník a nohy. 45 nebo 60 minut s konzultací."),
    "voda.html": ("Freediving na suchu: kurz Vnitřní ponor a retreat na Bali | Lenka Rekha",
                  "Kurz Vnitřní ponor: deset týdnů jógy, dechu a metodiky AIDA, lekce v jámě s certifikovaným instruktorem. Retreat V rytmu oceánu na Bali a kurzy freedivingu od léta 2027."),
    "firmy.html": ("Jóga pro firmy Přerov a Olomouc | Lenka Rekha",
                   "Firemní lekce jógové terapie a dechu v Přerově a Olomouci. Méně bolesti zad a stresu, nezávazná úvodní lekce, balíčky od 8 000 Kč měsíčně."),
    "moje-cesta.html": ("Lektorka jógy a freediverka Lenka Rekha: příběh a certifikace",
                        "Příběh lektorky jógy Lenky Rekhy: z korporátu přes Londýn, Indii a Filipíny k józe bez nálepek. Certifikace MŠMT, jógová terapie, AIDA4."),
    "rozvrh.html": ("Rozvrh lekcí jógy Přerov, Olomouc, Lipník, Hradčany | Lenka Rekha",
                    "Aktuální rozvrh lekcí jógy, jógové terapie, hravé flow a pránájámy v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech. Ceny 200–300 Kč."),
    "rezervace.html": ("Rezervace masáže a individuální lekce jógy Přerov | Lenka Rekha",
                       "Online rezervace intuitivní masáže a individuálních lekcí jógy v Přerově. Vyber si volný termín, potvrzení přijde e-mailem."),
    "kontakt.html": ("Kontakt: jóga, dech a masáže Přerov | Lenka Rekha",
                     "Napiš mi na WhatsApp, e-mail nebo přes formulář. Lekce jógy, masáže a kurzy v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech."),
}

FAQ = [
    ("Je jóga vhodná i pro začátečníky?",
     "Ano. Integrovaná jógová terapie je vhodná pro všechny, i pro ty, kdo mají za sebou zranění nebo je bolí záda. Hravá flow je spíš pro mírně pokročilé a pokročilé. Pokud si nejsi jistá nebo jistý, začni nezávaznou úvodní individuální lekcí."),
    ("Kde a kdy lekce jógy probíhají?",
     "V Přerově (Jóga a Pilates, studio Sangha), v Olomouci (centrum Dákiní), v Lipníku nad Bečvou (Frida cafe) a v Hradčanech (sál OÚ). Aktuální dny a časy najdeš v rozvrhu."),
    ("Kolik stojí lekce?",
     "Skupinové lekce jógy stojí 200–300 Kč. Balíček 5 individuálních lekcí je za 5 000 Kč, intuitivní masáž od 800 Kč, workshop Flow State Reset 900 Kč a kurz Vnitřní ponor 3 000 Kč."),
    ("Co je kurz Vnitřní ponor?",
     "Není to klasický jógový kurz ani kurz potápění. Je to deset týdnů, ve kterých propojujeme metodiku freedivingu AIDA s jógou, dechem a všímavostí. Kurz má 10 lekcí ve studiu a 1 lekci ve vodě s certifikovaným instruktorem."),
    ("Jaký je rozdíl mezi pránájámou a dechovými technikami?",
     "Dechové techniky jsou praktické nástroje, které použiješ hned, třeba na zklidnění nebo před spaním. Pránájáma jde hlouběji: je to komplexní jógová praxe, která pracuje s dechem, energií a pozorností zároveň."),
    ("Nabízíš jógu i pro firmy?",
     "Ano, pravidelné lekce jógové terapie a dechu pro týmy v Přerově a Olomouci. Začínáme nezávaznou úvodní lekcí, balíčky jsou od 8 000 Kč měsíčně."),
    ("Jak se na lekci přihlásím?",
     "Napiš mi na WhatsApp +420 778 522 095, e-mailem nebo přes formulář na webu. Odpovídám osobně, obvykle do 24 hodin."),
]


def faq_html():
    items = "".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return f"""<section class="section s-white wv-up" id="caste-otazky">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Časté otázky</p><h2>Co tě možná <span class="hand">zajímá</span></h2></div>
    <div class="faq" data-rv>{items}</div>
  </div>
</section>"""


def business(email, phone, ig, fb, places, gmaps):
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": SITE + "#lenka-rekha",
        "name": "Lenka Rekha – jóga, dech, freediving",
        "description": "Lekce jógy, jógové terapie a pránájámy, intuitivní masáž, workshopy, kurz freedivingu na suchu a retreat na Bali.",
        "url": SITE,
        "image": SITE + "assets/img/lenka-portret.jpg",
        "email": email,
        "telephone": phone.replace(" ", ""),
        "priceRange": "200–1000 Kč",
        "address": {"@type": "PostalAddress", "streetAddress": "Budovatelů 7", "postalCode": "750 02", "addressLocality": "Přerov", "addressCountry": "CZ"},
        "areaServed": ["Přerov", "Olomouc", "Lipník nad Bečvou", "Hradčany"],
        "sameAs": [ig, fb, gmaps],
        "founder": {
            "@type": "Person", "name": "Lenka Rekha",
            "jobTitle": "Lektorka jógy a jógové terapie, průvodkyně dechem, freediverka",
            "knowsAbout": ["jóga", "jógová terapie", "pránájáma", "dechové techniky", "freediving", "masáž"],
        },
        "location": [{"@type": "Place", "name": f"{pl}, {city}",
                      "address": {"@type": "PostalAddress", "streetAddress": addr, "addressCountry": "CZ"}}
                     for city, pl, addr in places],
    }


def events():
    loc_sangha = {"@type": "Place", "name": "Studio Sangha", "address": {"@type": "PostalAddress", "streetAddress": "nám. T. G. Masaryka 225/14", "postalCode": "750 02", "addressLocality": "Přerov", "addressCountry": "CZ"}}
    loc_kineo = {"@type": "Place", "name": "Studio Kineo", "address": {"@type": "PostalAddress", "streetAddress": "Anglická 682/17a", "postalCode": "353 01", "addressLocality": "Mariánské Lázně", "addressCountry": "CZ"}}
    org = {"@id": SITE + "#lenka-rekha"}

    def ev(name, start, end, loc, price, url):
        return {"@context": "https://schema.org", "@type": "Event", "name": name, "startDate": start, "endDate": end,
                "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled",
                "location": loc, "organizer": org, "performer": {"@type": "Person", "name": "Lenka Rekha"},
                "offers": {"@type": "Offer", "price": price, "priceCurrency": "CZK", "url": url}}
    return [
        ev("Workshop Flow State Reset", "2026-11-21T09:00+01:00", "2026-11-21T12:00+01:00", loc_kineo, "900", SITE + "dech.html#workshopy"),
        ev("Pránájáma ve studiu Sangha", "2026-11-29T09:00+01:00", "2026-11-29T10:00+01:00", loc_sangha, "300", SITE + "dech.html#pranajama"),
        ev("Pránájáma ve studiu Sangha", "2026-12-20T09:00+01:00", "2026-12-20T10:00+01:00", loc_sangha, "300", SITE + "dech.html#pranajama"),
    ]


def faq_schema():
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def sitemap(paths):
    urls = "".join(f"<url><loc>{SITE}{'' if p == 'index.html' else p}</loc></url>" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'


ROBOTS = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"
