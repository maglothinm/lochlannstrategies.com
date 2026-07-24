/* =============================================================================
   LOCHLANN STRATEGIES — MINIMAL INTERACTION SCRIPT
   Version 13.0

   The site remains fully usable without JavaScript.
   ============================================================================= */

(() => {
  "use strict";

  const header = document.querySelector("[data-site-header]");
  const mobileMenu = document.querySelector(".mobile-menu");

  const updateHeader = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  if (mobileMenu) {
    mobileMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.removeAttribute("open");
      });
    });

    document.addEventListener("click", (event) => {
      if (mobileMenu.open && !mobileMenu.contains(event.target)) {
        mobileMenu.removeAttribute("open");
      }
    });
  }
})();
