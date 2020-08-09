#!/usr/bin/env python
# run this in the output/ subdirectory to start a simple
# cgi server

from http.server import CGIHTTPRequestHandler
import http.server
import http.server

CGIHTTPRequestHandler.cgi_directories = ['/services']

def test(HandlerClass = CGIHTTPRequestHandler,
         ServerClass = http.server.HTTPServer):
    http.server.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
