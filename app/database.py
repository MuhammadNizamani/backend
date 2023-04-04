import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from psycopg2.extras import RealDictCursor


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesful!")
#         break
#     except Exception as error:
#         print("Database fail to connect")
#         print("error is ", error)
#         time.sleep(3)
