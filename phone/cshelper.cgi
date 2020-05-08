#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from sys import path
path.insert(0, '/home/groups3/cshelper/public_html/cgi-bin/cs_helper/phone/')
path.insert(1, '/home/groups3/cshelper/public_html/cgi=bin/cs_helper/phone/app/')
from app import app

print("Content-Type: application\n\n")

class ProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = ""
        environ['SERVER_PORT'] = "8080"
        environ['REQUEST_METHOD'] = "GET"
        environ['SCRIPT_NAME'] = ""
        environ['QUERY_STRING'] = ""
        environ['PATH_INFO'] = "/"
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)
    print("After CGIHandler run")


