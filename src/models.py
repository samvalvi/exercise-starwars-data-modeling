import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password= Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table planet
    # Notice that each column is also a normal Python instance attribute.
    id=Column(Integer, primary_key=True)
    favorite_id=Column(Integer, ForeignKey('Favorite.id'))
    name=Column(String(250), nullable=False)
    climate=Column(String(250), nullable=False)
    population=Column(Integer, nullable=False)
    orbital_period=Column(Integer, nullable=False)
    rotation_period=Column(Integer, nullable=False)
    diameter=Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table character
    # Notice that each column is also a normal Python instance attribute.
    id=Column(Integer, primary_key=True)
    favorite_id=Column(Integer, ForeignKey('Favorite.id'))
    name=Column(String(250), nullable=False)
    birth=Column(String(250), nullable=False)
    gender=Column(String(250), nullable=False)
    height=Column(Integer, nullable=False)
    skin=Column(String(250), nullable=False)
    eye=Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'Favorite'
    # Here we define columns for the table favorite
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('User.id'))
    planet_id=Column(Integer, ForeignKey('Planet.id'))
    character_id=Column(Integer, ForeignKey('Character.id'))

    def tod_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')