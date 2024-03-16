This tutorial covers the basics to show how a Python backend works in its simplest form, yet covering avery major concept.

Install Pycharm community edition https://www.jetbrains.com/help/pycharm/installation-guide.html

Based on: https://fastapi.tiangolo.com/tutorial/first-steps/ And also: https://sqlmodel.tiangolo.com/tutorial/ Can also help: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/ Manage multiple versions of Python with pyenv: https://realpython.com/intro-to-pyenv/ SQlite visualizer: https://sqlitebrowser.org/dl/

Example of pyenv

Example of virtual env. to ENTER:source env/bin/activate to LEAVE: deactivate

install FastAPI pip install fastapi==0.83.0

Implement hello world with GET in FastAPI

install pip uvicorn

Run Server
python3.8 -m uvicorn main:my_backend

Go to browser and check hello world message http://127.0.0.1:8000/

Stop Server ctrl + c

Run Server with reload python3.12 -m uvicorn main:app --reload  //sirve para que los cambios se realicen en realtime

See the documentation and play with it http://127.0.0.1:8000/docs

REST
METODOS HTTP:

GET  
POST <=> CREATE
DELETE <=> DELETE
PATCH <=> UPDATE
PUT <=> SOBREESCRIBIR

CODIGOS DE RESPUESTA

200 SUCCESS
300 REDIRECCION
400  ERROR DEL CLIENTE
500  ERROR DEL SERVIDOR


See alternative documentation http://127.0.0.1:8000/redoc

Add or remove async definition

Add a /my/path endpoint

Play with insomnia

Add a POST endpoint

Show possible error with 405 response indicating method not allowed

Show how the debugger works!

add error
run server from Pycharm with Bug execution, with: uvicorn.run('main:app', host='0.0.0.0', port=8000, proxy_headers=True, reload=True)
Use smart import from pycharm
add breakpoint
run endpoint, stop and reproduce error
solve error: ERROR: [Errno 48] Address already in use, solve with another script and with if name == 'main':
run again
install SQLModel pip install sqlmodel==0.0.16 => can try pycharm UI pip install pydantic==1.10.11

show Sqlite viewer

Create DB and table

Create heroes and show, with: SELECT * from hero;

Implement POST endpoint to insert a new Hero.

Talk about async and await

Talk about commit() in a DB.

Done! Congrats! :)