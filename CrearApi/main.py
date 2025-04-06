from fastapi import FastAPI, Request

app = FastAPI(title="my first API")

@app.get("/")
def inicio():
    return{"mensaje":"hola mundo"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str =None):
    return{"parametros":item_id, "q": q}

@app.post("/convertidor/")
async def convertir(request: Request):
    body= await request.json()
    amount=body.get("amount")
    to_currency=body.get("to_currency", "").upper()
    
    match to_currency:
        case "USD":
            llegada=amount*0.00026
        case "EUR":
            llegada=amount*0.00024
        case "GBP":
            llegada=amount*0.00020
        
    return{
            "amount": amount,
            "to_currency": to_currency,
            "llegada": llegada
            
            
        }