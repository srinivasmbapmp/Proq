// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navMobile = document.getElementById('navMobile');

navToggle.addEventListener('click', () => {
  const isOpen = navMobile.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

navMobile.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navMobile.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

// Footer year
document.getElementById('year').textContent = new Date().getFullYear();

// Contact form — opens the visitor's email client addressed to Business@proqconsultants.com.au.
// No network request is made; this is purely a mailto hand-off.
const form = document.getElementById('contactForm');
const formNote = document.getElementById('formNote');
const submitBtn = document.getElementById('submitBtn');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  // Honeypot: bots fill hidden fields — pretend success, submit nothing.
  const honeypot = form.querySelector('[name="bot-field"]').value;
  if (honeypot) {
    formNote.classList.remove('is-error');
    formNote.textContent = "Thanks — we'll be in touch shortly.";
    form.reset();
    return;
  }

  const data = new FormData(form);
  const name = data.get('name');
  const email = data.get('email');
  const subject = data.get('subject') || 'Website enquiry';
  const message = data.get('message');

  const mailto = `mailto:Business@proqconsultants.com.au?subject=${encodeURIComponent(
    subject
  )}&body=${encodeURIComponent(`From: ${name} (${email})\n\n${message}`)}`;

  window.location.href = mailto;
  formNote.classList.remove('is-error');
  formNote.textContent = 'Opening your email client to send this to Business@proqconsultants.com.au…';
  form.reset();
});

// Scroll-reveal animations
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
);
revealEls.forEach((el) => revealObserver.observe(el));

// Header shadow + back-to-top visibility on scroll
const header = document.getElementById('header');
const backToTop = document.getElementById('backToTop');

const onScroll = () => {
  const scrolled = window.scrollY > 12;
  header.classList.toggle('scrolled', scrolled);
  backToTop.classList.toggle('visible', window.scrollY > 500);
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();
