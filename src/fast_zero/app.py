from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserPublic, USerSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: USerSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    return user_with_id
