from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv
import pymysql
from routes import user_router

pymysql.install_as_MySQLdb()

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)
    
app = FastAPI()

@app.on_event('startup')
async def create_db():
    SQLModel.metadata.create_all(engine) 
    
app.include_router(user_router.router)

@app.get('/')
def test():
    with Session() as session:
        user = {"id": 0, "name": "dorugo", "cpf": "12312312398"}
        session.add(user)
        session.commit()
        session.refresh(user)
        return user