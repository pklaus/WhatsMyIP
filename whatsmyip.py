#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple HTTP Server written in Python:
It returns the REMOTE_ADDR to connecting clients.

Written in 2013 by Philipp Klaus <philipp.l.klaus →AT→ web.de>.
Check <https://github.com/pklaus/WhatsMyIP> for newer versions.
"""

import time
import socket
import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        ip = s.client_address[0]
        if ip.startswith('::ffff:'): ip = ip.split('::ffff:')[1]
        s.wfile.write(ip)

class HTTPServerV6(BaseHTTPServer.HTTPServer):
    address_family = socket.AF_INET6

def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', default='::', help='IPv6 to bind to. Default is "::".')
    parser.add_argument('--port', default=8080, type=int, help='Port to listen at. Default is 8080.')

    args = parser.parse_args()

    httpd = HTTPServerV6((args.host, args.port), RequestHandler)
    print time.asctime(), "Server Starts - %s:%s" % (args.host, args.port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (args.host, args.port)

if __name__ == '__main__':
    main()

