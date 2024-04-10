import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email=Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """
    

class User(Base):
    __tablename__="User"
    user_id = Column(Integer, primary_key=True) 
    user_Name= Column(String(50), unique=True, nullable=False, )
    name=Column(String(25), nullable=False)
    last_name= Column(String(25), nullable=False)
    subscription_date=Column(String(20), nullable=False) 
    email=Column(String(50), unique=True, nullable=False) 
    password=Column(String(50), unique=True, nullable=False)

class Planets(Base):
    __tablename__="Planets"
    planet_id= Column(Integer, primary_key=True)
    name= Column(String(25), nullable=False)
    rotation_period= Column(Integer, nullable=True)
    diameter= Column(Integer, nullable=True)
    orbital_period=Column(Integer, nullable=True)
    gravity= Column(Integer, nullable=True)
    population= Column( Integer, nullable= True)
    climate= Column (String(20), nullable= True)
    terrain= Column(String(20), nullable= True)
    surface_Water= Column(String(20), nullable= True)
    residents= Column (Integer, nullable= True)

class Characters(Base):
    __tablename__ ="Characters"
    character_id= Column(Integer, primary_key=True)
    character_name= Column(String(20), unique=True, nullable= False)
    height= Column(Integer, nullable=True)
    mass= Column(Integer, nullable= True)
    birth_year = Column(Integer, nullable = True)
    gender= Column(String(10), nullable= True)
    homeworld= Column(String(20), nullable= True)

class Favourite_planets(Base):
    __tablename__= "Favourite Planets"
    fav_planets_id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    planets_id = Column(Integer, ForeignKey('Planets.planet_id'))
    planet_name= Column(String(50), unique= True, nullable = False)

class Favourite_characters(Base):
    __tablename__="Favourite Characters"
    fav_character_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    character_id = Column(Integer, ForeignKey('Characters.character_id'))
    character_name= Column(String(20), unique=True, nullable= False)
    
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
