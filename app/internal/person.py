from fastapi import APIRouter
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config import connect
from schema import person
import json

route   = APIRouter()
db      = connect.conn
cursor  = db.cursor()

Persons = person.Persons

@route.get("/")
async def read_data(one=False):
    cursor.execute("SELECT * FROM users")

    data_arr = [
                    dict((cursor.description[i][0], value)
                    for i, value in enumerate(row)) 
                        for row in cursor.fetchall()
                ]
    
    isi = (data_arr[0] if data_arr else None) if one else data_arr
    json_output = json.dumps({"employees": isi})
    return json.loads(json_output)

@route.get("/items/{item_id}",status_code=200)
async def read_user_item(item_id: str):
    cursor.execute("SELECT * FROM users where id='"+item_id+"'")
    result = cursor.fetchall()
    row_count = cursor.rowcount
    if row_count == 0:
        item = {"employees": "It Does Not Exist"}
        return JSONResponse(status_code=201, content=item)
    else:
        return {"employees": result}
    
@route.post("/items/")
async def create_item(data:Persons):
    sql = "INSERT INTO users (email, password_salt, password_hash) VALUES (%s, %s,%s)"
    val = (data.email, data.psalt,data.phash)
    cursor.execute(sql, val)
    db.commit()
    return {"message": "Employee added successfully"}

@route.put("/items/{id}")
async def create_item(id: str, data:Persons):
    sql = "UPDATE users SET email ='"+data.email+"',password_salt ='"+data.psalt+"',password_hash ='"+data.phash+"' where id='"+id+"'"
    cursor.execute(sql)
    db.commit()
    return {"message": "Employee update successfully"}


@route.delete("/employees/{id}")
async def delete_employee(id: int):
    cursor.execute(f"DELETE FROM users WHERE id = {id}")
    db.commit()
    return {"message": "Employee deleted successfully"}