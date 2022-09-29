from fastapi import File
from pydantic import BaseModel


class AddIn(BaseModel):
    a: int | float
    b: int | float


class AddOut(BaseModel):
    result: int | float
