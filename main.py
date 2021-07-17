import dbs
import numpy
import analitycs
import pandas as pd

dbs.loadDB()

data = []
colums = ["cantidad","Items"]
rows = []


for i in range(0, len(dbs.objects) - 1):

    nameObject = \
        dbs.objects[i].name + ' Level ' + str(dbs.objects[i].level) + ' ' + \
        dbs.enchantments[dbs.objects[i].enchantment]

    if dbs.objects[i].object['cls'] == 'Armor':
        if len(rows) > 0 and nameObject == rows[len(rows) - 1]:
            reg[0] += 1
            reg[1] += len(dbs.objects[i].build)
            
        else:
            reg = []

            reg.append(1)
            reg.append(len(dbs.objects[i].build))
            data.append(reg)
            rows.append(nameObject)


print(pd.DataFrame(data,rows,colums))
print(len(rows))
print(len(data))