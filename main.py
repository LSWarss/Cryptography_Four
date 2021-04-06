from fastapi import FastAPI, Request
from encryptions.symetric import Symmetric
from encryptions.asymetric import Assymetric
from utility import tags_metadata, Message, Keys

symetric = None
assymetric = None

app = FastAPI(openapi_tags=tags_metadata)

# Root Routes and Utils

@app.get("/", tags=["Get Methods"])
async def root(): 
    return {"message": "Hello cryptography 🤖"}

# Symmetric Routes

@app.get("/symmetric/key", tags=["Get Methods", "Symmetric Methods"])
async def get_key():
    """Returns random symmetric key

    Returns:
        HEX: Symmetric Key
    """
    return Symmetric.generate_key()

@app.post("/symmetric/", tags=["Post Methods", "Symmetric Methods"],  status_code=201)
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

@app.post("/symmetric/encode", tags=["Post Methods","Symmetric Methods"], status_code=202)
async def post_symmetric_encode(message : Message):
    """Encrypts message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        bytes: Encoded message in HEX
    """
    return symetric.encode(message.value)

@app.post("/symmetric/decode", tags=["Post Methods","Symmetric Methods"],  status_code=202)
async def post_symmetric_decode(message : Message):
    """Decrypts encoded message send by a user when symmetric key is set

    Args:
        message (Message): Message base model 

    Returns:
        str: Decoded string
    """
    return symetric.decode(message.value)

# Assymetric Routes

@app.get("/asymmetric/key", tags=["Get Methods","Assymetric Methods"])
async def get_assymetric_key():
    """ Returns new public and private key in HEX and sets it up on server

    Returns:
        [type]: [description]
    """
    global assymetric
    assymetric = Assymetric()
    keys = assymetric.generate_keys()
    return {"Private key": keys["Private key"], "Public key": keys["Public key"]}

@app.get("/asymmetric/key/ssh", tags=["Get Methods","Assymetric Methods"])
async def get_assymetric_ssh_key():
    """ Returns public and private key in OpenSSH format

    Returns:
        [type]: [description]
    """
    keys = Assymetric.generate_ssh_keys()
    return {"Private key": keys["Private key"], "Public key": keys["Public key"]}

@app.post("/asymmetric/key", tags=["Post Methods","Assymetric Methods"], status_code=201)
async def set_assymetric_key():
    """Sets key on server 

    Returns:
        [type]: [description]
    """
    global assymetric
    assymetric = Assymetric()

    return {"message": "Keys set"}

@app.post("/asymmetric/verify", tags=["Post Methods","Assymetric Methods"],  status_code=202)
async def post_assymetric_verify(message : Message):
    """ Using the most recent setting of the key, verify if the message was signed by the key

    Args:
        message (Message): Message to verify

    Returns:
        [type]: [description]
    """
    return {"message" : "It was encoded with set key"}

@app.post("/asymmetric/sign", tags=["Post Methods","Assymetric Methods"],  status_code=202)
async def post_assymetric_sign(message : Message):
    """ Using the most recent setting of the key, signs the message and returns

    Args:
        message (Message): Message to sign

    Returns:
        [type]: [description]
    """
    return {"message" : "Message signed with set key"}

@app.post("/asymmetric/encode", tags=["Post Methods","Assymetric Methods"],  status_code=202)
async def post_assymetric_encode(message : Message):
    """Encodes message sent to the server

   Args:
        message (Message): Message to encode

    Returns:
        [type]: [description]
    """
    return {"message" : assymetric.encrypt(message.value)} if assymetric != None else {"message" : "Keys not set, try /asymmetric/key first :)"}

@app.post("/asymmetric/decode", tags=["Post Methods","Assymetric Methods"],  status_code=202)
async def post_assymetric_decode(message : Message):
    """Decodes message sent to the server

    Args:
        message (Message): Message to decode

    Returns:
        [type]: [description]
    """
    return {"message": "Key set"}