import uvicorn
from fastapi import FastAPI

from routes.campgrounds import router as campgrounds_router
from routes.login import router as login_router


app = FastAPI()


app.include_router(login_router)
app.include_router(campgrounds_router, prefix="/campgrounds")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
