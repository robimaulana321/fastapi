from fastapi.testclient import TestClient
import string
import random
from main import app
import hashlib

client = TestClient(app)

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

def test_read_person():
    response = client.get("/person")
    assert response.status_code == 200

def test_read_person_id():
    response = client.get("/person/items/2")
    assert response.status_code == 200
    assert response.json() == {
        "employees": [
            [2,"string@gjnasdnabsdaj.com","string","string"]
        ]
    }
    
def test_read_person_not():
    response = client.get("/person/items/foo")
    assert response.status_code == 201
    assert response.json() == {
        "employees": "It Does Not Exist"
    }


def test_create_person():
    phash    = hashlib.md5(res.encode('utf-8')).hexdigest()
    response = client.post(
        "/person/items/",
        json={"email": res+"@gmail.com", "psalt": res, "phash": phash},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee added successfully"
    }


def test_update_person():
    phash = hashlib.md5(res.encode('utf-8')).hexdigest()
    id    = str(3)
    response = client.put(
        "/person/items/"+id,
        json={"email": res+"@gmail.coms", "psalt": res, "phash": phash},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee update successfully"
    }