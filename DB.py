import pymongo

def DBConnect(string):
    """
    Connect to the MongoDB database.

    Returns:
        pymongo.MongoClient: The MongoDB client.
    """
    client = pymongo.MongoClient(string)
    return client