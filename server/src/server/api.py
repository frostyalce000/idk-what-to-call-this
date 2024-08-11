from fastapi import FastAPI, Request, Response, HTTPException
from src.server.routes.db import api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.definitions.credentials import EnvVariables

"""
Router prefix 
"""
DB = "/db"

app = FastAPI()


@app.get("/")
def health_check() -> Response:
    return Response("Success Remote", status_code=200)


@app.get("/database")
def check_database_connection():
    # DATABASE_URL = "postgresql+psycopg2://myuser:password@localhost:5433/py_strats_server"
    # DATABASE_URL = "postgresql://postgres:kr24TDThnM7vPoP@test-postgres.flycast:5433/test_database"
    DATABASE_URL = EnvVariables.database_url()
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    try:
        with engine.connect() as connection:
            return Response(status_code=200, content="Connected successfully.")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to connect to database")

app.include_router(api)
