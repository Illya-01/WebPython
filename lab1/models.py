from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Campground(Base):
    __tablename__ = "campgrounds"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    price = Column(Integer)
    image = Column(String, nullable=True)

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="campgrounds")
    reviews = relationship("Review", back_populates="campground")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)

    campgrounds = relationship("Campground", back_populates="author")
    reviews = relationship("Review", back_populates="author")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    rating = Column(Integer)

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="reviews")

    campground_id = Column(Integer, ForeignKey("campgrounds.id"))
    campground = relationship("Campground", back_populates="reviews")
