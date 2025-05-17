from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import json
import os

class MyRequestHandler(SimpleHTTPRequestHandler):
    """def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            try:
                with open('index.html', 'rb') as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()
                    self.wfile.write(content)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'index.html nem talalhato.')
        elif self.path == '/output.png':
            try:
                with open('output.png', 'rb') as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'image/png')
                    self.end_headers()
                    self.wfile.write(content)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'index.html nem talalhato.')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Az oldal nem talalhato.')
"""
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            response = {
                'status': 'success',
                'received': data
            }
            self.send_response(200)
        except json.JSONDecodeError:
            response = {
                'status': 'error',
                'message': 'Invalid JSON'
            }
            self.send_response(400)

        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Szerver fut a {port}-as porton...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
