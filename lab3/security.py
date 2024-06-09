from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from models import Role, User
from database import users_db


security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    user = users_db.find_one({"username": credentials.username})

    if not user or user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"Authenticate": "Basic"},
        )

    print(f"get_current_user: {user}")
    return User(**user)


def get_current_admin(user: User = Depends(get_current_user)):
    print(f"get_current_admin: {user}")

    if user.role != Role.admin:
        print(user.role)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    return user
