// Keep native al-folio publication toggles, with keyboard and screen-reader support.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".publications .links").forEach((links, index) => {
    ["abstract", "bibtex", "award"].forEach((kind) => {
      const trigger = links.querySelector(`a.${kind}`);
      const panel = links.parentElement.querySelector(`div.${kind}.hidden`);
      if (!trigger || !panel) return;
      panel.id = `${kind}-panel-${index}`;
      trigger.tabIndex = 0;
      trigger.setAttribute("aria-controls", panel.id);
      trigger.setAttribute("aria-expanded", "false");
      if (kind === "abstract") trigger.textContent = "Abstract";
      if (kind === "bibtex") trigger.textContent = "BibTeX";
      trigger.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          trigger.click();
        }
      });
      const syncPanel = () => {
        const open = panel.classList.contains("open");
        trigger.setAttribute("aria-expanded", String(open));
        panel.setAttribute("aria-hidden", String(!open));
        panel.inert = !open;
      };
      syncPanel();
      new MutationObserver(syncPanel).observe(panel, { attributes: true, attributeFilter: ["class"] });
    });
  });

  const pdfLink = document.querySelector('.post-title a[href$="/cv.pdf"]');
  if (pdfLink) {
    pdfLink.setAttribute("aria-label", "Download CV as PDF");
    pdfLink.title = "Download CV as PDF";
  }
});
