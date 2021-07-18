from dbs import *
import analitycs as an
import matplotlib.pyplot as plt

loadDB()

objectsPrices.append(Analitycs.ObjectPrice(len(objectsPrices),'ObjectPrice',None,searchByName('Algodón',objects).id,searchByName('Fort Sterling Market',markets).id,29))
objectsPrices.append(Analitycs.ObjectPrice(len(objectsPrices),'ObjectPrice',None,searchByName('Cañamo',objects).id,searchByName('Fort Sterling Market',markets).id,29))


an.loadFrame()



agrupacion = an.dataF.groupby(['name','market'])['price'].sum()


agrupacion.plot.bar(x=['name','market'],y='price', rot = 1)

plt.show()