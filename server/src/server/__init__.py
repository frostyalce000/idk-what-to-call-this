import logging

import sqlalchemy.exc
from fastapi import FastAPI

from src.database import SessionLocal, engine
from src.database import models

logger = logging.getLogger(__name__)
app = FastAPI()


def initialize_engine() -> bool:
    try:
        models.Base.metadata.create_all(bind=engine)
        logger.info(f"Successfully established database connection.")
        return True
    except sqlalchemy.exc.OperationalError as o:
        logger.error(f"Failed to create engine. Not connected to database. Error: {o}")
    except Exception as e:
        logger.error(f"Failed to create engine. An unknown error occurred: {e}")
    return False


initialize_engine()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
