import dbs
import analitycs
import matplotlib.pyplot as plt

dbs.loadDB()

dbs.objectsPrices.append(dbs.Analitycs.ObjectPrice(len(dbs.objectsPrices),'ObjectPrice',None,dbs.searchByName('Algodón',dbs.objects).id,dbs.searchByName('Fort Sterling Market',dbs.markets).id,29))
dbs.objectsPrices.append(dbs.Analitycs.ObjectPrice(len(dbs.objectsPrices),'ObjectPrice',None,dbs.searchByName('Cañamo',dbs.objects).id,dbs.searchByName('Fort Sterling Market',dbs.markets).id,29))


analitycs.loadFrame(dbs)

agrupacion = analitycs.dataF.groupby(['name','market'])['price'].sum()


agrupacion.plot.bar(x=['name','market'],y='price', rot = 1)

plt.show()