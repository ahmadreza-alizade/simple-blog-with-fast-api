from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, Response
app = FastAPI()

@app.get("/{myItem}")
async def myFunctionName(myItem:str):
    return {"myItem":myItem}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
