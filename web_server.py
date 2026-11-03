"""Local dashboard server for the simulated aquarium controller."""
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock, Thread
import json
import time

from main_controller import read_controller_state

ROOT = Path(__file__).resolve().parent / "interface"
lock = Lock()
latest = None


def sample_loop():
    global latest
    while True:
        try:
            state = read_controller_state()
            state["sampled_at"] = datetime.now(timezone.utc).isoformat()
            with lock:
                latest = state
        except Exception as error:
            # Do not present an old sample as current after a sensor failure.
            with lock:
                latest = None
            print(f"Controller read failed: {error}", flush=True)
        time.sleep(5)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/readings":
            with lock:
                snapshot = latest
            if snapshot is None:
                self.respond(503, b'{"error":"No current reading"}', "application/json")
            else:
                self.respond(200, json.dumps(snapshot).encode("utf-8"), "application/json; charset=utf-8")
        elif self.path in ("/", "/web.html", "/dashboard.js"):
            name = "dashboard.js" if self.path == "/dashboard.js" else "web.html"
            mime = "text/javascript" if name.endswith(".js") else "text/html"
            self.respond(200, (ROOT / name).read_bytes(), mime + "; charset=utf-8")
        else:
            self.send_error(404)

    def respond(self, status, data, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    Thread(target=sample_loop, daemon=True).start()
    server = ThreadingHTTPServer(("127.0.0.1", 8000), Handler)
    print("Open http://127.0.0.1:8000 (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard.")
    finally:
        server.server_close()
