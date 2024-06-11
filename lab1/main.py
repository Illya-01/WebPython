# import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routes.campgrounds import router as campgrounds_router
from routes.users import router as users_router
from routes.reviews import router as reviews_router


app = FastAPI()
views = Jinja2Templates(directory="views")
app.mount("/public", StaticFiles(directory="public"), name="public")


app.include_router(reviews_router)
app.include_router(campgrounds_router, prefix="/campgrounds")
app.include_router(users_router, prefix="/users")


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return views.TemplateResponse("campgrounds/index.html", {"request": request})


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
