import pandas as pd

<<<<<<< HEAD
def loadFrame(dbs,filterCls = None, filterObj = None):
    global dataF

    objects = []
    rows = []
    data = []
    columns = ['id','name','level','quality','enchantment','cls','createdDate','markets','price']

    for i in range(0, len(dbs.objects) - 1):
        iObject = dbs.objects[i]
        if (iObject.object['cls'] == filterCls or filterCls == None) and (iObject.object['obj'] == filterObj or filterObj == None):
            objects.append(iObject.id)

    for n in dbs.objectsPrices:
        if n.idObject in objects:
            iObject = dbs.objects[n.idObject]
            reg = []

            reg.append(iObject.id)
            reg.append(iObject.name)
            reg.append(iObject.level)
            reg.append(iObject.quality)
            reg.append(iObject.enchantment)
            reg.append(iObject.object['cls']['obj'])
            reg.append(n.createdDate)
            reg.append(dbs.markets[n.idMarket].name)
            reg.append(n.price)
            data.append(reg)
            rows.append(n.idObject)

    dataF = pd.DataFrame(data,columns=columns)
=======

pd.read_json()
>>>>>>> parent of 7e19327 (organizacion de clases finalizada)
