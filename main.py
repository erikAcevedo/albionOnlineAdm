import dbs
import analitycs

dbs.loadDB()

analitycs.loadFrame(dbs)

ejemplo = dbs.Analitycs.ObjectPrice(len(dbs.objectsPrices),'ObjectPrice',None,dbs.searchByName('Algodón',dbs.objects).id,dbs.searchByName('Caerleon Market',dbs.markets).id,28)

print(dbs.json.dumps(ejemplo, default=dbs.jsonDefault,indent=4))