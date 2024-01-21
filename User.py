import pymongo

def createUser(collection, name, password):
    """
    This function allows a user to sign in by entering their username, password, and a welcome message. 
    If the username already exists in the database, the function prompts the user to enter a different username.
    """
    result = collection.find_one({"name" : name})
    if result  is None:
        password = password.encode("utf-8")
        password = hashlib.sha256(password)
        message  = input("Write a welcome message : ")
        document = {
            "name" : name,
            "password" : password.hexdigest(),
            "message" : message
        }
        collection.insert_one(document)
    else:
        print("The user already exists, try another Username :")