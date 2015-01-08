import random
import string
import datetime
from utils.mongo_operations import get_bugs_table_instance


# Returns random string.
def random_string(length):
    return ''.join(random.choice(string.lowercase + string.digits) for i in range(length))


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

    for x in range(20):
        bugs_table.insert({
            "id": random_number(10),
            "name": random_string(5),
            "description": random_string(5),
            "status": random_status(),
            "time": random_time(),
            "assigned": random_string(5)
        })

    print "There are " + str(bugs_table.count()) + " records created in DB."


if __name__ == "__main__":
    check_db()
