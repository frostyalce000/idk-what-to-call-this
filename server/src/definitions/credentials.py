from dotenv import load_dotenv
import os


load_dotenv()


class Credentials:
    @classmethod
    def db_username(cls) -> str:
        return os.getenv("DB_USERNAME")

    @classmethod
    def db_password(cls) -> str:
        return os.getenv("DB_PASSWORD")


class EnvVariables:
    @classmethod
    def db_host(cls) -> str:
        return os.getenv("DB_HOST")

    @classmethod
    def db_port(cls) -> str:
        return os.getenv("DB_PORT")

    @classmethod
    def db_name(cls) -> str:
        return os.getenv("DB_NAME")

    @classmethod
    def database_url(cls) -> str:
        return os.getenv("DATABASE_URL")