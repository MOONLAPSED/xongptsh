"""
This module creates a simple HTTP server that serves HTML files from the local directory. 
It uses the http.server and socketserver modules from the Python standard library. 
The server is set to listen on localhost port 8000. 
The MyHandler class is a custom request handler that extends http.server.SimpleHTTPRequestHandler to serve HTML files.
"""
import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    This class is a custom HTTP request handler that serves HTML files from the local directory.
    It extends the SimpleHTTPRequestHandler class from the http.server module.
    """
    def do_GET(self):
        """
        This method handles HTTP GET requests. If the requested path ends with ".html", 
        it sends a 200 response and the contents of the HTML file. 
        Otherwise, it calls the superclass's do_GET method.

        Parameters:
        None

        Returns:
        None
        """
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
