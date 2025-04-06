from fastapi import APIRouter, HTTPException
#from models.producto_models import Producto
from services.producto_service import obtener_productos, obtener_producto_por_id

router = APIRouter()

#Start api is available
@router.get("/productos-start/")
def start_productos():
    return {"message": "Welcome to productos services into de global API"}

# Get all products
@router.get("/productos", response_model=list)
async def obtener_productos_endpoint():
    productos = obtener_productos()
    return productos

# Get product by ID
@router.get("/productos/{producto_id}")
async def obtener_producto_endpoint(producto_id: str):
    producto = obtener_producto_por_id(producto_id)
    if producto:
        return producto
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")