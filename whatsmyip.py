#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple HTTP Server written in Python:
It returns the REMOTE_ADDR to connecting clients.

Written in 2013 by Philipp Klaus <philipp.l.klaus →AT→ web.de>.
Check <https://github.com/pklaus/WhatsMyIP> for newer versions.
"""

import time
import socket
import http.server
import ipaddress

#HOST_NAME = 'example.net'
HOST_NAME = '::'
PORT_NUMBER = 8080


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        RequestHandler.do_HEAD(s)
        ip = ipaddress.ip_address(s.client_address[0])
        if ip.ipv4_mapped: ip = ip.ipv4_mapped
        s.wfile.write(str(ip).encode('ascii'))

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6

if __name__ == '__main__':
    httpd = HTTPServerV6((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

