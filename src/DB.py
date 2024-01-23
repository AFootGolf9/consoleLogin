from pymongo import MongoClient
import src.User as User

class Connection():
    def __init__(self, string):
        self.client = MongoClient(string)
        self.db = self.client.test
        self.Users = User.UserCollection(self.db)

    def createUser(self, name, password):
        self.Users.createUser(name, password)

    def autenticateUser(self, name, password):
        return self.Users.authenticateUser(name, password)

    