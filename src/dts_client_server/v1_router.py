from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

V1 = APIRouter()
V1
class DTSServer():
    _app:FastAPI = FastAPI()
    
    def __init__(self) -> None:
        pass
    def app (self) -> FastAPI:
        return DTSServer._app
    
    @_app.get("/")
    async def root():
        return {"message": "You found the root"}


    @_app.get("/auth")
    async def authRoot():
        return {"message": "you found the authroot"}


    @_app.get("/auth/login")
    async def login():
        return {"message": "successful login"}


    @_app.get("/auth/logout")
    async def logout():
        return {"message": "successful logout"}


    @_app.get("/docs")
    async def docs():
        return {"message": "docs will start here"}


    @_app.get("/actor/{actor_id}")
    async def getActor(actor_id):
        return {"message": f"getting info for {actor_id}"}


    @_app.get("/actor/{actor_id}/like")
    async def getActorLikes(actor_id):
        return {"message": f"getting the list of all {actor_id} likes"}


    @_app.post("/actor/{actorID}/like/{itemID}")
    async def actorLikeItem(actorID, itemID):
        return {"message": f"{actorID} now likes {itemID}"}



the_app = DTSServer.app()
    



