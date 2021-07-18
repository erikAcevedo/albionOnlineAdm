import dbs
import analitycs

dbs.loadDB()


ejemplo = dbs.Analitycs.ObjectPrice(len(dbs.objectsPrices),'ObjectPrice',None,dbs.searchByName('Algodón',dbs.objects).id,dbs.searchByName('Caerleon Market',dbs.markets).id,28)

dbs.objectsPrices.append(ejemplo)

print(analitycs.loadFrame(dbs))
