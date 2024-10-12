#!/usr/bin/python3
import http.server
import json
from http.server import HTTPServer



class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "new York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

server = HTTPServer(("localhost",8000), MyHandler)

server.serve_forever()