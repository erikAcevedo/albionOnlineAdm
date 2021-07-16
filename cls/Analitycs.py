from datetime import datetime

class Global:
    def __init__(self,id,object):
        self.id = id
        self.dateCrated = datetime.now()
        self.object = {'cls':self.__class__.__name__,'obj':object}

class PriceObject(Global):
    def __init__(self,id,object,idObject,idMarket,price):
        super().__init__(id,object)
        
        self.idObject = idObject
        self.idMarket = idMarket
        self.price = price