from fastapi import APIRouter, Depends, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from models import Campground, Review, User
from database import get_db


router = APIRouter()
views = Jinja2Templates(directory="views")


# show all campgrounds
@router.get("/", response_class=HTMLResponse)
def get_campgrounds(request: Request, db: Session = Depends(get_db)):
    campgrounds = db.query(Campground).all()
    return views.TemplateResponse(
        "campgrounds/show-all.html", {"request": request, "campgrounds": campgrounds}
    )


# create campground
@router.get("/new", response_class=HTMLResponse)
def new_campground(request: Request):
    return views.TemplateResponse("campgrounds/new-camp.html", {"request": request})


@router.post("/")
def create_campground(data=Body(), db: Session = Depends(get_db)):
    try:
        campground = Campground(
            title=data["title"],
            description=data["description"],
            location=data["location"],
            price=data["price"],
            image=data["image"],
            author_id=data["author_id"],
        )

        db.add(campground)
        db.commit()
        db.refresh(campground)
        return campground
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "Could not create a campground", "error": str(e)},
        )


# show one campground
@router.get("/{id}", response_class=HTMLResponse)
def get_campground(id, request: Request, db: Session = Depends(get_db)):
    campground = db.query(Campground).filter(Campground.id == id).first()

    if campground == None:
        return views.TemplateResponse(
            "error.html",
            {"request": request, "message": "Campground not found", "statusCode": 404},
        )

    reviews = db.query(Review).filter(Review.campground_id == id).all()
    author = db.query(User).filter(User.id == campground.author_id).first()

    return views.TemplateResponse(
        "campgrounds/show-camp.html",
        {
            "request": request,
            "campground": campground,
            "author": author,
            "reviews": reviews,
        },
    )


# edit campground
@router.get("/{id}/edit", response_class=HTMLResponse)
def edit_campground(id, request: Request, db: Session = Depends(get_db)):
    campground = db.query(Campground).filter(Campground.id == id).first()

    if campground == None:
        return views.TemplateResponse(
            "error.html",
            {"request": request, "message": "Campground not found", "statusCode": 404},
        )
    return views.TemplateResponse(
        "campgrounds/edit-camp.html", {"request": request, "campground": campground}
    )


# update campground
@router.put("/{id}")
def edit_campground(data=Body(), db: Session = Depends(get_db)):
    campground = db.query(Campground).filter(Campground.id == data["id"]).first()

    if campground == None:
        return JSONResponse(
            status_code=404, content={"message": "Campground not found"}
        )

    campground.title = data["title"]
    campground.description = data["description"]
    campground.location = data["location"]
    campground.price = data["price"]
    campground.image = data["image"]

    db.commit()
    db.refresh(campground)
    return campground


# delete campground
@router.delete("/{id}")
def delete_campground(id, db: Session = Depends(get_db)):
    campground = db.query(Campground).filter(Campground.id == id).first()

    if campground == None:
        return JSONResponse(
            status_code=404, content={"message": "Campground not found"}
        )

    db.delete(campground)
    db.commit()
    return {"message": "Campground deleted"}
