import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    image_src = Column(String(500), nullable = False)
    likes = Column(Integer, nullable = False) 
    description = Column(String(500), nullable = False)
    liked = relationship("liked")

class Liked(Base):
    __tablename__ = "liked"
    id = Column(Integer, primary_key = True)
    number_of_likes = Column(Integer, nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    userlikes = relationship("userlikes")

class Userlikes(Base):
    __tablename__ = "userlikes"
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    favorite_posts = relationship("user")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False)
    password = Column(String(500), nullable = False)
    userlikes = Column(Integer, ForeignKey("userlikes.id"), nullable = False)
    user_profile = relationship("profile", backref = "user")

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    description = Column(String(50), nullable = True)
    profile_pic_src = Column(String(500), nullable = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
