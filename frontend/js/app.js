const MOCK_DATA = {
  Kigali: { city: 'Kigali', country: 'Rwanda', current: { temperature: 24.5, wind_speed: 9.2, weather_code: 2 }, forecast: [{date:'2026-10-16',temperature_max:27,temperature_min:17,precipitation_probability:35},{date:'2026-10-17',temperature_max:28,temperature_min:18,precipitation_probability:55},{date:'2026-10-18',temperature_max:26,temperature_min:16,precipitation_probability:20},{date:'2026-10-19',temperature_max:29,temperature_min:18,precipitation_probability:45},{date:'2026-10-20',temperature_max:25,temperature_min:17,precipitation_probability:65}] },
  Nairobi: { city: 'Nairobi', country: 'Kenya', current: { temperature: 22.1, wind_speed: 12.4, weather_code: 3 }, forecast: [{date:'2026-10-16',temperature_max:25,temperature_min:14,precipitation_probability:25},{date:'2026-10-17',temperature_max:24,temperature_min:15,precipitation_probability:40},{date:'2026-10-18',temperature_max:26,temperature_min:14,precipitation_probability:15},{date:'2026-10-19',temperature_max:23,temperature_min:13,precipitation_probability:70},{date:'2026-10-20',temperature_max:25,temperature_min:14,precipitation_probability:30}] },
  London: { city: 'London', country: 'United Kingdom', current: { temperature: 13.8, wind_speed: 16.1, weather_code: 61 }, forecast: [{date:'2026-10-16',temperature_max:16,temperature_min:10,precipitation_probability:75},{date:'2026-10-17',temperature_max:15,temperature_min:9,precipitation_probability:60},{date:'2026-10-18',temperature_max:17,temperature_min:11,precipitation_probability:35},{date:'2026-10-19',temperature_max:14,temperature_min:8,precipitation_probability:null},{date:'2026-10-20',temperature_max:18,temperature_min:12,precipitation_probability:null}] }
};
let liveMode = false;
const $ = id => document.getElementById(id);
const weatherIcon = code => code >= 51 ? '☂' : code >= 3 ? '☁' : '☀';
const getMock = city => MOCK_DATA[Object.keys(MOCK_DATA).find(key => key.toLowerCase() === city.toLowerCase())];
async function loadWeather(city) {
  if (!liveMode) return getMock(city);
  const response = await fetch(`http://localhost:5000/api/weather?city=${encodeURIComponent(city)}`);
  if (!response.ok) throw new Error((await response.json()).error || 'The live weather service could not answer.');
  return response.json();
}
function render(record) {
  $('current-city').textContent = `${record.city}, ${record.country}`;
  $('current-temp').textContent = record.current.temperature;
  $('current-wind').textContent = `${record.current.wind_speed} km/h`;
  $('current-code').textContent = record.current.weather_code;
  $('current-icon').textContent = weatherIcon(record.current.weather_code);
  $('current-detail').textContent = record.current.weather_code >= 51 ? 'A wet-weather reading. Keep an eye on the clouds.' : 'A bright reading with a good chance for exploring.';
  $('forecast-list').innerHTML = record.forecast.map(day => `<div class="forecast-row"><span class="date">${day.date.slice(5)}</span><strong>${day.temperature_max}°</strong><span>${day.temperature_min}°</span><span class="rain-dot" title="${day.precipitation_probability ?? 'unknown'}% rain chance"></span></div>`).join('');
  const values = record.forecast.map(day => day.temperature_max); const max = Math.max(...values); 
  $('chart').innerHTML = record.forecast.map(day => `<div class="bar" style="height:${Math.max(10, day.temperature_max / max * 100)}%"><span>${day.temperature_max}°</span><i>${day.date.slice(8)}</i></div>`).join('');
  const probabilities = record.forecast.map(day => day.precipitation_probability).filter(value => value !== null && value !== undefined);
  const highest = probabilities.length ? Math.max(...probabilities) : null;
  $('umbrella-result').textContent = highest === null ? 'Rain chance unknown' : highest >= 40 ? `Pack an umbrella (${highest}% chance)` : `Leave it at home (${highest}% chance)`;
  $('chart-caption').textContent = `Five daily highs · average ${Math.round(values.reduce((sum, value) => sum + value, 0) / values.length)}°C`;
  $('status').textContent = liveMode ? 'Live readings from Flask + Open-Meteo.' : 'Sample readings loaded.';
  $('mode-label').textContent = liveMode ? 'LIVE DATA' : 'DEMO DATA';
}
async function refresh() { const city = $('city-input').value.trim(); $('error').hidden = true; $('status').textContent = 'Scanning the skies...'; try { const record = await loadWeather(city); if (!record) throw new Error(`No sample station found for “${city}”. Try Kigali, Nairobi, or London.`); render(record); } catch (error) { $('error').textContent = error.message; $('error').hidden = false; $('status').textContent = liveMode ? 'Live request failed.' : 'Ready for another station.'; } }
$('search-form').addEventListener('submit', event => { event.preventDefault(); refresh(); });
$('mode-toggle').addEventListener('click', () => { liveMode = !liveMode; $('mode-toggle').textContent = liveMode ? 'Switch to demo' : 'Switch to live'; $('mode-toggle').setAttribute('aria-pressed', liveMode); refresh(); });
document.querySelectorAll('.choice').forEach(button => button.addEventListener('click', () => { $('quiz-score').textContent = `${button.dataset.answer === 'rain' ? 1 : 0} / 1`; button.style.borderColor = button.dataset.answer === 'rain' ? '#f7c948' : '#f2654d'; }));
refresh();
