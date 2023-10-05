import pymongo

client = pymongo.MongoClient("")

db = client.test1

colection = db.users

def singIn():
    do = True
    while do:
        do = False
        userName = input("Username : ")

        result = colection.find_one({"name" : userName})

        if result  is None:
            password = input("Password (once chosen you can't change) : ")
            message  = input("Write a welcome message : ")
            document = {
                "name" : userName,
                "password" : password,
                "message" : message
            }
            colection.insert_one(document)
        else:
            print("The user already exists, try another Username :")
            do = True

def logIn():
    """
    This function prompts the user to enter a username and password, and checks if they match the records in a MongoDB collection.
    If the username or password is incorrect, the user is prompted to try again.
    If the username and password are correct, the function prints a message associated with the user's account.
    """
    do = True
    while do:
        do = False
        userName = input("Username : ")

        result = colection.find_one({"name" : userName})

        if result is None:
            print("The username don't exists, try again !!!")
            do = True
        else:
            do2 = True
            while do2:
                do2 = False
                password = input("password : ")
                if password != result["password"]:
                    print("Incorect password, try again !!!")
                    do2 = True
                else: 
                    print(result["message"])
