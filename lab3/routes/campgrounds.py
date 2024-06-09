from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId

from models import Campground, User
from security import get_current_admin
from database import collection

router = APIRouter()
views = Jinja2Templates(directory="views")


# show all campgrounds
@router.get("/", response_model=list[Campground], response_class=HTMLResponse)
async def get_campgrounds(request: Request):
    try:
        campgrounds = list(collection.find())
        for campground in campgrounds:
            campground["id"] = str(campground["_id"])
        return views.TemplateResponse(
            "campgrounds.html", {"request": request, "campgrounds": campgrounds}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# create campground
@router.get("/new", response_class=HTMLResponse)
async def show_campground_create_page(request: Request):
    return views.TemplateResponse("new-camp.html", {"request": request})


@router.post("/", response_model=Campground)
async def create_campground(
    campground: Campground, current_user: User = Depends(get_current_admin)
):
    try:
        result = collection.insert_one(campground.model_dump())
        return {"id": str(result.inserted_id), **campground.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# show single campground
@router.get(
    "/{campground_id}",
    response_model=Campground,
    response_class=HTMLResponse,
)
async def get_campground(campground_id: str, request: Request):
    campground = collection.find_one({"_id": ObjectId(campground_id)})
    if campground is not None:
        campground["id"] = str(campground["_id"])
        return views.TemplateResponse(
            "show-camp.html", {"request": request, "campground": campground}
        )
    else:
        raise HTTPException(status_code=404, detail="Campground not found")


# update campground
@router.get("/{campground_id}/edit", response_class=HTMLResponse)
async def show_campground_update_page(campground_id: str, request: Request):
    campground = collection.find_one({"_id": ObjectId(campground_id)})
    if campground is not None:
        campground["id"] = str(campground["_id"])
        return views.TemplateResponse(
            "edit-camp.html", {"request": request, "campground": campground}
        )
    else:
        raise HTTPException(status_code=404, detail="Campground not found")


@router.put("/{campground_id}", response_model=Campground)
async def update_campground(
    campground_id: str,
    campground: Campground,
    current_user: User = Depends(get_current_admin),
):
    result = collection.update_one(
        {"_id": ObjectId(campground_id)},
        {"$set": campground.model_dump(exclude_unset=True)},
    )
    if result.matched_count:
        return {"id": campground_id, **campground.model_dump()}
    else:
        raise HTTPException(status_code=404, detail="Campground not found")


# delete campground
@router.delete("/{campground_id}")
async def delete_campground(
    campground_id: str, current_user: User = Depends(get_current_admin)
):
    result = collection.delete_one({"_id": ObjectId(campground_id)})
    if result.deleted_count:
        return {"message": "Campground deleted"}
    else:
        raise HTTPException(status_code=404, detail="Campground not found")
