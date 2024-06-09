from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["camp"]
collection = db["campground"]

campgrounds = [
    {
        "title": "Bukovel",
        "price": 25,
        "description": "Beautiful view by Carpathian Mountains in Ukraine 🏔️",
        "image": "https://source.unsplash.com/random?carpathian-mountains",
    },
    {
        "title": "Somewhere Over the Rainbow Campground 🌈",
        "price": 12,
        "description": "A beautiful campground with a rainbow view!",
        "image": "https://source.unsplash.com/random?camp",
    },
    {
        "title": "Campground by the Lake 🏞️",
        "price": 10,
        "description": "A beautiful campground by the lake!",
        "image": "https://source.unsplash.com/random?camp",
    },
    {
        "title": "Campground in the Mountains 🏔️",
        "price": 15,
        "description": "A beautiful campground in the mountains!",
        "image": "https://source.unsplash.com/random?camp",
    },
    {
        "title": "Campground by the Ocean 🌊",
        "price": 20,
        "description": "A beautiful campground by the ocean!",
        "image": "https://source.unsplash.com/random?camp",
    },
    {
        "title": "Campground in the Forest 🌲",
        "price": 18,
        "description": "A beautiful campground in the forest!",
        "image": "https://source.unsplash.com/random?camp",
    },
]

# collection.delete_many({})
collection.insert_many(campgrounds)
