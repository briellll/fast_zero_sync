from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class USerSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserDB(USerSchema):
    id: int
