from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from db_setup import Base, Trainer, PokeBank, Pokemon, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pdb

app = Flask(__name__)
''' 
Route Road Map
main.html: displays Trainer, Pokebank, Pokemons, Items summaries
trainer.html: shows trainer info => badges, pokemon held, description
pokebank.html: shows pokebank info => all boxes and the pokemon in there
pokemons.html: shows pokemon info => registry of all pokemon caught (and seen?)
items.html: shows all 
'''
engine = create_engine('sqlite:///pokemon.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/index')
def mainPage():
	trainers = session.query(Trainer)
	pokemons = session.query(Pokemon)
	items = session.query(Item)
	pokebank = session.query(PokeBank)
	return render_template('index.html', trainers=trainers, pokemons=pokemons, items=items, pokebank=pokebank)

@app.route('/trainer')
def showTrainer():
	pass

@app.route('/pokedex')
def showPokedex():
	pass

@app.route('/item')
def showItemList():
	pass

if __name__ == '__main__':
    app.secret_key="gotta catch them all"
    app.debug = True #server reloads itself when change observed
    app.run(host = '0.0.0.0', port = 5000)