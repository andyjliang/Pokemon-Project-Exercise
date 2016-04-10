from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

''' 
Goal: emulating a pokemon game with a trainer, and  
Trainer		PokeBank     Pokemon    Item
id 			id           id         id
name 		Box Name     name       name 

'''

Base = declarative_base()

class Trainer(Base):
	__tablename__ = 'trainer'
	id = Column(Integer, primary_key=True)
	name = Column(String(15))

class PokeBank(Base):
	__tablename__ = 'pokebank'
	id = Column(Integer, primary_key=True)
	name = Column(String(15))

class Pokemon(Base):
	__tablename__ = 'pokemon'
	id = Column(Integer, primary_key=True)
	name = Column(String(15))

class Item(Base):
	__tablename__ = 'item'
	id = Column(Integer, primary_key=True)
	name = Column(String(15))
	
engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(engine)