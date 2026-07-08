import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import (icon_logo, badge_logo, forest_scene, growth_rail,
                  watering_can_icon, header, footer, scroll_indicator, leaf_field,
                  head, scripts)

OUT = "/home/claude/amis-nature"

def img(id_, w=1200, q=75):
    return f"https://images.unsplash.com/photo-{id_}?w={w}&q={q}&auto=format&fit=crop"

IMG = {
    "hero_home": img("1646504550926-15d1b5ac500f", 1800),
    "hero_services": img("1750762286053-28632f48e717", 1800),
    "hero_pepiniere": img("1776437210658-e490b4b4e586", 1800),
    "hero_realisations": img("1672850950522-334eb1259412", 1800),
    "hero_catalogue": img("1750762286044-d799678baf6d", 1800),
    "hero_contact": img("1639003332116-a2429ce6059b", 1800),
    "origin_photo": None,  # replaced with the sign photo
    "wheelbarrow": img("1734079692160-fcbe4be6ab96"),
    "shelf_plants": img("1683994851774-6e9642fb8a95"),
    "potted_table": img("1683994841256-245ab23fdc3e"),
    "pine": img("1658947156963-e644e61b8826"),
    "branch": img("1658399470598-e0b70461ed86"),
    "leaves_closeup": img("1654106620398-a6963c1df20f"),
    "indoor_plants": img("1762506169608-c0b10fe36b0a"),
    "flowers_closeup": img("1656909245926-3638866cf179"),
    "flowers_group": img("1658932409734-41551e7e4263"),
    "yellow_flower": img("1660540055938-1e92201bacc4"),
    "manicured_garden": img("1770234848941-8bd67b57d700"),
    "rocks_garden": img("1713371765638-8cf84d350b74"),
    "stone_steps": img("1758414335865-17baa986b85b"),
    "purple_yellow": img("1777269390807-b863b29845fe"),
}

SERVICE_ICONS = {
    "plants": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21V10M12 10C12 6 9 4 5 4c0 4 2 7 7 6zM12 10c0-4 3-6 7-6 0 4-2 7-7 6z"/></svg>',
    "leaf-hand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20c8 0 14-6 15-15-8 1-14 6-15 15zM4 20c1-4 3-6 6-8"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3c4 5 7 8.5 7 12a7 7 0 1 1-14 0c0-3.5 3-7 7-12z"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 5c3-1 6-1 8 0v15c-2-1-5-1-8 0zM20 5c-3-1-6-1-8 0v15c2-1 5-1 8 0z"/></svg>',
    "megaphone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 10v4l4 1 9 4V5L7 9z"/><path d="M16 9v6"/></svg>',
    "sprout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21V13M12 13C7 13 5 10 5 6c5 0 7 3 7 7zM12 13c0-4 2-7 7-7 0 4-2 7-7 7z"/></svg>',
}

SERVICES = [
    ("plants", "Production de Plants", "Pépinière de plants forestiers, fruitiers et ornementaux, du semis à la mise en terre — adaptés au climat sahélien."),
    ("leaf-hand", "Aménagement et Entretien des Espaces Verts", "Conception, plantation et entretien durable de jardins, parcs et espaces publics ou privés."),
    ("drop", "Assainissement", "Interventions de nettoyage, gestion des déchets verts et amélioration du cadre de vie."),
    ("book", "Formation - Conseil", "Accompagnement technique et formations pratiques en horticulture et gestion des espaces verts."),
    ("megaphone", "Vulgarisation - Sensibilisation", "Actions de sensibilisation en protection de l'environnement auprès des communautés et écoles."),
    ("sprout", "Maraîchage", "Appui à la production maraîchère : techniques culturales, semences et suivi des parcelles."),
]

SPECIES = [
    ("Manguier", "arbre", "Mangifera indica", IMG["pine"]),
    ("Neem", "arbre", "Azadirachta indica", IMG["branch"]),
    ("Baobab", "arbre", "Adansonia digitata", IMG["hero_home"]),
    ("Hibiscus", "arbuste", "Hibiscus rosa-sinensis", IMG["yellow_flower"]),
    ("Bougainvillier", "arbuste", "Bougainvillea spectabilis", IMG["purple_yellow"]),
    ("Rosier du désert", "arbuste", "Adenium obesum", IMG["flowers_closeup"]),
    ("Basilic", "aromatique", "Ocimum basilicum", IMG["leaves_closeup"]),
    ("Citronnelle", "aromatique", "Cymbopogon citratus", IMG["indoor_plants"]),
    ("Zinnia", "fleur", "Zinnia elegans", IMG["flowers_group"]),
    ("Pourpier", "fleur", "Portulaca grandiflora", IMG["stone_steps"]),
]

def reveal(html, cls=""):
    return f'<div class="reveal {cls}">{html}</div>'

# ============================================================
# PAGE : INDEX (ACCUEIL)
# ============================================================
def build_index():
    body = head("Accueil", "Pépinière, aménagement paysager et sensibilisation environnementale — Les Amis de la Nature, Bamako.", "accueil")
    body += f'''
{leaf_field()}
{growth_rail()}

<div id="intro">
  <button class="skip-intro">Passer</button>
  {forest_scene()}
  <div id="intro-logo" style="color:#EEE6D3; width:min(62vw,380px);">{badge_logo("intrologo")}</div>
  <p class="intro-tagline">« Un peuple sans forêt est un peuple qui meurt »</p>
</div>

{header("navlogo")}

<section class="hero" style="background-image:url('{IMG["hero_home"]}');">
  <div class="hero-inner">
    <span class="eyebrow">Bamako, Mali</span>
    <h1>Tous pour l'arbre,<br>l'arbre pour la vie.</h1>
    <p class="lead">Pépinière, aménagement d'espaces verts et sensibilisation environnementale — nous faisons pousser des projets qui durent.</p>
    <div class="hero-cta">
      <a href="contact.html" class="btn btn-primary">Nous contacter</a>
      <a href="services.html" class="btn btn-outline">Découvrir nos services</a>
    </div>
  </div>
</section>

<div class="quote-block">
  <blockquote>« Un peuple sans forêt<br>est un peuple qui meurt »</blockquote>
  <cite>Les Amis de la Nature</cite>
</div>

<section class="section-sand vine-anchor" style="--vine-svg:none;">
  <div class="wrap">
    {reveal('<span class="eyebrow">Ce que nous faisons</span><h2 style="margin-top:.4em;">Six métiers, une même racine</h2>')}
    <div class="services-grid" style="margin-top:2.4em;">
'''
    for icon, title, desc in SERVICES:
        body += f'''      <div class="service-card">
        <div class="service-icon">{SERVICE_ICONS[icon]}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>
'''
    body += f'''    </div>
    <div style="margin-top:3em; text-align:center;">
      <a href="services.html" class="btn btn-outline dark">Voir tous les services</a>
    </div>
  </div>
</section>

<section class="section-moss">
  <div class="wrap origin-split">
    {reveal(f'<img src="assets/panneau-origine.jpg" alt="Panneau Les Amis de la Nature" loading="lazy">')}
    <div>
      {reveal('<span class="eyebrow">Notre origine</span><h2 style="color:var(--cream); margin-top:.4em;">Une petite pépinière, une grande conviction</h2><p style="color:var(--sand); margin-top:1em;">Depuis notre panneau planté au bord de la route jusqu’à aujourd’hui, notre conviction n’a pas changé : chaque arbre planté est un pas vers un Mali plus vert. Nous accompagnons familles, entreprises et collectivités dans la production de plants, l’aménagement paysager et la sensibilisation à la protection de l’environnement.</p><a href="pepiniere.html" class="btn btn-outline" style="margin-top:1.4em; border-color:var(--lime); color:var(--lime);">Visiter la pépinière</a>')}
    </div>
  </div>
</section>

<section class="section-sand-deep">
  <div class="wrap" style="text-align:center;">
    {reveal('<span class="eyebrow" style="justify-content:center;">Nos réalisations</span><h2 style="margin-top:.4em;">Des projets qui prennent racine</h2>')}
  </div>
  <div class="wrap gallery-grid" style="margin-top:2.6em;">
    <div class="gallery-item"><img src="{IMG['manicured_garden']}" alt="Jardin aménagé" loading="lazy"><div class="gallery-overlay"><span class="tag">Aménagement</span><h4>Jardin résidentiel, Bamako</h4></div></div>
    <div class="gallery-item"><img src="{IMG['rocks_garden']}" alt="Espace vert paysager" loading="lazy"><div class="gallery-overlay"><span class="tag">Paysagisme</span><h4>Espace vert d'entreprise</h4></div></div>
    <div class="gallery-item"><img src="{IMG['stone_steps']}" alt="Allée fleurie" loading="lazy"><div class="gallery-overlay"><span class="tag">Aménagement</span><h4>Allée et massifs fleuris</h4></div></div>
  </div>
  <div style="text-align:center; margin-top:2.6em;">
    <a href="realisations.html" class="btn btn-outline dark">Voir toutes les réalisations</a>
  </div>
</section>

<section class="section-dark" style="text-align:center;">
  <div class="wrap" style="max-width:640px; margin:0 auto;">
    {reveal('<h2>Prêt à planter votre prochain projet ?</h2><p style="color:var(--sand); margin-top:1em;">Parlons de votre terrain, de votre jardin ou de votre projet d\’espace vert.</p><div style="margin-top:1.6em;"><a href="contact.html" class="btn btn-primary">Demander un devis</a></div>')}
  </div>
</section>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/index.html", "w") as f:
        f.write(body)

build_index()
print("index.html written")

# ============================================================
# PAGE : SERVICES
# ============================================================
def build_services():
    body = head("Nos Services", "Production de plants, aménagement paysager, assainissement, formation et sensibilisation — Les Amis de la Nature.", "services")
    body += f'''
{leaf_field()}
{growth_rail()}
{header("navlogo")}

<section class="hero-sub" style="background-image:url('{IMG["hero_services"]}'); background-size:cover; background-position:center; position:relative;">
  <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(15,35,24,.55), rgba(15,35,24,.85));"></div>
  <div class="wrap" style="position:relative; max-width:800px;">
    <span class="eyebrow" style="color:var(--lime-soft);">Nos services</span>
    <h1 style="color:var(--cream); font-size:clamp(2.2rem,5vw,3.6rem); margin-top:.3em;">Six métiers au service de vos espaces verts</h1>
    <p style="color:var(--sand); margin-top:1em; max-width:560px;">De la graine à l’arbre adulte, du terrain vague au jardin entretenu — nous accompagnons chaque étape.</p>
  </div>
</section>

<section class="section-sand">
  <div class="wrap">
    <div class="services-grid">
'''
    long_desc = {
        "plants": "Nous produisons des plants forestiers, fruitiers et ornementaux adaptés au climat sahélien : sélection des semences, mise en pépinière, repiquage et suivi jusqu’à la plantation définitive.",
        "leaf-hand": "Conception de jardins, parcs et espaces publics ou privés, plantation et programme d’entretien durable (taille, arrosage raisonné, fertilisation naturelle).",
        "drop": "Nettoyage de sites, gestion des déchets verts, actions de salubrité pour améliorer le cadre de vie des quartiers et des entreprises.",
        "book": "Formations pratiques en horticulture, pépinière et gestion des espaces verts, ainsi qu’un accompagnement-conseil pour vos projets d’aménagement.",
        "megaphone": "Campagnes de sensibilisation en milieu scolaire et communautaire pour la protection de l’environnement et la lutte contre la déforestation.",
        "sprout": "Appui technique aux producteurs maraîchers : choix des semences, techniques culturales adaptées, suivi agronomique des parcelles.",
    }
    for icon, title, desc in SERVICES:
        body += f'''      <div class="service-card" style="padding:2.6em 2em;">
        <div class="service-icon">{SERVICE_ICONS[icon]}</div>
        <h3>{title}</h3>
        <p>{long_desc[icon]}</p>
      </div>
'''
    body += f'''    </div>
  </div>
</section>

<section class="section-moss">
  <div class="wrap" style="display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center;">
    {reveal(f'<img src="{IMG["wheelbarrow"]}" alt="Aménagement paysager" style="border-radius:22px;" loading="lazy">')}
    <div>
      {reveal('<span class="eyebrow" style="color:var(--lime-soft);">Notre méthode</span><h2 style="color:var(--cream); margin-top:.4em;">Un accompagnement de bout en bout</h2><p style="color:var(--sand); margin-top:1em;">Diagnostic du terrain, proposition d’aménagement, mise en œuvre par nos équipes, puis suivi et entretien dans la durée. Chaque projet est pensé pour s’intégrer durablement à son environnement.</p><a href="contact.html" class="btn btn-primary" style="margin-top:1.4em;">Demander un devis</a>')}
    </div>
  </div>
</section>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/services.html", "w", encoding="utf-8") as f:
        f.write(body)

build_services()
print("services.html written")

# ============================================================
# PAGE : REALISATIONS
# ============================================================
def build_realisations():
    body = head("Nos Réalisations", "Portfolio de projets d'aménagement paysager et de pépinières réalisés par Les Amis de la Nature.", "realisations")
    projects = [
        (IMG["manicured_garden"], "Aménagement", "Jardin résidentiel — Badalabougou"),
        (IMG["rocks_garden"], "Paysagisme", "Espace vert d'entreprise — ACI 2000"),
        (IMG["stone_steps"], "Aménagement", "Allée et massifs fleuris — Hamdallaye"),
        (IMG["hero_realisations"], "Espace public", "Parc communautaire — Sotuba"),
        (IMG["wheelbarrow"], "Chantier", "Terrassement et plantation — Kalaban Coura"),
        (IMG["hero_pepiniere"], "Pépinière", "Production de plants — site Les Amis de la Nature"),
        (IMG["purple_yellow"], "Fleurissement", "Massifs et haies fleuries — Faladié"),
        (IMG["shelf_plants"], "Aménagement intérieur", "Verdissement d'un siège social — Bamako"),
    ]
    body += f'''
{leaf_field()}
{growth_rail()}
{header("navlogo")}

<section class="hero-sub" style="background-image:url('{IMG["hero_realisations"]}'); background-size:cover; background-position:center; position:relative;">
  <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(15,35,24,.5), rgba(15,35,24,.85));"></div>
  <div class="wrap" style="position:relative; max-width:800px;">
    <span class="eyebrow" style="color:var(--lime-soft);">Portfolio</span>
    <h1 style="color:var(--cream); font-size:clamp(2.2rem,5vw,3.6rem); margin-top:.3em;">Nos réalisations</h1>
    <p style="color:var(--sand); margin-top:1em; max-width:560px;">Un aperçu de nos chantiers d’aménagement paysager, de nos pépinières et de nos projets de verdissement.</p>
  </div>
</section>

<section class="section-sand">
  <div class="wrap gallery-grid">
'''
    for src, tag, title in projects:
        body += f'''    <div class="gallery-item"><img src="{src}" alt="{title}" loading="lazy"><div class="gallery-overlay"><span class="tag">{tag}</span><h4>{title}</h4></div></div>
'''
    body += f'''  </div>
</section>

<div class="quote-block">
  <blockquote>« Chaque chantier est une graine plantée pour demain »</blockquote>
  <cite>Les Amis de la Nature</cite>
</div>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/realisations.html", "w", encoding="utf-8") as f:
        f.write(body)

build_realisations()
print("realisations.html written")

# ============================================================
# PAGE : PEPINIERE
# ============================================================
def build_pepiniere():
    body = head("Pépinière", "Découvrez la pépinière Les Amis de la Nature : production de plants forestiers, fruitiers et ornementaux à Bamako.", "pepiniere")
    body += f'''
{leaf_field()}
{growth_rail()}
{header("navlogo")}

<section class="hero-sub" style="background-image:url('{IMG["hero_pepiniere"]}'); background-size:cover; background-position:center; position:relative;">
  <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(15,35,24,.5), rgba(15,35,24,.85));"></div>
  <div class="wrap" style="position:relative; max-width:800px;">
    <span class="eyebrow" style="color:var(--lime-soft);">Notre pépinière</span>
    <h1 style="color:var(--cream); font-size:clamp(2.2rem,5vw,3.6rem); margin-top:.3em;">Là où tout commence</h1>
    <p style="color:var(--sand); margin-top:1em; max-width:560px;">Une pépinière à taille humaine, pensée pour produire des plants robustes et bien adaptés au climat malien.</p>
  </div>
</section>

<section class="section-sand">
  <div class="wrap" style="display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center;">
    {reveal(f'<img src="{IMG["shelf_plants"]}" alt="Plants en pépinière" style="border-radius:22px;" loading="lazy">')}
    <div>
      {reveal('<span class="eyebrow">Notre process</span><h2 style="margin-top:.4em;">Du semis à la mise en terre</h2><p style="margin-top:1em; color:var(--moss);">Sélection rigoureuse des semences, germination sous ombrière, repiquage en sachets, puis endurcissement progressif avant la plantation définitive. Nous suivons chaque lot jusqu’à sa mise en terre chez le client.</p>')}
    </div>
  </div>
</section>

<section class="section-moss">
  <div class="wrap">
    {reveal('<span class="eyebrow" style="color:var(--lime-soft);">Nos plants disponibles</span><h2 style="color:var(--cream); margin-top:.4em;">Un choix adapté à chaque projet</h2>')}
    <div class="services-grid" style="margin-top:2.4em;">
      <div class="service-card"><h3>Arbres forestiers</h3><p>Neem, Eucalyptus, Baobab, Acacia — pour le reboisement et l’ombrage.</p></div>
      <div class="service-card"><h3>Arbres fruitiers</h3><p>Manguier, Citronnier, Goyavier, Papayer — pour les vergers familiaux.</p></div>
      <div class="service-card"><h3>Arbustes ornementaux</h3><p>Hibiscus, Bougainvillier, Rosier du désert — pour vos haies et massifs.</p></div>
      <div class="service-card"><h3>Plants maraîchers</h3><p>Semis et plants pour la production maraîchère de saison.</p></div>
    </div>
    <div style="text-align:center; margin-top:2.8em;">
      <a href="catalogue.html" class="btn btn-primary">Voir le catalogue complet</a>
    </div>
  </div>
</section>

<section class="section-sand-deep">
  <div class="wrap" style="text-align:center; max-width:640px;">
    {reveal('<h2>Envie de visiter la pépinière ?</h2><p style="margin-top:1em; color:var(--moss);">Nous accueillons volontiers particuliers, écoles et entreprises pour découvrir nos plants et discuter de vos besoins.</p><div style="margin-top:1.6em;"><a href="contact.html" class="btn btn-outline dark">Planifier une visite</a></div>')}
  </div>
</section>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/pepiniere.html", "w", encoding="utf-8") as f:
        f.write(body)

build_pepiniere()
print("pepiniere.html written")

# ============================================================
# PAGE : CATALOGUE
# ============================================================
def build_catalogue():
    body = head("Catalogue Espèces", "Catalogue des espèces disponibles à la pépinière Les Amis de la Nature : arbres, arbustes, aromatiques et fleurs.", "catalogue")
    body += f'''
{leaf_field()}
{growth_rail()}
{header("navlogo")}

<section class="hero-sub" style="background-image:url('{IMG["hero_catalogue"]}'); background-size:cover; background-position:center; position:relative;">
  <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(15,35,24,.5), rgba(15,35,24,.85));"></div>
  <div class="wrap" style="position:relative; max-width:800px;">
    <span class="eyebrow" style="color:var(--lime-soft);">Catalogue</span>
    <h1 style="color:var(--cream); font-size:clamp(2.2rem,5vw,3.6rem); margin-top:.3em;">Nos espèces</h1>
    <p style="color:var(--sand); margin-top:1em; max-width:560px;">Parcourez notre sélection de plants disponibles à la pépinière et filtrez par type.</p>
  </div>
</section>

<section class="section-sand">
  <div class="wrap">
    <div class="filter-bar">
      <button class="filter-chip active" data-filter="tous">Tous</button>
      <button class="filter-chip" data-filter="arbre">Arbres</button>
      <button class="filter-chip" data-filter="arbuste">Arbustes</button>
      <button class="filter-chip" data-filter="aromatique">Aromatiques</button>
      <button class="filter-chip" data-filter="fleur">Fleurs</button>
    </div>
    <div class="species-grid">
'''
    for name, type_, latin, photo in SPECIES:
        body += f'''      <div class="species-card" data-type="{type_}">
        <div class="species-photo"><img src="{photo}" alt="{name}" loading="lazy"></div>
        <div class="species-body">
          <span class="species-type">{type_}</span>
          <h4>{name}</h4>
          <p>{latin}</p>
        </div>
      </div>
'''
    body += f'''    </div>
  </div>
</section>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/catalogue.html", "w", encoding="utf-8") as f:
        f.write(body)

build_catalogue()
print("catalogue.html written")

# ============================================================
# PAGE : CONTACT
# ============================================================
def build_contact():
    body = head("Contact", "Contactez Les Amis de la Nature : pépinière, aménagement paysager et sensibilisation environnementale à Bamako.", "contact")
    phone_icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2C10 21 3 14 3 6a2 2 0 0 1 2-2z"/></svg>'
    mail_icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 5h16v14H4z"/><path d="M4 6l8 7 8-7"/></svg>'
    pin_icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>'
    body += f'''
{leaf_field()}
{growth_rail()}
{header("navlogo")}

<section class="hero-sub" style="background-image:url('{IMG["hero_contact"]}'); background-size:cover; background-position:center; position:relative;">
  <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(15,35,24,.5), rgba(15,35,24,.85));"></div>
  <div class="wrap" style="position:relative; max-width:800px;">
    <span class="eyebrow" style="color:var(--lime-soft);">Contact</span>
    <h1 style="color:var(--cream); font-size:clamp(2.2rem,5vw,3.6rem); margin-top:.3em;">Parlons de votre projet</h1>
    <p style="color:var(--sand); margin-top:1em; max-width:560px;">Une question, un devis, une visite de la pépinière ? Écrivez-nous ou appelez-nous.</p>
  </div>
</section>

<section class="section-sand">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">Nous joindre</span>
      <h2 style="margin-top:.4em; margin-bottom:1.2em;">Coordonnées</h2>
      <div class="contact-info-item">{phone_icon}<div><span style="display:block; font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:var(--moss);">Téléphone</span><a href="tel:+22320208207">20 20 82 07</a> · <a href="tel:+22366656534">66 65 65 34</a></div></div>
      <div class="contact-info-item">{mail_icon}<div><span style="display:block; font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:var(--moss);">Email</span><a href="mailto:paulbernadette@gmail.com">paulbernadette@gmail.com</a></div></div>
      <div class="contact-info-item">{pin_icon}<div><span style="display:block; font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:var(--moss);">Zone d'intervention</span><span>Bamako et environs, Mali</span></div></div>
    </div>
    <div>
      <form id="contact-form">
        <div class="field"><label for="name">Nom complet</label><input type="text" id="name" required></div>
        <div class="field"><label for="email">Email</label><input type="email" id="email" required></div>
        <div class="field"><label for="message">Votre message</label><textarea id="message" required></textarea></div>
        <button type="submit" class="btn btn-primary">Envoyer le message</button>
        <p class="form-note"></p>
      </form>
    </div>
  </div>
</section>

{footer()}
{scroll_indicator()}
{scripts()}'''
    with open(f"{OUT}/contact.html", "w", encoding="utf-8") as f:
        f.write(body)

build_contact()
print("contact.html written")
