from django.shortcuts import render
from http.server import HTTPServer,BaseHTTPRequestHandler
content = ''' <html> <h1> TCP/IP PROTOCOL SUITE <h1> </html>'''
class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
    print("This is my webserver")
   server_address =('',8000)
   httpd = HTTPServer(server_address,WebServer)
httpd.serve_forever