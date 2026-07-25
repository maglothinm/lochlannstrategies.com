/* =============================================================================
   LOCHLANN STRATEGIES — MINIMAL INTERACTION SCRIPT
   Version 15.0

   The site remains fully usable without JavaScript. This script only refines
   the sticky header and synchronizes the native <details> mobile menu state.
   ============================================================================= */

(() => {
  "use strict";

  const header = document.querySelector("[data-site-header]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");

  const updateHeader = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  const updateMenuState = () => {
    if (!mobileMenu) return;
    const summary = mobileMenu.querySelector("summary");
    if (!summary) return;

    const isOpen = mobileMenu.hasAttribute("open");
    summary.setAttribute("aria-expanded", String(isOpen));
    summary.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
  };

  updateHeader();
  updateMenuState();

  window.addEventListener("scroll", updateHeader, { passive: true });

  if (mobileMenu) {
    mobileMenu.addEventListener("toggle", updateMenuState);

    mobileMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.removeAttribute("open");
        updateMenuState();
      });
    });

    document.addEventListener("click", (event) => {
      if (mobileMenu.open && !mobileMenu.contains(event.target)) {
        mobileMenu.removeAttribute("open");
        updateMenuState();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && mobileMenu.open) {
        mobileMenu.removeAttribute("open");
        updateMenuState();
        mobileMenu.querySelector("summary")?.focus();
      }
    });
  }
})();
