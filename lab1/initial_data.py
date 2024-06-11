from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models import User, Campground

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()


img_url = "https://imgs.search.brave.com/HnFczZjzsOQ4B_qjw1x_PgtxHrdyH3MoYralmgSbOrU/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE0/NzYwNDE4MDA5NTkt/MmY2YmI0MTJjOGNl/P3E9ODAmdz0xMDAw/JmF1dG89Zm9ybWF0/JmZpdD1jcm9wJml4/bGliPXJiLTQuMC4z/Jml4aWQ9TTN3eE1q/QTNmREI4TUh4elpX/RnlZMmg4TVRaOGZH/TmhiWEJuY205MWJt/UjhaVzU4TUh4OE1I/eDhmREE9"

users = [
    {
        "username": "admin1",
        "password": "admin1",
        "role": "admin",
    },
    {
        "username": "admin2",
        "password": "admin2",
        "role": "admin",
    },
    {
        "username": "user1",
        "password": "user1",
        "role": "user",
    },
    {
        "username": "user2",
        "password": "user2",
        "role": "user",
    },
]


campgrounds = [
    {
        "title": "Bukovel",
        "description": "Beautiful view by Carpathian Mountains in Ukraine 🏔️",
        "location": "Bykovel, Ukraine",
        "price": 25,
        "image": img_url,
    },
    {
        "title": "Somewhere Over the Rainbow Campground 🌈",
        "description": "A beautiful campground with a rainbow view!",
        "location": "Sevastopol, Ukraine",
        "price": 12,
        "image": img_url,
    },
    {
        "title": "Campground by the Lake 🏞️",
        "description": "A beautiful campground by the lake!",
        "location": "Kolomyia, Ukraine",
        "price": 10,
        "image": img_url,
    },
    {
        "title": "Campground in the Mountains 🏔️",
        "description": "A beautiful campground in the mountains!",
        "location": "Verkhovyna, Ukraine",
        "price": 15,
        "image": img_url,
    },
    {
        "title": "Campground by the See 🌊",
        "description": "A beautiful campground by the see!",
        "location": "Odesa, Ukraine",
        "price": 20,
        "image": img_url,
    },
    {
        "title": "Campground in the Forest 🌲",
        "description": "A beautiful campground in the forest!",
        "location": "Mygove, Ukraine",
        "price": 18,
        "image": img_url,
    },
]


for user in users:
    db_user = User(**user)
    db.add(db_user)
db.commit()
print("Users added to the database")

for campground in campgrounds:
    campground["author_id"] = (
        db.query(User).filter(User.username == users[0]["username"]).first().id
    )
    db.add(Campground(**campground))
db.commit()
print("Campgrounds added to the database")
