"""Seed file to make sample data for db"""

from os import name
from models import User, db, Tag, Post
from app import app

#Create all tables
db.drop_all()
db.create_all()

river = User(first_name = "River", last_name = "Bottom")
joaquin = User(first_name = "Joaquin", last_name="Pheonix", image_url = "https://picsum.photos/536/354")
summer = User(first_name = "Summer", last_name="Winter")
octavia = User(first_name = "Octavia", last_name="Spencer")

db.session.add_all([river, joaquin, summer, octavia])

db.session.commit()

funny = Tag(name= "funny")
sad = Tag(name= "sad")
happy = Tag(name= "happy")
unbelievable = Tag(name= "unbelievable")
legendary = Tag(name= "legendary")
important = Tag(name= "important")

db.session.add_all([funny, sad, happy, unbelievable, legendary, important])

db.session.commit()

wiwi = Post(title ="wiwi", content="wiwiwoowoo", user_id = '1')
lklajs = Post(title ="lklajs", content="lkasjdf", user_id = '2')

db.session.add_all([wiwi, lklajs])
db.session.commit()

