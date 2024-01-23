import pymongo
import hashlib

class UserCollection():
    def __init__(self, DB):
        self.collection = DB.users

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
            
