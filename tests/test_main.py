from fastapi.testclient import TestClient
from main import app

test_key = "ZroWmwN2IZSbIcRN7pjwNeZsVD1wVdCFhUYNpVyGQ9k="

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
    response = client.get("/assymetric/key")
    assert response.status_code == 200
    assert response.json() != None

def test_get_assymetric_get_keys_ssh():
    response = client.get("/assymetric/key/ssh")
    assert response.status_code == 200
    assert response.json() != None

def test_post_assymetric_set_key(): 
    response = client.post("/assymetric/key")
    assert response.status_code == 201
    assert response.json() == {"message" : "Key set"}

def test_post_assymetric_verify():
    response = client.post("/assymetric/verify")
    assert response.status_code == 202
    assert response.json() == {"message" : "It was encoded with set key"}

def test_post_assymetric_sign():
    response = client.post("/assymetric/sign")
    assert response.status_code == 202
    assert response.json() == {"message" : "Message signed with set key"}

def test_post_assymetric_encode():
    response = client.post("/assymetric/encode")
    assert response.status_code == 202
    assert response.json() != None


def test_post_assymetric_decode():
    response = client.post("/assymetric/decode")
    assert response.status_code == 202
    assert response.json() != None
