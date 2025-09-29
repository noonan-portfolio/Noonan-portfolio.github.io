// 1) Weather for a fixed city (Milwaukee) + icon
(async function loadWeather() {
  const out = document.getElementById('weatherOut');

  // Milwaukee, WI
  const CITY = 'Milwaukee';
  const LAT = 43.0389;
  const LON = -87.9065;

  // Ask Open-Meteo for temperature, wind, and weather_code (used for icons)
  const url = `https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LON}&current=temperature_2m,wind_speed_10m,weather_code`;

  // Map Open-Meteo weather codes → emoji icon
  const ICON = {
    0: "☀️",        // clear
    1: "🌤️", 2: "🌤️", 3: "☁️",
    45: "🌫️", 48: "🌫️",
    51: "🌦️", 53: "🌦️", 55: "🌧️",
    56: "🌧️", 57: "🌧️",
    61: "🌧️", 63: "🌧️", 65: "🌧️",
    66: "🌧️", 67: "🌧️",
    71: "🌨️", 73: "🌨️", 75: "❄️",
    77: "❄️",
    80: "🌦️", 81: "🌧️", 82: "🌧️",
    85: "🌨️", 86: "🌨️",
    95: "⛈️", 96: "⛈️", 99: "⛈️"
  };

  try {
    const data = await fetch(url).then(r => r.json());
    const c = data?.current || {};
    const icon = ICON[c.weather_code] || "🌡️";
    out.innerHTML = `
      <span class="wx-icon">${icon}</span>
      <span><strong>${CITY}</strong>: ${c.temperature_2m ?? "?"}°C, wind ${c.wind_speed_10m ?? "?"} m/s</span>
    `;
  } catch (e) {
    out.textContent = 'Weather unavailable.';
  }
})();

// 2) Recent GitHub activity (public)
(async function loadGitHub() {
  const out = document.getElementById('ghOut');
  const user = 'Noonan-portfolio';
  try {
    const events = await fetch(`https://api.github.com/users/${user}/events/public`).then(r => r.json());
    (events || []).slice(0, 10).forEach(ev => {
      const li = document.createElement('li');
      li.innerHTML = `<strong>${ev.type}</strong> in <a target="_blank" href="${ev.repo && 'https://github.com/' + ev.repo.name}">${ev.repo?.name}</a> – ${new Date(ev.created_at).toLocaleString()}`;
      out.appendChild(li);
    });
  } catch (e) {
    out.innerHTML = '<li>Unable to load GitHub activity.</li>';
  }
})();

// 3) Public ICS calendar (paste your ICS URL below)
(async function loadCalendar() {
  const out = document.getElementById('calOut');
  const ICS_URL = './calendar.ics'; // now fetches from your repo
  try {
    const ics = await fetch(ICS_URL).then(r => r.text());
    const items = [];
    ics.split('\n').forEach(line => {
      if (line.startsWith('SUMMARY:')) items.push({ summary: line.slice(8) });
    });
    items.slice(0, 10).forEach(i => {
      const li = document.createElement('li');
      li.textContent = i.summary;
      out.appendChild(li);
    });
  } catch (e) {
    out.innerHTML = '<li>Calendar unavailable.</li>';
  }
})();

// 4) LocalStorage Todos
const form = document.getElementById('todoForm');
const input = document.getElementById('todoInput');
const list = document.getElementById('todoList');
const KEY = 'dashboard_todos';
function render() {
  list.innerHTML = '';
  const todos = JSON.parse(localStorage.getItem(KEY) || '[]');
  todos.forEach((t, i) => {
    const li = document.createElement('li');
    li.textContent = t;
    li.addEventListener('click', () => {
      todos.splice(i, 1); localStorage.setItem(KEY, JSON.stringify(todos)); render();
    });
    list.appendChild(li);
  });
}
form.addEventListener('submit', e => {
  e.preventDefault();
  const todos = JSON.parse(localStorage.getItem(KEY) || '[]');
  if (input.value.trim()) todos.unshift(input.value.trim());
  localStorage.setItem(KEY, JSON.stringify(todos));
  input.value=''; render();
});
render();
