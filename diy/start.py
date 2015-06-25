import os
import tornado.ioloop
import tornado.web
import memcache
import sys
reload( sys )
sys.setdefaultencoding('utf-8')

from jinja2_tornado import JinjaLoader
from urls import urls
from task import get_cookies

IP = '127.0.0.1'
port = '8000'

class Application(tornado.web.Application):
    def __init__(self, **kwargs):
        self.mc = memcache.Client(['%s:15211' % IP])
        tornado.web.Application.__init__(self, **kwargs)


application = Application(
    handlers=urls,
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_loader=JinjaLoader(os.path.join(os.path.dirname(__file__), 'templates/'),
        autoescape=True, extensions=['jinja2.ext.autoescape']),
)

if __name__ == "__main__":
    port = int(port)
    application.listen(port, IP)
    print("Listening...")
    tornado.ioloop.PeriodicCallback(get_cookies, 6*60*60*1000).start()
    tornado.ioloop.IOLoop.instance().start()
