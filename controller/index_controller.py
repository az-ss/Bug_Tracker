import tornado.ioloop
import tornado.web
from tornadotools.route import Route
from enums.template_path import Template_path
from utils.mongo_operations import get_all_data, get_row_by_id, delete_row_by_id


# Shows all bugs from the DB.
@Route(r"/")
class IndexController(tornado.web.RequestHandler):
    def get(self):
        bugs = get_all_data()
        items = []
        for bug in bugs:
            items.append(bug)
        self.render(Template_path.INDEX, title="Bug tracker", items=items)


# Delete bug by [ID] from DB.
@Route(r"/delete")
class EditHandler(tornado.web.RequestHandler):
    def get(self):
        bug_id = self.get_argument('id')
        delete_row_by_id(bug_id)
        self.render(Template_path.DELETE_POSITIVE, title="Bug deleted")