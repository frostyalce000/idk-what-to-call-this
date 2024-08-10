from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.definitions.credentials import EnvVariables

conn_str = EnvVariables.database_url()
# Create an engine
engine = create_engine(conn_str)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example: Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")

# Don't forget to close the session when done
session.close()