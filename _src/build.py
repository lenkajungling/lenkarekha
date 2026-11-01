"""Generátor webu lenkarekha.com — spusť `python3 _src/build.py` z kořene projektu.
Společná hlavička a patička jsou tady, obsah jednotlivých stránek níže."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EMAIL = "lenka.jungling@gmail.com"
PHONE = "+420 778 522 095"
WA = "https://wa.me/420778522095"
IG = "https://www.instagram.com/lenka_rekha_/"
FB = "https://www.facebook.com/LenkaRekha"
ICO = "13983237"
FORM = "https://formspree.io/f/mdavpakp"

# Čtyři pilíře: (slug, název, podpoložky (odkaz, text), krátký popis, fotka)
PILLARS = [
    ("dech", "Dech", [("dech.html#pranajama", "Pránájáma a dechové techniky"), ("dech.html#workshopy", "Workshop Flow State Reset")],
     "Pránájáma, dechové techniky a tříhodinový workshop Flow State Reset.", "relaxace-podlozka.jpg"),
    ("pohyb", "Pohyb", [("pohyb.html#individualne", "Individuální lekce"), ("pohyb.html#lekce", "Skupinové lekce"), ("firmy.html", "Firemní lekce"), ("dech.html#workshopy", "Workshop Flow State Reset")],
     "Hravá flow a integrovaná terapie ve skupině, individuální lekce a lekce pro firmy.", "lekce-skupina.jpg"),
    ("dotek", "Dotek", [("dotek.html#intuitivni-masaz", "Intuitivní masáž")],
     "Intuitivní masáž: sportovní masáž, aromaterapie, dech a thajská masáž v jednom.", "masaz.jpg"),
    ("voda", "Voda", [("voda.html#vnitrni-ponor", "Vnitřní ponor"), ("voda.html#retreat", "V rytmu oceánu: Bali, duben 2027"), ("voda.html#freediving", "Kurzy freedivingu od léta 2027")],
     "Vnitřní ponor, retreat na Bali a od léta 2027 kurzy freedivingu.", "ponor-lano.jpg"),
]
CESTA_SUB = [("moje-cesta.html#pribeh", "Můj příběh"), ("moje-cesta.html#vzdelani", "Vzdělání a certifikace"),
             ("moje-cesta.html#reference", "Reference"), ("podnikavky.html", "Komunita: Podnikavky Přerov")]

PLACES = [
    ("Přerov", "Jóga a Pilates", "Žerotínovo nám. 14, 750 02 Přerov"),
    ("Olomouc", "Centrum Dákiní", "8. května 12, 779 00 Olomouc"),
    ("Lipník nad Bečvou", "Frida cafe", "Losertova 624/12, 751 31 Lipník nad Bečvou"),
    ("Hradčany", "Hradčany 64", "751 11 Radslavice"),
]


REFS = {
    "arnaud": ("Arnaud", "online pranayama, freediver", "We had an online pranayama session and I can honestly say it was incredible! Even though Lenka is currently in India, the virtual class felt so personal and engaging, like being in a real in-person session. Using our headphones, I could fully immerse myself in her guidance, breathing exercises, and the sense of presence she creates. As a freediver, I found her pranayama techniques especially helpful for improving my breathing technique and breathholds, which are key for diving deeper and staying calm underwater. Lenka is such a talented and engaging teacher, and I highly recommend her classes to anyone looking to learn about yoga. Thank you, Lenka, for this amazing experience. Can’t wait for the next session!"),
    "sandra": ("Sandra", "masáž", "Ráda bych touto cestou poděkovala za vynikající masáž. Moje zkušenost byla maximálně pozitivní, a to především díky tomu, že masáž byla zaměřena přesně na problematické partie (záda, lopatky, šíje), které mě dlouhodobě trápí. Oceňuji velmi citlivý, ale přitom účinný přístup. Podařilo se uvolnit i hluboké svalové napětí. Po návštěvě cítím výrazné povolení. Celková péče probíhala v klidném a příjemném duchu. Vřele doporučuji!"),
    "marketa": ("Markéta", "online lekce na míru", "Lenčiny online lekce jsou skvělé. Vytvoří ti lekci přímo na míru. Řekneš jí předem, s čím máš problémy, a ona ti udělá lekci přímo na to. A hlavně to jsou cviky, které nejsou těžké a které můžeš dělat i sama doma. Všem moc doporučuji!"),
    "olga": ("Olga", "učitelka", "Jsem workoholik. Díky józe s Lenkou jsem zpomalila. Učím se mít ráda svoje tělo, trénuji dechové návyky a užívám si jejich vliv na energii i duši. Po hodině cvičení je mi skvěle. Umím pracovně vypnout, zklidnit se a zahnat negativní myšlenky."),
    "zuzka": ("Zuzka", "zubní lékařka", "Díky Lenčinu individuálnímu přístupu je pro mě nyní jóga radostí, záda mě nebolí a cvičím i sama doma."),
    "monika": ("Monika", "event manažerka, IN-HUB Přerov", "Lenka u nás v IN-HUB Přerov vede jógu pro naše členy a je vážně skvělá. Pro lidi je to ideální způsob, jak na chvíli vypnout od práce, protáhnout se a přijít během hektického dne na jiné myšlenky. Cením si toho, jak je flexibilní a časově nám vždycky vyjde vstříc. Pokud hledáte pro svou firmu někoho spolehlivého, s kým je radost spolupracovat a kdo lidem opravdu pomůže si odpočinout, Lenku stoprocentně doporučuji."),
    "zivina": ("Markéta", "Business Development, Živina", "Firemní lekce jógy s Lenkou navštěvovali zaměstnanci napříč společností, od administrativních pozic až po pracovníky ve výrobě. Pravidelný pohyb, vědomá práce s dechem a cílené uvolnění pomáhaly kompenzovat jednostranné zatížení, snižovat stres a podporovat celkovou pohodu zaměstnanců. Velmi oceňujeme profesionální vedení, individuální přístup a schopnost přizpůsobit lekce různým potřebám účastníků."),
}


def ref_cards(keys):
    out = []
    for k in keys:
        n, role, q = REFS[k]
        lang = ' lang="en"' if k == "arnaud" else ""
        out.append(f'<figure class="ref-card"><blockquote{lang}>{q}</blockquote><figcaption><strong>{n}</strong>{role}</figcaption></figure>')
    return "".join(out)


def maps(q):
    return "https://www.google.com/maps/search/?api=1&query=" + q.replace(" ", "+").replace(",", "%2C")


def logo(pre, sub=True):
    s = '<span class="logo-sub">FLOW • DIVE • YOGA</span>' if sub else ""
    return (f'<a class="logo" href="{pre}./" aria-label="Rekha — domů">r<span class="e">e</span>kha</a>{s}')


def page(path, title, desc, body, current=None):
    depth = path.count("/")
    pre = "../" * depth
    def item(slug, label, subs):
        cur = ' aria-current="page"' if slug == current else ""
        sub = "".join(f'<a href="{pre}{h}">{t}</a>' for h, t in subs)
        return (f'<div class="nav-item"><a class="nav-top" href="{pre}{slug}.html"{cur}>{label}</a>'
                f'<div class="nav-sub">{sub}</div></div>')
    nav = [item(sl, n, subs) for sl, n, subs, *_ in PILLARS]
    nav.append(item("moje-cesta", "Moje cesta", CESTA_SUB))
    kcur = ' aria-current="page"' if current == "kontakt" else ""
    nav.append(f'<a class="nav-top" href="{pre}kontakt.html"{kcur}>Kontakt</a>')
    fcur = ' aria-current="page"' if current == "firmy" else ""
    nav.append(f'<a class="nav-firmy" href="{pre}firmy.html"{fcur}>Pro firmy</a>')
    nav.append(f'<a class="btn nav-cta" href="{pre}rozvrh.html">Rozvrh</a>')
    svc_links = "".join(f'<li><a href="{pre}{sl}.html">{n}</a></li>' for sl, n, *_ in PILLARS)
    html = f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://lenkarekha.com/assets/img/freediving-kanon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;1,9..40,400&family=Dancing+Script:wght@500;600&display=swap">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <div>{logo(pre, sub=False)}</div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Hlavní menu">{''.join(nav)}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer wv-up">
  <div class="wrap">
    <p class="foot-big">Dech, pohyb,<br>dotek, <span class="hand">voda.</span></p>
    <div class="foot-grid">
      <div>
        <div>{logo(pre)}</div>
        <p style="margin-top:0.8rem">Lektorka jógy a jógové terapie, průvodkyně dechem a freediverka. Lekce v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech.</p>
      </div>
      <div>
        <h4>Dech · Pohyb · Dotek · Voda</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Web</h4>
        <ul>
          <li><a href="{pre}moje-cesta.html">Moje cesta</a></li>
          <li><a href="{pre}rozvrh.html">Rozvrh</a></li>
          <li><a href="{pre}moje-cesta.html#reference">Reference</a></li>
          <li><a href="{pre}firmy.html">Pro firmy</a></li>
          <li><a href="{pre}podnikavky.html">Podnikavky Přerov</a></li>
          <li><a href="{pre}gdpr.html">Ochrana osobních údajů</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{WA}">WhatsApp {PHONE}</a></li>
          <li><a href="{IG}">Instagram</a></li>
          <li><a href="{FB}">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>Lenka Jüngling</span>
      <span>IČO {ICO}</span>
      <span>Podnikatelka zapsaná v živnostenském rejstříku</span>
      <span>© 2026</span>
    </div>
  </div>
</footer>
<div class="depth" aria-hidden="true"><span class="depth-val">−0 m</span><span class="depth-line"><span class="depth-dot"></span></span></div>
<script src="{pre}assets/main.js"></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def contact_form(pre, topic="", subject="Nová zpráva z webu", button="Odeslat zprávu"):
    options = ["Dech: pránájáma nebo workshop", "Pohyb: skupinové lekce", "Individuální lekce", "Dotek: masáž",
               "Voda: Vnitřní ponor", "Retreat na Bali", "Firemní lekce", "Podnikavky", "Jiné"]
    opts = "".join(f'<option{" selected" if o == topic else ""}>{o}</option>' for o in options)
    return f"""<form class="form" action="{FORM}" method="POST" data-ajax>
  <input type="hidden" name="_subject" value="{subject}">
  <div class="row">
    <label for="f-name">Jméno *<input id="f-name" name="jmeno" type="text" required autocomplete="name"></label>
    <label for="f-contact">E-mail nebo telefon *<input id="f-contact" name="kontakt" type="text" required></label>
  </div>
  <label for="f-topic">Co tě zajímá?<select id="f-topic" name="tema">{opts}</select></label>
  <label for="f-msg">Zpráva<textarea id="f-msg" name="zprava" placeholder="Napiš mi, co potřebuješ, nebo s čím váháš."></textarea></label>
  <label class="check" for="f-gdpr"><input id="f-gdpr" name="souhlas" type="checkbox" value="ano" required><span>Souhlasím se <a href="{pre}gdpr.html">zpracováním osobních údajů</a> za účelem odpovědi na mou zprávu.</span></label>
  <div class="btn-row"><button class="btn" type="submit">{button}</button></div>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>"""


def cta_band(pre, title="Nevíš, co je pro tebe to pravé?", text="Napiš mi pár vět o tom, co tě trápí nebo co hledáš. Společně najdeme cestu.", btn="Napsat mi"):
    return f"""<section class="section s-deep wv-up cta-band">
  <div class="wrap">
    <div class="stack"><h2>{title}</h2><p style="max-width:52ch;opacity:.9">{text}</p></div>
    <a class="btn light" href="{pre}kontakt.html">{btn}</a>
  </div>
</section>"""


def band(pre, img, alt, inner="", cls="", pos="center"):
    """Fotka přes celou šířku, při posouvání se jemně pohybuje (parallax)."""
    return f"""<section class="band {cls}">
  <div class="band-media"><img src="{pre}assets/img/{img}" alt="{alt}" data-parallax style="object-position:{pos}"></div>
  <div class="band-inner"><div class="wrap">{inner}</div></div>
</section>"""


REKHA_LINE = """<svg class="rekha-line" viewBox="0 0 1440 160" preserveAspectRatio="none" aria-hidden="true">
  <path d="M-20 110 C 180 20, 330 150, 520 90 S 860 10, 1010 80 S 1300 150, 1460 60"/>
</svg>"""

# ======================= DOMŮ =======================
quiz = [
    ("dotek.html#intuitivni-masaz", "Cítím napětí v těle a potřebuju ho pustit.", "Chci vědomý dotek, ne jen mechaniku.", "Dotek"),
    ("dech.html", "Potřebuju se zklidnit a pořádně nadechnout.", "Pránájáma a dechové techniky pro klid a soustředění.", "Dech"),
    ("pohyb.html#lekce", "Necvičím málo, spíš necvičím správně.", "Chci detailní vedení, ne pořád to samé.", "Pohyb: integrovaná terapie"),
    ("pohyb.html#lekce", "Potřebuju se hýbat s radostí.", "Bez tlaku na výkon.", "Pohyb: hravá flow"),
    ("voda.html", "Táhne mě hloubka.", "Chci se naučit pracovat s nádechem, který vydrží.", "Voda"),
    ("pohyb.html#individualne", "Chci péči jen pro sebe.", "Individuálně, na míru, s podporou i mezi lekcemi.", "Individuálně"),
    ("firmy.html", "Hledám to samé pro svůj tým.", "Jóga a dech přímo na pracovišti.", "Pro firmy"),
]
quiz_rows = "".join(
    f'<li><a href="{h}"><strong>{q}</strong><small>{d}</small><span class="go">→ {t}</span></a></li>'
    for h, q, d, t in quiz)
quiz_rows += ('<li><a href="podnikavky.html"><strong>Podnikám (nebo chci) a hledám ženy, které tomu rozumí.</strong>'
              '<small>Neformální setkání v Přerově a okolí.</small><span class="go">→ Podnikavky Přerov</span></a></li>')


index_rows = "".join(
    (f'<li><a href="{sl}.html"><h3>{n}</h3><p>{d}</p><span class="arrow">→</span>'
     + (f'<img class="peek" src="assets/img/{img}" alt="" loading="lazy">' if img else '') + '</a></li>')
    for sl, n, subs, d, img in PILLARS)

MARQUEE = "".join(f"<span>{w}</span>" for w in ["dech", "pohyb", "dotek", "voda"] * 3)

home = f"""
{band('', 'freediving-kanon.jpg', 'Freediverka klesá mezi skalními stěnami do modré hloubky', """
      <div class="band-text">
        <h1>Dech, pohyb, dotek, <span class="hand">voda.</span><span class="sub">Cesta zpátky k sobě má víc podob.</span></h1>
        <p class="lead">Jsem Lenka Rekha, lektorka jógy a jógové terapie, průvodkyně dechem a freediverka. Přes deset let pomáhám lidem naslouchat vlastnímu tělu. Individuálně, ve skupině i pod hladinou.</p>
        <div class="btn-row">
          <a class="btn light" href="pohyb.html#individualne">Domluvit úvodní lekci</a>
          <a class="btn outline-light" href="kontakt.html">Napsat mi</a>
        </div>
      </div>""", "band-hero", "center 42%").replace('</section>', '<a class="scroll-cue" href="#co-hledas">ponoř se ↓</a></section>')}

<section class="section s-white wv-up" id="nabidka">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Co pro tebe mám</p><h2>Začni <span class="hand">tady</span></h2></div>
    <div class="offers" data-rv>
      <a class="offer-card" href="pohyb.html#individualne"><span class="tag">Nezávazná úvodní lekce</span><h3>Individuální lekce</h3><p>Jóga, dech a pohyb přesně pro tebe. Osobně i online, s podporou mezi lekcemi.</p><span class="btn">Rezervovat lekci</span></a>
      <a class="offer-card" href="dech.html#workshopy"><span class="tag">So 21. 11. · Mariánské Lázně</span><h3>Workshop Flow State Reset</h3><p>Tři hodiny pohybu a dechu. Odneseš si nástroje, jak se zklidnit a vrátit do flow.</p><span class="btn">Přihlásit se</span></a>
      <a class="offer-card" href="voda.html#vnitrni-ponor"><span class="tag">Nový běh od ledna 2027</span><h3>Kurz Vnitřní ponor</h3><p>Jóga a dech inspirované freedivingem. 10 lekcí ve studiu a 1 v jámě.</p><span class="btn">Mám zájem</span></a>
      <a class="offer-card" href="firmy.html"><span class="tag">Nezávazná úvodní lekce</span><h3>Jóga pro firmy</h3><p>Pravidelné lekce pro týmy v Přerově a Olomouci. Méně bolesti zad a stresu.</p><span class="btn">Poptat pro firmu</span></a>
    </div>
  </div>
</section>

<section class="section s-foam wv-up wv-down" id="co-hledas">
  <div class="wrap quiz">
    <div class="quiz-head">
      <p class="eyebrow">Rychlá orientace</p>
      <h2>Co tě dnes <span class="hand">přivádí?</span></h2>
      <p class="lead">Vyber větu, která ti je nejblíž. Ukážu ti, co pro tebe můžu udělat.</p>
    </div>
    <ul class="quiz-list" data-rv>{quiz_rows}</ul>
  </div>
</section>

{band('', 'lekce-bambus.jpg', 'Skupina cvičí jógu na bambusové terase s výhledem na moře', '<p class="band-quote">Nádech. Výdech. <span class="hand">Přítomný okamžik.</span></p>', 'right')}

<section class="section s-foam wv-up wv-down">
  <div class="wrap story">
    <div class="story-photo" data-rv>
      <img src="assets/img/lenka-portret.jpg" alt="Usměvavá Lenka Rekha s rukama pod bradou" loading="lazy">
      <span class="note">to jsem já, Lenka</span>
    </div>
    <div class="story-text" data-rv>
      <p class="eyebrow">Moje cesta</p>
      <p class="pull">Byla jsem političkou, spolumajitelkou kavárny a devět let jsem strávila v korporátu. <em>Pak přišel zlom, který rozum umlčel.</em></p>
      <p>Dnes učím to, co jsem se musela naučit sama: vnímat tělo, dech a to, co je uvnitř skutečné. Londýn, Indie, Filipíny, Bali a zase zpátky v Přerově.</p>
      <div><a class="link-arrow" href="moje-cesta.html">Celý příběh →</a></div>
    </div>
  </div>
</section>

{band('', 'lekce-terasa.jpg', 'Ranní lekce jógy na terase s výhledem na oceán', '<p class="band-quote">Jóga bez nálepek <span class="hand">a mantinelů.</span></p>')}

<section class="section s-mint wv-up">
  <div class="wrap">
    <div class="section-head stack" style="margin-bottom:2.6rem;max-width:820px">
      <p class="eyebrow">Čtyři cesty k sobě</p>
      <h2>Jak spolu můžeme <span class="hand">pracovat</span></h2>
    </div>
    <ul class="index" data-rv>{index_rows}</ul>
  </div>
</section>

{band('', 'lenka-plaz-sirka.jpg', 'Lenka s rukama nad hlavou a zavřenýma očima na pláži u moře', '<p class="band-quote">Nádech, který vydrží <span class="hand">déle, než si myslíš.</span></p>', 'right', '30% 35%')}

<section class="section s-teal wv-up wv-down">
  <div class="wrap">
    <p class="eyebrow" style="margin-bottom:2rem">Co říkají ti, kdo se mnou cvičí</p>
    <div class="refs-mag" data-rv>
      <figure class="big-quote">
        <blockquote>{REFS["zuzka"][2]}</blockquote>
        <figcaption>{REFS["zuzka"][0]}, {REFS["zuzka"][1]}</figcaption>
      </figure>
      <div class="small-quotes">
        <figure><blockquote>{REFS["olga"][2]}</blockquote><figcaption>{REFS["olga"][0]}, {REFS["olga"][1]}</figcaption></figure>
        <figure><blockquote>{REFS["sandra"][2]}</blockquote><figcaption>{REFS["sandra"][0]}, {REFS["sandra"][1]}</figcaption></figure>
        <div><a class="btn light" href="moje-cesta.html#reference">Všechny reference</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section s-deep wv-up" style="padding-top:clamp(5rem,9vw,7rem)">
  <div class="wrap contact-split">
    <div class="stack-lg">
      <p class="eyebrow">Kontakt</p>
      <h2>Napiš <span class="hand" style="color:var(--mint)">mi.</span></h2>
      <p class="lead">Ať už váháš, co je pro tebe to pravé, nebo přesně víš, co chceš. Odpovídám osobně, obvykle do 24 hodin.</p>
      <ul class="contact-list">
        <li><span class="k">WhatsApp</span><a href="{WA}">{PHONE}</a></li>
        <li><span class="k">E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="k">Instagram</span><a href="{IG}">@lenka_rekha_</a></li>
      </ul>
    </div>
    <div class="form-card" data-rv>{contact_form('')}</div>
  </div>
</section>
"""
page("index.html", "Lenka Rekha — dech, pohyb, dotek, voda",
     "Lenka Rekha: pránájáma, hravá flow, integrovaná terapie, intuitivní masáž a freediving. Přerov, Olomouc, Lipník nad Bečvou, Hradčany.",
     home, "index")

# ======================= MOJE CESTA =======================
journey = [
    ("Přerov · korporát", "Než přišla jóga", [
        "Vyrostla jsem v Přerově. Vystudovala jsem ekonomku a nastoupila do korporátu. Ne proto, že bych věděla, co chci, ale proto, že jsem to nevěděla. Vdala jsem se, abych unikla, a to doslova do Londýna.",
        "Třetinu života jsem byla manželkou, dvě třetiny hodnou dcerou, která následovala představu rodičů o ideálním životě: dostudovat, najít kancelářskou práci, vdát se, pořídit byt, založit rodinu. Rozhodovala jsem se rozumem, i když mi intuice radila něco jiného. A rozum byl vždycky hlasitější."], None),
    ("Londýn · Peru · Indie", "Londýn, Peru, Indie", [
        "V Londýně začala moje transformace. Studovala jsem u učitele aštángy Scotta Johnsona a poprvé si začala klást otázky, kterým jsem se předtím vyhýbala: Kdo jsem? Co vlastně chci? Jaké je moje poslání?",
        "Pak přišly tři intenzivní léčivé ceremonie v peruánské amazonské džungli. O rok později první cesta do Indie, do Maisúru, na intenzivní kurz u Saraswathi Jois, dcery zakladatele aštánga jógy. Jógu jsem zkoumala na sobě i skrze učení druhých, až jsem si udělala lektorský kurz u Kabira, studenta Oshovy tradice. Dávat energii korporátu přestalo dávat smysl."],
     ("indie-maisur.jpg", "Maisúr, Indie poprvé")),
    ("Zpátky v Přerově", "Návrat domů a další oklika", [
        "Po návratu domů jsem chtěla dávat zpátky komunitě. Kromě naší kavárny i skrze politiku. Byla jsem aktivní v Pirátské straně, organizovala sbírky v době covidu i za války na Ukrajině, dostala se do zastupitelstva a s kolegy jsme prosadili třeba vznik dostupného městského bydlení místo bourané Strojaře.",
        "Zároveň jsem začala učit. Nejdřív kamarády, pak menší skupinky. Honila jsem se za dokonalým provedením ásán, praktikovala aštángu denně a byla na sebe extrémně přísná, až jsem si skoro zničila koleno. Naštěstí jsem tehdy potkala učitelku, která mě zpomalila a naučila naslouchat tělu místo toho, abych ho přemáhala."],
     ("prerov-navrat.jpg", "Zpátky v Přerově")),
    ("Zlom", "Když intuici nikdo neposlouchá", [
        "Pak přišel rozchod. Samovolný potrat. Fungovala jsem na autopilota, přes spoustu lekcí jógy a ostré lokty v politice. Intuice říkala: odpočiň si, něco změň. Neposlechla jsem ji. Místo toho jsem se vrhla do intenzivního masérského kurzu. A po něm přišlo vyhoření."], None),
    ("Filipíny · Bali", "Freediving jako učitel", [
        "Tentokrát už intuici nešlo umlčet rozumem. Vyklidila jsem byt, prodala hromadu věcí a odstěhovala se na Filipíny. Půl roku jsem budovala jógovo-freedivingovou komunitu pod Blue Freedom, potkala světové špičky v oboru a hlavně se ponořila sama do sebe.",
        "Ten pocit, když padáte volným pádem hlouběji do hlubin a neexistuje nic než přítomný okamžik, se těžko popisuje. Freediving se pro mě stal učitelem a životním stylem. Dokončila jsem certifikát AIDA4 a asistentku instruktora, učila jógu a dech na místech jako Panglao, Siquijor nebo Amed na Bali, i po boku uznávaných jmen oboru, jako jsou Ben Piguet nebo Sergey Busargin."],
     ("lenka-snorchl.jpg", "Po ranním ponoru")),
    ("Indie podruhé", "Jógová terapie", [
        "Než jsem se vrátila do Česka, strávila jsem půl roku v Indii, převážnou část studiem jógové terapie pod vedením Sonal Chaudhari. Její učitel Kobad Variava se pod přímým dohledem B.K.S. Iyengara stal seniorním učitelem. Tahle linie je dodnes základem toho, jak k tělu přistupuji."],
     ("indie-setkani.jpg", "Indie, setkání s dalajlámou")),
    ("Teď a tady", "Jóga bez nálepek", [
        "Po téměř dvou letech v Asii jsem si konečně odpověděla na otázky, kdo jsem a co chci. Jsem lektorka, která skrze autentičnost předává vlastní zkušenost prací s tělem. V mém přístupu se potkává dotek, pohyb, jóga i poznatky z freedivingu.",
        "Naučila jsem se žít v přítomném okamžiku, místo abych zůstávala v minulosti nebo budoucnosti. Od striktní aštángy jsem se přesunula k józe bez nálepek a mantinelů. V mém pojetí je jóga prostě taková, jako jsem já sama. A tenhle posun neberu jako konečný. Pořád se učím být vděčnější, objevovat svoji sílu a obracet věci k dobru, i pro druhé.",
        "Podporuji ženy i muže na jejich cestě k autentičtějšímu životu. Individuálně, ve skupinách, na suchu i pod hladinou."],
     ("tanec-sal.jpg", "Tanec, celoživotní láska")),
]
tl = []
for place, h, paras, fig in journey:
    if place == "Filipíny · Bali":
        tl.append('</div></div></section>' + band('', 'zelva-ponor.jpg', 'Lenka se noří vedle mořské želvy nad písečným dnem', '<p class="band-quote">Tentokrát už intuici nešlo umlčet rozumem.</p>', '', 'center 58%') + '<section class="section"><div class="wrap"><div class="timeline">')
    ps = "".join(f"<p>{p}</p>" for p in paras)
    f = (f'<figure><img src="assets/img/{fig[0]}" alt="{fig[1]}" loading="lazy"><figcaption>{fig[1]}</figcaption></figure>' if fig else "")
    tl.append(f'<article class="tl-item" data-rv><div class="tl-place"><b>{len([x for x in tl if x.startswith("<article")]) + 1:02d}</b><span>{place}</span></div><div><h2>{h}</h2>{ps}{f}</div></article>')

kdo = [("kdo-01-kdo-jsem", "Kdo jsem?"), ("kdo-02-ucitelka", "učitelka"), ("kdo-03-joginka", "jogínka"), ("kdo-04-freediverka", "freediverka"),
       ("kdo-05-tanecnice", "tanečnice"), ("kdo-06-cestovatelka", "cestovatelka"), ("kdo-07-propojovatelka", "propojovatelka"), ("kdo-08-zena", "žena")]
KDO = "".join(f'<img src="assets/img/{f}.jpg" alt="Lenka Rekha — {t}" loading="lazy">' for f, t in kdo)
certs = [
    ("Aštánga jóga", "Scott Johnson", "Londýn"),
    ("Yoga Chikitsa", "Manju Jois", "Londýn"),
    ("Intenzivní kurz aštánga jógy", "Saraswathi Jois", "Maisúr, Indie"),
    ("Lektorský kurz jógy", "Kabir, Oshova tradice", ""),
    ("Lektor/ka jógy, akreditace MŠMT", '<span class="todo-inline">název kurzu, rok</span>', ""),
    ("Jógová terapie", "Sonal Chaudhari, linie B.K.S. Iyengara", "Indie"),
    ("Freediving AIDA4 a asistentka instruktora", "AIDA", "Filipíny"),
    ("Sportovní masáž", '<span class="todo-inline">kde</span>', ""),
]
CERTS = "".join(f'<li><strong>{a}</strong><span>{b}</span><em>{c}</em></li>' for a, b, c in certs)
cats = [("Pohyb", ["zuzka", "marketa", "olga"]), ("Dech", ["arnaud"]), ("Dotek", ["sandra"]), ("Firmy", ["monika", "zivina"])]
REFS_ALL = ('<div class="ref-slider"><div class="ref-track" tabindex="0" aria-label="Reference, posouvej do strany">'
            + "".join(ref_cards(k).replace('<figcaption>', f'<figcaption><span class="ref-cat">{c}</span>') for c, k in cats)
            + '</div><div class="ref-nav"><button type="button" class="ref-prev" aria-label="Předchozí reference">←</button>'
            '<button type="button" class="ref-next" aria-label="Další reference">→</button></div></div>')
REFS_ALL += '<div class="todo">Další reference z rekhayoga.cz.</div>'
cesta = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Moje cesta</p>
    <div class="split rev" style="align-items:end">
    <div class="stack-lg">
    <h1>Kdo je Lenka Rekha?</h1>
    <p class="roles">učitelka · jogínka · freediverka · tanečnice · cestovatelka · propojovatelka · žena</p>
    <p class="lead">Lektorka jógy a jógové terapie s více než desetiletou praxí. Průvodkyně dechem, která kombinuje pranajámu s technikami z freedivingu. Celoživotní tanečnice. Freediverka s certifikací AIDA4. A taky někdo, kdo si prošel pěkně dlouhou oklikou, než se dostal tam, kde je teď.</p>
    </div>
    <div class="split-media" style="max-width:380px;justify-self:end"><img src="assets/img/lenka-portret.jpg" alt="Portrét Lenky Rekhy"></div>
    </div>
  </div>
</section>
<nav class="subnav wv-up" aria-label="Moje cesta: obsah stránky"><div class="wrap">{"".join(f'<a href="{h}">{t}</a>' for h, t in CESTA_SUB)}</div></nav>
<section class="section" id="pribeh">
  <div class="wrap">
    <div class="timeline">{''.join(tl)}</div>
    <div class="todo" style="margin-top:3rem;max-width:720px">Fotky ke kapitolám 01 Než přišla jóga, 03 Návrat domů a 07 Teď a tady (bez nápisů).</div>
  </div>
</section>
<section class="section s-foam wv-up" id="vzdelani">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Vzdělání a certifikace</p><h2>U koho jsem se <span class="hand">učila</span></h2></div>
    <ul class="certs" data-rv>{CERTS}</ul>
  </div>
</section>
<section class="section s-white wv-up" id="reference">
  <div class="wrap stack-lg">
    <div class="section-head" style="margin-bottom:0"><p class="eyebrow">Reference</p><h2>Co říkají ti, kdo se mnou <span class="hand">cvičí</span></h2></div>
    {REFS_ALL}
  </div>
</section>
<section class="section s-deep wv-up" id="komunita">
  <div class="wrap">
    <div class="pod-band">
      <div class="stack">
        <span class="pod-badge">Komunita · Podnikavky Přerov</span>
        <h2>Setkání podnikavých žen</h2>
        <p>Kromě vlastní praxe organizuji pravidelné neformální setkání pro ženy, které podnikají nebo o tom přemýšlí. 15. listopadu slavíme první narozeniny.</p>
      </div>
      <a class="btn sun" href="podnikavky.html">Chci vědět víc</a>
    </div>
  </div>
</section>
{cta_band('', 'Podívej se, jak spolu můžeme pracovat', 'Dech, pohyb, dotek, voda. Individuálně i ve skupině.', 'Napsat mi')}
"""
page("moje-cesta.html", "Moje cesta — Lenka Rekha",
     "Z korporátu přes Londýn, Indii a Filipíny k józe bez nálepek. Příběh Lenky Rekhy.", cesta, "moje-cesta")

# ======================= ČTYŘI PILÍŘE =======================
def ask(label, href="kontakt.html", cls=""):
    return f'<a class="btn {cls}" href="{href}">{label}</a>'


def subnav(slug):
    p = next(x for x in PILLARS if x[0] == slug)
    return "".join(f'<a href="{h}">{t}</a>' for h, t in p[2])


def refs_section(keys, eyebrow="Co říkají ti, kdo to zažili"):
    if not keys:
        return ""
    first, rest = keys[0], keys[1:]
    n, role, q = REFS[first]
    lang = ' lang="en"' if first == "arnaud" else ""
    small = "".join(
        f'<figure><blockquote{" lang=\"en\"" if k == "arnaud" else ""}>{REFS[k][2]}</blockquote><figcaption>{REFS[k][0]}, {REFS[k][1]}</figcaption></figure>'
        for k in rest)
    return f"""<section class="section s-teal wv-up" id="reference">
  <div class="wrap">
    <p class="eyebrow" style="margin-bottom:2rem">{eyebrow}</p>
    <div class="refs-mag" data-rv>
      <figure class="big-quote{' long' if len(q) > 260 else ''}"><blockquote{lang}>{q}</blockquote><figcaption>{n}, {role}</figcaption></figure>
      <div class="small-quotes">{small}<div><a class="btn light" href="moje-cesta.html#reference">Všechny reference</a></div></div>
    </div>
  </div>
</section>"""


def pillar_page(slug, name, h1, lead, hero, sections, refs, cta_title, cta_text):
    """Stránka jednoho pilíře: úvodní fotka, podmenu, sekce s kotvami, reference, výzva."""
    head_inner = f"""<div class="band-text">
    <p class="crumbs"><a href="./">Domů</a> / {name}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p></div>"""
    head = (band('', hero[0], hero[1], head_inner, "band-page", hero[2]) if hero
            else f'<section class="page-hero wv-down"><div class="wrap">{head_inner}</div></section>')
    secs = []
    for i, (sid, eyebrow, h2, body, aside, img) in enumerate(sections):
        bg = "s-white" if i % 2 == 0 else "s-foam"
        photo = (f'<div class="page-photo" style="margin-bottom:2.2rem"><img src="assets/img/{img[0]}" alt="{img[1]}" loading="lazy"></div>' if img else "")
        secs.append(f"""<section class="section {bg} wv-up" id="{sid}">
  <div class="wrap page-grid">
    <div>{photo}<div class="prose"><p class="eyebrow">{eyebrow}</p><h2 style="margin-top:0">{h2}</h2>{body}</div></div>
    <aside class="aside-card">{aside}</aside>
  </div>
</section>""")
    body = f"""
{head}
<nav class="subnav wv-up" aria-label="{name}: obsah stránky"><div class="wrap">{subnav(slug)}</div></nav>
{''.join(secs)}
{refs_section(refs)}
{cta_band('', cta_title, cta_text, 'Napsat mi')}
"""
    page(f"{slug}.html", f"{name} — Lenka Rekha", lead[:155], body, slug)


# ---------- DECH ----------
pillar_page("dech", "Dech", 'Dech je první <span class="hand">pohyb.</span>',
    "Pránájáma, dechové techniky a workshop Flow State Reset. Kombinuji klasickou práci s dechem z jógy s technikami z freedivingu.",
    ("relaxace-podlozka.jpg", "Klient leží se zavřenýma očima na podložce, Lenka mu uvolňuje ramena", "center 40%"),
    [
        ("pranajama", "Pránájáma a dechové techniky", "Klid, který si můžeš kdykoli přivolat",
         """<p><strong>Dechové techniky</strong> jsou praktické nástroje: jak prodloužit výdech, zklidnit nervový systém, soustředit se nebo prodloužit zádrž. Naučíš se je rychle a použiješ je hned, třeba před spaním, před důležitým jednáním nebo před ponorem. Propojuji je s poznatky z freedivingu.</p>
<p><strong>Pránájáma</strong> jde hlouběji. Je to jedna z cest jógy, komplexní praxe, která pracuje s dechem, energií a pozorností zároveň. Nejde jen o techniku, ale o to, jak dech mění tvůj vnitřní stav. Potřebuje pravidelnost a čas, a o to víc ti dá.</p>
<h3>Pránájáma ve studiu Sangha</h3>
<p>Jednou měsíčně v neděli ráno, 9:00–10:00.</p>
<ul class="offer">
<li><span>Neděle 29. 11. 2026 · 9:00–10:00 · Sangha Přerov</span><span class="price">300 Kč</span></li>
<li><span>Neděle 20. 12. 2026 · 9:00–10:00 · Sangha Přerov</span><span class="price">300 Kč</span></li>
</ul>""",
         """<h3>Nejbližší pránájáma</h3><p>Neděle 29. 11. a 20. 12., 9:00–10:00, studio Sangha, 300 Kč.</p><p>Dechové techniky tě naučím i individuálně, osobně nebo online.</p>""" + ask("Přihlásit se"),
         ("lekce-filipiny.jpg", "Skupina na pláži v pozici válečníka s rukama nad hlavou")),
        ("workshopy", "Workshop", "Flow State Reset",
         """<p>Tříhodinový workshop. Praktický vhled do propojení pohybu a dechu jako nástrojů vědomé seberegulace. Bez výkonu a bez tlaku na dokonalost.</p>
<div class="blocks">
<div class="block"><span class="tag">Pohyb</span><h3>Pohyb a flow</h3><p>Jógovo-pohybová lekce inspirovaná elementem vody. Skrze spinální vlny, spirální linie a rotace postupně odkrýváme, kde v těle neseš chronické napětí, a právě tyhle pohybové vzorce cíleně uvolňujeme.</p></div>
<div class="block"><span class="tag">Dech</span><h3>Dech a nervový systém</h3><p>Začínáme BOLT testem (Body Oxygen Level Test), jednoduchým měřením tolerance CO₂. Pak prodloužený výdech, přirozené přechody do zádrží a technika udžají. Workshop uzavírá integrace a mindfulness.</p></div>
</div>
<p>Odneseš si konkrétní nástroje pro vědomou práci s vlastním stavem, přenositelné do každodenního života.</p>""",
         """<h3>Nejbližší workshop</h3>
<ul class="offer"><li><span>So 21. 11. 2026 · 9:00–12:00 · studio Kineo, Mariánské Lázně</span><span class="price">900 Kč</span></li></ul>
<p>Chceš workshop pro svou skupinu, studio nebo firmu? Napiš mi.</p>""" + ask("Přihlásit se"),
         ("lenka-tanec.jpg", "Lenka se zavřenýma očima a úsměvem v pohybu, soustředěná na dech")),
    ],
    ["arnaud"], "Chceš se nadechnout jinak?", "Napiš mi, co potřebuješ. Domluvíme pránájámu, workshop nebo individuální práci s dechem.")

# ---------- POHYB ----------
pillar_page("pohyb", "Pohyb", 'Pohyb bez <span class="hand">mantinelů.</span>',
    "Skupinové lekce hravá flow a integrovaná terapie, individuální lekce a lekce pro firmy.",
    ("lekce-skupina.jpg", "Skupina v pozici trojúhelníku na terase u moře", "center 40%"),
    [
        ("individualne", "Individuální lekce", "Péče ušitá na míru",
         """<p>Pro tebe, ne pro skupinu. Kombinuji jógu, dech, pohyb i masáž, přizpůsobené přesně tobě. Sledujeme tvůj progres, zadávám domácí úkoly a jsem ti k dispozici i mezi lekcemi. Osobně i online.</p>
<ul class="offer">
<li><span>Nezávazná úvodní lekce. Poznáme se a zjistíme, co potřebuješ.</span><span class="price">zdarma</span></li>
<li><span>Balíček 5 lekcí</span><span class="price">5 000 Kč</span></li>
<li><span>Balíček 10 lekcí, domácí úkoly, dokumentace progresu, podpora přes WhatsApp</span><span class="price">10 000 Kč</span></li>
</ul>""",
         f"""<h3>Domluv si úvodní lekci</h3><p>Napiš mi, co tě trápí nebo co hledáš. Domluvíme termín a místo.</p>{ask('Napsat mi')}<p style="font-size:.95rem">Nebo rovnou na <a href="{WA}">WhatsApp</a>.</p>""",
         ("lekce-popruh.jpg", "Lenka nastavuje klientovi jógový popruh přes ramena")),
        ("lekce", "Skupinové lekce", "Hravá flow a integrovaná terapie",
         """<h3>Integrovaná terapie</h3>
<p>Možná nepotřebuješ víc cvičit. Možná jen jinak. Detailní práce s tělem, přesné vedení a hlubší porozumění pohybu, inspirované linií B.K.S. Iyengara, ve které jsem se sama učila. Vhodné i pro ty, kdo mají za sebou zranění nebo je bolí záda.</p>
<h3>Hravá flow</h3>
<p>Rozproudi energii a pohybuj se s radostí. Dynamické sekvence, síla a kreativita. Někdy jemnější, jindy silovější, vždy bez tlaku a vždy trochu jiná.</p>
<p>Lekce probíhají v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech. Cena 200–300 Kč za lekci.</p>""",
         """<h3>Přijď na lekci</h3><p>Všechny časy najdeš v rozvrhu. Místo si rezervuj přes WhatsApp.</p>""" + ask("Rozvrh lekcí", "rozvrh.html"),
         ("lenka-tanec-smich.jpg", "Lenka se smíchem tančí ve světlém sále")),
        ("firmy", "Firemní lekce", "Jóga a dech přímo u vás",
         """<p>Pravidelné lekce jógové terapie pro týmy v Přerově a Olomouci. Ulevují zádům a hlavě, zlepšují posturu při dlouhém sezení a posilují odolnost vůči stresu. Začínáme nezávaznou úvodní lekcí.</p>""",
         """<h3>Pro firmy</h3><p>Balíčky, ceny a reference firem najdeš na samostatné stránce.</p>""" + ask("Nabídka pro firmy", "firmy.html"),
         None),
    ],
    ["zuzka", "olga", "marketa"], "Nevíš, která lekce je pro tebe?", "Napiš mi pár vět o tom, co tě trápí nebo co hledáš. Společně najdeme cestu.")

# ---------- DOTEK ----------
pillar_page("dotek", "Dotek", 'Dotek, který tělu vrátí <span class="hand">rovnováhu.</span>',
    "Intuitivní masáž: sportovní masáž, aromaterapie, dech a prvky thajské masáže v jednom. Zaměřuji se hlavně na záda, šíji, hlavu a hrudník.",
    ("masaz.jpg", "Ruce masírují šíji a krk ležící klientky", "center 38%"),
    [
        ("intuitivni-masaz", "Intuitivní masáž", "Vědomý dotek",
         """<p>Moje intuitivní masáž kombinuje <strong>sportovní masáž, aromaterapii, práci s dechem a prvky thajské masáže</strong>. Není to jen mechanická technika. Je to vědomý dotek, který uvolní napětí, zklidní nervový systém a znovu tě propojí s vlastním tělem a dechem.</p>
<p>Každé setkání přizpůsobuji tomu, co tělo právě potřebuje. Někdy hlubší práce se svaly, jindy jemnější přístup k celkovému uvolnění. Začínáme krátkou konzultací, pak masíruji.</p>
<p>Jsem lektorka jógy a dlouhodobě pracuji s dechem a vědomým pohybem. Jako tanečnice i freediverka se učím vnímat tělo, rytmus a dech v hlubší rovině. Dotek je přirozeným rozšířením téhle práce.</p>
<p>Brzy v nabídce i thajská masáž na futonu.</p>""",
         """<h3>Pro koho</h3><p>Pro každého, kdo cítí napětí v těle, potřebuje si odpočinout nebo chce svému tělu dopřát vědomou péči.</p><p><span class="todo-inline">kde masíruješ?</span></p>""" + ask("Rezervovat masáž"),
         None),
        ("cenik", "Ceník", "Kolik to stojí",
         """<ul class="offer">
<li><span>Intuitivní masáž · 45 minut + 10 minut konzultace</span><span class="price">800 Kč</span></li>
<li><span>Intuitivní masáž · 60 minut + 10 minut konzultace</span><span class="price">1 000 Kč</span></li>
</ul>
<p>Brzy v nabídce i <strong>thajská masáž na futonu</strong>.</p>""",
         """<h3>Rezervace</h3><p>Termín domluvíme přes WhatsApp nebo e-mail.</p>""" + ask("Napsat mi"),
         None),
    ],
    ["sandra"], "Cítíš napětí, které nechce povolit?", "Napiš mi a domluvíme termín masáže.")

# ---------- VODA ----------
pillar_page("voda", "Voda", 'Nádech, který vydrží <span class="hand">déle.</span>',
    "Vnitřní ponor, retreat V rytmu oceánu na Bali a od léta 2027 kurzy freedivingu.",
    ("ponor-lano.jpg", "Freediverka u lana pod hladinou proti slunci", "center 30%"),
    [
        ("vnitrni-ponor", "Vnitřní ponor", "Příprava na freediving",
         """<p>Kurz, který propojuje metodiku Molchanovs a AIDA s jógou a prací s dechem. Nejde o čas ani hloubku. Jde o zkušenost, klid a schopnost zůstat v těle i tam, kde by tělo chtělo panikařit.</p>
<ul>
<li>10 lekcí ve studiu a 1 lekce v jámě.</li>
<li>Skupina 8–10 lidí, uzavřená podpora na WhatsAppu, týdenní domácí úkoly.</li>
<li>Pro dospělé 30+, kteří rádi zkoušejí nové věci. Nejde o výkon, jde o zážitek.</li>
</ul>
<ul class="offer">
<li><span>Kurz (10 lekcí ve studiu)</span><span class="price">3 000 Kč</span></li>
<li><span>Lekce v jámě</span><span class="price"><span class="todo-inline">cena</span></span></li>
</ul>""",
         """<h3>Další běh začíná v lednu 2027</h3><p>Místa ve skupině jsou omezená. Napiš mi a pošlu ti termíny jako první.</p>""" + ask("Mám zájem o kurz"),
         ("meditace-bazen.jpg", "Lenka sedí se zavřenýma očima v meditaci na okraji bazénu, odráží se ve vodě")),
        ("retreat", "V rytmu oceánu", "Retreat na Bali, duben 2027",
         """<p>Retreat, který spojuje jógu, dech a freediving v Amedu na Bali, na jednom z nejkrásnějších míst pro ponor. Prostor zpomalit a ponořit se hlouběji do sebe i do vody.</p>
<p><strong>Další retreat proběhne v dubnu 2027</strong> <span class="todo-inline">přesné datum</span>. Program, ubytování, ceny a přihlášku najdeš na stránce retreatu.</p>""",
         """<h3>Duben 2027 · Amed, Bali</h3><p>Všechny podrobnosti a přihláška.</p><a class="btn" href="https://lenkajungling.github.io/v-rytmu-oceanu/">Stránka retreatu</a>
<div class="todo" style="margin-top:.6rem">Stránka retreatu se upravuje na dubnový termín. Formulář z MailerLite pro novinky o retreatech.</div>""",
         ("lekce-terasa.jpg", "Ranní lekce na terase s výhledem na oceán v Amedu")),
        ("freediving", "Od léta 2027", "Kurzy freedivingu",
         """<p>Od léta 2027 otevřu kurzy freedivingu ve vodě. Navážou na Vnitřní ponor a povedou tě od prvních ponorů s bezpečností a klidem.</p>""",
         """<h3>Chceš vědět jako první?</h3><p>Napiš mi a dám ti vědět, jakmile vypíšu termíny.</p>""" + ask("Dej mi vědět"),
         ("bazen.jpg", "Freediveři u bóje v bazénu")),
    ],
    [], "Táhne tě hloubka?", "Napiš mi a pošlu ti termíny dalšího Vnitřního ponoru i retreatu.")

# ---------- PRO FIRMY ----------
firmy_inner = """<div class="band-text">
    <p class="crumbs"><a href="./">Domů</a> / <a href="pohyb.html">Pohyb</a> / Pro firmy</p>
    <h1>Pohyb a dech pro celý <span class="hand">tým.</span></h1>
    <p class="lead">Pravidelné lekce jógové terapie přímo u vás, v Přerově a Olomouci. Snižují bolest zad a hlavy, zlepšují posturu při dlouhodobém sezení a posilují odolnost vůči stresu.</p></div>"""
firmy = f"""
{band('', 'lekce-korekce.jpg', 'Lenka koriguje pozici klientky na lekci', firmy_inner, 'band-page')}
<section class="section s-white wv-up">
  <div class="wrap page-grid">
    <div class="prose">
      <h2 style="margin-top:0">Proč to funguje</h2>
      <div class="blocks">
        <div class="block"><h3>Úleva od bolesti zad a hlavy</h3><p>Jógová terapie cílí na příčiny obtíží: zkrácené svaly, přetížené fascie a kompenzační vzorce při dlouhém sezení u počítače.</p></div>
        <div class="block"><h3>Lepší postura</h3><p>Systematická práce s tělem mění způsob, jak lidé sedí, stojí a dýchají, i mimo lekci.</p></div>
        <div class="block"><h3>Méně stresu</h3><p>Dechové techniky z pránájámy, které využívají i profesionální freediveři, dokáží během minut zklidnit nervovou soustavu a obnovit soustředění.</p></div>
        <div class="block"><h3>Silnější tým</h3><p>Sdílená praxe stmeluje. Lekce jsou prostor, kde se lidé potkají jinak než u monitoru.</p></div>
      </div>
      <h2>Balíčky</h2>
      <ul class="offer">
        <li><span><strong>Nezávazná úvodní lekce</strong> pro váš tým</span><span class="price">zdarma</span></li>
        <li><span><strong>Měsíční spolupráce</strong> · 4 × 50 min, skupina do 15 osob</span><span class="price">12 000 Kč / měs.</span></li>
        <li><span><strong>Půlroční spolupráce</strong> · 4 × 50 min měsíčně, celkem 48 000 Kč, ušetříte 24 000 Kč</span><span class="price">8 000 Kč / měs.</span></li>
      </ul>
      <p>Ceny jsou bez DPH. Doprava v rámci Přerova a Olomouce zdarma. Lekce probíhají před pracovní dobou nebo po ní, bez zásahu do chodu firmy. Workshop Flow State Reset nabízím i pro týmy.</p>
    </div>
    <aside class="aside-card"><h3>Nabídka pro váš tým</h3><p>Napište mi. Do 48 hodin se ozvu s konkrétním návrhem frekvence, formátu a ceny.</p>{ask('Poptat spolupráci')}</aside>
  </div>
</section>
{refs_section(["monika", "zivina"], "Co říkají firmy")}
{cta_band('', 'Chcete to vyzkoušet?', 'Začněte nezávaznou úvodní lekcí.', 'Napsat mi')}
"""
page("firmy.html", "Pro firmy — Lenka Rekha", "Jógová terapie a dech pro firmy v Přerově a Olomouci. Nezávazná úvodní lekce.", firmy, "firmy")

# ======================= ROZVRH =======================
rows = [
    ("prerov", "Pondělí", "15:00–16:00", "MENS rehabilitace", "soukromá skupinka", "Přerov", "Jóga a Pilates", ""),
    ("lipnik", "Pondělí", "17:00–18:00", "Hravá flow", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("lipnik", "Pondělí", "18:15–19:15", "Integrovaná terapie", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("olomouc", "Úterý", "17:45–18:45", "Jóga", "kurz, volné místo", "Olomouc", "Centrum Dákiní", "300 Kč"),
    ("prerov", "Středa", "16:45–18:00", "Integrovaná terapie", "kurz, volné místo", "Přerov", "Jóga a Pilates", "300 Kč"),
    ("prerov", "Středa", "18:15–19:30", "Hravá flow", "kurz, volné místo", "Přerov", "Jóga a Pilates", "300 Kč"),
    ("lipnik", "Čtvrtek", "15:00–16:00", "Integrovaná terapie", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("lipnik", "Čtvrtek", "16:15–17:15", "Hravá flow", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("hradcany", "Čtvrtek", "18:00–19:00", "Jóga", "", "Hradčany", "Hradčany 64", "200 Kč"),
    ("prerov", "Neděle", "9:00–10:00", "Pránájáma", "1× měsíčně: 29. 11. a 20. 12.", "Přerov", "Studio Sangha", "300 Kč"),
]
trs = "".join(
    f'<tr data-city="{c}"><td class="day">{d}</td><td>{t}</td><td>{l}{f"<small>{n}</small>" if n else ""}</td><td>{city}<small>{pl}</small></td><td>{p}</td></tr>'
    for c, d, t, l, n, city, pl, p in rows)
rozvrh = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Rozvrh</p>
    <h1>Rozvrh lekcí</h1>
    <p class="lead">Přerov, Olomouc, Lipník nad Bečvou a Hradčany. Na lekci se stačí ozvat na WhatsApp nebo e-mail. Středeční lekce v Přerově a úterní v Olomouci běží jako kurzy, ale je v nich volné místo.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtr podle místa">
      <button type="button" data-city="vse" aria-pressed="true">Vše</button>
      <button type="button" data-city="prerov" aria-pressed="false">Přerov</button>
      <button type="button" data-city="olomouc" aria-pressed="false">Olomouc</button>
      <button type="button" data-city="lipnik" aria-pressed="false">Lipník nad Bečvou</button>
      <button type="button" data-city="hradcany" aria-pressed="false">Hradčany</button>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Den</th><th>Čas</th><th>Lekce</th><th>Místo</th><th>Cena</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
    </div>
    <div class="blocks" style="margin-top:2rem">
      <div class="block"><span class="tag">Kurz</span><h3>Vnitřní ponor</h3><p>Další běh kurzu (10 lekcí ve studiu a 1 v jámě) začíná v lednu 2027.</p><a class="link-arrow" href="voda.html#vnitrni-ponor">O kurzu →</a></div>
      <div class="block"><span class="tag">Workshop</span><h3>Flow State Reset</h3><p>So 21. 11. 2026, 9:00–12:00, studio Kineo, Mariánské Lázně, 900 Kč.</p><a class="link-arrow" href="dech.html#workshopy">O workshopu →</a></div>
    </div>
    <div class="btn-row" style="margin-top:2.4rem">
      <a class="btn" href="{WA}">Rezervovat přes WhatsApp</a>
      <a class="btn ghost" href="kontakt.html">Napsat zprávu</a>
    </div>
  </div>
</section>
"""
page("rozvrh.html", "Rozvrh — Lenka Rekha",
     "Rozvrh lekcí jógy: Přerov, Olomouc, Lipník nad Bečvou, Hradčany.", rozvrh, "pohyb")

# ======================= PODNIKAVKY =======================
podnikavky = f"""
<section class="page-hero pod wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Podnikavky Přerov</p>
    <span class="pod-badge">Podnikavky Přerov</span>
    <h1>Setkání podnikavých žen</h1>
    <p class="lead">Pravidelné, neformální setkání pro ženy, které podnikají, nebo o tom teprve přemýšlí. Přerov a okolí.</p>
  </div>
</section>
<section class="section" id="o-nas">
  <div class="wrap page-grid">
    <div class="prose">
      <h2 style="color:var(--sun);margin-top:0">O Podnikavkách</h2>
      <p>Podnikavky Přerov jsou místo, kde se ženy z regionu potkávají, sdílí zkušenosti, inspirují se navzájem a budují si vlastní podnikatelskou síť. Bez tlaku, bez soutěžení, s otevřenou náručí pro začátečnice i zkušené podnikatelky.</p>
      <p>Setkání organizuji já, Lenka Rekha, protože vím, jaké to je začínat vlastní cestu bez opory. A jak moc pomůže mít kolem sebe ženy, které tomu rozumí.</p>
      <div class="page-photo"><img src="assets/img/podnikavky-inhub.jpg" alt="Lenka s kolegyní mluví ke ženám na setkání Podnikavek v IN-HUB Přerov" style="aspect-ratio:4/5;max-width:420px;object-position:center 30%"></div>
      <div class="todo">Logo Podnikavek (připravuje se).</div>
    </div>
    <aside class="aside-card" style="background:var(--sun-tint);color:var(--ink)" id="akce">
      <h3 style="color:var(--sun-dark)">Nejbližší setkání</h3>
      <ul class="offer"><li><span><strong>15. 11. 2026</strong> · první narozeniny Podnikavek 🎉<br><span class="todo-inline">čas a místo</span></span></li></ul>
    </aside>
  </div>
</section>
<section class="section" style="background:var(--sun-tint)" id="prihlaska">
  <div class="wrap split">
    <div class="stack">
      <h2 style="color:var(--sun-dark)">Přihlas se na nejbližší setkání</h2>
      <p class="lead">Stačí pár údajů. Pošlu ti podrobnosti a místo konání.</p>
    </div>
    <div class="form-card">
      <form class="form" action="{FORM}" method="POST" data-ajax>
        <input type="hidden" name="_subject" value="Přihláška — Podnikavky Přerov">
        <input type="hidden" name="tema" value="Podnikavky">
        <div class="row">
          <label for="p-name">Jméno *<input id="p-name" name="jmeno" type="text" required autocomplete="name"></label>
          <label for="p-email">E-mail *<input id="p-email" name="email" type="email" required autocomplete="email"></label>
        </div>
        <label for="p-how">Jak dlouho podnikáš (nebo plánuješ)?<input id="p-how" name="podnikani" type="text"></label>
        <label for="p-exp">Co od setkání očekáváš?<textarea id="p-exp" name="ocekavani"></textarea></label>
        <label class="check" for="p-gdpr"><input id="p-gdpr" name="souhlas" type="checkbox" value="ano" required><span>Souhlasím se <a href="gdpr.html">zpracováním osobních údajů</a> za účelem organizace setkání.</span></label>
        <div class="btn-row"><button class="btn sun" type="submit">Přihlásit se</button></div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""
page("podnikavky.html", "Podnikavky Přerov — setkání podnikavých žen",
     "Neformální setkání pro ženy, které podnikají nebo o tom přemýšlí. Přerov a okolí.", podnikavky, "moje-cesta")

# ======================= KONTAKT =======================
places = "".join(f'<a class="place" href="{maps(a + ", " + p)}"><strong>{c}</strong><span>{p}<br>{a}</span></a>'.replace('<a class="place"', '<a class="place" style="text-decoration:none"') for c, p, a in PLACES)
kontakt = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Kontakt</p>
    <h1>Napiš mi.</h1>
    <p class="lead">Ať už váháš, co je pro tebe to pravé, nebo už přesně víš, co chceš, ozvi se. Odpovídám osobně, obvykle do 24 hodin.</p>
  </div>
</section>
<section class="section">
  <div class="wrap page-grid">
    <div class="form-card">{contact_form('')}</div>
    <aside class="stack-lg">
      <ul class="contact-list">
        <li><span class="k">WhatsApp / telefon</span><a href="{WA}">{PHONE}</a></li>
        <li><span class="k">E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="k">Instagram</span><a href="{IG}">@lenka_rekha_</a></li>
        <li><span class="k">Facebook</span><a href="{FB}">Lenka Rekha</a></li>
      </ul>
    </aside>
  </div>
</section>
<section class="section tint">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Kde cvičíme</p><h2>Místa lekcí</h2></div>
    <div class="places">{places}</div>
  </div>
</section>
"""
page("kontakt.html", "Kontakt — Lenka Rekha", "Kontakt na Lenku Rekhu: WhatsApp, e-mail, Instagram, místa lekcí.", kontakt, "kontakt")

# ======================= GDPR =======================
gdpr = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Ochrana osobních údajů</p>
    <h1>Zásady ochrany osobních údajů</h1>
    <p class="lead">Platné od 1. listopadu 2026.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="prose">
      <h2>Kdo zpracovává vaše údaje</h2>
      <p>Správcem osobních údajů je Lenka Jüngling, IČO {ICO}, působící pod značkou Lenka Rekha, se sídlem v Přerově. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <h2>Jaké údaje sbírám</h2>
      <p>Prostřednictvím formulářů na tomto webu sbírám jen to, co sami vyplníte:</p>
      <ul><li>jméno</li><li>e-mail nebo telefon</li><li>téma, o které máte zájem</li><li>obsah zprávy</li><li>u přihlášky na Podnikavky také informace o vašem podnikání a očekáváních</li></ul>
      <h2>K čemu údaje používám</h2>
      <p>Výhradně k tomu, abych vám odpověděla, domluvila s vámi lekci, masáž, kurz nebo účast na akci a poslala vám k nim potřebné informace. Pokud se přihlásíte k odběru novinek, posílám vám e-mailem informace o nových kurzech, workshopech a retreatech.</p>
      <h2>Právní základ</h2>
      <p>Zpracování probíhá na základě vašeho souhlasu, který udělujete zaškrtnutím pole ve formuláři (čl. 6 odst. 1 písm. a) GDPR).</p>
      <h2>Jak dlouho údaje uchovávám</h2>
      <p>Po dobu nezbytnou k vyřízení vaší zprávy nebo k poskytnutí služby, nejdéle však 2 roky od posledního kontaktu. Odběr novinek můžete kdykoli zrušit odkazem v každém e-mailu.</p>
      <h2>Komu údaje předávám</h2>
      <p>Vaše údaje neprodávám, nepronajímám ani nepředávám třetím stranám za účelem marketingu. Technicky je zpracovávají tito zpracovatelé, kteří se řídí vlastními zásadami GDPR:</p>
      <ul><li>Formspree (formspree.io): doručení zpráv z formulářů</li><li>MailerLite (mailerlite.com): rozesílání novinek, pouze pokud se k nim přihlásíte</li><li>GitHub Pages: hosting webu</li></ul>
      <h2>Vaše práva</h2>
      <ul><li>požádat o přístup ke svým osobním údajům</li><li>požádat o jejich opravu nebo výmaz</li><li>kdykoli odvolat souhlas se zpracováním, stačí napsat e-mail</li><li>podat stížnost u Úřadu pro ochranu osobních údajů (uoou.gov.cz)</li></ul>
      <p>Pro uplatnění práv mi napište na <a href="mailto:{EMAIL}">{EMAIL}</a>. Odpovím do 30 dnů.</p>
      <h2>Cookies</h2>
      <p>Tento web nepoužívá analytické ani marketingové cookies a nesleduje chování návštěvníků. Písma se načítají ze služby Google Fonts.</p>
    </div>
  </div>
</section>
"""
page("gdpr.html", "Ochrana osobních údajů — Lenka Rekha", "Zásady ochrany osobních údajů webu lenkarekha.com.", gdpr)

print("hotovo")
