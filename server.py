import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# setup server settings
HOST = os.environ.get("HOST", "localhost")
PORT = os.environ.get("PORT", 8080)


# class with all logic
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f"{{\"text\":\"Hello again!\"}}", "utf-8"))


# create an object
server = HTTPServer((HOST, PORT), Handler)

try:
    # finally run it
    print(f"Now you can open http://{HOST}:{PORT}/\npress Ctrl+C to stop...")
    server.serve_forever()
except KeyboardInterrupt:
    # handling interruption and stop server
    server.server_close()
    print("\nStopped")
