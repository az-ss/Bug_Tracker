import tornado.ioloop
import tornado.web
from tornadotools.route import Route
import controller.index_controller
import controller.edit_controller
import controller.add_controller

if __name__ == "__main__":
    # Launches Tornado server
    application = tornado.web.Application([] + Route.routes())
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()