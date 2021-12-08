import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import numpy as np
# why do we need it? - well, we don't :)
# just to train installing packages in docker :)

# setup server settings
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", 8080)

# define Fibonacci series juts to use numpy
f_0 = np.array([
    [0],
    [1],
])
f_step = np.array([
    [0, 1],
    [1, 1]
])
f_n = f_0
n = 0


# class with all logic
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # server response part
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f"{{\"text\":\"Hello again!\"}}", "utf-8"))

        # fun part (numpy + Fibonacci)
        global n, f_step, f_n
        n += 1
        f_n = f_step @ f_n
        print(f"{n}'th Fibonacci number is {f_n[0]}")

        print()


# create an server object
server = HTTPServer((HOST, PORT), Handler)

try:
    # finally run it
    print(f"Now you can open http://{HOST}:{PORT}/\npress Ctrl+C to stop...")
    server.serve_forever()
except KeyboardInterrupt:
    # handling interruption and stop server
    server.server_close()
    print("\nStopped")
