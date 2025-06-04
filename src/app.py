import http

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.routes import auth, tasks, users
from src.schemas import Message

app = FastAPI(title='API dos sonhos!')

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tasks.router)


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
