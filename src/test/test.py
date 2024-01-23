import sys
sys.path.append("./src/main")
from DB import Connection
from configparser import ConfigParser


file = "././config.ini"
config = ConfigParser()
config.read(file)

def test_connection():
    """
    This function tests the connection to the MongoDB database.
    """
    connection = Connection(config.get("MongoDB", "url"))
    if connection is None:
        raise Exception("Connection to MongoDB failed")
    connection.createUser("test", "test")
    connection.deleteUser("test")
    print('ok')

test_connection()