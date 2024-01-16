from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from external import bpjs
from internal import person,user

# app = FastAPI()
from config import connect

app = FastAPI(
    title="FastAPI",
    # docs_url=None,
    # redoc_url=None,
    openapi_url="/api/openapi.json"
)

app.include_router(
    bpjs.route,
    tags=["bpjs"],
    prefix="/bpjs"
)

app.include_router(
    person.route,
    tags=["internal"],
    prefix="/person"
)

app.include_router(
    user.route,
    tags=["internal orm"],
    prefix="/user"
)

@app.get("/")
def main():
    return {"message": "Hello Bigger Applications!"}