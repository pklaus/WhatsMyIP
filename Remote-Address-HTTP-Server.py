#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple HTTP Server written in Python:
It returns the REMOTE_ADDR to connecting clients.

Inspired by
* http://wiki.python.org/moin/BaseHttpServer
* and http://www.righto.com/2011/02/ipv6-web-serving-with-arc-or-python.html

Written on 2013-02-18 by Philipp Klaus <philipp.l.klaus →AT→ web.de>.
Check <https://gist.github.com/pklaus/4980542> for newer versions.
"""

import time
import socket
import BaseHTTPServer


#HOST_NAME = 'example.net'
HOST_NAME = '::'
PORT_NUMBER = 8080


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write(s.client_address[0])

class HTTPServerV6(BaseHTTPServer.HTTPServer):
    address_family = socket.AF_INET6

if __name__ == '__main__':
    httpd = HTTPServerV6((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
