from pydantic import BaseModel

class ASObject (BaseModel):
    """ 
    https://www.w3.org/ns/activitystreams#Object
    """
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
    """ 
    https://www.w3.org/ns/activitystreams#Link
    """
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
    """ 
    https://www.w3.org/ns/activitystreams#Activity	
    """
    actor:str
    instrument:str
    object:ASObject
    origin:str
    result:str
    target:str
       
class ASIntransitiveActivity(ASActivity):
    """ 
    https://www.w3.org/ns/activitystreams#IntransitiveActivity	
    super.object property must not be used
    """

class ASCollection(ASObject):
    """ 
    https://www.w3.org/ns/activitystreams#Collection	
    """
    current:str
    first:str
    items:str
    last:str
    totalItems:str
   
class ASOrderedCollection(ASCollection):
    """ 
    https://www.w3.org/ns/activitystreams#OrderedCollection
    """

class ASCollectionPage(ASCollection):
    """ 
    https://www.w3.org/ns/activitystreams#CollectionPage	
    """
    partOf:str
    next: str
    prev: str 
    
class ASOrderedCollectionPage(ASOrderedCollection,ASCollectionPage):
    startIndex:str
    
