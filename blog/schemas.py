from importlib import import_module
from pydantic import BaseModel





class Blog(BaseModel):
    title: str
    body: str