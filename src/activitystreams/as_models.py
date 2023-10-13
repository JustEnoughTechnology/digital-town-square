from pydantic import BaseModel

class ASObject (BaseModel):
    id:str
    name:str
    type: str
    attachment:str
    attributedTo:str
    audience:str
    bcc:str
    bto:str
    cc:str
    content:str
    context:str
    duration:str
    endTime:str
    generator:str
    icon:str
    image:str
    inReplyTo:str
    location:str
    mediaType:str
    preview:str
    published:str
    replies:str
    startTime:str
    summary:str
    tag:str
    to:str
    update:str
    url:str
    
class ASLink (BaseModel):
    id:str
    name:str
    type:str
    href:str
    rel:str
    mediaType:str
    hreflang:str
    height:str
    width:str
    preview:str
    

class ASActivity (ASObject):
    pass 

class ASIntransitiveActivity(ASActivity):
    pass 

class ASCollection(ASObject):
    pass

class ASOrderedCollection(ASCollection):
    pass 

class ASCollectionPage(ASCollection):
    pass 

class ASOrderedCollectionPage(ASOrderedCollection,ASCollectionPage):
    pass 





 









