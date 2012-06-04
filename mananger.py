import os
import sys

import tornado.web
import tornado.ioloop

api_dir = os.path.abspath('api')
sys.path.append(api_dir)
handler_dir = os.path.abspath('handler')
sys.path.append(handler_dir)

from mainHandler import MainHandler
from testHandler import TestHandler

settings = {
  "static_path": os.path.join(os.path.dirname(__file__), "static"),
  "template_path": os.path.join(os.path.dirname(__file__), "template"),
  "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
  "login_url": "/login",
  "xsrf_cookies": True,

  "debug": True,
}

application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/test", TestHandler),
  #(r"/login", LoginHandler),
  (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)

def main(port):
  application.listen(port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main(int(sys.argv[1]))
