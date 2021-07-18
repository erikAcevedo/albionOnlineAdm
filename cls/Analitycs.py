class Global:
    def __init__(self,id,object,createdDate):
        self.id = id
        self.createdDate = createdDate
        self.object = {'cls':self.__class__.__name__,'obj':object}

class ObjectPrice(Global):
    def __init__(self,id,object,createdDate,idObject,idMarket,price):
        super().__init__(id,object,createdDate)
        
        self.idObject = idObject
        self.idMarket = idMarket
        self.price = price