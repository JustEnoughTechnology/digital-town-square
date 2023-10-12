from pydantic import BaseModel

class ASObject (BaseModel):
    pass

class ASLink (BaseModel):
    pass

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





 









