from cls.Environment import Market
from cls.Analitycs import ObjectsPricesRevision
from os import name
from numpy import array, number
import pandas as pd
from dbs import *

def loadFrame(filterRevision=None, filterCls = None, filterObj = None):
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

def priceOfTheObjectInTheMarkets(obj,principalMarketsOnly=True):
    priceOfMarkets = []
    if type(obj) == str:
        o = searchByName(obj,objects)
    else:
        o = objects[obj]

    for m in markets:
        if principalMarketsOnly:
            if m.object['obj']=='Principal': 
                a = Analitycs.ObjectPrice(len(objectsPrices),'priceOfTheObjectInTheMarkets',None,o.id,m.id,input('Price of ' + m.name + ': '))
        else:
                a = Analitycs.ObjectPrice(len(objectsPrices),'priceOfTheObjectInTheMarkets',None,o.id,m.id,input('Price of ' + m.name + ': '))

        objectsPrices.append(a)
        priceOfMarkets.append(objectsPrices[len(objectsPrices)-1].id)

    objectsPricesRevision.append(Analitycs.ObjectsPricesRevision(len(objectsPricesRevision),'priceOfTheObjectInTheMarkets',None,priceOfMarkets))

    return objectsPricesRevision[len(objectsPricesRevision)-1]

def priceOfTheObjectsInTheMarkets(objs,principalMarketsOnly=True):
    priceOfMarkets = []
    if type(objs) == list:
        
        for m in markets:
            for obj in objs:
                if type(obj) == str:
                    o = searchByName(obj,objects)
                else:
                    o = objects[obj]

                if not o == None:
                    if (m.object['obj']=='Principal') or (not principalMarketsOnly):
                        a = Analitycs.ObjectPrice(len(objectsPrices),'priceOfTheObjectInTheMarkets',None,o.id,m.id,input('Price of ' + o.name + ' in ' + m.name + ': '))

                        objectsPrices.append(a)
                        priceOfMarkets.append(objectsPrices[len(objectsPrices)-1].id)

                else:
                    print('No existe el objeto ' + obj)

    if len(priceOfMarkets) == 0:
        objectsPricesRevision.append(Analitycs.ObjectsPricesRevision(len(objectsPricesRevision),'priceOfTheObjectInTheMarkets',None,priceOfMarkets))
        return objectsPricesRevision[len(objectsPricesRevision)-1]

def priceOfTheObjectsInTheSpecificMarkets(objs,mrks):
    priceOfMarkets = []
    if type(objs) == list and type(mrks) == list:
        
        for mrk in mrks:
            if type(mrk) == str:
                m = searchByName(mrk,markets)
            else:
                m = markets[mrk]

            for obj in objs:
                if type(obj) == str:
                    o = searchByName(obj,objects)
                else:
                    o = objects[obj]

                if not o == None:
                    if (m.object['obj']=='Principal'):
                        a = Analitycs.ObjectPrice(len(objectsPrices),'priceOfTheObjectInTheMarkets',None,o.id,m.id,input('Price of ' + o.name + ' in ' + m.name + ': '))

                        objectsPrices.append(a)
                        priceOfMarkets.append(objectsPrices[len(objectsPrices)-1].id)

                else:
                    print('No existe el objeto ' + obj)

    if len(priceOfMarkets) == 0:
        objectsPricesRevision.append(Analitycs.ObjectsPricesRevision(len(objectsPricesRevision),'priceOfTheObjectInTheMarkets',None,priceOfMarkets))
        return objectsPricesRevision[len(objectsPricesRevision)-1]

def totalPriceRevision(objRevision):
    s = 0

    if type(objRevision) == Analitycs.ObjectsPricesRevision:
        for i in objRevision.objectPrices:
            s += objectsPrices[i].price
    elif type(objRevision) == list:
        for o in objRevision:
            for i in objRevision.objectPrices:
                s += objectsPrices[i].price
    elif type(objRevision) == int:
        for i in objectsPricesRevision[objRevision].objectPrices:
            s += objectsPrices[i].price

    return s



def createRevision(objs,mrks,principalMarketsOnly=True):
    idRevision = len(objectsPricesRevision)

    def solicitarPrecio(idObject,idMarket):
        return int(input('Price of ' + objects[idObject].largeName(db) + ' in ' + markets[idMarket].name + ': '))

    def crearPrice(idObject,idMarket):
        objectsPrices.append(Analitycs.ObjectPrice(len(objectsPrices),'priceOfTheObjectInTheMarkets',None, idObject,idMarket,solicitarPrecio(idObject,idMarket),idRevision))

        return objectsPrices[len(objectsPrices)- 1]

    def solicitarObjectos(objs,idMarket):
        r = []
        if type(objs) == int:
            r.append(crearPrice(objs,idMarket).id)
        elif type(objs) == list:
            for o in objs:
                r.append(crearPrice(o,idMarket).id)

        return r

    O = []

    if type(mrks) == list:
        for i in mrks:
            if principalMarketsOnly:
                if markets[i].object['obj']=='Principal':
                    O += solicitarObjectos(objs,i)
            else:
                O += solicitarObjectos(objs,i)
    else:
        if markets[mrks].object['obj']=='Principal':
            O += solicitarObjectos(objs,mrks)
    
    objectsPricesRevision.append(Analitycs.ObjectsPricesRevision(idRevision,"createRevision",None,O))

    return dataJson(objectsPricesRevision[len(objectsPricesRevision)-1])