// Fixed example readings for the public demo.
async function refreshDashboard() {
  const data = {
    water_temp: 78.2,
    air_temp: 74.5,
    humidity: 46.0,
    water_level_ok: true,
    heater: false,
    fan: false,
    ato: false
  };

  document.getElementById("water-temp").textContent =
    data.water_temp.toFixed(1);

  document.getElementById("air-temp").textContent =
    data.air_temp.toFixed(1);

  document.getElementById("humidity").textContent =
    data.humidity.toFixed(1);

  document.getElementById("water-level").textContent =
    data.water_level_ok ? "OK" : "LOW";

  for (const key of ["heater", "fan", "ato"]) {
    const status = document.getElementById(key + "-status");

    status.textContent = data[key] ? "On" : "Off";
    status.classList.toggle("on", data[key]);
  }

  document.getElementById("alerts").textContent =
    "Example display — no live alerts.";

  document.getElementById("updated").textContent =
    "Example readings";

  document.getElementById("connection-status").textContent =
    "Static demo · No controller connected";
}

refreshDashboard();
setInterval(refreshDashboard, 3000);


// --------------------------------------------------
// Animate sidebar links that jump to page sections
// --------------------------------------------------

// Animation duration in milliseconds.
// Smaller number = faster scroll.
const scrollDuration = 900;

let activeScroll = null;

function animateScrollTo(target) {
  // If another scroll animation is running, stop it.
  if (activeScroll !== null) {
    cancelAnimationFrame(activeScroll);
    activeScroll = null;
  }

  // Respect the operating system's reduced-motion setting.
  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  // Leave a little space between the section and the top of the screen.
  const topSpacing = 20;

  const startPosition = window.scrollY;
  const targetPosition = Math.max(
    0,
    target.getBoundingClientRect().top + window.scrollY - topSpacing
  );

  if (reduceMotion) {
    window.scrollTo(0, targetPosition);
    return;
  }

  const distance = targetPosition - startPosition;
  let startTime = null;

  function step(currentTime) {
    if (startTime === null) {
      startTime = currentTime;
    }

    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / scrollDuration, 1);

    // Ease in and out so the scroll starts and stops gently.
    const easedProgress =
      progress < 0.5
        ? 2 * progress * progress
        : 1 - Math.pow(-2 * progress + 2, 2) / 2;

    window.scrollTo(0, startPosition + distance * easedProgress);

    if (progress < 1) {
      activeScroll = requestAnimationFrame(step);
    } else {
      activeScroll = null;
    }
  }

  activeScroll = requestAnimationFrame(step);
}


// Find links in the sidebar whose destinations start with "#".
document.querySelectorAll('.sidebar a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const targetId = link.getAttribute("href").slice(1);
    const target = document.getElementById(targetId);

    // If the section doesn't exist, leave the link's normal behavior alone.
    if (!target) return;

    event.preventDefault();
    animateScrollTo(target);

    // Keep the section's address in the browser URL.
    history.pushState(null, "", "#" + targetId);
  });
});
