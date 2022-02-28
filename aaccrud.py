from pymongo import MongoClient
from bson.objectid import ObjectId

# SNHU CS 340 - Salah Bedoui

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:55233' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            print('True')
        else:
            raise Exception('False')

# Complete this read method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            read_result = self.database.animals.find(data, {'_id': 0})
            for x in read_result:
                print(x)
        else:
            raise Exception('Nothing to read, because data parameter is empty')

# Complete this update method to implement the U in CRUD
    def update(self, data, dataUpdate):
        if data is not None:
            self.database.animals.update_many(data, dataUpdate)
            for x in self.database.animals.find(data, {'_id': 0}):
                print(x)
        else:
            raise Exception('Nothing to update, because data parameter is empty')
        
# Complete this delete method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_many(data)
            for x in self.database.animals.find(data, {'_id': 0}):
                print(x)
        else:
            raise Exception('Nothing to delete, because data parameter is empty')
