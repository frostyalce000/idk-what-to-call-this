from fastapi import FastAPI, Request, Response
from src.server.routes.db import api

"""
Router prefix 
"""
DB = "/db"

app = FastAPI()


@app.get("/")
def health_check() -> Response:
    return Response("Success Remote", status_code=200)


app.include_router(api)
