from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://admin:123@cluster0.alr5w.mongodb.net/",
            tlsAllowInvalidCertificates=True  # Desactiva verificación de SSL
        )
        self.db = self.client["pracmongo"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()