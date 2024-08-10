import pandas as pd
from src.database.database import engine, Base
from src.database import models

models.Base.metadata.create_all(bind=engine)

# Sample DataFrame
data = {
    'symbol': ['AAPL', 'GOOGL'],
    'timeframe': ['m1', 'm1'],
    'timestamp': ['2024-08-01 10:00:00', '2024-08-01 10:01:00'],
    'open': [150.0, 2800.0],
    'high': [152.0, 2820.0],
    'low': [149.0, 2790.0],
    'close': [151.0, 2810.0]
}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
# Insert DataFrame into the database
df.to_sql('prices', con=engine, if_exists='append', index=False)
