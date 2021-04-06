from fastapi.testclient import TestClient
from main import app

test_key = "ZroWmwN2IZSbIcRN7pjwNeZsVD1wVdCFhUYNpVyGQ9k="
test_message = "It's a trap!"
test_encrypted_string = "13303aa602e4bf9b9e5d813954baf9e62a776a7dba4135a1f7c3c3430ba6e8437126f360889f5e12143b921c2c977511469ff6d1f8241e48bee2c1877c93e12e530ecf53ca91b916805344a0fbec4e1fc7f0741049cc3cb336e74b0b372b1d424f0f8f342f7ca2d487b26d3baff44b7fcf46ea7ef5222987f665d7fa6545422ce84f2c594103edf1a60d3de9def00502869de9df272e986c636bae40a6df406ad1576f3d70d0b935ec4e0583492e4f0cbd06d0ac7062c995250cec0e9735e33a0b16cbfaf65615787dff66295d8c194345e01f89cd43bdca16b320b4d0e6c23d0ce49febde7449654da9bc6bd9548bbadf22f7b89127f4532304cf3f71ae5800"

client = TestClient(app)

def test_test():
    assert 2 == 2

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello cryptography 🤖"}

def test_get_key(): 
    response = client.get("/symmetric/key")
    assert response.status_code == 200
    assert response.json() != None

def test_set_key():
    response = client.post(f'/symmetric/?key={test_key}')
    assert response.status_code == 201
    assert response.json() == {"message" : "Key set"}

def test_post_symmetric_encode():
    response = client.post('/symmetric/encode', json= {"value": "Gdzie noca stapa jez"})
    assert response.status_code == 202
    assert response.json() != None

def test_post_symmetric_decode():
    response = client.post('/symmetric/decode', json= {"value": "gAAAAABgaxioOIcTfz0PYl6SzHB885mfLExImD9Wct1azW6gK814yMS-xRtHwgdyL8otEyIjvwBD5cSDJnY1Kf2-_N2F8bJIscmtgcFZsMKLQJ0iSjChYXM="})
    assert response.status_code == 202
    assert response.json() == "Gdzie noca stapa jez"

def test_get_assymetric_get_keys():
    response = client.get("/asymmetric/key")
    assert response.status_code == 200
    assert response.json() != None

def test_get_assymetric_get_keys_ssh():
    response = client.get("/asymmetric/key/ssh")
    assert response.status_code == 200
    assert response.json() != None

def test_post_assymetric_set_key(): 
    response = client.post("/asymmetric/key")
    assert response.status_code == 201
    assert response.json() == {"message" : "Key set"}

def test_post_assymetric_verify():
    response = client.post("/asymmetric/verify", json={""})
    assert response.status_code == 202
    assert response.json() == {"message" : "It was encoded with set key"}

def test_post_assymetric_sign():
    response = client.post("/asymmetric/sign", json={"value": test_message})
    assert response.status_code == 202
    assert response.json() == {"message" : "Message signed with set key"}

def test_post_assymetric_encode():
    response = client.post("/asymmetric/encode", json={"value": test_message})
    assert response.status_code == 202
    assert response.json() != None


def test_post_assymetric_decode():
    response = client.post("/asymmetric/decode", json={"value": test_encrypted_string})
    assert response.status_code == 202
    assert response.json() != None
