# Aquarium dashboard: getting started

This copy keeps your sensor and actuator modules and connects your dashboard to the existing simulation. It uses only Python's standard library; no Flask install is required.

## Run it

1. Open this project folder in VS Code. Open a terminal in the folder containing `web_server.py`.
2. Run `python web_server.py` (on Windows, `py web_server.py` may work if `python` does not).
3. Open http://127.0.0.1:8000 in your browser. Don't open `interface/web.html` directly: the page needs the server's API.
4. Press Ctrl+C in the terminal to stop. Run either the dashboard server or `main_controller.py`, not both: they would be independent simulations.

## What changed

- `main_controller.py`: `read_controller_state()` takes one set of readings, runs your existing control rules and alerts, and returns a dictionary. The original terminal mode still works with `python main_controller.py`.
- `web_server.py`: runs that function every five seconds and serves the latest snapshot at `/api/readings`. It listens only on this computer.
- `interface/web.html`: the original layout, adapted to display OK/LOW for your float switch and read-only actuator states. Its CSS remains in the `<style>` block.
- `interface/dashboard.js`: fetches the snapshot every three seconds and updates the page. Several browser refreshes can show the same sample; the displayed time is when Python sampled it.

Follow a value: `sensors/water_temp_sensor.py` returns a simulated number → `read_controller_state()` adds it to the `water_temp` dictionary key → `/api/readings` sends it as JSON → `dashboard.js` places it in the HTML element with `id="water-temp"`. To add a reading, add its sensor call and dictionary field, an HTML element, and a JavaScript update.

Your existing thresholds are unchanged. Alert thresholds and heater/fan thresholds differ, so an alert can appear while equipment is off. The random sensors generate independent values; turning an actuator on does not affect the next reading. This is a simulation and has no hardware safeguards; do not use it to control real equipment without developing and testing sensor error handling, independent limits, ATO timeouts and other fail-safes. This local development server has no authentication and is not intended to be exposed to a network.
