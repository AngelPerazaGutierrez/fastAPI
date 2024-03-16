from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session

##desde https://fastapi.tiangolo.com/tutorial/ reviso la estructura que me sirve y la aplico acá
# Esta nos define la clase Hero prepara una tabla con los campos descritos


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"  #leda nombre a nuestra base de datos
sqlite_url = f"sqlite:///{sqlite_file_name}" #crea la ruta y la guarda en la variable

engine = create_engine(sqlite_url, echo=True) #toma la ruta guardada y la ejecuta como engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine) #crea la base y las tablas para que podamos ingresar la info


def create_heroes(): #creamos los heros
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson") #hace una instancia de Hero definido en la linea 5, y recibe los params
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session: #tomamos ruta y sobre ella se hace la sesion
        session.add(hero_1) #se añade a los heros que definimos anteriormente
        session.add(hero_2)
        session.add(hero_3)
        session.commit()


if __name__ == "__main__": #se realiza para decir que este es la funcion principal y lo que ejecutará
    create_db_and_tables()
    create_heroes()

