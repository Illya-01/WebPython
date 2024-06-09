from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import User

users_db = {
    "admin1": {"username": "admin1", "password": "admin1", "role": "admin"},
    "user1": {"username": "user1", "password": "user1", "role": "user"},
}

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    user = users_db.get(credentials.username)
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

    if user.role != "admin":
        print(user.role)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    return user
