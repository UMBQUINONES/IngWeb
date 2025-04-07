from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://admin:123@apismongo.ri0tyfu.mongodb.net/?retryWrites=true&w=majority&appName=ApisMongo",   
            tlsAllowInvalidCertificates=True  # Desactiva verificación de SSL
        )
        self.db = self.client["pracmongo"]#

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()