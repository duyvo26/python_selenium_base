from pydantic import BaseModel


class User(BaseModel):
    id_user: str
    username: str
    password: str
