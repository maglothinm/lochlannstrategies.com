/* =============================================================================
   LOCHLANN STRATEGIES — SHARED SITE BEHAVIOR

   Progressive enhancement only:
   - sticky-header scrolled state
   - restrained reveal motion
   - copy-email control

   Navigation and all content remain usable without JavaScript.
   ============================================================================= */

"use strict";

document.documentElement.classList.add("has-js");

const siteHeader = document.querySelector("[data-site-header]");

function updateHeaderState() {
  if (!siteHeader) {
    return;
  }

  siteHeader.dataset.scrolled = window.scrollY > 12 ? "true" : "false";
}

updateHeaderState();
window.addEventListener("scroll", updateHeaderState, { passive: true });

const revealItems = document.querySelectorAll(".reveal");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (revealItems.length && "IntersectionObserver" in window && !reducedMotion) {
  const observer = new IntersectionObserver(
    (entries, revealObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.08 },
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

const copyEmailButton = document.querySelector("[data-copy-email]");

if (copyEmailButton) {
  const email = copyEmailButton.dataset.copyEmail;
  const defaultLabel = copyEmailButton.getAttribute("aria-label") || "Copy email address";

  copyEmailButton.addEventListener("click", async () => {
    if (!email) {
      return;
    }

    try {
      await navigator.clipboard.writeText(email);
      copyEmailButton.setAttribute("aria-label", "Email address copied");

      window.setTimeout(() => {
        copyEmailButton.setAttribute("aria-label", defaultLabel);
      }, 1800);
    } catch (error) {
      window.location.href = `mailto:${email}`;
    }
  });
}
