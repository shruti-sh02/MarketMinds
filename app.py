"""MarketMinds API scaffold using Python's standard library."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MarketMindsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            status = 200
            data = {
                "name": "MarketMinds",
                "description": "Enterprise Technology Intelligence Platform",
                "endpoints": ["/health"],
            }
        elif self.path == "/health":
            status = 200
            data = {"service": "marketminds", "status": "ok"}
        else:
            status = 404
            data = {"error": "Endpoint not found"}

        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), MarketMindsHandler)
    print("MarketMinds running at http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
