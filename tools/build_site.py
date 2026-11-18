#!/usr/bin/env python3
"""Erzeugt alle HTML-Seiten von metallschilder24.com aus einer gemeinsamen Vorlage.

Aufruf (im Repository-Hauptordner):  python3 tools/build_site.py
Kopf, Navigation und Fußbereich werden hier zentral gepflegt; die Seiteninhalte
stehen in den PAGES weiter unten bzw. für die Startseite in tools/home_main.html.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://metallschilder24.com/"
WP = SITE + "wp-content/uploads/"
PHONE = "0155 63336455"
PHONE_LINK = "tel:+4915563336455"
MAIL = "info@metallschilder24.com"
OG_IMAGE = WP + "2026/11/metallschilder24-produktbeispiele.png"

NAV = [
    ("typenschilder.html", "Typenschilder", {"typenschilder.html", "typenschilder-bedruckt.html", "typenschilder-graviert.html"}),
    ("firmenschilder.html", "Firmenschilder", {"firmenschilder.html"}),
    ("hinweisschilder.html", "Hinweisschilder", {"hinweisschilder.html"}),
    ("befestigungen.html", "Befestigungen", {"befestigungen.html"}),
    ("ueber-uns.html", "Über uns", {"ueber-uns.html", "kundenmeinungen.html"}),
    ("kontakt.html", "Kontakt", {"kontakt.html"}),
]

ORG = {
    "@type": "LocalBusiness",
    "@id": SITE + "#org",
    "name": "GSD Metall-Schilder Drucksysteme",
    "alternateName": "GSD Metallschilder",
    "url": SITE,
    "logo": WP + "2015/01/cropped-FB_Kopf_gif-270x270.gif",
    "image": OG_IMAGE,
    "email": MAIL,
    "telephone": "+49 155 63336455",
    "founder": {"@type": "Person", "name": "Günter Schneider"},
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Bergstraße 12",
        "postalCode": "89312",
        "addressLocality": "Günzburg",
        "addressCountry": "DE",
    },
    "areaServed": ["DE", "AT", "CH"],
    "sameAs": ["https://www.xing.com/companies/gsd-metallschilderdrucksysteme"],
}

ICON = {
    "mail": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "phone": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "pin": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "clock": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}


# --------------------------------------------------------------------------- Bausteine

def header(current):
    items = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if current in group else ""}>{label}</a></li>'
        for href, label, group in NAV
    )
    return f"""<a class="skip" href="#inhalt">Zum Inhalt springen</a>

<div class="topbar">
  <div class="wrap">
    <span class="hint">Metallschilder für Unternehmen · Lieferung nach Deutschland, Österreich &amp; Schweiz</span>
    <span class="contacts">
      <a href="{PHONE_LINK}">{PHONE}</a>
      <a href="mailto:{MAIL}">{MAIL}</a>
    </span>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="GSD Metallschilder – Startseite">
      <strong>GSD Metallschilder</strong>
      <span>Spezialist für Metallschilder</span>
    </a>
    <nav class="main" id="hauptmenue" aria-label="Hauptmenü">
      <ul>
{items}
      </ul>
    </nav>
    <div class="header-cta">
      <a class="btn btn-navy" href="kontakt.html#anfrage">Angebot anfragen</a>
      <button class="menu-btn" type="button" aria-controls="hauptmenue" aria-expanded="false">
        <span class="sr-only">Menü öffnen</span>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>
"""


FOOTER = f"""<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>GSD Metallschilder</h4>
        <p>GSD Metall-Schilder Drucksysteme<br>Inh. Günter Schneider<br>Bergstraße 12 · 89312 Günzburg</p>
        <p><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{PHONE_LINK}">{PHONE}</a></p>
      </div>
      <div>
        <h4>Produkte</h4>
        <ul>
          <li><a href="typenschilder.html">Typenschilder</a></li>
          <li><a href="typenschilder-bedruckt.html">Typenschilder bedruckt</a></li>
          <li><a href="typenschilder-graviert.html">Typenschilder graviert</a></li>
          <li><a href="firmenschilder.html">Firmenschilder</a></li>
          <li><a href="hinweisschilder.html">Hinweisschilder</a></li>
          <li><a href="weitere-schilder.html">Alle Metallschilder</a></li>
        </ul>
      </div>
      <div>
        <h4>Befestigungen</h4>
        <ul>
          <li><a href="befestigungen.html#annieten">Annieten</a></li>
          <li><a href="befestigungen.html#anschrauben">Anschrauben</a></li>
          <li><a href="befestigungen.html#selbstklebend">Selbstklebend</a></li>
          <li><a href="befestigungen.html#befestigungssatz">Befestigungssatz</a></li>
        </ul>
      </div>
      <div>
        <h4>Unternehmen</h4>
        <ul>
          <li><a href="ueber-uns.html">Über uns</a></li>
          <li><a href="kundenmeinungen.html">Kundenmeinungen</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
          <li><a href="https://www.xing.com/companies/gsd-metallschilderdrucksysteme" rel="noopener" target="_blank">XING</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>© <span id="year">2026</span> GSD Metallschilder – Spezialist für Metallschilder</span>
      <span><a href="impressum.html">Impressum</a> · <a href="impressum.html#datenschutz">Datenschutz</a> · <a href="sitemap.html">Sitemap</a></span>
    </div>
  </div>
</footer>

<div class="mobile-cta">
  <a class="btn btn-call" href="{PHONE_LINK}">Anrufen</a>
  <a class="btn btn-accent" href="kontakt.html#anfrage">Angebot anfragen</a>
</div>
"""


def page_hero(crumbs, eyebrow, title, lead="", actions=True, art=None):
    trail = [("index.html", "Startseite")] + crumbs
    lis = []
    for i, (href, label) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
        else:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
    q = f"?art={art}" if art else ""
    act = f"""
      <div class="actions">
        <a class="btn btn-accent" href="kontakt.html{q}#anfrage">Angebot anfragen <span aria-hidden="true">→</span></a>
        <a class="btn btn-ghost" href="{PHONE_LINK}">{PHONE}</a>
      </div>""" if actions else ""
    lead_html = f'\n    <p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-hero" aria-labelledby="seitentitel">
  <div class="wrap">
    <nav class="crumbs" aria-label="Brotkrümelnavigation"><ol>{''.join(lis)}</ol></nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1 id="seitentitel">{title}</h1>{lead_html}{act}
  </div>
</section>"""


def cta(title="Ihr Schild beginnt mit einer Anfrage.",
        text="Beschreiben Sie Einsatzzweck, Stückzahl und Maße – Material und Ausführung klären wir gemeinsam.",
        art=None):
    q = f"?art={art}" if art else ""
    return f"""<section class="cta-section" aria-label="Angebot anfragen">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="actions">
        <a class="btn btn-accent" href="kontakt.html{q}#anfrage">Angebot anfragen <span aria-hidden="true">→</span></a>
        <a class="btn btn-ghost" href="mailto:{MAIL}">E-Mail schreiben</a>
      </div>
    </div>
  </div>
</section>"""


def gallery(items):
    figs = "\n".join(
        f'    <figure><a href="{full}" target="_blank" rel="noopener"><img src="{thumb or full}" alt="{alt}" loading="lazy" width="400" height="300"></a><figcaption>{cap}</figcaption></figure>'
        for full, thumb, alt, cap in items
    )
    return f'<div class="gallery">\n{figs}\n  </div>'


def subnav(current):
    tabs = [
        ("typenschilder.html", "Übersicht"),
        ("typenschilder-bedruckt.html", "Bedruckt"),
        ("typenschilder-graviert.html", "Graviert"),
    ]
    lis = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{l}</a></li>' for h, l in tabs
    )
    return f'<nav class="subnav" aria-label="Typenschilder"><div class="wrap"><ul>{lis}</ul></div></nav>'


def quote_form(heading="Angebot anfragen", full=False):
    extra = ""
    if full:
        extra = """
      <div class="grid2">
        <div class="field">
          <label for="f-bef">Befestigung</label>
          <select id="f-bef" name="befestigung">
            <option>Noch offen – bitte beraten</option>
            <option>Annieten</option>
            <option>Anschrauben</option>
            <option>Selbstklebend</option>
            <option>Mit Befestigungssatz</option>
          </select>
        </div>
        <div class="field">
          <label for="f-land">Lieferland</label>
          <select id="f-land" name="lieferland">
            <option>Deutschland</option>
            <option>Österreich</option>
            <option>Schweiz</option>
          </select>
        </div>
      </div>"""
    return f"""<form class="quote" id="quote-form" novalidate>
      <h3 id="anfrage">{heading}</h3>
      <p class="sub">Ihre Angaben werden in eine E-Mail an uns übernommen. Fotos, Zeichnungen oder Vorlagen können Sie dort direkt anhängen.</p>
      <div class="grid2">
        <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-firma">Firma <span class="opt">(optional)</span></label><input id="f-firma" name="firma" autocomplete="organization"></div>
      </div>
      <div class="grid2">
        <div class="field"><label for="f-mail">E-Mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-tel">Telefon <span class="opt">(optional)</span></label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
      </div>
      <div class="grid2">
        <div class="field">
          <label for="f-art">Schildart</label>
          <select id="f-art" name="schildart">
            <option>Typenschild</option>
            <option>Graviertes Schild</option>
            <option>Firmenschild</option>
            <option>Hinweisschild</option>
            <option>Sonstiges / noch offen</option>
          </select>
        </div>
        <div class="field">
          <label for="f-mat">Material</label>
          <select id="f-mat" name="material">
            <option>Noch offen – bitte beraten</option>
            <option>Aluminium</option>
            <option>Edelstahl</option>
            <option>Messing</option>
          </select>
        </div>
      </div>{extra}
      <div class="grid2">
        <div class="field"><label for="f-menge">Stückzahl</label><input id="f-menge" name="stueckzahl" inputmode="numeric" placeholder="z. B. 50"></div>
        <div class="field"><label for="f-mass">Maße (mm)</label><input id="f-mass" name="masse" placeholder="z. B. 80 × 40"></div>
      </div>
      <div class="field"><label for="f-text">Einsatzzweck, Beschriftung, Wunschtermin</label><textarea id="f-text" name="nachricht" required placeholder="Beschreiben Sie kurz Ihr Vorhaben …"></textarea></div>
      <label class="consent"><input type="checkbox" id="f-ok" required> <span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung meiner Anfrage verwendet werden (siehe <a href="impressum.html#datenschutz">Datenschutz</a>).</span></label>
      <button class="btn btn-accent" type="submit">Anfrage per E-Mail senden <span aria-hidden="true">→</span></button>
      <p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
    </form>"""


def render(filename, title, description, body, crumbs=None, extra_ld=None, robots="index, follow, max-image-preview:large"):
    url = SITE if filename == "index.html" else SITE + filename
    graph = [ORG, {"@type": "WebSite", "@id": SITE + "#website", "url": SITE,
                   "name": "GSD Metallschilder", "inLanguage": "de-DE", "publisher": {"@id": SITE + "#org"}}]
    if crumbs:
        trail = [("index.html", "Startseite")] + crumbs
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": label,
                 "item": SITE if href == "index.html" else SITE + href}
                for i, (href, label) in enumerate(trail)
            ],
        })
    if extra_ld:
        graph.extend(extra_ld)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#232050">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="GSD Metallschilder">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMAGE}">
<link rel="icon" href="{WP}2015/01/cropped-FB_Kopf_gif-32x32.gif" sizes="32x32">
<link rel="apple-touch-icon" href="{WP}2015/01/cropped-FB_Kopf_gif-180x180.gif">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(filename)}
<main id="inhalt">
{body}
</main>

{FOOTER}
<script src="assets/main.js" defer></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename


# --------------------------------------------------------------------------- Seiten

def faq_ld(pairs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


HOME_FAQ = [
    ("Wie lange dauert die Lieferung?", "Die übliche Lieferzeit beträgt 10–14 Tage. Den konkreten Termin stimmen wir für Ihren Auftrag ab."),
    ("Welche Materialien sind möglich?", "Aluminium, Edelstahl und Messing – bedruckt, mechanisch graviert oder lasergraviert."),
    ("Wohin liefern Sie?", "Wir liefern nach Deutschland, Österreich und in die Schweiz."),
    ("Was benötigen Sie für ein Angebot?", "Einsatzzweck, Stückzahl, Maße in Millimetern sowie – soweit bekannt – Material, Befestigung, Beschriftung und Wunschtermin. Eine Skizze oder ein Muster hilft."),
]


def build():
    out = []

    # Startseite ------------------------------------------------------------
    with open(os.path.join(ROOT, "tools", "home_main.html"), encoding="utf-8") as f:
        home = f.read()
    out.append(render(
        "index.html",
        "Metallschilder &amp; Typenschilder nach Maß | GSD Metallschilder",
        "Typenschilder, gravierte Schilder und Firmenschilder aus Aluminium, Edelstahl und Messing – individuell nach Ihren Vorgaben. Lieferung in 10–14 Tagen nach Deutschland, Österreich und in die Schweiz.",
        home, extra_ld=[faq_ld(HOME_FAQ)]))

    # Typenschilder ---------------------------------------------------------
    c = [("typenschilder.html", "Typenschilder")]
    body = page_hero(c, "Metallschilder für Firmen", "Typenschilder für Maschinen, Geräte und Anlagen",
                     "Bedruckt oder graviert, aus Aluminium, Edelstahl oder Messing – mit Modell, Seriennummer und technischen Daten nach Ihren Vorgaben. Lieferung nach Deutschland, Österreich und in die Schweiz.",
                     art="Typenschild") + "\n" + subnav("typenschilder.html") + f"""
<section aria-labelledby="ausfuehrung">
  <div class="wrap">
    <p class="eyebrow">Welche Ausführung benötigen Sie?</p>
    <h2 id="ausfuehrung">Bedruckt oder graviert.</h2>
    <p class="lead">Beide Ausführungen fertigen wir nach Ihren Maßen und Daten. Welche besser passt, hängt vor allem von Einsatzort, Beanspruchung und Stückzahl ab.</p>
    <div class="option-grid">
      <article class="option">
        <img src="https://metallschilder24.com/img/typenschild-1.jpg" alt="Bedrucktes Typenschild mit CE-Kennzeichnung und technischen Daten" loading="lazy" width="259" height="167">
        <div class="body">
          <h3>Bedruckte Typenschilder</h3>
          <p>Direktdruck, Sublimationsdruck, Eloxal-Unterdruck und Siebdruck – vom Einzelstück bis zur Serie, auch mit Logo und Farben.</p>
          <a class="more" href="typenschilder-bedruckt.html">Druckverfahren vergleichen</a>
        </div>
      </article>
      <article class="option">
        <img src="{WP}2013/08/graviert-1.jpg" alt="Graviertes Schild aus Messing mit Schriftzug Muster" loading="lazy" width="800" height="457">
        <div class="body">
          <h3>Gravierte Typenschilder</h3>
          <p>Mechanische Gravur oder Lasergravur in Edelstahl, Aluminium oder Messing – besonders langlebig und edel in der Optik.</p>
          <a class="more" href="typenschilder-graviert.html">Mehr über Gravuren</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="soft" aria-labelledby="angaben">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Für Ihr Angebot</p>
      <h2 id="angaben">Diese Angaben helfen uns.</h2>
      <ul class="checks">
        <li><strong>Stückzahl:</strong> Wie viele Schilder benötigen Sie?</li>
        <li><strong>Maße:</strong> Breite und Höhe, möglichst in Millimetern.</li>
        <li><strong>Einsatzzweck:</strong> Wo und unter welchen Bedingungen werden die Schilder eingesetzt?</li>
        <li><strong>Material und Ausführung:</strong> Soweit bekannt, z. B. Aluminium oder Edelstahl, bedruckt oder graviert.</li>
        <li><strong>Beschriftung und Termin:</strong> Welche Angaben sollen auf das Schild, und wann benötigen Sie es?</li>
      </ul>
      <p style="margin-top:18px">Material oder Verfahren stehen noch nicht fest? Beschreiben Sie zunächst den geplanten Einsatz – wir beraten Sie.</p>
    </div>
    <div class="aside-box">
      <h3>Direkt anfragen</h3>
      <ul class="contact-list">
        <li>{ICON['mail']}<span><a href="mailto:{MAIL}">{MAIL}</a><small>Vorlagen und Fotos gern als Anhang</small></span></li>
        <li>{ICON['phone']}<span><a href="{PHONE_LINK}">{PHONE}</a><small>Persönliche Beratung</small></span></li>
        <li>{ICON['clock']}<span><strong>10–14 Tage</strong><small>Übliche Lieferzeit</small></span></li>
      </ul>
      <a class="btn btn-accent" href="kontakt.html?art=Typenschild#anfrage">Angebot für Typenschilder anfragen <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section aria-labelledby="beispiele">
  <div class="wrap">
    <p class="eyebrow">Beispiele</p>
    <h2 id="beispiele">Typenschilder aus unserer Fertigung.</h2>
    {gallery([
        ("https://metallschilder24.com/img/typenschild-1.jpg", None, "Typenschild mit CE-Zeichen und technischen Daten", "Typenschild mit CE-Kennzeichnung"),
        ("https://metallschilder24.com/img/typenschild-2.jpg", None, "Typenschild aus Aluminium mit Leerfeldern", "Typenschild mit Leerfeldern"),
        (WP + "2013/08/typenschild-5.jpg", None, "Technisches Schild mit Piktogrammen für Luftdruck", "Technisches Schild mit Piktogrammen"),
        (WP + "2013/08/typenschild-6.jpg", None, "Warnschild mit Symbol und rotem Feld", "Mehrfarbig bedrucktes Warnschild"),
        (WP + "2013/08/typenschild-4.jpg", None, "Kleines bedrucktes Schild mit Logo", "Bedrucktes Schild mit Logo"),
    ])}
  </div>
</section>

{cta("Typenschilder anfragen.", "Nennen Sie uns Stückzahl, Maße und Einsatzzweck – wir erstellen Ihnen ein passendes Angebot.", "Typenschild")}"""
    out.append(render("typenschilder.html", "Typenschilder für Maschinen &amp; Anlagen – bedruckt oder graviert | GSD Metallschilder",
                      "Typenschilder aus Aluminium, Edelstahl oder Messing für Maschinen, Geräte und Anlagen – bedruckt oder graviert, nach Ihren Vorgaben. Lieferung in 10–14 Tagen im DACH-Gebiet.",
                      body, c))

    # Typenschilder bedruckt -----------------------------------------------
    c = [("typenschilder.html", "Typenschilder"), ("typenschilder-bedruckt.html", "Bedruckt")]
    body = page_hero(c, "Typenschilder", "Bedruckte Typenschilder",
                     "Vier Druckverfahren für unterschiedliche Anforderungen: Hier sehen Sie auf einen Blick, welches Verfahren zu Stückzahl, Einsatzort und Gestaltung passt.",
                     art="Typenschild") + "\n" + subnav("typenschilder-bedruckt.html") + """
<section aria-labelledby="vergleich">
  <div class="wrap">
    <p class="eyebrow">Übersicht</p>
    <h2 id="vergleich">Druckverfahren im Vergleich.</h2>
    <div class="table-wrap">
      <table class="compare">
        <thead><tr><th scope="col">Verfahren</th><th scope="col">Vorteile</th><th scope="col">Nachteile</th></tr></thead>
        <tbody>
          <tr>
            <th scope="row">Sublimationsdruck</th>
            <td class="pro"><ul><li>Schnell und einfach umsetzbar</li><li>Völlig flexible Gestaltung, auch in Fotoqualität</li><li>Geschützte Oberfläche, edles Aussehen</li><li>Kleinauflagen ohne Aufpreis oder Mindestmenge</li></ul></td>
            <td class="con"><ul><li>Im Außenbereich nur begrenzte Lebensdauer</li><li>Nur bedingt für hohe Stückzahlen</li><li>Eingeschränkte Materialauswahl</li></ul></td>
          </tr>
          <tr>
            <th scope="row">Siebdruck</th>
            <td class="pro"><ul><li>Ideal für große Stückzahlen</li><li>Lange Lebensdauer</li><li>Große Materialauswahl</li><li>Bei großen Stückzahlen relativ günstig</li></ul></td>
            <td class="con"><ul><li>Einricht- und Vorkosten</li></ul></td>
          </tr>
          <tr>
            <th scope="row">Direktdruck</th>
            <td class="pro"><ul><li>Niedrige Kosten, kurze Produktionszeit</li><li>Hohe Flexibilität bei den Materialien</li><li>Druck auf strukturierte Oberflächen (z. B. Warzenblech)</li><li>Sehr hohe maximale Materialhöhe (ca. 10 cm)</li><li>Weiß als Abdeck-, Untergrund- oder Spotfarbe</li></ul></td>
            <td class="con"><ul><li>Kein Schutz gegen mechanische Beanspruchung</li></ul></td>
          </tr>
          <tr>
            <th scope="row">Eloxal-Unterdruck</th>
            <td class="pro"><ul><li>Äußerst widerstandsfähig im Außenbereich</li><li>Geeignet für Industrie und Problembereiche</li></ul></td>
            <td class="con"><ul><li>Nur auf Aluminium</li></ul></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="note">Weitere Verfahren wie Prägung oder Ätzung auf Anfrage.</p>
  </div>
</section>

<section class="soft" aria-labelledby="verfahren">
  <div class="wrap">
    <p class="eyebrow">Die Verfahren im Detail</p>
    <h2 id="verfahren">So entstehen bedruckte Typenschilder.</h2>
    <div class="info-cards two">
      <div class="info-card"><h3>Sublimationsdruck</h3><p>Schnelle, einfache Bearbeitung mit geschützter Oberfläche. Kleinst- und Kleinauflagen ohne Aufpreis oder Mindestmenge – mit individueller Gestaltung in Fotoqualität.</p></div>
      <div class="info-card"><h3>Eloxal-Unterdruck</h3><p>Ein spezielles Verfahren auf Aluminium mit offenporiger Oberfläche. Nach dem Druck werden die Poren geschlossen – dadurch sind die Schilder besonders widerstandsfähig, speziell in Industrie und Außenbereich.</p></div>
      <div class="info-card"><h3>Siebdruck</h3><p>Die günstige und hochwertige Standardanwendung für große Stückzahlen.</p></div>
      <div class="info-card"><h3>Digitaler Direktdruck</h3><p>Die Farbe wird direkt auf das Material gedruckt und sofort mit UV-Licht gehärtet. Das Ergebnis hat eine leicht satinierte Anmutung, ähnlich wie hochwertiges bedrucktes Papier.</p></div>
    </div>
  </div>
</section>

<section aria-labelledby="beispiele">
  <div class="wrap">
    <p class="eyebrow">Beispiele</p>
    <h2 id="beispiele">Bedruckte Schilder aus unserer Fertigung.</h2>
    """ + gallery([
        (WP + "2013/08/typenschild-5.jpg", None, "Bedrucktes technisches Schild mit Piktogrammen", "Technisches Schild mit Piktogrammen"),
        (WP + "2013/08/typenschild-6.jpg", None, "Mehrfarbig bedrucktes Warnschild", "Mehrfarbiger Druck"),
        (WP + "2013/08/typenschild-3.jpg", None, "Fotodruck einer Landschaft auf Metall", "Druck in Fotoqualität"),
        (WP + "2013/08/typenschild-4.jpg", None, "Kleines bedrucktes Schild mit Logo", "Schild mit Logo"),
    ]) + """
  </div>
</section>

""" + cta("Unsicher, welches Verfahren passt?", "Beschreiben Sie uns Einsatzort und Stückzahl – wir empfehlen Ihnen das passende Druckverfahren.", "Typenschild")
    out.append(render("typenschilder-bedruckt.html", "Bedruckte Typenschilder – Druckverfahren im Vergleich | GSD Metallschilder",
                      "Sublimationsdruck, Siebdruck, Direktdruck oder Eloxal-Unterdruck: Vor- und Nachteile der Druckverfahren für Typenschilder im Überblick.",
                      body, c))

    # Typenschilder graviert -----------------------------------------------
    c = [("typenschilder.html", "Typenschilder"), ("typenschilder-graviert.html", "Graviert")]
    body = page_hero(c, "Typenschilder", "Gravierte Typenschilder",
                     "Sehr hohe Lebensdauer und eine exklusive, edle Optik: Gravierte Schilder bleiben auch unter rauen Bedingungen dauerhaft lesbar.",
                     art="Graviertes Schild") + "\n" + subnav("typenschilder-graviert.html") + f"""
<section aria-labelledby="materialien">
  <div class="wrap split">
    <div class="prose">
      <p class="eyebrow">Materialien</p>
      <h2 id="materialien">Was sich gravieren lässt.</h2>
      <p>Für gravierte Schilder kommen Edelstahl, Aluminium und Messing zum Einsatz, außerdem Acrylglas und mehrschichtige Kunststoffe. Bei Schichtstoffen reicht die Gravur bis in eine andersfarbige Schicht – so entsteht ein kontrastreiches Schriftbild.</p>
      <ul class="methods" style="margin-top:20px">
        <li><strong>Edelstahl</strong></li><li><strong>Aluminium</strong></li><li><strong>Messing</strong></li><li>Acrylglas</li><li>Schichtstoff-Kunststoffe</li>
      </ul>
    </div>
    <figure class="figure-card">
      <img src="{WP}2013/08/graviert-1.jpg" alt="Graviertes Messingschild mit Schriftzug Muster" width="800" height="457" loading="lazy">
      <figcaption>Gravur in Messing</figcaption>
    </figure>
  </div>
</section>

<section class="soft" aria-labelledby="verfahren">
  <div class="wrap">
    <p class="eyebrow">Verfahren</p>
    <h2 id="verfahren">Mechanische Gravur oder Lasergravur.</h2>
    <div class="info-cards">
      <div class="info-card">
        <h3>Mechanische Gravur</h3>
        <p>Rotierende Fräser (Frässtichel) tragen das Material ab. Computergesteuerte Graviermaschinen verarbeiten Vektordaten – so lassen sich Motive verlustfrei und exakt wiederholbar übertragen.</p>
      </div>
      <div class="info-card">
        <h3>Lasergravur</h3>
        <p>Die modernste Graviertechnik: Der Laserstrahl erhitzt das Material so stark, dass es sich kontrasterzeugend verändert oder abgetragen wird. Durch Steuerung der Pulse sind sogar Halbtöne und Fotos auf Metall möglich.</p>
      </div>
      <div class="info-card">
        <h3>Maskengravur</h3>
        <p>Eine Maske mit der Vorlage wird verkleinert auf das Werkstück abgebildet. Ein einziger, energiereicher Laserpuls trägt die gesamte Kontur auf einmal ab – ideal für wiederkehrende Zeichen.</p>
      </div>
    </div>
  </div>
</section>

<section aria-labelledby="beispiele">
  <div class="wrap">
    <p class="eyebrow">Beispiele</p>
    <h2 id="beispiele">Gravierte Schilder.</h2>
    {gallery([
        (WP + "2013/08/graviert-1.jpg", None, "Graviertes Messingschild mit Schriftzug Muster", "Gravur in Messing"),
        (WP + "2013/08/graviert-2.jpg", None, "Graviertes Hinweisschild: Wartungsöffnung nur bei ausgeschaltetem Hauptschalter öffnen", "Graviertes Hinweisschild"),
        (WP + "2013/08/typenschild-7.jpg", None, "Graviertes Kanzleischild aus Messing", "Kanzleischild aus Messing"),
    ])}
  </div>
</section>

{cta("Gravierte Schilder anfragen.", "Nennen Sie uns Material, Maße und Beschriftung – oder beschreiben Sie einfach den Einsatz.", "Graviertes Schild")}"""
    out.append(render("typenschilder-graviert.html", "Gravierte Typenschilder – Lasergravur &amp; mechanische Gravur | GSD Metallschilder",
                      "Gravierte Typenschilder aus Edelstahl, Aluminium oder Messing: mechanische Gravur, Lasergravur und Maskengravur für langlebige, edle Kennzeichnung.",
                      body, c))

    # Firmenschilder --------------------------------------------------------
    c = [("firmenschilder.html", "Firmenschilder")]
    body = page_hero(c, "Firmen-, Kanzlei- und Praxisschilder", "Firmenschilder, die Eindruck machen",
                     "Das klassische Kanzleischild, Praxisschild oder Firmenschild – in der gewünschten Größe, im passenden Material und zu guten Preisen. Die passenden Befestigungssets liefern wir auf Wunsch gleich mit.",
                     art="Firmenschild") + f"""
<section aria-labelledby="ausfuehrungen">
  <div class="wrap">
    <p class="eyebrow">Ausführungen</p>
    <h2 id="ausfuehrungen">Vier Wege zu Ihrem Firmenschild.</h2>
    <div class="info-cards four">
      <div class="info-card"><h3>Graviert</h3><p>Aus lackiertem Messing – zeitlos und repräsentativ.</p></div>
      <div class="info-card"><h3>Eloxal-Unterdruck</h3><p>Bedruckt und besonders widerstandsfähig im Außenbereich.</p></div>
      <div class="info-card"><h3>Direktdruck</h3><p>Flexibel, farbig und wirtschaftlich – auch mit Logo.</p></div>
      <div class="info-card"><h3>Folienkaschiert</h3><p>Kaschiert mit hochwertiger Folie.</p></div>
    </div>
  </div>
</section>

<section class="soft" aria-labelledby="beispiele">
  <div class="wrap">
    <p class="eyebrow">Beispiele</p>
    <h2 id="beispiele">Firmenschilder aus unserer Fertigung.</h2>
    {gallery([
        (WP + "2013/08/typenschild-7.jpg", None, "Graviertes Kanzleischild aus Messing", "Graviertes Firmenschild in Messing"),
        (WP + "2013/08/firmenschild-2.jpg", None, "Bedrucktes Firmenschild Holzhaus Rottenacker", "Sublimationsdruck"),
        (WP + "2013/08/firmenschild-3.jpg", None, "Bedrucktes Schild Quality and Design", "Sublimationsdruck auf Alublech"),
        (WP + "2013/08/firmenschild-1.jpg", None, "Metallschild mit Fotodruck einer Landschaft", "Metallschild bedruckt"),
    ])}
  </div>
</section>

<section aria-labelledby="montage">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Montage</p>
      <h2 id="montage">Passend befestigt.</h2>
      <p class="lead">Ob mit Abstandshaltern an der Fassade, verschraubt am Eingang oder selbstklebend im Empfang: Wir liefern auf Wunsch den kompletten Befestigungssatz aus Dübeln, Schrauben, Abdeckkappen und Abstandhaltern.</p>
      <a class="btn btn-navy" href="befestigungen.html">Befestigungen ansehen</a>
    </div>
    <div class="aside-box">
      <h3>Für Ihr Angebot</h3>
      <ul class="checks">
        <li>Gewünschte Größe in Millimetern</li>
        <li>Logo oder Gestaltungsvorlage</li>
        <li>Innen- oder Außenbereich</li>
        <li>Material, soweit bekannt</li>
        <li>Befestigung und Wunschtermin</li>
      </ul>
    </div>
  </div>
</section>

{cta("Ihr Firmenschild anfragen.", "Senden Sie uns Ihr Logo und die gewünschte Größe – wir erstellen Ihnen ein individuelles Angebot.", "Firmenschild")}"""
    out.append(render("firmenschilder.html", "Firmenschilder, Kanzleischilder &amp; Praxisschilder aus Metall | GSD Metallschilder",
                      "Firmenschilder, Kanzlei- und Praxisschilder aus Messing, Aluminium oder Edelstahl – graviert, bedruckt oder folienkaschiert, inklusive passendem Befestigungssatz.",
                      body, c))

    # Hinweisschilder -------------------------------------------------------
    c = [("hinweisschilder.html", "Hinweisschilder")]
    body = page_hero(c, "Kennzeichnung", "Hinweisschilder in vielen Ausführungen",
                     "Gefahren- und Warnhinweise, Wegweiser, Wartungshinweise oder nummerierte Palettenschilder – bedruckt oder graviert, in der Form und Größe, die Sie brauchen.",
                     art="Hinweisschild") + f"""
<section aria-labelledby="einsatz">
  <div class="wrap">
    <p class="eyebrow">Einsatzbereiche</p>
    <h2 id="einsatz">Klare Hinweise – dauerhaft lesbar.</h2>
    <div class="info-cards">
      <div class="info-card"><h3>Warn- und Gefahrenhinweise</h3><p>Für Maschinen, Anlagen und Betriebsbereiche – gut sichtbar und beständig.</p></div>
      <div class="info-card"><h3>Wegweiser &amp; Beschilderung</h3><p>Orientierung für Besucher, Kunden und Mitarbeitende.</p></div>
      <div class="info-card"><h3>Nummerierte Schilder</h3><p>Zum Beispiel Palettenschilder mit fortlaufender Nummerierung.</p></div>
    </div>
  </div>
</section>

<section class="soft" aria-labelledby="beispiele">
  <div class="wrap">
    <p class="eyebrow">Beispiele</p>
    <h2 id="beispiele">Hinweisschilder aus unserer Fertigung.</h2>
    {gallery([
        (WP + "2013/08/hinweisschild-3.jpg", None, "Hinweisschild: Wartungsöffnung nur bei ausgeschaltetem Hauptschalter öffnen", "Graviertes Hinweisschild"),
        (WP + "2013/08/hinweisschild-4.jpg", None, "Technisches Hinweisschild mit Piktogrammen", "Technisches Hinweisschild"),
        (WP + "2013/08/hinweisschild-5.jpg", None, "Palettenschild mit Nummer 7099", "Palettenschild mit fortlaufender Nummerierung"),
        (WP + "2017/02/PferdeboxSchild-gif.gif", None, "Boxenschild mit Pferdename und Abstammung", "Individuelles Boxenschild"),
        (WP + "2013/08/hinweisschild-6.jpg", None, "Ausschnitt aus einem grün-weiß bedruckten Firmenschild", "Ausschnitt aus einem Firmenschild"),
    ])}
  </div>
</section>

{cta("Hinweisschilder anfragen.", "Nennen Sie uns Text, Maße und Stückzahl – auch Serien mit fortlaufender Nummerierung sind möglich.", "Hinweisschild")}"""
    out.append(render("hinweisschilder.html", "Hinweisschilder &amp; Warnschilder aus Metall | GSD Metallschilder",
                      "Hinweisschilder aus Metall: Warn- und Gefahrenhinweise, Wegweiser, Wartungshinweise und nummerierte Palettenschilder – bedruckt oder graviert.",
                      body, c))

    # Weitere Schilder (Übersicht) -----------------------------------------
    c = [("weitere-schilder.html", "Alle Metallschilder")]
    body = page_hero(c, "Produktübersicht", "Alle Metallschilder im Überblick",
                     "Von der technischen Kennzeichnung bis zum repräsentativen Firmenschild – wählen Sie den passenden Bereich.") + f"""
<section aria-label="Produktbereiche">
  <div class="wrap">
    <div class="option-grid three" style="margin-top:0">
      <article class="option">
        <img src="https://metallschilder24.com/img/typenschild-1.jpg" alt="Typenschild mit CE-Kennzeichnung" loading="lazy">
        <div class="body"><h3>Typenschilder</h3><p>Für Maschinen, Geräte und Anlagen – bedruckt oder graviert.</p><a class="more" href="typenschilder.html">Zu den Typenschildern</a></div>
      </article>
      <article class="option">
        <img src="{WP}2013/08/typenschild-7.jpg" alt="Graviertes Kanzleischild aus Messing" loading="lazy">
        <div class="body"><h3>Firmenschilder</h3><p>Graviert aus lackiertem Messing, bedruckt im Eloxal-Unterdruck oder Direktdruck, oder mit hochwertiger Folie kaschiert.</p><a class="more" href="firmenschilder.html">Zu den Firmenschildern</a></div>
      </article>
      <article class="option">
        <img src="{WP}2013/08/hinweisschild-3.jpg" alt="Hinweisschild Wartungsöffnung" loading="lazy">
        <div class="body"><h3>Hinweisschilder</h3><p>In vielerlei Ausführungen und Formen – wie Gefahrenwarnschilder, Wegweiser usw.</p><a class="more" href="hinweisschilder.html">Zu den Hinweisschildern</a></div>
      </article>
    </div>
  </div>
</section>

{cta()}"""
    out.append(render("weitere-schilder.html", "Metallschilder im Überblick – Typen-, Firmen- &amp; Hinweisschilder | GSD Metallschilder",
                      "Alle Metallschilder im Überblick: Typenschilder, Firmenschilder und Hinweisschilder aus Aluminium, Edelstahl und Messing.",
                      body, c))

    # Befestigungen ---------------------------------------------------------
    c = [("befestigungen.html", "Befestigungen")]
    body = page_hero(c, "Montage", "Befestigungen für Ihre Metallschilder",
                     "Annieten, anschrauben oder kleben: Wir bereiten Ihre Schilder passend zur Montage vor und liefern auf Wunsch den kompletten Befestigungssatz.") + """
<nav class="subnav" aria-label="Befestigungsarten"><div class="wrap"><ul>
  <li><a href="#annieten">Annieten</a></li><li><a href="#anschrauben">Anschrauben</a></li><li><a href="#selbstklebend">Selbstklebend</a></li><li><a href="#befestigungssatz">Befestigungssatz</a></li>
</ul></div></nav>

<section aria-label="Befestigungsarten">
  <div class="wrap prose" style="max-width:900px">
    <article class="fasten" id="annieten">
      <img src="https://metallschilder24.com/img/blindnieten.jpg" alt="Drei Blindnieten in verschiedenen Größen" loading="lazy">
      <div>
        <h2>Annieten</h2>
        <p>Das Annieten erfolgt in der Regel mit <strong>Blindnieten</strong> (umgangssprachlich auch POP-Nieten). Sie benötigen nur Zugang zu einer Seite des Bauteils und werden mit einer Blindnietzange gesetzt.</p>
        <details>
          <summary><strong>So funktioniert ein Blindniet</strong></summary>
          <p>Der Blindniet besteht aus einem hohlen Nietkörper mit Kopf und einem durchgesteckten Dorn mit Sollbruchstelle. Der Niet wird durch die Bohrung geführt, dann zieht die Zange den Dorn heraus. Dadurch staucht und weitet sich der Niet hinter der Bohrung. Am Ende reißt der Dorn an der Sollbruchstelle innerhalb des Nietkörpers ab und ragt nicht hervor. Bei Blindnieten für Spezialanwendungen (z. B. im Flugzeugbau) wird der verbleibende Dornrest zusätzlich mit einem eingepressten Ring gesichert.</p>
        </details>
      </div>
    </article>
    <article class="fasten" id="anschrauben">
      <img src="https://metallschilder24.com/img/anschrauben.jpg" alt="Verschiedene Schraubenköpfe" loading="lazy">
      <div>
        <h2>Anschrauben</h2>
        <p>Die Befestigung mit Schrauben ist – je nach Anforderungen und Vorgaben – wahlweise mit oder ohne Abstandshalter möglich. Es gibt eine Vielzahl von Schraubmöglichkeiten und Ausführungen; hierzu beraten wir Sie gern.</p>
      </div>
    </article>
    <article class="fasten" id="selbstklebend">
      <img src="https://metallschilder24.com/img/selbstklebend.jpg" alt="Rolle Klebefilm" loading="lazy">
      <div>
        <h2>Selbstklebend</h2>
        <p>Wir bringen einen Klebefilm auf die Rückseite der Schilder auf. Dafür verwenden wir den <strong>Klebefilm 3M™ 468MP</strong>.</p>
        <ul>
          <li>Hochwertiger Reinacrylat-Klebstoff, entwickelt für Schilder, Folientastaturen und Frontblenden</li>
          <li>Für Metall, hochenergetische Lack- und Kunststoffoberflächen</li>
          <li>Hervorragend beständig gegen UV-Strahlung, Temperatur, Chemikalien und Lösemittel</li>
        </ul>
      </div>
    </article>
    <article class="fasten" id="befestigungssatz">
      <img src="https://metallschilder24.com/img/befestigungssatz.jpg" alt="Befestigungssatz mit Dübeln, Schrauben und Abstandhaltern" loading="lazy">
      <div>
        <h2>Befestigungssatz</h2>
        <p>Als Ergänzung bieten wir einen kompletten Befestigungssatz an – bestehend aus <strong>Dübeln, Schrauben, Abdeckkappen und Abstandhaltern</strong> in verschiedensten Ausführungen.</p>
      </div>
    </article>
  </div>
</section>

""" + cta("Welche Befestigung passt?", "Nennen Sie uns Untergrund und Einsatzort – wir empfehlen die passende Lösung.")
    out.append(render("befestigungen.html", "Befestigungen für Metallschilder – Nieten, Schrauben, Klebefilm | GSD Metallschilder",
                      "Metallschilder annieten, anschrauben oder selbstklebend mit 3M™ 468MP – und auf Wunsch mit komplettem Befestigungssatz aus Dübeln, Schrauben und Abstandhaltern.",
                      body, c))

    # Über uns --------------------------------------------------------------
    c = [("ueber-uns.html", "Über uns")]
    body = page_hero(c, "Über GSD Metallschilder", "Das Erfolgsgeheimnis: ein effektives Netzwerk",
                     "Erfahrung in der Schilderherstellung, kombiniert mit spezialisierten Partnern – für schnelle, konkrete Antworten auf Ihre Anfrage.", actions=False) + f"""
<section aria-labelledby="geschichte">
  <div class="wrap split rev">
    <figure class="portrait">
      <img src="{WP}2025/12/786EE714-C82F-4C31-94DA-018194104376.png" alt="Porträt von Günter Schneider" width="1024" height="1024" loading="lazy">
      <figcaption><strong>Günter Schneider</strong><br>Gründer und Inhaber</figcaption>
    </figure>
    <div class="prose">
      <p class="eyebrow">Erfahrung</p>
      <h2 id="geschichte">Persönlich für Ihr Unternehmen da.</h2>
      <p>Gründer und Firmeninhaber <strong>Günter Schneider</strong> blickt auf über 27 Jahre Erfahrung in Schilderdruck und Schilderherstellung zurück.</p>
      <p>Im Lauf der Zeit hat sich gezeigt: Für unsere Kunden ist es deutlich besser, wenn wir auf ein großes Partnernetzwerk zurückgreifen können. Durch die starken Veränderungen im Druckwesen sind viele Spezialisten entstanden – und genau das ist ein entscheidender Vorteil gegenüber einem einzigen großen Maschinenpark.</p>
      <p><strong>„Vernetzung“ ist das entscheidende Stichwort.</strong> Wir ergänzen uns durch spezifisches Fachwissen und können daher schnell konkrete Antworten auf Kundenanfragen liefern.</p>
      <div class="stats">
        <div><strong>27+ Jahre</strong><span>Erfahrung im Schilderdruck</span></div>
        <div><strong>10–14 Tage</strong><span>Übliche Lieferzeit</span></div>
        <div><strong>DE · AT · CH</strong><span>Lieferung im DACH-Gebiet</span></div>
      </div>
    </div>
  </div>
</section>

<section class="soft" aria-labelledby="vorteile">
  <div class="wrap">
    <p class="eyebrow">Ihr Vorteil</p>
    <h2 id="vorteile">Warum ein Netzwerk besser ist.</h2>
    <div class="info-cards">
      <div class="info-card"><h3>Das richtige Verfahren</h3><p>Statt eines Verfahrens für alles: Für jede Anforderung arbeiten wir mit dem passenden Spezialisten.</p></div>
      <div class="info-card"><h3>Schnelle Antworten</h3><p>Gebündeltes Fachwissen bedeutet konkrete Aussagen zu Material, Verfahren und Termin.</p></div>
      <div class="info-card"><h3>Ein Ansprechpartner</h3><p>Sie sprechen mit uns – wir koordinieren alles Weitere bis zur Lieferung.</p></div>
    </div>
    <p style="margin-top:28px"><a href="kundenmeinungen.html"><strong>Was unsere Kunden sagen →</strong></a></p>
  </div>
</section>

{cta()}"""
    out.append(render("ueber-uns.html", "Über uns – GSD Metall-Schilder Drucksysteme | GSD Metallschilder",
                      "GSD Metallschilder: über 27 Jahre Erfahrung in Schilderdruck und Schilderherstellung – mit einem Netzwerk spezialisierter Partner für schnelle, konkrete Antworten.",
                      body, c))

    # Kundenmeinungen -------------------------------------------------------
    c = [("ueber-uns.html", "Über uns"), ("kundenmeinungen.html", "Kundenmeinungen")]
    body = page_hero(c, "Kundenmeinungen", "Was unsere Kunden sagen",
                     "Auszüge aus Rückmeldungen, die uns per E-Mail erreicht haben.", actions=False) + """
<section aria-label="Kundenstimmen">
  <div class="wrap">
    <div class="testimonials">
      <figure class="testimonial">
        <blockquote><p>„Danke Ihnen, es ist gut geworden, passt und war wieder mal unkompliziert. Herzlichen Dank dafür und wahrscheinlich bis ins nächste Jahr wieder.“</p></blockquote>
        <figcaption><strong>Franz Dußmann</strong>Pflegedienstleiter, RoMed Klinikum Rosenheim</figcaption>
      </figure>
      <figure class="testimonial">
        <blockquote><p>„Die Schilder sind angekommen und zu unserer Zufriedenheit ausgefallen. Danke!“</p></blockquote>
        <figcaption><strong>Katrin Galipp-Bolte</strong>Kundin</figcaption>
      </figure>
    </div>
  </div>
</section>

""" + cta("Werden Sie unser nächster zufriedener Kunde.", "Beschreiben Sie Ihr Vorhaben – wir melden uns mit einem individuellen Angebot.")
    out.append(render("kundenmeinungen.html", "Kundenmeinungen | GSD Metallschilder",
                      "Rückmeldungen von Kunden der GSD Metallschilder zu Typenschildern, Firmenschildern und Hinweisschildern.",
                      body, c))

    # Kontakt ---------------------------------------------------------------
    c = [("kontakt.html", "Kontakt")]
    body = page_hero(c, "Ihre Anfrage an Metallschilder24", "Sie haben die Vorgaben. Wir das passende Angebot.",
                     "Ob Typenschild, Gravur oder Firmenschild: Beschreiben Sie Ihren Bedarf. Material und Ausführung müssen noch nicht endgültig feststehen.", actions=False) + f"""
<section aria-label="Anfrageformular und Kontakt">
  <div class="wrap kontakt-grid">
    {quote_form("Was benötigen Sie?", full=True)}
    <aside>
      <div class="aside-box">
        <div class="person">
          <img src="{WP}2025/12/786EE714-C82F-4C31-94DA-018194104376-300x300.png" alt="Günter Schneider" width="84" height="84">
          <div><strong>Günter Schneider</strong><span>GSD Metall-Schilder Drucksysteme</span></div>
        </div>
        <ul class="contact-list">
          <li>{ICON['mail']}<span><a href="mailto:{MAIL}">{MAIL}</a><small>Zeichnung, Foto oder Vorlage gern als Anhang</small></span></li>
          <li>{ICON['phone']}<span><a href="{PHONE_LINK}">{PHONE}</a><small>Mobil</small></span></li>
          <li>{ICON['phone']}<span><a href="tel:+4982219668204">08221 / 9668204</a><small>Festnetz</small></span></li>
          <li>{ICON['pin']}<span>Bergstraße 12<br>89312 Günzburg</span></li>
        </ul>
      </div>
      <div class="aside-box" style="margin-top:20px;background:#fff;border:1px solid var(--line)">
        <h3>Hilfreich für Ihr Angebot</h3>
        <ul class="checks">
          <li>Stückzahl und Maße in Millimetern</li>
          <li>Einsatzbereich und Umgebungsbedingungen</li>
          <li>Material und Befestigung, soweit bekannt</li>
          <li>Beschriftung und gewünschter Liefertermin</li>
        </ul>
        <p style="margin:18px 0 0;font-size:.92rem"><strong>Üblicherweise 10–14 Tage.</strong> Den konkreten Liefertermin klären wir für Ihren Auftrag. Lieferung nach Deutschland, Österreich und in die Schweiz.</p>
      </div>
    </aside>
  </div>
</section>"""
    out.append(render("kontakt.html", "Kontakt &amp; Angebot anfragen | GSD Metallschilder",
                      "Fragen Sie Ihr Metallschild unverbindlich an: Typenschilder, Gravuren, Firmenschilder. Per Formular, E-Mail oder Telefon – GSD Metallschilder, Günzburg.",
                      body, c))

    # Impressum (Rechtstext unverändert übernommen) -------------------------
    c = [("impressum.html", "Impressum")]
    with open(os.path.join(ROOT, "tools", "impressum_main.html"), encoding="utf-8") as f:
        legal = f.read()
    body = page_hero(c, "Rechtliches", "Impressum &amp; Datenschutz", actions=False) + legal
    out.append(render("impressum.html", "Impressum &amp; Datenschutz | GSD Metallschilder",
                      "Impressum und Datenschutzhinweise der GSD Metall-Schilder Drucksysteme, Inh. Günter Schneider, Günzburg.",
                      body, c, robots="index, follow"))

    # Sitemap ---------------------------------------------------------------
    c = [("sitemap.html", "Sitemap")]
    body = page_hero(c, "Übersicht", "Sitemap", actions=False) + """
<section aria-label="Alle Seiten">
  <div class="wrap">
    <ul class="sitemap-list">
      <li><a href="index.html">Startseite</a></li>
      <li><a href="weitere-schilder.html">Alle Metallschilder</a>
        <ul>
          <li><a href="typenschilder.html">Typenschilder</a></li>
          <li><a href="typenschilder-bedruckt.html">Typenschilder bedruckt</a></li>
          <li><a href="typenschilder-graviert.html">Typenschilder graviert</a></li>
          <li><a href="firmenschilder.html">Firmenschilder</a></li>
          <li><a href="hinweisschilder.html">Hinweisschilder</a></li>
        </ul>
      </li>
      <li><a href="befestigungen.html">Befestigungen</a>
        <ul>
          <li><a href="befestigungen.html#annieten">Annieten</a></li>
          <li><a href="befestigungen.html#anschrauben">Anschrauben</a></li>
          <li><a href="befestigungen.html#selbstklebend">Selbstklebend</a></li>
          <li><a href="befestigungen.html#befestigungssatz">Befestigungssatz</a></li>
        </ul>
      </li>
      <li><a href="ueber-uns.html">Über uns</a>
        <ul><li><a href="kundenmeinungen.html">Kundenmeinungen</a></li></ul>
      </li>
      <li><a href="kontakt.html">Kontakt</a></li>
      <li><a href="impressum.html">Impressum &amp; Datenschutz</a></li>
    </ul>
  </div>
</section>"""
    out.append(render("sitemap.html", "Sitemap | GSD Metallschilder",
                      "Übersicht aller Seiten von metallschilder24.com.", body, c))

    # sitemap.xml -----------------------------------------------------------
    urls = "\n".join(
        f"  <url><loc>{SITE if p == 'index.html' else SITE + p}</loc></url>" for p in out)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
    print("\n".join(out))


if __name__ == "__main__":
    build()
