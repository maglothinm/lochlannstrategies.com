(() => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.getElementById('mobile-menu');
  const year = document.querySelector('[data-year]');

  if (year) year.textContent = String(new Date().getFullYear());

  const updateHeader = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
  };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      panel.hidden = expanded;
    });

    panel.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        panel.hidden = true;
      });
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 928) {
        toggle.setAttribute('aria-expanded', 'false');
        panel.hidden = true;
      }
    });
  }
})();
