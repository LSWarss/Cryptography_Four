from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    value: str

@app.get("/")
async def root(): 
    return {"message": "Hello cryptography 🤖"}

# Symmetric Routes

@app.get("/symmetric/key")
async def get_key():
    """Returns random symmetric key

    Returns:
        HEX: Symmetric Key
    """
    return "HEX key"

@app.post("/symmetric/")
async def post_key(key):
    """Sets symmetric key posted in the reques

    Args:
        key HEX: Symmetric Key

    Returns:
        JSON: Message if the key was succesfully set
    """
    return {"message" : "Key set"}

@app.post("/symmetric/encode")
async def post_symmetric_encode(message : Message):
    """Encrypts message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        [type]: [description]
    """
    return message

@app.post("/symmetric/encode")
async def post_symmetric_decode(message : Message):
    """Decrypts encoded message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        [type]: [description]
    """
    return message

