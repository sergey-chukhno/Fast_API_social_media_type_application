from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.database import get_db, Base
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import command

# SQL_ALCHEMY_DATABASE_URL = "postgresql://postgres:3311@localhost:5432/fastapi_test"
SQL_ALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}_test'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

client = TestClient(app)

@pytest.fixture(scope="function")
def session():
   Base.metadata.drop_all(bind=engine)
   Base.metadata.create_all(bind=engine)
   db = TestingSessionLocal()
   try: 
      yield db
      db.commit() 
   finally: 
      db.close()

@pytest.fixture(scope="function")
def client(session): 
   # Dependency 
  def override_get_db(): 
      try: 
          yield session
      finally: 
        session.close()
  app.dependency_overrides[get_db] = override_get_db
  yield TestClient(app)

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