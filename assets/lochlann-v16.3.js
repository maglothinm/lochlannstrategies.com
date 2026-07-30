(() => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.getElementById('mobile-menu');
  const year = document.querySelector('[data-year]');

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  const updateHeader = () => {
    if (header) {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    }
  };

  const closeMenu = ({ returnFocus = false } = {}) => {
    if (!toggle || !panel) {
      return;
    }

    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
    panel.hidden = true;
    document.body.classList.remove('menu-open');

    if (returnFocus) {
      toggle.focus();
    }
  };

  const openMenu = () => {
    if (!toggle || !panel) {
      return;
    }

    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close navigation');
    panel.hidden = false;
    document.body.classList.add('menu-open');

    const firstLink = panel.querySelector('a');
    if (firstLink) {
      firstLink.focus({ preventScroll: true });
    }
  };

  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      if (expanded) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    panel.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => closeMenu());
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu({ returnFocus: true });
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 928) {
        closeMenu();
      }
    });
  }
})();
