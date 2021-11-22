import json
import os
from typing import Text
from matplotlib.pyplot import text

from numpy import number
from cls import Objects, Environment, Analitycs

SRC_ORG = 'C:/Users/erika/Documents/proyectos/albionOnlineAdm/'
SRC_DB = 'dbs/db.json'

SRC = os.path.join(SRC_ORG,SRC_DB)

db = {}



objects = []
levels = []
qualitys = []
enchantments = []
items = []
cities = []
markets = []
objectsPrices = []
objectsPricesRevision = []
consumables = []

def stateAPP():
    if db == {}:
        return False
    else:
        return True

def searchByName(nameObject, arr):
    for i in arr:
        if i.name == nameObject:
            return i
            break
    
def searchPriceByObjectName(nameObject):
    r = []
    idObject = searchByName(nameObject,objects).id
    for i in objectsPrices:
        if i.idObject == idObject:
            r.append(i)
    
    return r

def jsonDefault(object):
    return object.__dict__

def loadDB():

    
    def loadClass(dbs, obj):

        for r in dbs:
            if type(r) == number or type(r) == str:
                obj.append(r)
            elif r['object']['cls'] == 'Market':
                obj.append(Environment.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['object']['obj'],
                    r['citie']
                ))
            elif r['object']['cls'] == 'ObjectsPricesRevision':
                obj.append(Analitycs.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['object']['obj'],
                    r['createdDate'],
                    r['objectPrices']
                ))
            elif r['object']['cls'] == 'Citie':
                obj.append(Environment.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['object']['obj'],
                    r['returns']
                ))
            elif r['object']['cls'] == 'ObjectPrice':
                obj.append(Analitycs.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['object']['obj'],
                    r['createdDate'],
                    r['idObject'],
                    r['idMarket'],
                    r['price'],
                    r['idRevision']
                ))
            elif r['object']['cls'] == 'Armor':

                obj.append(Objects.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['level'],
                    r['quality'],
                    r['enchantment'],
                    r['object']['obj'],
                    r['build'],
                    r['weight'],
                    r['itemValue'],
                    r['creator']
                ))
            elif r['object']['cls'] == 'Consumable':

                obj.append(Objects.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['level'],
                    r['quality'],
                    r['enchantment'],
                    r['object']['obj'],
                    r['build'],
                    r['weight']
                ))
            elif r['object']['cls'] == 'Resource':
                obj.append(Objects.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['level'],
                    r['quality'],
                    r['enchantment'],
                    r['object']['obj'],
                    r['build'],
                    r['weight'],
                    r['itemValue']
                ))

        return obj

    if not stateAPP():
        with open(
            SRC,
            'r'
        ) as file:
            DB = json.load(file)

        loadClass(DB['Levels'],levels)
        loadClass(DB['Qualitys'],qualitys)
        loadClass(DB['Enchantments'],enchantments)

        loadClass(DB['Cities'],cities)
        loadClass(DB['Markets'],markets)
        loadClass(DB['Objects'],objects)

        loadClass(DB['ObjectsPrices'],objectsPrices)
        loadClass(DB['ObjectsPricesRevision'],objectsPricesRevision)


        db['Objects'] = objects
        db['Items'] = items
        db['Cities'] = cities
        db['Markets'] = markets
        
        db['ObjectsPrices'] = objectsPrices
        db['ObjectsPricesRevision'] = objectsPricesRevision

        db['Levels'] = levels
        db['Qualitys'] = qualitys
        db['Enchantments'] = enchantments

    return db

def dataJson(dbs = db):
    return json.dumps(dbs, sort_keys=False, default=jsonDefault, indent=4)

def saveDB():
    with open(
        SRC,
        'w'
    ) as file:
        
        return json.dump(
            db, file, default=jsonDefault,indent=4
        )

