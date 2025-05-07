from fastapi.testclient import TestClient
from intro_setup.second_file import app as second_app

client = TestClient(second_app)

def test_read_home():
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "vakam da mapla home la irunthu!"}

def test_read_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message_1": "vakam da mapla about la irunthu!", "message_2": "Nan tha Dinesh J!"}
