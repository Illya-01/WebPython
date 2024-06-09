from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models import User
from security import users_db

router = APIRouter()
views = Jinja2Templates(directory="views")


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return views.TemplateResponse("index.html", {"request": request})


@router.post("/users/login", response_model=User)
async def login(user: User):
    print(f"entered login: {user.username} {user.password} {user.role}")

    user_in_db = users_db.find_one({"username": user.username})
    if (
        not user_in_db
        or user_in_db["password"] != user.password
        or user_in_db["role"] != user.role
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"Authenticate": "Basic"},
        )
    return User(**user_in_db)
