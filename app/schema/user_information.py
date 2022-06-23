from pydantic import BaseModel
from typing import Optional


class Information(BaseModel):
    id: int
    name: str
    age: int
    bio: Optional[str]


class PublicInformation(BaseModel):
    name: str
    bio: Optional[str]
