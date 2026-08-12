/* Lochlann Strategies v17.2.0 — navigation, reveal, progress, and hero motion */
(() => {
  "use strict";

  const doc = document;
  const body = doc.body;
  const header = doc.querySelector("[data-site-header]");
  const progress = doc.querySelector("[data-scroll-progress]");
  const menuToggle = doc.querySelector("[data-menu-toggle]");
  const mobileMenu = doc.querySelector("[data-mobile-menu]");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const inertRegions = [
    doc.querySelector(".skip-link"),
    doc.querySelector("main"),
    doc.querySelector("footer")
  ].filter(Boolean);

  let scrollFrame = 0;
  let menuCloseTimer = 0;
  let lastFocused = null;

  const focusableSelector = [
    "a[href]",
    "button:not([disabled])",
    "input:not([disabled])",
    "select:not([disabled])",
    "textarea:not([disabled])",
    "[tabindex]:not([tabindex='-1'])"
  ].join(",");

  function updateScrollState() {
    scrollFrame = 0;

    const y = window.scrollY || doc.documentElement.scrollTop || 0;
    if (header) {
      header.classList.toggle("is-scrolled", y > 18);
    }

    if (progress) {
      const root = doc.documentElement;
      const available = Math.max(1, root.scrollHeight - window.innerHeight);
      const percent = Math.min(100, Math.max(0, (y / available) * 100));
      progress.style.setProperty("--scroll-progress", `${percent}%`);
    }
  }

  function requestScrollUpdate() {
    if (!scrollFrame) {
      scrollFrame = window.requestAnimationFrame(updateScrollState);
    }
  }

  function setBackgroundInert(isInert) {
    inertRegions.forEach((region) => {
      region.toggleAttribute("inert", isInert);
    });
  }

  function menuFocusable() {
    if (!mobileMenu) return [];

    const drawerItems = Array.from(mobileMenu.querySelectorAll(focusableSelector))
      .filter((element) => !element.hasAttribute("hidden"));

    return menuToggle ? [menuToggle, ...drawerItems] : drawerItems;
  }

  function openMenu() {
    if (!menuToggle || !mobileMenu || menuToggle.getAttribute("aria-expanded") === "true") {
      return;
    }

    window.clearTimeout(menuCloseTimer);
    lastFocused = doc.activeElement;
    mobileMenu.hidden = false;
    body.classList.add("menu-open");
    setBackgroundInert(true);
    menuToggle.setAttribute("aria-expanded", "true");
    menuToggle.setAttribute("aria-label", "Close navigation");

    window.requestAnimationFrame(() => {
      mobileMenu.classList.add("is-open");
      const firstLink = mobileMenu.querySelector(focusableSelector);
      if (firstLink) firstLink.focus({ preventScroll: true });
    });
  }

  function closeMenu({ restoreFocus = true, immediate = false } = {}) {
    if (!menuToggle || !mobileMenu || menuToggle.getAttribute("aria-expanded") !== "true") {
      return;
    }

    window.clearTimeout(menuCloseTimer);
    mobileMenu.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");

    const finish = () => {
      mobileMenu.hidden = true;
      body.classList.remove("menu-open");
      setBackgroundInert(false);
      if (restoreFocus && lastFocused instanceof HTMLElement) {
        lastFocused.focus({ preventScroll: true });
      }
    };

    if (immediate || reducedMotion.matches) {
      finish();
    } else {
      menuCloseTimer = window.setTimeout(finish, 280);
    }
  }

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => {
      const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
      if (isOpen) closeMenu();
      else openMenu();
    });

    mobileMenu.addEventListener("click", (event) => {
      const link = event.target.closest("a");
      if (link) closeMenu({ restoreFocus: false });
    });

    doc.addEventListener("keydown", (event) => {
      if (menuToggle.getAttribute("aria-expanded") !== "true") return;

      if (event.key === "Escape") {
        event.preventDefault();
        closeMenu();
        return;
      }

      if (event.key !== "Tab") return;

      const focusable = menuFocusable();
      if (!focusable.length) return;

      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (event.shiftKey && doc.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && doc.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 960) {
        closeMenu({ restoreFocus: false, immediate: true });
      }
    });
  }

  const revealItems = Array.from(doc.querySelectorAll("[data-reveal]"));
  if (revealItems.length) {
    if (!("IntersectionObserver" in window) || reducedMotion.matches) {
      revealItems.forEach((item) => item.classList.add("is-visible"));
    } else {
      const observer = new IntersectionObserver(
        (entries, activeObserver) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            activeObserver.unobserve(entry.target);
          });
        },
        {
          threshold: 0.12,
          rootMargin: "0px 0px -8% 0px"
        }
      );

      revealItems.forEach((item) => observer.observe(item));
    }
  }

  const heroVisual = doc.querySelector("[data-hero-visual]");
  const precisePointer = window.matchMedia("(pointer: fine)");

  if (heroVisual && precisePointer.matches && !reducedMotion.matches) {
    heroVisual.addEventListener("pointermove", (event) => {
      const rect = heroVisual.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width - 0.5) * -10;
      const y = ((event.clientY - rect.top) / rect.height - 0.5) * -8;
      heroVisual.style.setProperty("--pointer-x", `${x}px`);
      heroVisual.style.setProperty("--pointer-y", `${y}px`);
    });

    heroVisual.addEventListener("pointerleave", () => {
      heroVisual.style.setProperty("--pointer-x", "0px");
      heroVisual.style.setProperty("--pointer-y", "0px");
    });
  }

  doc.querySelectorAll("[data-current-year]").forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });

  window.addEventListener("scroll", requestScrollUpdate, { passive: true });
  window.addEventListener("resize", requestScrollUpdate, { passive: true });
  updateScrollState();
})();
