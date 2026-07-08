import os

BASE = "/home/claude/amis-nature"

# ---------- SVG PIECES ----------

def icon_logo(prefix):
    return f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="50" cy="50" r="46" fill="none" stroke="currentColor" stroke-width="2.4" opacity=".85"/>
  <circle cx="50" cy="50" r="39" fill="none" stroke="currentColor" stroke-width="1" opacity=".5"/>
  <path id="{prefix}-star-l" d="M18 50l1.6 3.4 3.7.5-2.7 2.6.6 3.7-3.2-1.8-3.2 1.8.6-3.7-2.7-2.6 3.7-.5z" fill="currentColor" opacity=".8"/>
  <use href="#{prefix}-star-l" x="60"/>
  <path d="M50 26c-9 8-15 17-15 27 0 10 7 16 15 19 8-3 15-9 15-19 0-10-6-19-15-27z" fill="currentColor" opacity=".9"/>
  <path d="M50 34v34M50 44l-7 6M50 50l7 6" stroke="var(--forest-deep,#0F2318)" stroke-width="1.4" fill="none" opacity=".55"/>
</svg>'''

def badge_logo(prefix):
    return f'''<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" id="{prefix}">
  <defs>
    <path id="{prefix}-arctop" d="M 34,124 A 90,90 0 0 1 206,124" fill="none"/>
  </defs>
  <circle cx="120" cy="124" r="108" fill="none" stroke="currentColor" stroke-width="2.6" opacity=".9"/>
  <circle cx="120" cy="124" r="97" fill="none" stroke="currentColor" stroke-width="1" opacity=".55"/>
  <path d="M30 124l2 4.4 4.8.6-3.5 3.4.8 4.8-4.1-2.3-4.1 2.3.8-4.8-3.5-3.4 4.8-.6z" fill="currentColor" opacity=".85" transform="translate(3 0)"/>
  <path d="M30 124l2 4.4 4.8.6-3.5 3.4.8 4.8-4.1-2.3-4.1 2.3.8-4.8-3.5-3.4 4.8-.6z" fill="currentColor" opacity=".85" transform="translate(173 0)"/>
  <path d="M120 78c-15 13-26 29-26 46 0 17 12 27 26 32 14-5 26-15 26-32 0-17-11-33-26-46z" fill="currentColor" opacity=".95"/>
  <path d="M120 96v58M120 112l-12 10M120 124l12 10M120 136l-10 8" stroke="#0F2318" stroke-width="1.8" fill="none" opacity=".5"/>
  <text font-family="Fraunces, serif" font-size="14.5" letter-spacing="2.6" fill="currentColor">
    <textPath href="#{prefix}-arctop" startOffset="50%" text-anchor="middle">LES AMIS DE LA NATURE</textPath>
  </text>
  <text x="120" y="214" font-family="Inter, sans-serif" font-size="9.5" letter-spacing="1.5" fill="currentColor" text-anchor="middle" font-style="italic" opacity=".85">TOUS POUR L'ARBRE, L'ARBRE POUR LA VIE</text>
</svg>'''

def vine_svg():
    return '''<svg class="intro-vine left" viewBox="0 0 120 800" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10 0 C40 100 -10 200 20 300 C45 380 0 460 25 560 C45 640 5 720 20 800" stroke="#3E6B4C" stroke-width="3" fill="none" opacity=".7"/>
  <g fill="#A7C25C" opacity=".85">
    <ellipse cx="18" cy="120" rx="10" ry="5" transform="rotate(30 18 120)"/>
    <ellipse cx="24" cy="260" rx="12" ry="6" transform="rotate(-20 24 260)"/>
    <ellipse cx="10" cy="420" rx="10" ry="5" transform="rotate(40 10 420)"/>
    <ellipse cx="26" cy="600" rx="11" ry="5" transform="rotate(-15 26 600)"/>
    <ellipse cx="14" cy="740" rx="10" ry="5" transform="rotate(25 14 740)"/>
  </g>
</svg>'''

def vine_svg_right():
    return '''<svg class="intro-vine right" viewBox="0 0 120 800" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10 0 C40 100 -10 200 20 300 C45 380 0 460 25 560 C45 640 5 720 20 800" stroke="#3E6B4C" stroke-width="3" fill="none" opacity=".7"/>
  <g fill="#A7C25C" opacity=".85">
    <ellipse cx="18" cy="150" rx="10" ry="5" transform="rotate(-30 18 150)"/>
    <ellipse cx="24" cy="300" rx="12" ry="6" transform="rotate(20 24 300)"/>
    <ellipse cx="10" cy="460" rx="10" ry="5" transform="rotate(-40 10 460)"/>
    <ellipse cx="26" cy="620" rx="11" ry="5" transform="rotate(15 26 620)"/>
  </g>
</svg>'''

def growth_rail():
    return '''<div id="growth-rail" aria-hidden="true">
    <svg viewBox="0 0 34 800" preserveAspectRatio="none">
      <path class="rail-stem" d="M17 0 C24 100 10 200 20 300 C28 380 8 460 20 560 C28 640 10 720 17 800"/>
      <path id="rail-progress" d="M17 0 C24 100 10 200 20 300 C28 380 8 460 20 560 C28 640 10 720 17 800" fill="none" stroke="#A7C25C" stroke-width="3"/>
    </svg>
  </div>'''

def watering_can_icon():
    return '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 10h9l4-3h4l1 2-4 2v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M12 10V7M20 9l1.5-1.5"/></svg>'''

NAV_ITEMS = [
    ("index.html", "Accueil", "accueil"),
    ("services.html", "Services", "services"),
    ("realisations.html", "Réalisations", "realisations"),
    ("pepiniere.html", "Pépinière", "pepiniere"),
    ("catalogue.html", "Catalogue", "catalogue"),
    ("contact.html", "Contact", "contact"),
]

def nav_links():
    items = ""
    for href, label, key in NAV_ITEMS:
        items += f'<a href="{href}" data-page="{key}">{label}<span class="leaf-hover"><svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path d="M12 2C7 2 3 6 3 11c0 6 5 9 9 11 4-2 9-5 9-11 0-5-4-9-9-9z"/></svg></span></a>\n'
    return items

def header(prefix):
    return f'''<header class="site-header">
    <a href="index.html" class="brand">
      <span style="color:var(--lime)">{icon_logo(prefix)}</span>
      <span class="brand-word">Les Amis de <b>la Nature</b></span>
    </a>
    <nav class="nav-links">
      {nav_links()}
    </nav>
    <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
  </header>'''

def footer():
    return '''<footer class="site-footer">
    <div class="footer-grid">
      <div>
        <h5>Les Amis de la Nature</h5>
        <p style="color:var(--sand-deep); font-size:.9rem; max-width:320px;">Pépinière, aménagement paysager et sensibilisation environnementale à Bamako. « Tous pour l'arbre, l'arbre pour la vie. »</p>
      </div>
      <div>
        <h5>Navigation</h5>
        <a href="services.html">Nos services</a>
        <a href="realisations.html">Nos réalisations</a>
        <a href="pepiniere.html">Pépinière</a>
        <a href="catalogue.html">Catalogue espèces</a>
      </div>
      <div>
        <h5>Services</h5>
        <a href="services.html">Production de plants</a>
        <a href="services.html">Aménagement d'espaces verts</a>
        <a href="services.html">Assainissement</a>
        <a href="services.html">Formation - Conseil</a>
      </div>
      <div>
        <h5>Contact</h5>
        <a href="tel:+22320208207">20 20 82 07</a>
        <a href="tel:+22366656534">66 65 65 34</a>
        <a href="mailto:paulbernadette@gmail.com">paulbernadette@gmail.com</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Les Amis de la Nature — Bamako, Mali</span>
      <span>« Un peuple sans forêt est un peuple qui meurt »</span>
    </div>
  </footer>'''

def scroll_indicator():
    return f'<div class="scroll-indicator" title="Retour en haut">{watering_can_icon()}</div>'

def leaf_field():
    return '<div id="leaf-field" aria-hidden="true"></div>'

def head(title, desc, page_key):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Les Amis de la Nature</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-page="{page_key}">
'''

def scripts():
    return '''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="js/main.js"></script>
</body>
</html>'''

print("helpers loaded")
