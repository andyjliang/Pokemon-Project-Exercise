from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup.py import Base, Trainer, PokeBank, Pokemon, Item

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

trainer1 = Trainer(name="Ash Ketchum")
pokemon1 = Pokemon(name="Pikachu")
pokemon2 = Pokemon(name="Charmander")
pokemon3 = Pokemon(name="Squirtle")
pokemon4 = Pokemon(name="Bulbasaur")
pokemon5 = Pokemon(name="Pidgeotto")
pokemon6 = Pokemon(name="Butterfree")
box1 = PokeBank(name="Box1")
item = Pokemon(name="Everstone")

session.add(trainer1)
session.add(pokemon1)
session.add(pokemon2)
session.add(pokemon3)
session.add(pokemon4)
session.add(pokemon5)
session.add(pokemon6)
session.add(box1)
session.add(item1)
session.commit()

print('successful database population. game on')