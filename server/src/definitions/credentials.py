from dotenv import load_dotenv
import os


load_dotenv()


class Credentials:
    pass


class EnvVariables:
    @classmethod
    def database_url(cls) -> str:
        return os.getenv("DATABASE_URL")
