from http import HTTPStatus
from fast_zero.schemas import Message
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/soma/{num1}/{num2}', status_code=HTTPStatus.OK, response_model=Message)
async def soma(num1: int, num2: int):
    return {"message": str(num1 + num2)}


@app.get('/olamundo', response_class=HTMLResponse)
async def say_hello():
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
