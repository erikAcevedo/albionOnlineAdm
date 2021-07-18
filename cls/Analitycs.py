from datetime import datetime

class Global:
    def __init__(self,id,object,cratedDate):
        self.id = id
        if cratedDate == None:
            self.cratedDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.cratedDate = cratedDate
        self.object = {'cls':self.__class__.__name__,'obj':object}

class ObjectPrice(Global):
    def __init__(self,id,object,cratedDate,idObject,idMarket,price):
        super().__init__(id,object,cratedDate)
        
        self.idObject = idObject
        self.idMarket = idMarket
        self.price = price