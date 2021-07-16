import json
import os
import cls.Objects as Objects
import cls.Environment as Environment
import cls.Analitycs as Analitycs

SRC_ORG = 'C:/Users/erika/Documents/proyectos/albionProyect_py/v0/'
SRC_DB = 'dbs/db.json'

SRC = os.path.join(SRC_ORG,SRC_DB)

db = {}

def jsonDefault(object):
    return object.__dict__

def loadDB():
    global levels,qualitys,enchantments,items,cities,objects,markets

    global pricesObjects

    objects = []
    levels = []
    qualitys = []
    enchantments = []
    items = []
    cities = []
    markets = []
    pricesObjects = []
    
    def loadClass(dbs, obj):

        for r in dbs:
            if r['object']['cls'] == 'Market':
                obj.append(Environment.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['object']['obj'],
                    r['citie']
                ))
            elif r['object']['cls'] == 'Citie':
                obj.append(Environment.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['name'],
                    r['object']['obj'],
                    r['returns']
                ))
            elif r['object']['cls'] == 'PriceObject':
                obj.append(Analitycs.__getattribute__(r['object']['cls'])(
                    r['id'],
                    r['object']['obj'],
                    r['idObject'],
                    r['idMarket'],
                    r['price']
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
            else:
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

    with open(
        SRC,
        'r'
    ) as file:

        DB = json.load(file)

    loadClass(DB['Cities'],cities)
    loadClass(DB['Markets'],markets)
    loadClass(DB['Objects'],objects)

    levels = DB['Levels']
    qualitys = DB['Qualitys']
    enchantments = DB['Enchantments']
    
    

    db['Objects'] = objects
    db['Items'] = items
    db['Cities'] = cities
    db['Markets'] = markets

    db['PricesObjects'] = pricesObjects

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
