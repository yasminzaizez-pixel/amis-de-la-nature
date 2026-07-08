/* =========================================================
   LES AMIS DE LA NATURE — main.js
   ========================================================= */
document.addEventListener('DOMContentLoaded', () => {

  const hasGSAP = typeof gsap !== 'undefined';
  if (hasGSAP) gsap.registerPlugin(ScrollTrigger);

  /* ---------- NAV : fond au scroll + toggle mobile + lien actif ---------- */
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  const onScrollNav = () => {
    if (window.scrollY > 60) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  };
  onScrollNav();
  window.addEventListener('scroll', onScrollNav, { passive: true });

  if (toggle) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));
  }

  const current = document.body.dataset.page;
  document.querySelectorAll('.nav-links a[data-page]').forEach(a => {
    if (a.dataset.page === current) a.classList.add('active');
  });

  /* ---------- INTRO CINÉMATIQUE (page d'accueil uniquement) ---------- */
  const intro = document.getElementById('intro');
  if (intro) {
    document.body.classList.add('intro-active');
    const skipBtn = intro.querySelector('.skip-intro');
    const vines = intro.querySelectorAll('.intro-vine');
    const logo = intro.querySelector('#intro-logo');
    const tagline = intro.querySelector('.intro-tagline');

    const finishIntro = () => {
      if (hasGSAP) gsap.killTweensOf([vines, logo, tagline]);
      intro.style.transition = 'opacity .6s ease';
      intro.style.opacity = '0';
      document.body.classList.remove('intro-active');
      setTimeout(() => intro.remove(), 650);
    };

    if (skipBtn) skipBtn.addEventListener('click', finishIntro);

    if (hasGSAP) {
      const tl = gsap.timeline({ delay: .2, onComplete: () => setTimeout(finishIntro, 1100) });
      tl.to(vines, { opacity: 1, duration: 1.1, stagger: .15, ease: 'power2.out' })
        .fromTo(logo, { scale: .3, opacity: 0, rotate: -8 }, { scale: 1, opacity: 1, rotate: 0, duration: 1.1, ease: 'back.out(1.6)' }, '-=.5')
        .to(tagline, { opacity: 1, y: 0, duration: .9, ease: 'power2.out' }, '-=.3');
    } else {
      finishIntro();
    }
  }

  /* ---------- VIGNE DE PROGRESSION (fixed left rail) ---------- */
  const railPath = document.getElementById('rail-progress');
  if (railPath) {
    const railLength = railPath.getTotalLength();
    railPath.style.strokeDasharray = railLength;
    railPath.style.strokeDashoffset = railLength;
    const updateRail = () => {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const pct = scrollable > 0 ? window.scrollY / scrollable : 0;
      railPath.style.strokeDashoffset = railLength * (1 - pct);
    };
    updateRail();
    window.addEventListener('scroll', updateRail, { passive: true });
    window.addEventListener('resize', updateRail);
  }

  /* ---------- FEUILLES FLOTTANTES ambiantes ---------- */
  const leafField = document.getElementById('leaf-field');
  if (leafField && window.innerWidth > 700) {
    const leafSVG = `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C7 2 3 6 3 11c0 6 5 9 9 11 4-2 9-5 9-11 0-5-4-9-9-9zm0 3c1.5 3 1.5 9 0 13"/></svg>`;
    let count = 0;
    const spawnLeaf = () => {
      if (count > 14) return;
      const leaf = document.createElement('div');
      leaf.className = 'floating-leaf';
      leaf.innerHTML = leafSVG;
      const fromLeft = Math.random() > 0.5;
      const startX = fromLeft ? -20 : window.innerWidth + 20;
      const y = Math.random() * window.innerHeight;
      leaf.style.left = startX + 'px';
      leaf.style.top = y + 'px';
      leafField.appendChild(leaf);
      count++;
      if (hasGSAP) {
        gsap.to(leaf, {
          x: fromLeft ? window.innerWidth * (0.3 + Math.random() * 0.4) : -window.innerWidth * (0.3 + Math.random() * 0.4),
          y: '+=' + (Math.random() * 160 - 80),
          rotate: Math.random() * 360,
          opacity: .55,
          duration: 6 + Math.random() * 4,
          ease: 'sine.inOut',
          onComplete: () => { leaf.remove(); count--; }
        });
        gsap.to(leaf, { opacity: 0, duration: 2, delay: 6 + Math.random() * 2 });
      } else {
        leaf.remove(); count--;
      }
    };
    setInterval(spawnLeaf, 1800);
  }

  /* ---------- REVEAL générique au scroll ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); revealObserver.unobserve(e.target); } });
  }, { threshold: .15 });
  revealEls.forEach(el => revealObserver.observe(el));

  /* ---------- CARTES SERVICES : poussent comme des plants ---------- */
  const cards = document.querySelectorAll('.service-card');
  const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('grown'); cardObserver.unobserve(e.target); } });
  }, { threshold: .2 });
  cards.forEach(c => cardObserver.observe(c));

  /* ---------- Indicateur de scroll (arrosoir) ---------- */
  const scrollInd = document.querySelector('.scroll-indicator');
  if (scrollInd) {
    window.addEventListener('scroll', () => {
      scrollInd.classList.toggle('show', window.scrollY > 400);
    }, { passive: true });
    scrollInd.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ---------- CATALOGUE : filtres ---------- */
  const chips = document.querySelectorAll('.filter-chip');
  const speciesCards = document.querySelectorAll('.species-card');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      chips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      const type = chip.dataset.filter;
      speciesCards.forEach(card => {
        card.classList.toggle('hide', type !== 'tous' && card.dataset.type !== type);
      });
    });
  });

  /* ---------- FORMULAIRE CONTACT (front-end uniquement) ---------- */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const note = contactForm.querySelector('.form-note');
      note.textContent = "Merci ! Votre message a bien été préparé — votre application mail va s'ouvrir pour l'envoi.";
      note.classList.add('show');
      const name = contactForm.querySelector('#name').value;
      const email = contactForm.querySelector('#email').value;
      const msg = contactForm.querySelector('#message').value;
      const subject = encodeURIComponent('Contact depuis le site — ' + name);
      const body = encodeURIComponent(msg + '\n\n— ' + name + ' (' + email + ')');
      window.location.href = `mailto:paulbernadette@gmail.com?subject=${subject}&body=${body}`;
    });
  }

});
