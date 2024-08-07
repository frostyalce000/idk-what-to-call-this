from fastapi import FastAPI, Request, Response


app = FastAPI()


@app.get("/")
def health_check(request: Request) -> Response:
    return Response("Success Remote", status_code=200)
