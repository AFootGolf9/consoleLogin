from pymongo import MongoClient
import User.User as User
import Product.Product as Product

class Connection():
    def __init__(self, string):
        self.client = MongoClient(string)
        self.db = self.client.test
        self.users = User.UserCollection(self.db)
        self.products = Product.ProductCollection(self.db)

    def createUser(self, name, password):
        self.users.createUser(name, password)

    def autenticateUser(self, name, password):
        return self.users.authenticateUser(name, password)
    
    def deleteUser(self, name):
        self.users.deleteUser(name)

    def changePassword(self, name, password):
        self.users.changePassword(name, password)
    
    def changeAuthorization(self, name, authorization):
        self.users.changeAuthorization(name, authorization)

    def createProduct(self, name, price, description):
        self.products.createProduct(name, price, description)

    def deleteProduct(self, name):
        self.products.deleteProduct(name)

    def changePrice(self, name, price):
        self.products.changePrice(name, price)

    def changeDescription(self, name, description):
        self.products.changeDescription(name, description)

    def getProduct(self, name):
        return self.products.getProduct(name)
    
    def getAllproducts(self):
        return self.products.getAllproducts()