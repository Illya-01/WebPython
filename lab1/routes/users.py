from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse

from database import get_db
from models import User

router = APIRouter()


@router.post("/login")
def login(data=Body(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data["username"]).first()

    if user == None or user.password != data["password"] or user.role != data["role"]:
        return JSONResponse(
            status_code=401, content={"message": "Incorrect username or password"}
        )
    return user
