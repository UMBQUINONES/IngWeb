from db.database import database
#from bson import ObjectId
#from models.producto_models import Producto

#Obtener todos los productos
def obtener_productos():
    collection = database.get_collection("productos")  # Selecciona la colección "productos"
    productos = list(collection.find({}, {"_id": 0}))  # Excluye "_id"
    return productos

def obtener_producto_por_id(producto_id):
    collection = database.get_collection("productos")  # Selecciona la colección "productos"
    producto = collection.find_one({"_id": producto_id}) #BUSQUEDA POR ID
    if producto:
        return producto
    else:
        return None