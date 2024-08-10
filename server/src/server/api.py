from fastapi import FastAPI, Request, Response

"""
Router prefix 
"""
DB = "/db"

app = FastAPI()


@app.get("/")
def health_check(request: Request) -> Response:
    return Response("Success Remote", status_code=200)
