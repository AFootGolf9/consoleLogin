from pymongo import MongoClient
import User.User as User
import Product.Product as Product

class Connection():
    def __init__(self, string):
        self.client = MongoClient(string)
        self.db = self.client.test
        self.Users = User.UserCollection(self.db)
        self.Products = Product.ProductCollection(self.db)

    def createUser(self, name, password):
        self.Users.createUser(name, password)

    def autenticateUser(self, name, password):
        return self.Users.authenticateUser(name, password)
    
    def deleteUser(self, name):
        self.Users.deleteUser(name)

    def changePassword(self, name, password):
        self.Users.changePassword(name, password)
    
    def changeAuthorization(self, name, authorization):
        self.Users.changeAuthorization(name, authorization)

    def createProduct(self, name, price, description):
        self.Products.createProduct(name, price, description)

    def deleteProduct(self, name):
        self.Products.deleteProduct(name)

    def changePrice(self, name, price):
        self.Products.changePrice(name, price)

    def changeDescription(self, name, description):
        self.Products.changeDescription(name, description)

    def getProduct(self, name):
        return self.Products.getProduct(name)
    
    def getAllProducts(self):
        return self.Products.getAllProducts()