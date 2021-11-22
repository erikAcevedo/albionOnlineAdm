class Item:
    def __init__(self, id, name, level, quality, enchantment, object, build, weight, itemValue):
        self.id = id
        self.weight = weight
        self.itemValue = itemValue
        self.name = name
        self.level = level
        self.quality = quality
        self.enchantment = enchantment
        self.object = object
        self.build = build

    def largeName(self,dbs):
        return self.name + ', Nivel ' + str(self.level) + ', ' + dbs.qualitys[self.quality] + ', ' + dbs.enchantments[self.enchantment]

    def constructionTree(self,dbs,searchInTree=False,execute=0):
        r = []

        if not len(self.build) == 0:
            for n in self.build:
                r.append({'execute':execute,'quantity':n['quantity'],'item':dbs.objects[n['item']]})
                if searchInTree: r = r + dbs.objects[n['item']].constructionTree(dbs,searchInTree,execute + 1)
        
        return r

            

class Resource(Item):
    def __init__(self, id, name, level, quality, enchantment, object, build, weight, itemValue):
        super().__init__(id, name, level, quality, enchantment, {'cls':self.__class__.__name__,'obj':object}, build, weight, itemValue)

class Armor(Item):
    def __init__(self, id, name, level, quality, enchantment, object, build, weight, itemValue, creator):
        super().__init__(id, name, level, quality, enchantment, {'cls':self.__class__.__name__,'obj':object}, build, weight, itemValue)
        self.creator = creator

class Material(Item):
    def __init__(self, id, name, level, enchantment, object, weight, itemValue):
        super().__init__(id, name, level, 0, enchantment, {'cls':self.__class__.__name__,'obj':object}, [], weight, itemValue)

class Consumable(Item):
    def __init__(self, id, name, level, quality, enchantment, object, build, weight):
        super().__init__(id, name, level, quality, enchantment, {'cls':self.__class__.__name__,'obj':object}, build, weight, 0)