class Global:
    def __init__(self,id,name,object):
        self.id = id
        self.name = name
        self.object = {'cls':self.__class__.__name__,'obj':object}
    

class Citie(Global):
    def __init__(self,id,name,object,returns):
        super().__init__(id,name,object)

        self.returns = returns

class Market(Global):
    def __init__(self,id,name,object,citie):
        super().__init__(id,name,object)
        
        self.citie = citie