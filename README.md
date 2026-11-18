# metallschilder24.com – überarbeitete Website

Statische HTML-Seiten (ohne WordPress-Abhängigkeit). Bilder werden weiterhin vom
bestehenden Server unter `metallschilder24.com/wp-content/uploads/` und `/img/` geladen.

## Seiten bearbeiten

Kopf, Navigation und Fußbereich sind in `tools/build_site.py` zentral hinterlegt.
Nach Änderungen alle Seiten neu erzeugen:

    python3 tools/build_site.py

- Startseiten-Inhalt: `tools/home_main.html`
- Impressum/Datenschutz: `tools/impressum_main.html`
- Gestaltung: `assets/style.css`, Menü und Formular: `assets/main.js`

## Alte → neue Adressen (für Weiterleitungen)

| Alt                | Neu                               |
|--------------------|-----------------------------------|
| `/?page_id=7`      | `/typenschilder.html`             |
| `/?page_id=9`      | `/typenschilder-bedruckt.html`    |
| `/?page_id=11`     | `/typenschilder-graviert.html`    |
| `/?page_id=17`     | `/weitere-schilder.html`          |
| `/?page_id=19`     | `/firmenschilder.html`            |
| `/?page_id=21`     | `/hinweisschilder.html`           |
| `/?page_id=32`     | `/befestigungen.html`             |
| `/?page_id=34`     | `/befestigungen.html#annieten`    |
| `/?page_id=36`     | `/befestigungen.html#anschrauben` |
| `/?page_id=38`     | `/befestigungen.html#selbstklebend` |
| `/?page_id=40`     | `/befestigungen.html#befestigungssatz` |
| `/?page_id=42`     | `/kundenmeinungen.html`           |
| `/?page_id=44`     | `/kontakt.html`                   |
| `/?page_id=48`     | `/ueber-uns.html`                 |
| `/?page_id=56`     | `/sitemap.html`                   |
| `/?page_id=58`     | `/impressum.html`                 |
