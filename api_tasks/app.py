import http
from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from api_tasks.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='API dos sonhos!')
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


@app.post(
    '/users/', status_code=http.HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_id)
    return user_id


@app.get('/users/', status_code=http.HTTPStatus.OK, response_model=UserList)
def read_user():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND, detail='User not found'
        )
    return database.pop(user_id - 1)


@app.get(
    '/users/{user_id}',
    status_code=http.HTTPStatus.OK,
    response_model=UserPublic,
)
def read_user_by_id(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=http.HTTPStatus.NOT_FOUND, detail='User not found'
        )
    return database[user_id - 1]
