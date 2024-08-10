import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


db_router = APIRouter()
logger = logging.getLogger(__name__)
