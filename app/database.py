from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import config
from app.config import settings

SQL_ALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

Base = declarative_base()

# Dependency 
def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()

while True: 
    try: 
        conn = psycopg2.connect(host='localhost', database='fastapi', user= 'postgres', password="3311", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connected to the database')
        break
    except Exception as e:
        print('Connection failed')
        print(e)
        time.sleep(2)
    
