from pydantic import BaseModel

class Persons(BaseModel):
    email: str
    psalt: str
    phash: str
