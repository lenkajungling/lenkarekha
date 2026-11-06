"""Generátor webu lenkarekha.com — spusť `python3 _src/build.py` z kořene projektu.
Společná hlavička a patička jsou tady, obsah jednotlivých stránek níže."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import seo

ROOT = Path(__file__).resolve().parent.parent

EMAIL = "lenka.jungling@gmail.com"
PHONE = "+420 778 522 095"
WA = "https://wa.me/420778522095"
IG = "https://www.instagram.com/lenka_rekha_/"
FB = "https://www.facebook.com/LenkaRekha"
GMAPS = "https://share.google/nSKn5DJrgDvnfQj9e"
ICO = "13983237"
FORM = "https://formspree.io/f/mdavpakp"

# Čtyři pilíře: (slug, název, podpoložky (odkaz, text), krátký popis, fotka)
PILLARS = [
    ("dech", "Dech", [("dech.html#pranajama", "Lekce: Pránájáma a dechové techniky"), ("dech.html#workshopy", "Workshop: Flow State Reset"), ("voda.html#vnitrni-ponor", "Kurz: Vnitřní ponor (u Vody)")],
     "Pránájáma, dechové techniky a tříhodinový workshop Flow State Reset. Dech je i základ kurzu Vnitřní ponor u Vody.", "relaxace-podlozka.jpg"),
    ("pohyb", "Pohyb", [("pohyb.html#individualne", "Lekce: Individuální"), ("pohyb.html#lekce", "Lekce: Skupinové"), ("firmy.html", "Lekce: Pro firmy"), ("dech.html#workshopy", "Workshop: Flow State Reset (u Dechu)"), ("voda.html#vnitrni-ponor", "Kurz: Vnitřní ponor (u Vody)")],
     "Jóga: hravá flow a integrovaná terapie ve skupině, individuální lekce a jóga pro firmy.", "pohyb-terasa.jpg"),
    ("dotek", "Dotek", [("dotek.html#intuitivni-masaz", "Intuitivní masáž")],
     "Masáž: intuitivní masáž, která spojuje sportovní masáž, aromaterapii, dech a thajskou masáž.", "dotek-ruce.jpg"),
    ("voda", "Voda", [("voda.html#vnitrni-ponor", "Kurz: Vnitřní ponor"), ("voda.html#retreat", "Retreat: V rytmu oceánu"), ("voda.html#freediving", "Kurz: Freediving (od léta 2027)")],
     "Freediving: kurz Vnitřní ponor, retreat V rytmu oceánu na Bali a od léta 2027 kurzy freedivingu.", "ponor-lano.jpg"),
]
CESTA_SUB = [("moje-cesta.html#pribeh", "Můj příběh"), ("moje-cesta.html#vzdelani", "Vzdělání a certifikace"),
             ("moje-cesta.html#reference", "Reference"), ("podnikavky.html", "Komunita: Podnikavky Přerov")]

SANGHA = "nám. T. G. Masaryka 225/14, 750 02 Přerov"
KINEO = "Anglická 682/17a, 353 01 Mariánské Lázně"
PLACES = [
    ("Přerov", "Jóga a Pilates", "Žerotínovo nám. 14, 750 02 Přerov"),
    ("Přerov", "Studio Sangha", SANGHA),
    ("Olomouc", "Centrum Dákiní", "8. května 12, 779 00 Olomouc"),
    ("Lipník nad Bečvou", "Frida cafe", "Losertova 624/12, 751 31 Lipník nad Bečvou"),
    ("Hradčany", "Sál OÚ", "Hradčany 64, 751 11 Radslavice"),
]


REFS = {
    "arnaud": ("Arnaud", "online pránájáma, freediver", "Měli jsme online lekci pránájámy a byla úžasná. I když byla Lenka zrovna v Indii, lekce působila osobně, jako bychom byli ve stejné místnosti. Se sluchátky jsem se mohl úplně ponořit do jejího vedení a dechových cvičení. Jako freediverovi mi její techniky pránájámy hodně pomohly zlepšit dýchání a zádrže, které jsou klíčové pro hlubší ponor a klid pod vodou. Lenka je talentovaná a poutavá učitelka a její lekce vřele doporučuji každému, kdo se chce o józe dozvědět víc. Děkuju, Lenko, už se těším na další lekci!"),
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
        lang = ""
        out.append(f'<figure class="ref-card"><blockquote{lang}>{q}</blockquote><figcaption><strong>{n}</strong>{role}</figcaption></figure>')
    return "".join(out)


def maps(q):
    return "https://www.google.com/maps/search/?api=1&query=" + q.replace(" ", "+").replace(",", "%2C")


def logo(pre, sub=True):
    s = '<span class="logo-sub">FLOW • DIVE • YOGA</span>' if sub else ""
    return (f'<a class="logo" href="{pre}./" aria-label="Rekha — domů">r<span class="e">e</span>kha</a>{s}')


def nbsp(html):
    """Česká typografie: jednopísmenná slova (a, i, v, k, s, z, o, u) nezůstávají na konci řádku."""
    parts = re.split(r"(<script.*?</script>|<style.*?</style>|<[^>]+>)", html, flags=re.S)
    one = re.compile(r"(?<![\w&;])([AaIiKkOoSsUuVvZz])\s+(?=\S)")
    return "".join(x if x.startswith("<") else one.sub(r"\1&nbsp;", x) for x in parts)


BUILT = []


def page(path, title, desc, body, current=None):
    BUILT.append(path)
    title, desc = seo.META.get(path, (title, desc))
    canon = seo.SITE + ("" if path == "index.html" else path)
    schema = seo.ld(seo.business(EMAIL, PHONE, IG, FB, PLACES, GMAPS))
    if path == "index.html":
        schema += seo.ld(seo.faq_schema())
    if path == "dech.html":
        schema += "".join(seo.ld(e) for e in seo.events())
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
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="cs_CZ">
<link rel="canonical" href="{canon}">
<meta property="og:image" content="https://lenkarekha.com/assets/img/nahled.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{pre}assets/fonts.css">
<link rel="stylesheet" href="{pre}assets/style.css">
<link rel="icon" href="{pre}favicon.ico" sizes="32x32">
<link rel="icon" href="{pre}assets/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta name="theme-color" content="#369694">
<script data-goatcounter="https://lenkarekha.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
{schema}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <div>{logo(pre, sub=False)}</div>
    <span class="depth-mini" aria-hidden="true">−0 m</span>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Hlavní menu">{''.join(nav)}</nav>
  </div>
  <span class="depth-bar" aria-hidden="true"></span>
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
          <li><a href="{pre}obchodni-podminky.html">Obchodní podmínky</a></li>
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
          <li><a href="{GMAPS}" target="_blank" rel="noopener">Google: recenze</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>Lenka Jüngling</span>
      <span>Budovatelů 7, 750 02 Přerov</span>
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
    head, _, rest = html.partition("<body>")
    html = head + "<body>" + nbsp(rest)
    # fotky ve WebP (menší a rychlejší); JPG zůstává jen pro náhled na sociálních sítích a pro vyhledávače
    html = re.sub(r'(src="[^"]*assets/img/)([^"/]+)\.jpg"',
                  lambda m: m.group(1) + m.group(2) + (".webp" if (ROOT / "assets/img" / (m.group(2) + ".webp")).exists() else ".jpg") + '"', html)
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def contact_form(pre, topic="", subject="Nová zpráva z webu", button="Odeslat zprávu"):
    options = ["Úvodní lekce (nezávazná)", "Dech: pránájáma nebo workshop", "Pohyb: skupinové lekce", "Individuální lekce", "Dotek: masáž",
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
  <p class="form-note">Údaje použiju jen k odpovědi na tvou zprávu. Víc v <a href="{pre}gdpr.html">zásadách ochrany osobních údajů</a>.</p>
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
    ("firmy.html", "Hledám jógu pro svůj tým.", "Jóga a dech přímo na pracovišti.", "Pro firmy"),
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
{band('', 'lenka-plaz-sirka.jpg', 'Usměvavá Lenka Rekha s rukama nad hlavou na pláži u moře', """
      <div class="band-text">
        <h1>Dech, pohyb, dotek, <span class="hand">voda.</span><span class="sub">Cesta zpátky k sobě má víc podob.</span></h1>
        <p class="lead">Jsem Lenka Rekha, lektorka jógy a jógové terapie, průvodkyně dechem a freediverka. Téměř deset let pomáhám lidem naslouchat vlastnímu tělu. Individuálně, ve skupině, offline i online. Lekce jógy vedu v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech.</p>
        <div class="btn-row">
          <a class="btn light" href="kontakt.html?tema=Úvodní">Domluvit úvodní lekci</a>
          <a class="btn outline-light" href="kontakt.html">Napsat mi</a>
        </div>
      </div>""", "band-hero band-split", "18% 40%").replace('</section>', '<a class="scroll-cue" href="#co-hledas">ponoř se ↓</a></section>')}

<section class="section s-white wv-up wv-down" id="co-hledas">
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
      <span class="note">těší mě, Lenka</span>
    </div>
    <div class="story-text" data-rv>
      <p class="eyebrow">Moje cesta</p>
      <p class="pull">Byla jsem političkou, spolumajitelkou kavárny a devět let jsem strávila v korporátu. <em>Pak přišel zlom, který umlčel rozum.</em></p>
      <p>Dnes předávám to, co jsem se musela naučit sama: být víc v těle a méně v hlavě skrze dech, dotek, pohyb a vodu. Londýn, Indie, Filipíny, Bali a zase zpátky v Přerově.</p>
      <div><a class="link-arrow" href="moje-cesta.html">Celý příběh →</a></div>
    </div>
  </div>
</section>

{band('', 'plaz-skupina.jpg', 'Rozesmáté ženy po lekci jógy na pláži, s rukama nad hlavou', '<p class="band-quote">Jóga bez nálepek <span class="hand">a mantinelů.</span></p>', '', 'center 42%')}

<section class="section s-mint wv-up" id="spoluprace">
  <div class="wrap">
    <div class="section-head stack" style="margin-bottom:2.6rem;max-width:820px">
      <p class="eyebrow">Čtyři cesty k sobě</p>
      <h2>Jak můžeme <span class="hand">spolupracovat</span></h2>
    </div>
    <ul class="index" data-rv>{index_rows}</ul>
  </div>
</section>

{band('', 'freediving-kanon.jpg', 'Freediverka stoupá mezi skalními stěnami ke světlu', '<p class="band-quote">Nádech, který vydrží <span class="hand">déle, než si myslíš.</span></p>', '', 'center 40%')}

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

{seo.faq_html()}

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
        "Vyrostla jsem v Přerově. Vystudovala jsem ekonomku a nastoupila do korporátu. Ne proto, že bych věděla, co chci, ale proto, že jsem to vyjma tance nevěděla vůbec. Vdala jsem se a přestěhovala se do Londýna.",
        "Třetinu života jsem byla manželkou, dvě třetiny hodnou dcerou, která následovala představu rodičů o ideálním životě: dostudovat, najít kancelářskou práci, vdát se, pořídit byt, založit rodinu. Rozhodovala jsem se rozumem, i když mi intuice radila něco jiného. A rozum byl vždycky hlasitější."],
     ("pred-jogou.jpg", "Služebka v Rumunsku")),
    ("Londýn · Peru · Indie · 2016–2019", "Londýn, Peru, Indie", [
        "V Londýně začala moje transformace. Studovala jsem u učitele aštángy Scotta Johnsona a poprvé si začala klást otázky, kterým jsem se předtím vyhýbala: Kdo jsem? Co vlastně chci? Jaké je moje poslání?",
        "Pak přišly léčivé ceremonie v peruánské Amazonii. O rok později první cesta do Indie, do Maisúru, na intenzivní kurz u Saraswathi Jois, dcery zakladatele aštánga jógy. Jógu jsem zkoumala na sobě i skrze učení druhých. Dávat energii korporátu přestávalo dávat smysl."],
     ("indie-maisur.jpg", "Maisúr, Indie poprvé")),
    ("Přerov · 2019–2022", "Návrat domů", [
        "Po návratu domů jsem chtěla dávat zpátky komunitě. Otevřeli jsme kavárnu a pustila jsem se i do politiky. Organizovala jsem workshopy, sbírky a akce, dostala se do zastupitelstva a s kolegy jsme prosadili třeba vznik dostupného městského bydlení.",
        "Začala jsem učit v jógových studiích a budovat skupinky v okolních vesnicích. Poptávka po lekcích rostla, a tak jsem si u Kabira, studenta Oshovy tradice, udělala lektorský certifikát. V době covidu jsem z korporátu odešla. Jóga, kavárna i politika, všechno hezky jelo."],
     ("prerov-navrat.jpg", "Workshop v kavárně")),
    ("Zlom · 2023", "Když intuici nikdo neposlouchá", [
        "Pak přišel rozchod. Samovolný potrat. Fungovala jsem na autopilota, přes spoustu lekcí jógy a ostré lokty v politice. Intuice říkala: odpočiň si, něco změň. Neposlechla jsem ji. Místo toho jsem se vrhla do intenzivního masérského kurzu. A po něm přišlo vyhoření. Každý den jsem se probouzela s vyčerpáním, astmatem a alergiemi. Můj nervový systém se přetížil."], None),
    ("Filipíny · Bali · 2024", "Freediving jako učitel", [
        "Vyklidila jsem byt, prodala hromadu věcí, zahodila dýchátko a odstěhovala se na Filipíny. Půl roku jsem budovala jógovo-freedivingovou komunitu pod Blue Freedom, potkala světové špičky v oboru a hlavně se ponořila sama do sebe.",
        "Ten pocit, když padáte volným pádem hlouběji do hlubin a neexistuje nic než přítomný okamžik, se těžko popisuje. Freediving se pro mě stal učitelem a životním stylem. Dokončila jsem certifikát AIDA4 a asistentku instruktora, učila jógu a dech na místech jako Panglao, Siquijor nebo Amed na Bali."],
     ("filipiny-ponor.jpg", "Po ponoru, Filipíny")),
    ("Indie podruhé · 2025", "Jógová terapie", [
        "Než jsem se vrátila do Česka, strávila jsem půl roku v Indii, převážnou část studiem jógové terapie pod vedením Sonal Chaudhari. Její učitel Kobad Variava se pod přímým dohledem B.K.S. Iyengara stal seniorním učitelem. Tahle linie je pro mě inspirací v tom, jak k tělu přistupuji. Zároveň jsem učila v korporátu v Bombaji i v mezinárodní komunitě v Arambolu (Goa) či Dharamkotu (Himáčalpradéš)."],
     ("indie-setkani.jpg", "Setkání s dalajlámou")),
    ("Teď a tady", "Jóga bez nálepek", [
        "Po téměř dvou letech v Asii jsem si konečně odpověděla na otázky, kdo jsem a co chci. Dnes do jednoho přístupu propojuji jógu, pohyb, práci s dechem, vědomý dotek a poznatky z freedivingu.",
        "Od striktní aštángy jsem se přesunula k józe bez nálepek a mantinelů. Zajímá mě, jak pozici podle své fyziologie uděláš, ale taky jak se cítíš a jak dýcháš. Učím se žít v přítomném okamžiku, být vděčnější a obracet věci k dobru, i pro druhé. A tenhle posun neberu jako konečný.",
        "Pomáhám ženám i mužům být víc v těle a méně v hlavě a najít své autentické já."],
     ("ted-a-tady.jpg", "Teď a tady")),
]
tl = []
for place, h, paras, fig in journey:
    if place.startswith("Filipíny · Bali"):
        tl.append('</div></div></section>' + band('', 'zelva-ponor.jpg', 'Lenka se noří vedle mořské želvy nad písečným dnem', '<p class="band-quote">Tentokrát už intuici nešlo umlčet rozumem.</p>', '', 'center 58%') + '<section class="section"><div class="wrap"><div class="timeline">')
    ps = "".join(f"<p>{p}</p>" for p in paras)
    f = (f'<figure><img src="assets/img/{fig[0]}" alt="{fig[1]}" loading="lazy"><figcaption>{fig[1]}</figcaption></figure>' if fig else "")
    tl.append(f'<article class="tl-item{" has-fig" if fig else ""}" data-rv><div class="tl-place"><b>{len([x for x in tl if x.startswith("<article")]) + 1:02d}</b><span>{re.sub(r" · (\d{4})", r"<br>\1", place)}</span></div><div class="tl-text"><h2>{h}</h2>{ps}</div>{f}</article>')

kdo = [("kdo-01-kdo-jsem", "Kdo jsem?"), ("kdo-02-ucitelka", "učitelka"), ("kdo-03-joginka", "jogínka"), ("kdo-04-freediverka", "freediverka"),
       ("kdo-05-tanecnice", "tanečnice"), ("kdo-06-cestovatelka", "cestovatelka"), ("kdo-07-propojovatelka", "propojovatelka"), ("kdo-08-zena", "žena")]
KDO = "".join(f'<img src="assets/img/{f}.jpg" alt="Lenka Rekha — {t}" loading="lazy">' for f, t in kdo)
certs = [
    ("Aštánga jóga", "Scott Johnson", "Londýn 2017"),
    ("Yoga Chikitsa", "Manju Jois", "Londýn 2018"),
    ("Intenzivní kurz aštánga jógy", "Saraswathi Jois", "Indie 2019"),
    ("Lektorka jógy, multistyl (akreditace MŠMT)", "Kabir", "Olomouc 2020"),
    ("Dynamické meditace", "Kabir", "Olomouc 2021"),
    ("Sportovní masáž (akreditace MŠMT)", "Vzdělávací zařízení zdravotně-hygienických služeb Zlín", "Zlín 2023"),
    ("Freediving: asistentka instruktora (AIDA4)", "AIDA", "Filipíny 2024"),
    ("Jógová terapie", "Sonal Chaudhari, linie B.K.S. Iyengara", "Indie 2025"),
]
CERTS = "".join(f'<li><strong>{a}</strong><span>{b}</span><em>{c}</em></li>' for a, b, c in certs)
cats = [("Pohyb", ["zuzka", "marketa", "olga"]), ("Dech", ["arnaud"]), ("Dotek", ["sandra"]), ("Firmy", ["monika", "zivina"])]
REFS_ALL = ('<div class="ref-slider"><div class="ref-track" tabindex="0" aria-label="Reference, posouvej do strany">'
            + "".join(ref_cards(k).replace('<figcaption>', f'<figcaption><span class="ref-cat">{c}</span>') for c, k in cats)
            + '</div><div class="ref-nav"><button type="button" class="ref-prev" aria-label="Předchozí reference">←</button>'
            '<button type="button" class="ref-next" aria-label="Další reference">→</button></div></div>')
cesta = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Moje cesta</p>
    <div class="split rev" style="align-items:end">
    <div class="stack-lg">
    <h1>Kdo je Lenka Rekha?</h1>
    <p class="roles">učitelka · jogínka · freediverka · tanečnice · cestovatelka · propojovatelka</p>
    <p class="lead">Jsem lektorka jógy a jógové terapie s téměř desetiletou praxí a průvodkyně dechem, která kombinuje pránájámu s technikami z freedivingu.</p>
    <p class="lead">Pomáhám klientům individuálně vnímat vlastní tělo skrze dech, dotek, pohyb i všímavost. Pracuji i s komunitami v pravidelných kurzech online i offline a pořádám workshopy po celém Česku. Vedle vlastní lektorské praxe jsem také spoluzakladatelkou komunity Podnikavky Přerov. Celý život tančím a miluju být pod vodou.</p>
    <p class="lead">A taky jsem si prošla pěkně dlouhou oklikou, než jsem se dostala tam, kde jsem dnes.</p>
    </div>
    <div class="split-media" style="max-width:380px;justify-self:end"><img src="assets/img/lenka-portret.jpg" alt="Portrét Lenky Rekhy"></div>
    </div>
  </div>
</section>
<nav class="subnav wv-up" aria-label="Moje cesta: obsah stránky"><div class="wrap">{"".join(f'<a href="{h}">{t}</a>' for h, t in CESTA_SUB)}</div></nav>
<section class="section" id="pribeh">
  <div class="wrap">
    <div class="timeline">{''.join(tl)}</div>
    
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
<section class="section s-foam wv-up" id="komunita">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Komunita · Podnikavky Přerov</p><h2>Setkání podnikavých <span class="hand">žen</span></h2></div>
    <div class="stack" style="max-width:66ch">
      <p class="lead">Kromě vlastní praxe organizuji pravidelné neformální setkání pro ženy, které podnikají nebo o tom přemýšlí. 15. listopadu slavíme první narozeniny.</p>
      <div><a class="btn" href="podnikavky.html">Chci vědět víc</a></div>
    </div>
  </div>
</section>
{cta_band('', 'Podívej se, jak můžeme spolupracovat', 'Dech, pohyb, dotek, voda. Individuálně i ve skupině.', 'Napsat mi').replace('<a class="btn light" href="kontakt.html">Napsat mi</a>', '<div class="btn-row"><a class="btn light" href="./#spoluprace">Jak můžeme spolupracovat</a><a class="btn outline-light" href="kontakt.html">Napsat mi</a></div>')}
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
    lang = ""
    small = "".join(
        f'<figure><blockquote{""}>{REFS[k][2]}</blockquote><figcaption>{REFS[k][0]}, {REFS[k][1]}</figcaption></figure>'
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
    topic = {"dech": "Dech", "pohyb": "Pohyb", "dotek": "Dotek", "voda": "Voda"}.get(slug)
    if topic:
        body = body.replace('href="kontakt.html"', f'href="kontakt.html?tema={topic}"')
    page(f"{slug}.html", f"{name} — Lenka Rekha", lead[:155], body, slug)


# ---------- DECH ----------
pillar_page("dech", "Dech", 'Dech je první <span class="hand">pohyb.</span>',
    "Pránájáma, dechové techniky a workshop Flow State Reset. Kombinuji klasickou práci s dechem z jógy s technikami z freedivingu.",
    ("relaxace-podlozka.jpg", "Klient leží se zavřenýma očima na podložce, Lenka mu uvolňuje ramena", "center 40%"),
    [
        ("pranajama", "Lekce: Pránájáma a dechové techniky", "Klid, který si můžeš kdykoli přivolat",
         """<p><strong>Dechové techniky</strong> jsou praktické nástroje: jak prodloužit výdech, zklidnit nervový systém, soustředit se nebo prodloužit zádrž. Naučíš se je rychle a použiješ je hned, třeba před spaním, před důležitým jednáním nebo před ponorem. Propojuji je s poznatky z freedivingu.</p>
<p><strong>Pránájáma</strong> jde hlouběji. Je to jedna z cest jógy, komplexní praxe, která pracuje s dechem, energií a pozorností zároveň. Nejde jen o techniku, ale o to, jak dech mění tvůj vnitřní stav. Potřebuje pravidelnost a čas, a o to víc ti dá.</p>""",
         f"""<h3>Nejbližší pránájáma</h3><p>Neděle 29. 11. a 20. 12., 9:00–10:00, <a href="{maps('Studio Sangha, ' + SANGHA)}" target="_blank" rel="noopener">studio Sangha</a> (nám. T. G. Masaryka 14), 300 Kč.</p><p>Dechové techniky tě naučím i individuálně, osobně nebo online.</p>""" + ask("Přihlásit se"),
         ("lenka-tanec.jpg", "Lenka se zavřenýma očima a úsměvem v pohybu, soustředěná na dech")),
        ("workshopy", "Workshop: Flow State Reset", "Lehkost, radost a stav flow",
         """<p>Tříhodinový workshop. Praktický vhled do propojení pohybu a dechu jako nástrojů vědomé seberegulace. Bez výkonu a bez tlaku na dokonalost.</p>
<div class="blocks">
<div class="block"><span class="tag">Pohyb</span><h3>Pohyb a flow</h3><p>Jógovo-pohybová lekce plná organického pohybu inspirovaná elementem vody. Skrze spinální vlny, spirální linie, rotace, třesení a další postupně odkrýváme, kde v těle neseš chronické napětí, a právě tyhle pohybové vzorce cíleně uvolňujeme.</p></div>
<div class="block"><span class="tag">Dech</span><h3>Dech a nervový systém</h3><p>Začínáme výchozím bodem, například BOLT testem (Body Oxygen Level Test). Pak přichází zklidnění, prohloubení dechu a hlavně výdechu, který se přenese do zádrže. Vydržíš déle, než si myslíš. Workshop uzavírá integrace a mindfulness.</p></div>
</div>
<p>Odneseš si konkrétní nástroje pro vědomou práci s vlastním stavem, přenositelné do každodenního života.</p>""",
         f"""<h3>Nejbližší workshop</h3>
<ul class="offer"><li><span>So 21. 11. 2026 · 9:00–12:00 · <a href="{maps('Kineo, ' + KINEO)}" target="_blank" rel="noopener">studio Kineo, Anglická 17a, Mariánské Lázně</a></span><span class="price">900 Kč</span></li></ul>
<p>Chceš workshop pro svou skupinu, studio nebo firmu? Napiš mi.</p>""" + ask("Přihlásit se"),
         ("lenka-tanec-smich.jpg", "Lenka se smíchem tančí ve světlém sále")),
    ],
    ["arnaud"], "Chceš se nadechnout jinak?", "Napiš mi, co potřebuješ. Domluvíme pránájámu, workshop nebo individuální práci s dechem.")

# ---------- POHYB ----------
pillar_page("pohyb", "Pohyb", 'Pohyb bez <span class="hand">mantinelů.</span>',
    "Skupinové lekce hravá flow a integrovaná terapie, individuální lekce a lekce pro firmy.",
    ("pohyb-terasa.jpg", "Skupina cvičí jógu s rukama nad hlavou na terase s výhledem na moře", "center 45%"),
    [
        ("individualne", "Lekce: Individuální", "Péče ušitá na míru",
         """<p>Pro tebe, ne pro skupinu. Kombinuji jógu, dech, pohyb i masáž, přizpůsobené přesně tobě. Sleduji a zapisuji tvůj progres, zadávám domácí úkoly a jsem ti k dispozici i mezi lekcemi přes WhatsApp. Osobně i online.</p>
<ul class="offer">
<li><span>Nezávazná úvodní lekce. Poznáme se a zjistíme, co potřebuješ.</span><span class="price">zdarma</span></li>
<li><span>Balíček 5 lekcí</span><span class="price">5 000 Kč</span></li>
<li><span>Balíček 10 lekcí</span><span class="price">10 000 Kč</span></li>
</ul>""",
         f"""<h3>Domluv si úvodní lekci</h3><p>Napiš mi, co tě trápí nebo co hledáš. Domluvíme termín a místo.</p>{ask('Napsat mi')}<p style="font-size:.95rem">Nebo rovnou na <a href="{WA}">WhatsApp</a>.</p>""",
         ("lekce-popruh.jpg", "Lenka nastavuje klientovi jógový popruh přes ramena")),
        ("lekce", "Lekce: Skupinové", "Hravá flow a integrovaná terapie",
         """<h3>Integrovaná terapie</h3>
<p>Možná nepotřebuješ víc cvičit. Možná jen jinak. Detailní práce s tělem, přesné vedení a hlubší porozumění pohybu, inspirované linií B.K.S. Iyengara. Vhodná pro všechny, i pro ty, kdo mají za sebou zranění nebo je bolí záda.</p>
<h3>Hravá flow</h3>
<p>Rozproudi energii a pohybuj se s radostí. Dynamické sekvence, síla a kreativita. Někdy jemnější, jindy silovější, vždy bez tlaku a vždy trochu jiná. Vhodná pro mírně pokročilé a pokročilé.</p>
<p>Lekce probíhají v Přerově, Olomouci, Lipníku nad Bečvou a Hradčanech. Cena 200–300 Kč za lekci.</p>""",
         """<h3>Přijď na lekci</h3><p>Všechny časy najdeš v rozvrhu. Místo si rezervuj přes WhatsApp.</p>""" + ask("Rozvrh lekcí", "rozvrh.html"),
         ("lekce-studio.jpg", "Lenka upravuje pozici trojúhelníku skupině ve světlém studiu")),
        ("firmy", "Lekce: Pro firmy", "Jóga a dech přímo u vás",
         """<p>Pravidelné lekce jógové terapie pro týmy v Přerově a Olomouci. Ulevují zádům a hlavě, zlepšují posturu při dlouhém sezení a posilují odolnost vůči stresu. Začínáme nezávaznou úvodní lekcí.</p>""",
         """<h3>Pro firmy</h3><p>Balíčky, ceny a reference firem najdeš na samostatné stránce.</p>""" + ask("Nabídka pro firmy", "firmy.html"),
         None),
    ],
    ["zuzka", "olga", "marketa"], "Nevíš, která lekce je pro tebe?", "Napiš mi pár vět o tom, co tě trápí nebo co hledáš. Společně najdeme cestu.")

# ---------- DOTEK ----------
pillar_page("dotek", "Dotek", 'Dotek, který tělu vrátí <span class="hand">rovnováhu.</span>',
    "Intuitivní masáž: sportovní masáž, aromaterapie, dech a prvky thajské masáže v jednom. Zaměřuji se hlavně na záda, šíji, hlavu, hrudník a nohy.",
    ("dotek-ruce.jpg", "Ruce Lenky Rekhy na zádech klientky při intuitivní masáži", "center 40%"),
    [
        ("intuitivni-masaz", "Intuitivní masáž", "Vědomý dotek",
         """<p>Moje intuitivní masáž kombinuje <strong>sportovní masáž, aromaterapii, práci s dechem a prvky thajské masáže</strong>. Není to jen mechanická technika. Je to vědomý dotek, který uvolní napětí, zklidní nervový systém a znovu tě propojí s vlastním tělem a dechem.</p>
<p>Každé setkání přizpůsobuji tomu, co tělo právě potřebuje. Někdy hlubší práce se svaly, jindy jemnější přístup k celkovému uvolnění. Začínáme krátkou konzultací, pak masíruji.</p>
<p>Jsem lektorka jógy a dlouhodobě pracuji s dechem a vědomým pohybem. Jako tanečnice i freediverka se učím vnímat tělo, rytmus a dech v hlubší rovině. Dotek je přirozeným rozšířením téhle práce.</p>
<p>Brzy v nabídce i thajská masáž na futonu.</p>""",
         """<h3>Pro koho</h3><p>Pro každého, kdo cítí napětí v těle, potřebuje si odpočinout nebo chce svému tělu dopřát vědomou péči.</p><p><strong>Kde:</strong> <a href="https://www.google.com/maps/search/?api=1&query=Wilsonova%2C+Přerov" target="_blank" rel="noopener">Přerov, Wilsonova ulice</a></p>""" + ask("Rezervovat masáž"),
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
    ("freediving-kanon.jpg", "Freediverka klesá mezi skalními stěnami do modré hloubky", "center 42%"),
    [
        ("vnitrni-ponor", "Kurz: Vnitřní ponor", "Příprava na freediving",
         """<p><strong>Tohle není klasický jógový kurz. Není to ani kurz potápění.</strong> Je to deset týdnů, ve kterých zjistíš, co všechno dokáže tvůj dech a tvoje tělo, když jim dáš prostor.</p>
<p>Kurz propojuje metodiku AIDA s jógou, dechem a všímavostí. Nejde o čas ani hloubku. Jde o zkušenost, klid a schopnost zůstat v těle i tam, kde by tělo chtělo panikařit.</p>
<ul>
<li>10 lekcí ve studiu a 1 lekce ve vodě: jáma v Aquapalace Čestlice nebo Deep Spot (podle domluvy), vždy s certifikovaným instruktorem freedivingu.</li>
<li>Skupina 8–10 lidí, uzavřená podpora na WhatsAppu, týdenní domácí úkoly.</li>
<li>Pro dospělé 25+, kteří rádi zkoušejí nové věci.</li>
</ul>
<ul class="offer">
<li><span>Kurz (10 lekcí ve studiu)</span><span class="price">3 000 Kč</span></li>
<li><span>Lekce v jámě (Čestlice / Deep Spot) s certifikovaným instruktorem</span><span class="price">podle domluvy</span></li>
</ul>""",
         """<h3>Další běh začíná v lednu 2027</h3><p>Místa ve skupině jsou omezená. Napiš mi a pošlu ti termíny jako první.</p>""" + ask("Mám zájem o kurz"),
         ("meditace-bazen.jpg", "Lenka sedí se zavřenýma očima v meditaci na okraji bazénu, odráží se ve vodě")),
        ("retreat", "Retreat: V rytmu oceánu", "Amed, Bali, duben 2027",
         """<p>Tohle je víc než jógový retreat na Bali. Tohle je spojení s vodou a se sebou samým skrze opravdové uvolnění a bytí v přítomném okamžiku. Pod vodou to ani jinak nejde.</p>
<p>Provedu tě místem, které považuju za svůj druhý domov. Amed je vesnice, kde je stále málo turistů, ceny nejsou přemrštěné a nikdo si na nic nehraje. Majestátný Agung jde vidět z ulice, ze břehu i z vody. Magické místo.</p>
<p><strong>Další retreat proběhne v dubnu 2027.</strong> Přesné datum, program, ubytování i ceny brzy doplním.</p>""",
         """<h3>Duben 2027 · Amed, Bali</h3><p>Chceš o retreatu vědět jako první? Napiš mi a pošlu ti podrobnosti, jakmile budou.</p>""" + ask("Mám zájem o retreat") + """
<!-- Po aktualizaci stránky retreatu sem vrátit odkaz: https://lenkajungling.github.io/v-rytmu-oceanu/ -->""",
         ("amed-bali.jpg", "Pobřeží Amedu na Bali se sopkou Agung při západu slunce")),
        ("freediving", "Kurz: Freediving", "Od léta 2027",
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
{band('', 'lekce-korekce.jpg', 'Lenka koriguje pozici klientky na lekci', firmy_inner, 'band-page band-top', 'center 8%')}
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
{refs_section(["zivina", "monika"], "Co říkají firmy")}
{cta_band('', 'Chcete to vyzkoušet?', 'Začněte nezávaznou úvodní lekcí.', 'Napsat mi')}
"""
page("firmy.html", "Pro firmy — Lenka Rekha", "Jógová terapie a dech pro firmy v Přerově a Olomouci. Nezávazná úvodní lekce.", firmy, "firmy")

# ======================= ROZVRH =======================
rows = [
    ("prerov", "Pondělí", "15:00–16:00", "Integrovaná terapie", "soukromá skupinka", "Přerov", "", ""),
    ("lipnik", "Pondělí", "17:00–18:00", "Hravá flow", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("lipnik", "Pondělí", "18:15–19:15", "Integrovaná terapie", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("olomouc", "Úterý", "17:45–18:45", "Vnitřní ponor", "kurz, volné místo", "Olomouc", "Centrum Dákiní", "300 Kč"),
    ("prerov", "Středa", "16:45–18:00", "Integrovaná terapie", "kurz, volné místo", "Přerov", "Jóga a Pilates", "300 Kč"),
    ("prerov", "Středa", "18:15–19:30", "Hravá flow", "kurz, volné místo", "Přerov", "Jóga a Pilates", "300 Kč"),
    ("lipnik", "Čtvrtek", "15:00–16:00", "Integrovaná terapie", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("lipnik", "Čtvrtek", "16:15–17:15", "Hravá flow", "", "Lipník nad Bečvou", "Frida cafe", "250 Kč"),
    ("hradcany", "Čtvrtek", "18:00–19:00", "Jóga", "", "Hradčany", "Sál OÚ", "200 Kč"),
    ("prerov", "Neděle", "9:00–10:00", "Pránájáma", "1× měsíčně: 29. 11. a 20. 12.", "Přerov", "Studio Sangha", "300 Kč"),
]
ADDR = {pl: a for _, pl, a in PLACES}


def place_cell(city, pl):
    if not pl:
        return city
    q = ADDR.get(pl, f"{pl}, {city}")
    return f'{city}<small><a class="map-link" href="{maps(q)}" target="_blank" rel="noopener">{pl}</a></small>'


trs = "".join(
    f'<tr data-city="{c}"><td class="day">{d}</td><td>{t}</td><td>{l}{f"<small>{n}</small>" if n else ""}</td><td>{place_cell(city, pl)}</td><td>{p}</td></tr>'
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
      <p>Setkání Podnikavek pořádám společně se <strong>Zuzanou Balcárkovou</strong>. V říjnu 2025 jsme si sedly na kafe a shodly se, že nechceme jen tlachat nad kafíčkem, ale také se posouvat v našem podnikání. Nechceme jezdit za službami dál, když je v Přerově a okolí určitě spousta podnikavých žen, jen o nich ještě nevíme. A tak vznikl nápad na pravidelná setkávání Podnikavek.</p>
      <p>Za ten rok jsme se vzdělaly v AI, finanční gramotnosti nebo brandingu. Naučily jsme se dobře si stanovit cíle, opečovat nervovou soustavu, spojit se do projektů či navázat přátelství.</p>
      <p><strong>A v roce 2027 budeme pokračovat dál, v novém formátu!</strong> Více informací brzy.</p>
      <div class="page-photo"><img src="assets/img/podnikavky-inhub.jpg" alt="Lenka s kolegyní mluví ke ženám na setkání Podnikavek v IN-HUB Přerov" style="aspect-ratio:4/5;max-width:420px;object-position:center 30%"></div>
    </div>
    <aside class="aside-card" style="background:var(--sun-tint);color:var(--ink)" id="akce">
      <h3 style="color:var(--sun-dark)">Nejbližší setkání</h3>
      <ul class="offer"><li><span><strong>15. 11. 2026</strong> · první narozeniny Podnikavek 🎉</span></li></ul>
      <p>Čas a místo ti pošlu po <a class="pod-link" href="#prihlaska">přihlášení</a>.</p>
    </aside>
  </div>
</section>
<section class="section" style="background:var(--sun-tint)" id="vize">
  <div class="wrap">
    <p class="eyebrow" style="color:var(--sun);margin-bottom:1.6rem">Naše vize</p>
    <figure class="big-quote pod-vize"><blockquote>Komunita žen, které podnikají s lehkostí, odvahou a naplněním, aniž by ztrácely stabilitu ve svých vztazích a ve svém vnitřním světě. Ženy, které jsou spokojené nejen v tom, co tvoří, ale i v tom, jak žijí.</blockquote></figure>
  </div>
</section>
<section class="section" id="reference">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow" style="color:var(--sun)">Co o nás řekly</p><h2>Zkušenosti <span class="hand" style="color:var(--sun)">Podnikavek</span></h2></div>
    <div class="pod-refs">
      <figure class="ref-card"><blockquote>Na setkání je skvělá energie. Seznámíš se s dalšími úžasnými ženami, které ti dají nestranný náhled. Pohled zvenčí, který by tebe třeba nenapadl. Zažiješ přednášku na zajímavé téma, inspiruje tě to k dalším krokům, můžeš si odnést různá uvědomění a aha momenty. Získáš kontakty na ženy, se kterými se můžeš propojit i soukromě, vzájemně se obohatit a navázat spolupráce.</blockquote><figcaption><strong>Účastnice</strong>Podnikavky Přerov</figcaption></figure>
      <figure class="ref-card"><blockquote>Sem může přijít kdokoliv a může se cítit naprosto uvolněně a přijatě. Může prezentovat svoje podnikání, ale i sny a touhy, a nechat se inspirovat ostatními. Stojí za to si to zkusit a poznat nové ženy.</blockquote><figcaption><strong>Účastnice</strong>Podnikavky Přerov</figcaption></figure>
      <figure class="ref-card"><blockquote>Inspirativní prostředí žen, které podnikají v zajímavých oblastech. Hledají, jak se zlepšit, jak se ukotvit. Nebo taky dobré pro nakopnutí k akci nebo uspořádání svých myšlenek, jak začít nebo kam dál…</blockquote><figcaption><strong>Účastnice</strong>Podnikavky Přerov</figcaption></figure>
    </div>
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
        <p class="form-note">Údaje použiju jen k organizaci setkání. Víc v <a href="gdpr.html">zásadách ochrany osobních údajů</a>.</p>
        <div class="btn-row"><button class="btn sun" type="submit">Přihlásit se</button></div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""
page("podnikavky.html", "Podnikavky Přerov — setkání podnikavých žen",
     "Podnikavky Přerov: pravidelná setkání podnikavých žen, která pořádají Lenka Rekha a Zuzana Balcárková. Přednášky, inspirace a propojení. Přerov a okolí.", podnikavky, "moje-cesta")

# ======================= KONTAKT =======================
places = "".join(f'<a class="place" href="{maps(a)}" target="_blank" rel="noopener"><strong>{c}</strong><span>{p}<br>{a}</span></a>'.replace('<a class="place"', '<a class="place" style="text-decoration:none"') for c, p, a in PLACES)
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
        <li><span class="k">Google</span><a href="{GMAPS}" target="_blank" rel="noopener">Profil a recenze</a></li>
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
    <p class="lead">Platné od 1. prosince 2026.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="prose">
      <h2>Kdo zpracovává vaše údaje</h2>
      <p>Správcem osobních údajů je Lenka Jüngling, IČO {ICO}, se sídlem Budovatelů 7, 750 02 Přerov, podnikající pod značkou Lenka Rekha. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>, {PHONE}.</p>
      <h2>Jaké údaje zpracovávám</h2>
      <p>Prostřednictvím formulářů, e-mailu nebo WhatsAppu zpracovávám jen to, co mi sami sdělíte:</p>
      <ul><li>jméno</li><li>e-mail nebo telefon</li><li>téma, o které máte zájem, a obsah zprávy</li><li>u přihlášky na Podnikavky také informace o vašem podnikání a očekáváních</li><li>informace o zdravotním stavu, pokud mi je sami sdělíte kvůli bezpečnému vedení lekce, masáže nebo kurzu</li></ul>
      <h2>K čemu a na jakém základě</h2>
      <ul><li><strong>Odpověď na dotaz, domluva a poskytnutí služby</strong> (lekce, masáž, kurz, workshop, retreat): plnění smlouvy a jednání o ní, čl. 6 odst. 1 písm. b) GDPR.</li><li><strong>Vedení účetnictví a daňové evidence</strong>: plnění právní povinnosti, čl. 6 odst. 1 písm. c) GDPR.</li><li><strong>Informace o zdravotním stavu</strong>: zpracovávám jen s vaším výslovným souhlasem, čl. 9 odst. 2 písm. a) GDPR, a pouze proto, abych lekci nebo masáž přizpůsobila vašim možnostem.</li></ul>
      <h2>Jak dlouho údaje uchovávám</h2>
      <p>Po dobu nezbytnou k vyřízení vaší zprávy nebo k poskytnutí služby, nejdéle 2 roky od posledního kontaktu. Doklady o platbách uchovávám po dobu, kterou stanoví účetní a daňové předpisy.</p>
      <h2>Komu údaje předávám</h2>
      <p>Vaše údaje neprodávám, nepronajímám ani nepředávám třetím stranám za účelem marketingu. Technicky je zpracovávají tito zpracovatelé:</p>
      <ul><li>Formspree (formspree.io, USA): doručení zpráv z formulářů do mého e-mailu. Předání do USA probíhá na základě standardních smluvních doložek EU.</li><li>Google (Gmail): e-mailová schránka, ve které zprávy přijímám.</li><li>GitHub Pages (GitHub, USA): hosting webu.</li></ul>
      <h2>Měření návštěvnosti</h2>
      <p>Pro základní přehled o návštěvnosti používám službu GoatCounter. Nepoužívá cookies, neukládá IP adresy a nesleduje vás napříč weby. Vidím jen souhrnná čísla, například kolik lidí přišlo na kterou stránku a odkud.</p>
      <h2>Vaše práva</h2>
      <ul><li>požádat o přístup ke svým osobním údajům</li><li>požádat o jejich opravu, výmaz nebo omezení zpracování</li><li>vznést námitku proti zpracování</li><li>kdykoli odvolat souhlas, stačí napsat e-mail</li><li>podat stížnost u Úřadu pro ochranu osobních údajů (uoou.gov.cz)</li></ul>
      <p>Pro uplatnění práv mi napište na <a href="mailto:{EMAIL}">{EMAIL}</a>. Odpovím do 30 dnů.</p>
      <h2>Cookies</h2>
      <p>Tento web nepoužívá žádné cookies. Písma jsou uložená přímo na tomto webu, nenačítají se od třetích stran.</p>
    </div>
  </div>
</section>
"""
page("gdpr.html", "Ochrana osobních údajů — Lenka Rekha", "Zásady ochrany osobních údajů webu lenkarekha.com.", gdpr)

# ======================= OBCHODNÍ PODMÍNKY =======================
vop = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="crumbs"><a href="./">Domů</a> / Obchodní podmínky</p>
    <h1>Obchodní podmínky</h1>
    <p class="lead">Přihlašování, platby a storno. Platné od 1. prosince 2026.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="prose">
      <h2>Kdo služby poskytuje</h2>
      <p>Lenka Jüngling, IČO {ICO}, se sídlem Budovatelů 7, 750 02 Přerov, podnikatelka zapsaná v živnostenském rejstříku, podnikající pod značkou Lenka Rekha. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>, {PHONE}.</p>
      <h2>Jak se přihlásit</h2>
      <p>Na lekci, masáž, kurz nebo workshop se přihlásíš zprávou přes formulář, e-mail nebo WhatsApp. Přihláška je závazná ve chvíli, kdy ti termín potvrdím, a u akcí placených předem po přijetí platby. Na pravidelné skupinové lekce se přihlásíš stejně, místo ti potvrdím podle kapacity sálu.</p>
      <h2>Ceny a platba</h2>
      <ul><li><strong>Všechny platby probíhají převodem na účet</strong>, platební údaje ti pošlu s potvrzením přihlášky.</li><li><strong>Kurzy, workshopy a balíčky lekcí:</strong> platba předem.</li><li><strong>Retreat:</strong> záloha a doplatek podle podmínek, které dostaneš s přihláškou.</li></ul>
      <p>Aktuální ceny najdeš u jednotlivých služeb a v rozvrhu. Nejsem plátkyně DPH.</p>
      <h2>Zrušení a storno</h2>
      <ul>
        <li><strong>Individuální lekce a masáž:</strong> termín můžeš zdarma zrušit nebo přesunout nejpozději 24 hodin předem. Při pozdějším zrušení nebo nepříchodu účtuji plnou cenu.</li>
        <li><strong>Workshop:</strong> při zrušení nejpozději 7 dní předem vracím celou částku. Později částku nevracím, ale můžeš za sebe poslat náhradníka.</li>
        <li><strong>Kurz (např. Vnitřní ponor):</strong> při zrušení nejpozději 14 dní před začátkem vracím celou částku. Později a po zahájení kurzu částku nevracím. Za sebe můžeš poslat náhradníka. Vynechanou lekci lze po domluvě nahradit v jiném termínu, pokud to kapacita dovolí.</li>
        <li><strong>Balíček individuálních lekcí:</strong> platí 6 měsíců od zakoupení, nevyčerpané lekce se nevracejí.</li>
        <li><strong>Retreat:</strong> řídí se zvláštními storno podmínkami, které dostaneš s přihláškou.</li>
      </ul>
      <p>Pokud akci zruším já (nemoc, nízký počet přihlášených, vyšší moc), nabídnu ti náhradní termín, nebo vrátím celou zaplacenou částku.</p>
      <h2>Odstoupení od smlouvy</h2>
      <p>Pokud smlouvu uzavíráš na dálku (e-mailem, přes formulář nebo WhatsApp), nemáš podle § 1837 písm. j) občanského zákoníku právo odstoupit od smlouvy do 14 dnů. Jde totiž o služby související s využitím volného času, které se poskytují v určeném termínu. Zrušení se proto řídí storno podmínkami výše.</p>
      <h2>Zdraví a bezpečnost</h2>
      <p>Lekce, masáže i kurzy nenahrazují lékařskou péči. Před první lekcí nebo masáží mi prosím řekni o svých zdravotních omezeních, těhotenství, úrazech nebo operacích, abych mohla praxi přizpůsobit. Cvičíš v rámci svých možností a na vlastní odpovědnost. V případě pochybností se nejdřív poraď s lékařem.</p>
      <p>Lekce ve vodě v rámci kurzu Vnitřní ponor vede certifikovaný instruktor freedivingu a platí pro ni jeho bezpečnostní pravidla.</p>
      <h2>Reklamace a spory</h2>
      <p>Pokud nebudeš se službou spokojená nebo spokojený, napiš mi prosím na <a href="mailto:{EMAIL}">{EMAIL}</a>. Reklamaci vyřídím bez zbytečného odkladu, nejpozději do 30 dnů. Pokud se nedohodneme, můžeš se obrátit na Českou obchodní inspekci (<a href="https://adr.coi.cz" target="_blank" rel="noopener">adr.coi.cz</a>), která řeší mimosoudní spory se spotřebiteli.</p>
      <h2>Fotografie z lekcí</h2>
      <p>Na lekcích a akcích občas fotím. Fotky, na kterých jsi poznat, zveřejním jen s tvým souhlasem.</p>
    </div>
  </div>
</section>
"""
page("obchodni-podminky.html", "Obchodní podmínky — Lenka Rekha", "Přihlašování, platby a storno podmínky lekcí, masáží, kurzů a workshopů Lenky Rekhy.", vop)

# ======================= 404 =======================
nf = f"""
<section class="page-hero wv-down">
  <div class="wrap">
    <p class="eyebrow">Chyba 404</p>
    <h1>Tady je jen <span class="hand">hluboká voda.</span></h1>
    <p class="lead">Stránka, kterou hledáš, neexistuje nebo se přestěhovala. Nadechni se a zkus to odjinud.</p>
    <div class="btn-row" style="margin-top:1.5rem"><a class="btn" href="./">Na úvodní stránku</a><a class="btn ghost" href="rozvrh.html">Rozvrh lekcí</a><a class="btn ghost" href="kontakt.html">Kontakt</a></div>
  </div>
</section>
"""
page("404.html", "Stránka nenalezena — Lenka Rekha", "Stránka neexistuje.", nf)
_nf = (ROOT / "404.html").read_text(encoding="utf-8")
_nf = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|data:)', r'\1="/', _nf)
_nf = _nf.replace('href="/./"', 'href="/"').replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"')
(ROOT / "404.html").write_text(_nf, encoding="utf-8")

(ROOT / "sitemap.xml").write_text(seo.sitemap([p for p in BUILT if p not in ("gdpr.html", "obchodni-podminky.html", "404.html")]), encoding="utf-8")
(ROOT / "robots.txt").write_text(seo.ROBOTS, encoding="utf-8")
print("hotovo")
