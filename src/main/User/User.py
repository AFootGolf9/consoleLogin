import pymongo
import hashlib

class UserCollection():
    def __init__(self, db):
        self.collection = db.users

    def createUser(self, name, password):
        """
        Create a new user with the given name and password.

        Args:
            name (str): The name of the user.
            password (str): The password for the user.

        Raises:
            Exception: If a user with the same name already exists.

        Returns:
            None
        """
        result = self.collection.find_one({"name" : name})
        if result is None:
            password = password.encode("utf-8")
            password = hashlib.sha256(password)
            document = {
                "name" : name,
                "password" : password.hexdigest(),
                "authorization" : "user"
            }
            self.collection.insert_one(document)
        else:
            raise Exception("User already exists")
        
    def authenticateUser(self, name, password):
        """
        Authenticates a user by checking if the provided name and password match the stored credentials.

        Args:
            name (str): The name of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the authentication is successful, False otherwise.

        Raises:
            Exception: If the user does not exist.
        """
        
        result = self.collection.find_one({"name" : name})
        
        if result is None:
            raise Exception("User does not exist")
        else:
            password = password.encode("utf-8")
            password = hashlib.sha256(password)
            if password.hexdigest() == result["password"]:
                return True
            else:
                return False
            
    def deleteUser(self, name):
        """
        Deletes a user from the database.

        Args:
            name (str): The name of the user.

        Raises:
            Exception: If the user does not exist.

        Returns:
            None
        """
        
        result = self.collection.delete_one({"name" : name})
        
        if result.deleted_count == 0:
            raise Exception("User does not exist")

    def changePassword(self, name, password):
        """
        Changes the password of a user.

        Args:
            name (str): The name of the user.
            password (str): The new password of the user.

        Raises:
            Exception: If the user does not exist.

        Returns:
            None
        """
        
        password = password.encode("utf-8")
        password = hashlib.sha256(password)
        result = self.collection.update_one({"name" : name}, {"$set" : {"password" : password.hexdigest()}})
        
        if result.modified_count == 0:
            raise Exception("User does not exist")
    
    def changeAuthorization(self, name, authorization):
        """
        Changes the authorization of a user.

        Args:
            name (str): The name of the user.
            authorization (str): The new authorization of the user.

        Raises:
            Exception: If the user does not exist.

        Returns:
            None
        """
        
        result = self.collection.update_one({"name" : name}, {"$set" : {"authorization" : authorization}})
        
        if result.modified_count == 0:
            raise Exception("User does not exist")
            