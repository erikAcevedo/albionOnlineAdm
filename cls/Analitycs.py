from datetime import datetime

class Global:
    def __init__(self,id,object,createdDate):
        self.id = id
        if createdDate == None:
            self.createdDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.createdDate = createdDate
        self.object = {'cls':self.__class__.__name__,'obj':object}

class ObjectPrice(Global):
    def __init__(self,id,object,createdDate,idObject,idMarket,price):
        super().__init__(id,object,createdDate)
        
        self.idObject = idObject
        self.idMarket = idMarket
        self.price = price