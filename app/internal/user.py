from fastapi import APIRouter
from fastapi import FastAPI
from prisma import Prisma
from schema import user

route       = APIRouter()
UserCreate  = user.UserCreate
UserRead    = user.UserRead

@route.get("/")
async def read_data(one=False):
    async with Prisma() as db:
        data = await db.user.find_many()
    return  {"detail": data}

@route.get("/{id}")
async def read_data(id:int):
    async with Prisma() as db:
        data = await db.user.find_many(
            where=
                    {
                        'id':id
                    }
        )
    return  {"detail": data}

@route.post("/")
async def create_user(user: UserCreate):
    async with Prisma() as db:
        data = await db.user.create(
            data=user.model_dump()
        )
    return data

@route.put("/{id}")
async def update_user(id: int, user: UserCreate):
    async with Prisma() as db:
        data = await db.user.update(
            where={"id": id},
            data=user.model_dump()
        )
    return data

@route.delete("/{id}")
async def update_user(id: int,):
    async with Prisma() as db:
        data = await db.user.delete(
            where={"id": id}
        )
    return data