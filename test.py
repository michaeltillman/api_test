#!/usr/bin/env python
"""
 HTTP server to post listener data.
"""
import json
import ConfigParser
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import cgi

list1 = []


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_header('Content-type', 'application/json')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(list1)

    def do_POST(self):
        # Doesn't do anything with posted data
        self.send_header('Content-type', 'application/json')
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()
        data = json.loads(post_body)
        list1.append(data)
        self.wfile.write(data)

if __name__ == "__main__":
    #Config = ConfigParser.ConfigParser()
    #Config.read("/etc/listener/listener.conf")
    port = 9001#Config.getint('api', 'port')
    host = "localhost"#Config.get('api', 'host')
    server_address = (host, port)
    httpd = HTTPServer(server_address, Server)
    print 'Starting httpd on port 3333...'
    httpd.serve_forever()
