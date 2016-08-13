#!/usr/bin/env python
# encoding:utf-8

import os
import sys


import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado import web
from tornado.options import define, options

from utils.views import IndexHandler, UpFileHandler, DownloadHandler, ErrorHandler

define("port", default=8010, help="run port", type=int)
define("listen_ip", default="0.0.0.0", help="listen ip", type="str")

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload/", UpFileHandler),
            (r"/download/",DownloadHandler),
            (r"/.*", ErrorHandler),
            ]
        settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH,
            debug = True
            )
        tornado.web.Application.__init__(self, handlers, **settings)



def main():
    print "service  start at: %s:%d ..." % (options.listen_ip,options.port)
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port, address=options.listen_ip)
    tornado.ioloop.IOLoop.instance().start()
    
     
if __name__ == "__main__":
    main()
