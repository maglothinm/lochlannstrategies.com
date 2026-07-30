/* Lochlann Strategies v16.3.2 — fixed global navigation */
(() => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.getElementById('mobile-menu');
  const year = document.querySelector('[data-year]');
  let menuScrollPosition = 0;

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  const updateHeader = () => {
    if (header) {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    }
  };

  const lockPageScroll = () => {
    menuScrollPosition = window.scrollY;
    document.body.style.position = 'fixed';
    document.body.style.top = `-${menuScrollPosition}px`;
    document.body.style.right = '0';
    document.body.style.left = '0';
    document.body.style.width = '100%';
  };

  const unlockPageScroll = () => {
    const restorePosition = menuScrollPosition;
    const root = document.documentElement;
    const previousBehavior = root.style.scrollBehavior;

    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.right = '';
    document.body.style.left = '';
    document.body.style.width = '';

    root.style.scrollBehavior = 'auto';
    window.scrollTo(0, restorePosition);

    window.requestAnimationFrame(() => {
      root.style.scrollBehavior = previousBehavior;
      updateHeader();
    });
  };

  const closeMenu = ({ returnFocus = false } = {}) => {
    if (!toggle || !panel) {
      return;
    }

    const wasOpen = toggle.getAttribute('aria-expanded') === 'true';

    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
    panel.hidden = true;
    document.body.classList.remove('menu-open');

    if (wasOpen) {
      unlockPageScroll();
    }

    if (returnFocus) {
      toggle.focus();
    }
  };

  const openMenu = () => {
    if (!toggle || !panel) {
      return;
    }

    lockPageScroll();
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
