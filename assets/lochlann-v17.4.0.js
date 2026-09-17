(() => {
  'use strict';

  const root = document.documentElement;
  const body = document.body;
  const header = document.querySelector('[data-site-header]');
  const progress = document.querySelector('[data-scroll-progress]');
  const menuButton = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  const main = document.querySelector('main');
  const footer = document.querySelector('footer');
  let lastScroll = window.scrollY;
  let menuOpen = false;
  let lastFocused = null;

  const focusableSelector = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function updateScrollState() {
    const y = window.scrollY;
    if (header) {
      header.classList.toggle('is-scrolled', y > 20);
      const goingDown = y > lastScroll && y > 160;
      header.classList.toggle('is-hidden', goingDown && !menuOpen);
    }
    if (progress) {
      const doc = document.documentElement;
      const max = Math.max(1, doc.scrollHeight - doc.clientHeight);
      progress.style.setProperty('--scroll-progress', `${Math.min(100, (y / max) * 100)}%`);
    }
    lastScroll = y;
  }

  function setBackgroundInert(value) {
    [main, footer].forEach((node) => {
      if (!node || node === menu) return;
      if ('inert' in node) node.inert = value;
      if (value) node.setAttribute('aria-hidden', 'true');
      else node.removeAttribute('aria-hidden');
    });
  }

  function closeMenu({ restoreFocus = true } = {}) {
    if (!menu || !menuButton || !menuOpen) return;
    menuOpen = false;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation');
    menuButton.classList.remove('is-open');
    menu.classList.remove('is-open');
    body.classList.remove('menu-open');
    setBackgroundInert(false);
    window.setTimeout(() => {
      if (!menuOpen) menu.hidden = true;
    }, 320);
    if (restoreFocus && lastFocused instanceof HTMLElement) lastFocused.focus();
  }

  function openMenu() {
    if (!menu || !menuButton || menuOpen) return;
    menuOpen = true;
    lastFocused = document.activeElement;
    menu.hidden = false;
    requestAnimationFrame(() => menu.classList.add('is-open'));
    menuButton.setAttribute('aria-expanded', 'true');
    menuButton.setAttribute('aria-label', 'Close navigation');
    menuButton.classList.add('is-open');
    body.classList.add('menu-open');
    setBackgroundInert(true);
    const first = menu.querySelector(focusableSelector);
    if (first instanceof HTMLElement) first.focus();
  }

  menuButton?.addEventListener('click', () => (menuOpen ? closeMenu() : openMenu()));
  menu?.addEventListener('click', (event) => {
    if (event.target instanceof Element && event.target.closest('a')) closeMenu({ restoreFocus: false });
  });

  document.addEventListener('keydown', (event) => {
    if (!menuOpen || !menu) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      closeMenu();
      return;
    }
    if (event.key !== 'Tab') return;
    const focusables = [...menu.querySelectorAll(focusableSelector)].filter((node) => node instanceof HTMLElement && !node.hasAttribute('hidden'));
    if (!focusables.length) return;
    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  const revealItems = [...document.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -5% 0px' });
    revealItems.forEach((node) => observer.observe(node));
  } else {
    revealItems.forEach((node) => node.classList.add('is-visible'));
  }

  const visual = document.querySelector('[data-hero-visual]');
  if (visual && window.matchMedia('(pointer: fine)').matches && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    visual.addEventListener('pointermove', (event) => {
      const rect = visual.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width - 0.5) * 10;
      const y = ((event.clientY - rect.top) / rect.height - 0.5) * 10;
      visual.style.setProperty('--pointer-x', `${x}px`);
      visual.style.setProperty('--pointer-y', `${y}px`);
    });
    visual.addEventListener('pointerleave', () => {
      visual.style.setProperty('--pointer-x', '0px');
      visual.style.setProperty('--pointer-y', '0px');
    });
  }

  document.querySelectorAll('[data-current-year]').forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });

  window.addEventListener('scroll', updateScrollState, { passive: true });
  window.addEventListener('resize', () => {
    if (window.matchMedia('(min-width: 901px)').matches && menuOpen) closeMenu({ restoreFocus: false });
    updateScrollState();
  }, { passive: true });
  updateScrollState();
})();
