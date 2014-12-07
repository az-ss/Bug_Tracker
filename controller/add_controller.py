import tornado.ioloop
import tornado.web
from tornadotools.route import Route
from enums.template_path import Template_path
from utils.generate_bugs import random_number
from utils.mongo_operations import get_bugs_table_instance

# Shows [Add Bug] form.
@Route(r"/add")
class AddController(tornado.web.RequestHandler):
    def get(self):
        self.render(Template_path.ADD, title='Add bug')


# Adds new bug into DB.
@Route(r"/add_bug")
class AddBugInfo(tornado.web.RequestHandler):
    def post(self):
        message = "Bug added successfully."
        item = {
            "id": random_number(10),
            "name": self.get_argument('name'),
            "description": self.get_argument('description'),
            "status": self.get_argument('status'),
            "time": self.get_argument('time'),
            "assigned": self.get_argument('assigned')
        }
        bugs_table = get_bugs_table_instance()
        bugs_table.insert(item)
        self.render(Template_path.ADD_POSITIVE, msg=message, item=item)