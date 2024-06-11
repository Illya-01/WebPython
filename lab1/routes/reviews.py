from fastapi.responses import JSONResponse
from models import Review
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from database import get_db


router = APIRouter()


@router.post("/campgrounds/{campground_id}/reviews")
def create_review(
    data=Body(),
    db: Session = Depends(get_db),
):
    review = Review(
        text=data["text"],
        rating=data["rating"],
        author_id=data["review_author_id"],
        campground_id=data["campground_id"],
    )

    db.add(review)
    db.commit()
    db.refresh(review)
    return review


@router.delete("/campgrounds/{campground_id}/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()

    if review is None:
        return JSONResponse(status_code=404, content={"detail": "Review not found"})

    db.delete(review)
    db.commit()
    return {"message": "Review deleted"}
