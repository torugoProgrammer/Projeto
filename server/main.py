from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv
import pymysql
from routes import user_router

pymysql.install_as_MySQLdb()
load_dotenv()

DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()
app.include_router(user_router.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
