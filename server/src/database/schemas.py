from pydantic import BaseModel
from typing import Dict, Any, List

""" 
SAMPLE RETURN JSON 


"""
RETURN_JSON = [
    {
        "timestamp": "timestamp",
    }
]


class PriceArray(BaseModel):
    prices: Dict[str, Any]


class PriceBase(BaseModel):
    price_data: List[PriceArray]


class PriceRequestBase(BaseModel):
    symbol: str
    timeframe: str
    from_date: str
    end_date: str
