datos = [5,6,7,8,9]
for i in range(0,5):
    print ( datos[i] , end=" " )
print()
 
datos.remove(6)
for i in range(0, len(datos)):
    print ( datos[i] , end=" " )
print()
 
datos[0]=-2
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()
 
datos.insert(1,23)
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()
 
datos = datos + [31,32,33]
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()