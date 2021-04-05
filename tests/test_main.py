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
    assert response.status_code == 200
    assert response.json() == {"message" : "Key set"}

def test_post_symmetric_encode():
    response = client.post('/symmetric/encode', json= {"value": "Gdzie noca stapa jez"})
    assert response.status_code == 200
    assert response.json() != None

def test_post_symmetric_decode():
    response = client.post('/symmetric/decode', json= {"value": "gAAAAABgaxioOIcTfz0PYl6SzHB885mfLExImD9Wct1azW6gK814yMS-xRtHwgdyL8otEyIjvwBD5cSDJnY1Kf2-_N2F8bJIscmtgcFZsMKLQJ0iSjChYXM="})
    assert response.status_code == 200
    assert response.json() == "Gdzie noca stapa jez"