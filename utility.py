from pydantic import BaseModel

# Swagger tags 
tags_metadata = [
    {"name": "Get Methods", "description": "To catch them is my real test"},
    {"name": "Post Methods", "description": "To train them is my cause!"},
    {"name": "Symmetric Methods", "description": "The best set of methods, look those are even symmetrical!"},
    {"name": "Assymetric Methods", "description": "Where do you bury people with OCD? In a symmetry!"},
]

error_messages = {
    "Key not set" : {"message" : "Keys not set, try /asymmetric/key first :)"}
}

class Message(BaseModel):
    value: str

class MessageWithSignature(BaseModel):
    value : str
    signature: str

class Keys(BaseModel):
    private_key : str
    public_key : str

