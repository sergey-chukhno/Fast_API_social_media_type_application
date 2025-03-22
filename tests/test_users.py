from app import schemas
from jose import jwt
from app.config import settings
import pytest



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
  payload = jwt.decode(login_response.access_token, settings.secret_key, algorithms=[settings.algorithm])
  id: str = payload.get("user_id")
  assert id == test_user['id']
  assert login_response.token_type == "bearer"
  assert response.status_code == 200
  print(response.json())