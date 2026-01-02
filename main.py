from fastapi import FastAPI , Header , Request
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
async def  read_root():
    return {'message':'Hello World'}

@app.get('/greet')#here we are not giving any path parameter as name so we have to give parameter in url path = http://127.0.0.1:8000/greet?name=Anuj
async def print_name(name:str = "anuj")->dict: 
    return {'message':f'hello {name}'}

class CreateBook(BaseModel):
    title : str
    author : str

@app.put('/create_book')
async def create_book(book:CreateBook):
    return {
        'title': book.title,
        'author':book.author
    }
    
@app.get('/get_header')
async def get_header(
    accept:str = Header(None),
    content_type:str = Header(None),
    host:str = Header(None),
    accept_language:str  =  Header(None)
):
    request_header = {}
    
    request_header['Accept']=accept
    request_header['Host']=host
    request_header['accept-language']=accept_language
    request_header['content_type']=content_type
    
    return request_header

@app.get('/full_header')
async def full_header(request:Request):
    return request.headers