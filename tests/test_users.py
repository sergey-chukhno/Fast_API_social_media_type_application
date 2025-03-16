from app import schemas
from tests.database import client, session
import pytest

@pytest.fixture
def test_user(session, client):
  user_data = {
    "email": "sergey@gmail.com",
    "password": "password123"
  }
  response = client.post("/users/", json = user_data) 
  assert response.status_code == 201
  print(response.json())
  new_user = response.json()
  new_user['password'] = user_data['password']
  return new_user

# def test_root(client):
#   response = client.get("/")
#   print(response.json().get("message"))
#   assert response.status_code == 200
#   #assert response.json().get("message") == "Hello World"

def test_create_user(client):
  response = client.post(
    "/users/",
    json = {
      "email": "hello123@gmail.com", 
      "password": "password123"
    }
  )
  new_user = schemas.UserOut(**response.json())
  assert new_user.email == "hello123@gmail.com"
  print(response.json())
  assert response.status_code == 201

def test_login_user(test_user, client):
  response = client.post("/login", data = {
      "username": test_user['email'],
      "password": test_user['password']
  }
  )
  login_response = schemas.Token(**response.json())
  payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
  id: str = payload.get("user_id")
  assert response.status_code == 200
  print(response.json())