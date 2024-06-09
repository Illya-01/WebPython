from pydantic import BaseModel
from enum import Enum
from typing import Optional


# class Role(str, Enum):
#     admin = "admin"
#     user = "user"


class User(BaseModel):
    username: str
    password: str
    role: str


class Campground(BaseModel):
    title: str
    price: float
    description: str
    image: Optional[str] = None
