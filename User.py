import pymongo
import hashlib


def createUser(collection, name, password):
    """
    Create a new user in the collection.

    Args:
        collection (pymongo.collection.Collection): The MongoDB collection to insert the user document into.
        name (str): The name of the user.
        password (str): The password of the user.

    Raises:
        Exception: If a user with the same name already exists in the collection.
    """
    result = collection.find_one({"name" : name})
    if result is None:
        password = password.encode("utf-8")
        password = hashlib.sha256(password)
        document = {
            "name" : name,
            "password" : password.hexdigest(),
            "authorization" : "user"
        }
        collection.insert_one(document)
    else:
        raise Exception("User already exists")
    
def authenticateUser(collection, name, password):
    """
    Authenticate a user.

    Args:
        collection (pymongo.collection.Collection): The MongoDB collection to search for the user in.
        name (str): The name of the user.
        password (str): The password of the user.

    Returns:
        bool: True if the user exists and the password is correct, False otherwise.
    """
    result = collection.find_one({"name" : name})
    if result is None:
        return False
    else:
        password = password.encode("utf-8")
        password = hashlib.sha256(password)
        if password.hexdigest() == result["password"]:
            return True
        else:
            return False
        
