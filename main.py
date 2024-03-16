from fastapi import FastAPI, Request #se importan las librerias a utilizar
from sqlmodel import Session  #importo a sesion de Sqlmodel

from create_db import Hero, engine # de igual forma se importa a Hero de la creacion de la base y al motor

my_backend= FastAPI() #hago la instancia de fastAPI y la pongo en el nombre de app, por lo general asi se llama, en este ejemplo my_backend

#con @llamo mi instacncia y pongo el metodo get, este no tiene cuerpo para enviar parametros desde el back
#nos retorna el mensaje "hello World"

@my_backend.get("/")
def hello_world():
    return {'msg': 'Hello World'}

#debeos dejar dos espacios entre def para que python no bote error


@my_backend.post("/") #el el body de post podemos pasar estos paramentros como nombre, nombre secreto y edad para que los guarde en db
async def add_hero(request: Request): #funcion asyncrona que añade al hero desde el body del POST
    body = await request.json() #uso Json ya que desde el post.body estoy recibiendo los datos con Await espero hasta que responda el post
    hero = Hero(name=body['name'], secret_name=body['secret_name'], age=body['age']) #llamo a cada item del diccionario en body
    with Session(engine) as session: #llamo la sesion
        session.add(hero) #add al hero a la base
        session.commit() # hago el commit del hero

    return {"msg": "Hero added successfully."} #mensaje retornado en back si fue exitoso