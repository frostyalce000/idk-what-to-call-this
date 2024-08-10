import logging

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from src.database.schemas import PriceRequestBase
from src.server import get_db
from src.database import crud

db_router = APIRouter()
logger = logging.getLogger(__name__)

api = APIRouter()


@api.get("/api/price/")
def get_price_data(db: Session = Depends(get_db)):
    try:
        symbol = "AAPL"
        timeframe = "m1"
        price_request = PriceRequestBase(
            symbol=symbol,
            timeframe=timeframe,
            from_date="",
            end_date=""
        )
        prices = crud.get_price_data(db, price_request)
        print(prices)
        return Response(status_code=200)
    except Exception as e:
        logger.error(f"Failed to get price data. Error: {e}", exc_info=True)