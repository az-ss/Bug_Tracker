import tornado.ioloop
import tornado.web
from tornadotools.route import Route
from enums.template_path import Template_path
from utils.mongo_operations import get_row_by_id, update_element


# Shows [Edit bug] form.
@Route(r"/edit")
class EditController(tornado.web.RequestHandler):
    def get(self):
        bug_id = self.get_argument('id')
        item = get_row_by_id(bug_id)
        self.render(Template_path.EDIT, title="Edit bug", item=item)


# Updates [Bug info] on DB.
@Route(r"/update_bug")
class UpdateBugInfo(tornado.web.RequestHandler):
    def post(self):
        message = "Bug edited successfully."
        item = {
            "_id": self.get_argument('_id'),
            "id": self.get_argument('id'),
            "name": self.get_argument('name'),
            "description": self.get_argument('description'),
            "status": self.get_argument('status'),
            "time": self.get_argument('time'),
            "assigned": self.get_argument('assigned')
        }

        update_element(item)
        self.render(Template_path.EDIT_POSITIVE, msg=message, item=item)