from pymongo import MongoClient


# Connects to DB.
def get_bugs_table_instance():
    client = MongoClient('localhost', 27017)
    db = client.test
    return db['bugs_collection']


# Returns all records from DB.
def get_all_data():
    bugs_table = get_bugs_table_instance()
    return bugs_table.find()


# Returns one row records from DB by element id.
def get_row_by_id(element_id):
    bugs_table = get_bugs_table_instance()
    return bugs_table.find_one({"id": element_id})


# Delete one row record from DB by element id.
def delete_row_by_id(element_id):
    bugs_table = get_bugs_table_instance()
    return bugs_table.remove({"id": element_id})


# updates DB record.
def update_element(item):
      bugs_table = get_bugs_table_instance()
      bugs_table.update({'id': item['id']}, {'$set': {
          'id': item['id'],
          'name': item['name'],
          'description': item['description'],
          'status': item['status'],
          'time': item['time'],
          'assigned': item['assigned']
      }})