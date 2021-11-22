albionOnlineAdm

Libreria para la gestion para Albion Online de venta, crafteo, refinamiento, etc.

dbs. Contiene y almacenara todos los objetos necesarios para el uso y almaccenaminto de informacion de la libreria. Funciones (carga,guardado,insertado  ybusqueda), Clases, listas de clases y objetos.

analytics as an. Contiene las funciones para procesar contenido e informacion, por ejemplo:
    an.priceOfTheObjectsInTheSpecificMarkets(['Travertino',202],['Brigewatch Market', 5])
En este ejemplo estoy solicitare los precios de los objetos Travertino y Bloque de travertino (en este caso mando el id 202) en los mercados Brigewatch Market y Lymhurst Market, hay otras funciones que te piden los precios de todos los mercados para 1 o varios objetos etc.

an.loadFrame(). Carga el frame de los objetos y sus precios en los mercados para calcular datos estadisticos. Esta libreria se ocupa en conjunto con pandas as pd  que se alojan en an y de igual forma se puede descargar y matplotlib.pyplot as plt para visualizar graficamente.

By. DupplerEffect