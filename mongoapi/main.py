from fastapi import FastAPI, Request
from routes.producto_routes import router as producto_router

app = FastAPI(title="apimongo")

app.include_router(producto_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI! crud mongoDB"} 






