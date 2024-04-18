from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from typing import List
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get("/users", response_model=List[User], tags=["users"])
def get_users():
    users_data = conn.execute(users.select()).fetchall()
    user_list = []
    for user in users_data:
        # Convierte la tupla en un diccionario
        user_dict = dict(zip(users.columns.keys(), user))
        user_list.append(user_dict)
    return user_list

@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first

@user.get("/users/{id}", tags=["users"], response_model=User, description="Get a single user by Id",)
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: int, user: User):
    conn.execute(users.update().values(name=user.name,
                email= user.email, 
                password=f.encrypt(user.password.encode("utf-8"))
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()