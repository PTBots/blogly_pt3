"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Default_Image_url = 'https://freepikpsd.com/file/2019/10/default-profile-image-png-1-Transparent-Images.png'

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, unique=False)
    last_name = db.Column(db.String, nullable=False, unique=False)
    image_url = db.Column(db.Text, nullable=True, default=Default_Image_url)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Returns the full name"""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    added_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def date(self):
        """Returns the date of the post"""

        return('{:%Y-%m-%d @ %H:%M:%S}'.format(datetime.datetime.now()))

class PostTag(db.Model):
    """Tag on a post"""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    posts = db.relationship('Post', secondary="posts_tags", backref="tags")

def connect_db(app):
    """connect to database"""

    db.app = app
    db.init_app(app)