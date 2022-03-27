from email import message
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    bruno0 = "bruno0"
    bruno1= "bruno1"
    bruno2= "bruno2"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name, "message": f"Vai {model_name}! Você consegue!"}