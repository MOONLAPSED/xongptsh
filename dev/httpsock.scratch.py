import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".html"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(self.path[1:], "r") as f:
                self.copyfile(f, self.wfile)
        else:
            super().do_GET()

port = 8000
server = socketserver.TCPServer(("localhost", port), MyHandler)
server.serve_forever()
