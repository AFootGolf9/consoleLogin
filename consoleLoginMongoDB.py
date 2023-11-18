import pymongo

client = pymongo.MongoClient("mongodb+srv://user:password2@cluster0.w2q60oh.mongodb.net/?retryWrites=true&w=majority")

db = client.test1

colection = db.users

def singIn():
    """
    This function allows a user to sign in by entering their username, password, and a welcome message. 
    If the username already exists in the database, the function prompts the user to enter a different username.
    """
    do = True
    while do:
        do = False
        userName = input("Username : ")

        result = colection.find_one({"name" : userName})

        if result  is None:
            password = input("coloque uma senha mas lembre-se vc deve se lembrar : ")
            message  = input("coloque uma mensagem de boas vindas : ")
            document = {
                "name" : userName,
                "password" : password,
                "message" : message
            }
            colection.insert_one(document)
        else:
            print("O usuario já existe, tente outro nome:")
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
            print("O usuario não existe, tente novamente!!!")
            do = True
        else:
            do2 = True
            while do2:
                do2 = False
                password = input("password : ")
                if password != result["password"]:
                    print("senha incoreta, tente novamente!!!")
                    do2 = True
                else: 
                    print(result["message"])
