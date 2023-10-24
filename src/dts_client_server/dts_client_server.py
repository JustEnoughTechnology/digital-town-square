from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {"message":"You found the root"}

@app.get('/auth')
async def authRoot():
    return {"message":"you found the authroot"}

@app.get('/auth/login')
async def login ():
    return {"message":"successful login"}

@app.get('/auth/logout')
async def logout():
    return {"message":"successful logout"}

@app.get('/docs')
async def docs():
    return {"message":"docs will start here"}

@app.get('/actor/{actor_id}')
async def getActor(actor_id):
    return {"message":f"getting info for {actor_id}"}

@app.get('/actor/{actor_id}/like')
async def getActorLikes(actor_id):
    return {"message":f"getting the list of all {actor_id} likes"}

@app.post('/actor/{actorID}/like/{itemID}')
async def actorLikeItem(actorID, itemID):
    return {"message": f"{actorID} now likes {itemID}"}


