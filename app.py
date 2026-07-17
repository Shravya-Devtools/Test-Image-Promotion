from http.server import SimpleHTTPRequestHandler, HTTPServer

class MockAppHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Image Pipeline Verification App (v1.0.0)</h1>")

if __name__ == "__main__":
    print("Server starting on port 8080...")
    HTTPServer(("0.0.0.0", 8080), MockAppHandler).serve_forever()
