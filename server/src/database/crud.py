from sqlalchemy.orm import Session
from src.database import models, schemas
import logging

logger = logging.getLogger(__name__)


def get_price_data(db: Session, request: schemas.PriceRequestBase):
    logger.info(f"Getting price data")
    price = models.Price
    values = db.query(models.Price).filter(price.symbol == request.symbol).filter(price.timeframe == request.timeframe).limit(100).all()
    return values
