(function hangarMotion() {
  const fine = window.matchMedia("(pointer: fine)").matches;
  const bloom = document.querySelector(".bloom");
  if (bloom && fine) {
    window.addEventListener("pointermove", (event) => {
      const x = (event.clientX / window.innerWidth) * 100;
      const y = (event.clientY / window.innerHeight) * 100;
      bloom.style.setProperty("--mx", `${x}%`);
      bloom.style.setProperty("--my", `${y}%`);
    });
  }
  const plate = document.querySelector("[data-tilt]");
  if (plate && fine && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const reset = () => {
      plate.style.setProperty("--tx", "0deg");
      plate.style.setProperty("--ty", "0deg");
    };
    plate.addEventListener("pointermove", (event) => {
      const box = plate.getBoundingClientRect();
      const px = (event.clientX - box.left) / box.width;
      const py = (event.clientY - box.top) / box.height;
      plate.style.setProperty("--tx", `${((px - 0.5) * 9).toFixed(2)}deg`);
      plate.style.setProperty("--ty", `${((0.5 - py) * 9).toFixed(2)}deg`);
      plate.style.setProperty("--lx", `${(px * 100).toFixed(1)}%`);
      plate.style.setProperty("--ly", `${(py * 100).toFixed(1)}%`);
    });
    plate.addEventListener("pointerleave", reset);
  }
  const quip = document.querySelector("#bot-quip");
  const lines = [
    "unit 04 is chewing gum and sorting files",
    "I eat .jpg for breakfast and leave .bin in Other",
    "please do not unscrew my personality.dll",
    "beep. that was a joke. I cannot beep.",
    "if it is in Downloads, it is already too late",
    "running on coffee and pathlib",
  ];
  if (quip) {
    let i = Math.floor(Math.random() * lines.length);
    quip.textContent = lines[i];
    window.setInterval(() => {
      i = (i + 1) % lines.length;
      quip.textContent = lines[i];
    }, 4200);
  }
})();

(function rotateHeroSig() {
  const block = document.querySelector("#hero-sig code");
  const bank = document.querySelector("#hero-sigs");
  if (!block || !bank) return;
  let list = [];
  try {
    list = JSON.parse(bank.textContent || "[]");
  } catch {
    return;
  }
  if (!list.length) return;

  const key = "hero-sig-last";
  let last = "";
  try {
    last = sessionStorage.getItem(key) || "";
  } catch {
    last = "";
  }

  const order = list
    .map((item, index) => ({ item, sort: Math.random(), index }))
    .sort((a, b) => a.sort - b.sort)
    .map((row) => row.item);
  if (order[0] === last && order.length > 1) {
    order.push(order.shift());
  }

  let i = 0;
  const show = () => {
    block.textContent = order[i];
    try {
      sessionStorage.setItem(key, order[i]);
    } catch {
      /* private mode is fine */
    }
    i = (i + 1) % order.length;
  };
  show();
  window.setInterval(show, 5200);
})();

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const id = link.getAttribute("href");
    const target = id && document.querySelector(id);
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
