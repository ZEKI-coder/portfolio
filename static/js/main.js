/* ══════════════════════════════════════════════════════
   PORTFOLIO — main.js
   ══════════════════════════════════════════════════════ */

// ── Cursor glow ──────────────────────────────────────
const glow = document.getElementById('cursorGlow');
document.addEventListener('mousemove', e => {
  glow.style.left = e.clientX + 'px';
  glow.style.top  = e.clientY + 'px';
});

// ── Navbar scroll ────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ── Burger menu ──────────────────────────────────────
const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav-links');
burger.addEventListener('click', () => navLinks.classList.toggle('open'));
navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));

// ── Reveal on scroll (IntersectionObserver) ──────────
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => io.observe(el));

// ── Skill bars animation ─────────────────────────────
const skillFills = document.querySelectorAll('.skill-fill');
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      el.style.width = el.dataset.level + '%';
      skillObserver.unobserve(el);
    }
  });
}, { threshold: 0.3 });
skillFills.forEach(el => skillObserver.observe(el));

// ── Typewriter effect ────────────────────────────────
function typeWriter(el, text, speed = 60) {
  let i = 0;
  el.textContent = '';
  const tick = () => {
    if (i < text.length) {
      el.textContent += text.charAt(i++);
      setTimeout(tick, speed);
    }
  };
  setTimeout(tick, 800); // small initial delay
}
const typedEl = document.querySelector('.typed-text');
if (typedEl) typeWriter(typedEl, typedEl.dataset.text);

// ── Contact form ─────────────────────────────────────
const form = document.getElementById('contactForm');
const status = document.getElementById('formStatus');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = form.querySelector('button[type="submit"]');
  btn.disabled = true;
  btn.textContent = 'Envoi en cours...';
  status.textContent = '';

  const payload = {
    name:    document.getElementById('fname').value,
    email:   document.getElementById('femail').value,
    message: document.getElementById('fmessage').value,
  };

  try {
    const res  = await fetch('/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    status.textContent = '✓ ' + data.message;
    status.style.color = 'var(--neon)';
    form.reset();
  } catch {
    status.textContent = '✗ Erreur — réessaie plus tard.';
    status.style.color = 'var(--red)';
  } finally {
    btn.disabled = false;
    btn.textContent = 'Envoyer le message';
  }
});

// ── Smooth active nav link highlight ─────────────────
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
  });
  navAnchors.forEach(a => {
    a.style.color = a.getAttribute('href') === '#' + current ? 'var(--neon)' : '';
  });
}, { passive: true });