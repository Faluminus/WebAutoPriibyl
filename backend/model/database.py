from sqlmodel import SQLModel, Field, create_engine
from  ..variables import *

POSTGRESQL_FILE_NAME = ""
POSTGRE_URL = ""

class PartFilter(SQLModel, table=True):
    pass

class CarFilter(SQLModel, table=True):
    pass

class Car(SQLModel, table=True):
    pass

class Part(SQLModel, table=True):
    pass

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db_and_tables()