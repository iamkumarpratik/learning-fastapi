from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI(debug=True)


class Information(BaseModel):
    id: int
    name: str
    age: int
    bio: Optional[str]


class PublicInformation(BaseModel):
    name: str
    bio: Optional[str]


@app.get('/')
async def home():
    return {'status': 'Success', 'data': 'Server is running.'}


# Below is an example of path parametre.
@app.get('/parameter/{name}')
async def parameter(name):
    return {"status": "success", "data": name}


# Below is an example of query parametre.
@app.get('/query/parameters')
async def query(name: str, age: int):
    query_generated_data = f"Hello {name}, you are {age} years old."
    return {"status": "success", "data": query_generated_data}


# Use of pydantic models on api to validate and structure data.
@app.post('/my/information/', response_model=PublicInformation, response_model_exclude_unset=True)
async def my_information(information: Information):
    return information

