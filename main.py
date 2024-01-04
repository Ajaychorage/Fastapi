from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

db ={}

class Books(BaseModel):
    BookId:int
    BookName:str
    Author:str

@app.post("/")
def Add_Book(Books:Books):
    db[Books.BookName] =Books.Author
    return {"Books" :Books }

@app.get("/")
def get_all_Books():
    return db


@app.put("/")
def Update_Book(Books:Books):
    db[Books.BookName] =Books.Author
    return db

@app.delete("/")
def delete_Book(BookName: str):
    del db[BookName]
    return db



