import pymongo

class ProductCollection():
    def __init__(self, db):
        self.collection = db.Products
    
    def createProduct(self, name, price, description):
            """
            Creates a new product with the given name, price, and description.

            Args:
                name (str): The name of the product.
                price (float): The price of the product.
                description (str): The description of the product.

            Raises:
                Exception: If a product with the same name already exists.

            Returns:
                None
            """
            result = self.collection.find_one({"name": name})
            
            if result is None:
                document = {
                    "name": name,
                    "price": price,
                    "description": description
                }
                self.collection.insert_one(document)
            else:
                raise Exception("Product already exists")

    def deleteProduct(self, name):
        """
        Deletes a product from the collection based on its name.

        Args:
            name (str): The name of the product to be deleted.

        Raises:
            Exception: If the product does not exist in the collection.
        """
        result = self.collection.delete_one({"name": name})
        
        if result.deleted_count == 0:
            raise Exception("Product does not exist")
    
    def changePrice(self, name, price):
        """
        Change the price of a product.

        Args:
            name (str): The name of the product.
            price (float): The new price of the product.

        Raises:
            Exception: If the product does not exist.

        Returns:
            None
        """
        result = self.collection.update_one({"name": name}, {"$set": {"price": price}})

        if result.modified_count == 0:
            raise Exception("Product does not exist")
    
    def changeDescription(self, name, description):
            """
            Change the description of a product.

            Args:
                name (str): The name of the product.
                description (str): The new description for the product.

            Raises:
                Exception: If the product does not exist.

            Returns:
                None
            """
            result = self.collection.update_one({"name": name}, {"$set": {"description": description}})

            if result.modified_count == 0:
                raise Exception("Product does not exist")
    
    def getProduct(self, name):
        """
        Retrieves a product from the collection based on its name.

        Args:
            name (str): The name of the product to retrieve.

        Returns:
            dict: The product document from the collection.

        Raises:
            Exception: If the product does not exist in the collection.
        """
        result = self.collection.find_one({"name": name})
        
        if result is None:
            raise Exception("Product does not exist")
        else:
            return result
        
    def getAllProducts(self):
        """
        Retrieves all products from the collection.

        Returns:
            A cursor object containing all the products.
        """
        return self.collection.find({})
    