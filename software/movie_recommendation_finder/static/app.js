function isPick(node) {
  return Boolean(node && node.closest(".ticket, .vibe, .slide-btn, a, input, select, textarea, button"));
}

document.querySelectorAll("[data-slider]").forEach((slider) => {
  const viewport = slider.querySelector(".slide-viewport");
  if (!viewport) return;

  const step = () => Math.max(120, Math.round(viewport.clientWidth * 0.55));

  slider.querySelectorAll("[data-slide]").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      viewport.scrollBy({ left: Number(button.getAttribute("data-slide")) * step(), behavior: "smooth" });
    });
  });

  viewport.addEventListener(
    "wheel",
    (event) => {
      if (Math.abs(event.deltaY) < Math.abs(event.deltaX) && event.deltaX) return;
      if (event.deltaY === 0) return;
      viewport.scrollLeft += event.deltaY;
      event.preventDefault();
    },
    { passive: false },
  );

  let drag = null;
  viewport.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) return;
    if (isPick(event.target)) return;
    drag = {
      id: event.pointerId,
      x: event.clientX,
      left: viewport.scrollLeft,
      moved: false,
    };
  });
  viewport.addEventListener("pointermove", (event) => {
    if (!drag || event.pointerId !== drag.id) return;
    const delta = event.clientX - drag.x;
    if (Math.abs(delta) < 12 && !drag.moved) return;
    if (!drag.moved) {
      drag.moved = true;
      viewport.setPointerCapture(event.pointerId);
    }
    viewport.scrollLeft = drag.left - delta;
  });
  const stop = () => {
    drag = null;
  };
  viewport.addEventListener("pointerup", stop);
  viewport.addEventListener("pointercancel", stop);
});

const likedInput = document.querySelector("#liked-film");
const filmSearch = document.querySelector("#film-search");
const cards = document.querySelectorAll(".ticket");

function selectTicket(card) {
  if (!likedInput || !card) return;
  likedInput.value = card.getAttribute("data-title") || "";
  cards.forEach((other) => other.classList.toggle("is-on", other === card));
}

cards.forEach((card) => {
  card.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    selectTicket(card);
  });
});

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

const moodInput = document.querySelector("#picked-mood");
const vibes = document.querySelectorAll(".vibe");
vibes.forEach((chip) => {
  chip.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    if (!moodInput) return;
    moodInput.value = chip.getAttribute("data-mood") || "";
    vibes.forEach((other) => other.classList.toggle("is-on", other === chip));
  });
});
