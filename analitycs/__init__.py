import pandas as pd
from dbs import *

def loadFrame(filterCls = None, filterObj = None):
    global data,rows,columns,dataF
    idObjects = []
    rows = []
    data = []
    columns = ['id','name','level','quality','enchantment','cls','createdDate','market','price']

    for i in range(0, len(objects) - 1):
        iObject = objects[i]
        if (iObject.object['cls'] == filterCls or filterCls == None) and (iObject.object['obj'] == filterObj or filterObj == None):
            idObjects.append(iObject.id)

    for n in objectsPrices:
        if n.idObject in idObjects:
            iObject = objects[n.idObject]
            reg = []

            reg.append(iObject.id)
            reg.append(iObject.name)
            reg.append(iObject.level)
            reg.append(iObject.quality)
            reg.append(iObject.enchantment)
            reg.append(iObject.object['cls'])
            reg.append(n.createdDate)
            reg.append(markets[n.idMarket].name)
            reg.append(n.price)
            data.append(reg)
            rows.append(n.id)

    dataF = pd.DataFrame(data,index=rows,columns=columns)
    return dataF