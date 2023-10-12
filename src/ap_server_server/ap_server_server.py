from fastapi import FastAPI, status
from logging import Logger
from pydantic import BaseModel

class 

class AP_Server():
    app = FastAPI() 
    
    def __init__(self) -> None:
        pass
        

    @app.post("/{actor}/inbox",status_code=status.HTTP_200_OK)
    async def post_inbox(actor):
        