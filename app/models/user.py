# from sqlalchemy import Table,Column
# from config import connect

# users = Table(
#     'users',connect,
#     Column('id',int,primary_key=True),
#     Column('name',str(255)),
#     Column('email',str(255)),
#     Column('password',str(255)),
# )
# models/pegawai.py
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.sqltypes import Date
from config import connect

metadata = MetaData()
user = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String(255)),
    Column("password_salt", String(255)),
    Column("password_hash", String(255)),
)