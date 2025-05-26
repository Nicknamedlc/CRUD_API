import http

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI(title="API dos sonhos!")
database = []


@app.get('/', status_code=http.HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/olamundo/', response_class=HTMLResponse)
def say_hello():
    return """
    <html>
      <head>
        <title>Olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
        <h2> Hoje é um novo dia</h2>
      </body>
    </html>"""


@app.post('/users/', status_code=http.HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_id = UserDB(**user.model_dump(),id = len(database)+1)
    database.append(user_id)
    return user_id

@app.get('/users/{user_id}',status_code=http.HTTPStatus.OK, response_model=UserPublic)
def read_user(user_id: int):
    return database[user_id-1]