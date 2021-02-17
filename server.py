import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.0.8", PORT), handler) as httpd:
    print("Server started at 192.168.0.8:" + str(PORT))
    httpd.serve_forever()
