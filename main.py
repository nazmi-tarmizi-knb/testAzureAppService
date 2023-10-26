# -*- coding: utf-8 -*-


from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import os

origins = [
"https://login.windows.net"
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])
]

app = FastAPI(middleware=middleware)

#create dummy database
my_dict = {1:"Number 1",2:"Number 2",3:"Number 3"}

#home
@app.get('/')
def home():
    return "The server is online"


#get method
@app.get('/get-something-by-id/{item_id}')
def get_by_id(item_id:int):
    return my_dict[item_id]



#library for data parsing and validation
from pydantic import BaseModel

#create data class (our custom data type)
class Data(BaseModel):
    item_id: int
    value: str
    


#post
@app.post('/set-value-by-id/')
def set_value_by_id(data:Data):
    my_dict[data.item_id]=data.value

    return data
