from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class University(BaseModel):
    name: str
    location: str


@app.get('/')
def index():
    return {"TEST": "just testing..."}

@app.get('/universities')
def get_universities():
    return db

@app.get('/universities/{id}')
def get_university(id: int):
    return db[id-1]

@app.post('/universities')
def add_university(university: University):
    db.append(university.dict())
    return db[-1]

@app.delete('/university/{id}')
def delete_university(id: int):
    try:
        db.pop(id-1) #db is of type list; get index
    except:
        return "INDEX OUT OF SCOPE"
    else:
        return "DELETED"