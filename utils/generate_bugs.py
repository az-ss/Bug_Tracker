import random
import string
import datetime
from utils.mongo_operations import get_bugs_table_instance


# Returns random string.
def random_string(text, length):
    return ''.join(random.choice(text + string.lowercase + string.digits) for i in range(length))


# Returns random integer.
def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))


# Returns random boolean.
def random_status():
    return random.choice([True, False])


# Returns random time.
def random_time():
    return datetime.datetime.utcnow()


# Inserts to DB generated data.
def check_db():
    bugs_table = get_bugs_table_instance()
    bugs_table.remove()

    for x in range(4):
        bugs_table.insert(random_bugs())

    print bugs_table.count()


# Removes [_id] to get it unique.
def random_bugs():
    try:
        del BUGS['_id']
    except:
        pass
    return BUGS


# [Bug] template for DB.
BUGS = {
    "id": random_number(10),
    "name": random_string("Name", 5),
    "description": random_string("Description", 5),
    "status": random_status(),
    "time": random_time(),
    "assigned": random_string("Assigned", 5)
}

if __name__ == "__main__":
    check_db()
