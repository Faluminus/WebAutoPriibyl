import os

from sqlmodel import SQLModel, Field, create_engine, Session, select
from  ..variables import PartDetail, CarDetail
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost:5432/{DB}"

class PartFilters(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

class CarFilter(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Car(CarDetail, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Part(PartDetail, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db_and_tables()