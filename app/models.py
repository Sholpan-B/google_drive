from pydantic import BaseModel
from typing import List


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class File(BaseModel):
    name: str
    owner: str


class Folder(BaseModel):
    name: str
    owner: str
    files: List[File] = []
    folders: List['Folder'] = []

