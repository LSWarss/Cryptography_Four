from fastapi import FastAPI, Request
from pydantic import BaseModel
from encryptions.symetric import Symmetric

app = FastAPI()
symetric = None

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
    return Symmetric.generate_key()

@app.post("/symmetric/")
async def post_key(key):
    """Sets symmetric key posted in the reques

    Args:
        key HEX: Symmetric Key

    Returns:
        JSON: Message if the key was succesfully set
    """
    global symetric
    symetric = Symmetric(key)
    return {"message" : "Key set"}

@app.post("/symmetric/encode")
async def post_symmetric_encode(message : Message):
    """Encrypts message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        bytes: Encoded message in HEX
    """
    return symetric.encode(message.value)

@app.post("/symmetric/decode")
async def post_symmetric_decode(message : Message):
    """Decrypts encoded message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        str: Decoded string
    """
    return symetric.decode(message.value)
