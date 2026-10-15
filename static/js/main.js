document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const id = link.getAttribute("href");
    const target = id && document.querySelector(id);
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

document.querySelectorAll("[data-slider]").forEach((slider) => {
  const viewport = slider.querySelector(".slide-viewport");
  if (!viewport) return;

  const step = () => Math.max(160, Math.round(viewport.clientWidth * 0.72));
  const go = (direction) => {
    viewport.scrollBy({ left: direction * step(), behavior: "smooth" });
  };

  slider.querySelectorAll("[data-slide]").forEach((button) => {
    button.addEventListener("click", () => go(Number(button.getAttribute("data-slide"))));
  });

  let drag = null;
  viewport.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) return;
    drag = { id: event.pointerId, x: event.clientX, left: viewport.scrollLeft, moved: false };
    viewport.setPointerCapture(event.pointerId);
  });
  viewport.addEventListener("pointermove", (event) => {
    if (!drag || event.pointerId !== drag.id) return;
    const delta = event.clientX - drag.x;
    if (Math.abs(delta) > 8) drag.moved = true;
    viewport.scrollLeft = drag.left - delta;
  });
  viewport.addEventListener("click", (event) => {
    if (drag && drag.moved) event.preventDefault();
  }, true);
  const stopDrag = () => {
    drag = null;
  };
  viewport.addEventListener("pointerup", stopDrag);
  viewport.addEventListener("pointercancel", stopDrag);
});

const likedInput = document.querySelector("#liked-film");
const filmSearch = document.querySelector("#film-search");
if (likedInput) {
  const cards = document.querySelectorAll(".film-card");
  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const title = card.getAttribute("data-title") || "";
      likedInput.value = title;
      if (filmSearch) filmSearch.value = title;
      cards.forEach((other) => other.classList.toggle("is-on", other === card));
      card.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    });
  });
  const current = document.querySelector(".film-card.is-on");
  if (current) {
    current.scrollIntoView({ inline: "center", block: "nearest" });
  }
  if (filmSearch) {
    filmSearch.addEventListener("input", () => {
      const needle = filmSearch.value.trim().toLowerCase();
      cards.forEach((card) => {
        const title = (card.getAttribute("data-title") || "").toLowerCase();
        const keep = !needle || !title || title.includes(needle);
        card.classList.toggle("is-hidden", !keep);
      });
    });
  }
}
