from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:3311@localhost/fastapi'

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
