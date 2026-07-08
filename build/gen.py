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

def _tree(cx, base_y, s, kind, color, opacity, delay):
    """Un arbre stylisé (silhouette), utilisé pour composer la forêt d'intro."""
    style = f'transform-origin:{cx}px {base_y}px; transition-delay:{delay:.2f}s; opacity:{opacity}'
    if kind == "acacia":
        # silhouette à couronne plate — l'arbre emblématique de la savane
        trunk = f'<path d="M{cx} {base_y} C {cx-2*s} {base_y-14*s} {cx+3*s} {base_y-22*s} {cx} {base_y-34*s}" stroke="{color}" stroke-width="{2.6*s}" fill="none"/>'
        canopy = (f'<ellipse cx="{cx}" cy="{base_y-38*s}" rx="{34*s}" ry="{7.5*s}" fill="{color}"/>'
                  f'<ellipse cx="{cx-14*s}" cy="{base_y-33*s}" rx="{16*s}" ry="{5.5*s}" fill="{color}" opacity=".85"/>'
                  f'<ellipse cx="{cx+15*s}" cy="{base_y-33*s}" rx="{15*s}" ry="{5*s}" fill="{color}" opacity=".85"/>')
        inner = trunk + canopy
    elif kind == "baobab":
        trunk = f'<path d="M{cx-6*s} {base_y} C {cx-9*s} {base_y-30*s} {cx-4*s} {base_y-40*s} {cx} {base_y-46*s} C {cx+4*s} {base_y-40*s} {cx+9*s} {base_y-30*s} {cx+6*s} {base_y}z" fill="{color}"/>'
        canopy = (f'<ellipse cx="{cx}" cy="{base_y-56*s}" rx="{20*s}" ry="{15*s}" fill="{color}" opacity=".9"/>'
                  f'<ellipse cx="{cx-13*s}" cy="{base_y-50*s}" rx="{11*s}" ry="{9*s}" fill="{color}" opacity=".8"/>'
                  f'<ellipse cx="{cx+14*s}" cy="{base_y-50*s}" rx="{12*s}" ry="{9*s}" fill="{color}" opacity=".8"/>')
        inner = trunk + canopy
    else:  # "round" — canopée arrondie, écho du logo
        trunk = f'<rect x="{cx-2*s}" y="{base_y-20*s}" width="{4*s}" height="{20*s}" fill="{color}"/>'
        canopy = (f'<ellipse cx="{cx}" cy="{base_y-42*s}" rx="{16*s}" ry="{20*s}" fill="{color}"/>'
                  f'<ellipse cx="{cx-10*s}" cy="{base_y-30*s}" rx="{11*s}" ry="{13*s}" fill="{color}" opacity=".9"/>'
                  f'<ellipse cx="{cx+10*s}" cy="{base_y-30*s}" rx="{11*s}" ry="{13*s}" fill="{color}" opacity=".9"/>')
        inner = trunk + canopy
    return f'<g class="tree" style="{style}">{inner}</g>'

def forest_scene():
    """Scène de forêt pour l'ouverture : plusieurs plans d'arbres qui poussent en cascade, dense et immersive."""
    back = [(20,1.3,"acacia"),(160,1.1,"round"),(300,1.5,"acacia"),(460,1.2,"round"),
            (620,1.4,"baobab"),(780,1.15,"acacia"),(940,1.35,"round"),(1100,1.25,"acacia"),
            (1260,1.45,"round"),(1420,1.2,"acacia"),(1560,1.3,"round"),(1700,1.15,"acacia"),
            (1830,1.35,"round")]
    mid  = [(80,2.0,"round"),(260,2.4,"acacia"),(480,1.9,"baobab"),(720,2.2,"acacia"),
            (940,2.5,"round"),(1160,2.0,"baobab"),(1380,2.3,"acacia"),(1560,1.95,"round"),
            (1750,2.2,"acacia")]
    front= [(0,3.4,"round"),(200,3.9,"acacia"),(430,3.2,"baobab"),(720,3.7,"round"),
            (1000,3.0,"acacia"),(1260,3.8,"baobab"),(1480,3.3,"round"),(1700,3.6,"acacia"),
            (1860,3.1,"round")]

    def layer(trees, base_y, color, opacity, start_delay, step, klass):
        out = f'<svg class="forest-layer {klass}" viewBox="0 0 1800 900" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg">'
        for i,(x,s,kind) in enumerate(trees):
            out += _tree(x, base_y, s, kind, color, opacity, start_delay + i*step)
        out += '</svg>'
        return out

    return f'''<div id="intro-forest" aria-hidden="true">
    {layer(back, 830, "var(--moss-light)", .55, 0.0, .04, "back")}
    {layer(mid, 860, "var(--moss)", .8, .22, .05, "mid")}
    {layer(front, 900, "var(--forest-deep)", .97, .48, .06, "front")}
    <div class="forest-ground"></div>
    <div class="forest-vignette"></div>
  </div>'''

def scroll_plant():
    """La plante-témoin : grandit avec la progression de la page, rétrécit si l'on remonte."""
    return '''<div id="growth-rail" aria-hidden="true">
    <svg viewBox="0 0 34 800" preserveAspectRatio="none">
      <path class="rail-stem" d="M17 800 C24 700 10 600 20 500 C28 420 8 340 20 260 C28 180 10 100 17 0"/>
      <path id="rail-progress" d="M17 800 C24 700 10 600 20 500 C28 420 8 340 20 260 C28 180 10 100 17 0" fill="none" stroke="#A7C25C" stroke-width="3"/>
      <g class="rail-leaf" data-at="0.12" style="transform-origin:20px 620px;"><ellipse cx="20" cy="620" rx="11" ry="5.5" fill="#A7C25C" transform="rotate(28 20 620)"/></g>
      <g class="rail-leaf" data-at="0.22" style="transform-origin:14px 560px;"><ellipse cx="14" cy="560" rx="10" ry="5" fill="#8FB868" transform="rotate(-30 14 560)"/></g>
      <g class="rail-leaf" data-at="0.35" style="transform-origin:24px 470px;"><ellipse cx="24" cy="470" rx="12" ry="6" fill="#A7C25C" transform="rotate(24 24 470)"/></g>
      <g class="rail-leaf" data-at="0.48" style="transform-origin:10px 380px;"><ellipse cx="10" cy="380" rx="11" ry="5.5" fill="#8FB868" transform="rotate(-26 10 380)"/></g>
      <g class="rail-leaf" data-at="0.6" style="transform-origin:26px 290px;"><ellipse cx="26" cy="290" rx="12" ry="6" fill="#A7C25C" transform="rotate(30 26 290)"/></g>
      <g class="rail-leaf" data-at="0.72" style="transform-origin:8px 190px;"><ellipse cx="8" cy="190" rx="11" ry="5.5" fill="#8FB868" transform="rotate(-24 8 190)"/></g>
      <g class="rail-leaf" data-at="0.84" style="transform-origin:24px 100px;"><ellipse cx="24" cy="100" rx="12" ry="6" fill="#A7C25C" transform="rotate(26 24 100)"/></g>
      <g class="rail-flower" data-at="0.94" style="transform-origin:17px 22px;">
        <g fill="#D89467">
          <ellipse cx="17" cy="10" rx="6" ry="8"/><ellipse cx="17" cy="10" rx="6" ry="8" transform="rotate(72 17 10)"/>
          <ellipse cx="17" cy="10" rx="6" ry="8" transform="rotate(144 17 10)"/><ellipse cx="17" cy="10" rx="6" ry="8" transform="rotate(216 17 10)"/>
          <ellipse cx="17" cy="10" rx="6" ry="8" transform="rotate(288 17 10)"/>
        </g>
        <circle cx="17" cy="10" r="4" fill="#EEE6D3"/>
      </g>
    </svg>
  </div>'''

# alias conservé pour compatibilité
def growth_rail():
    return scroll_plant()

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
