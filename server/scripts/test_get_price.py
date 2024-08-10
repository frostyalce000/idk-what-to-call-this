from src.database.crud import get_price_data
from src.database.schemas import PriceRequestBase

if __name__ == "__main__":
    price_request = PriceRequestBase(
        symbol="AAPL",
        timeframe="m1",
        from_date="",
        to_date=""
    )
    print(get_price_data())
