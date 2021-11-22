import pandas as pd
import numpy as np 

df = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('ABCD'), index=list('abcd'))

"""
Si quiero modificar un elem en particular:
1) ingreso a la columna: 
- mediante una llave   ->  df['B']
- mediante un atributo ->  df.B    
2) nos situamos sobre el elem: 
- mediante el indice q nosotros especificamos -> df.B['b']
- mediante el indice numérico ->                 df.B[1]
3) le asigno el nuevo valor_
- df.B['b'] = 50
"""
df.B['b'] = 50

"""
Si queremos cambiar todos los valores de una columna,
df.B = 10,20,30,40
"""
df.B = 10,20,30,40

"""
Si queremos eliminar una columna:
Usamos el método drop(<columna>, axis=1)
El método drop() NO modifica al DF,
si no que genera uno nuevo.
"""
df.drop('A', axis=1)

"""
Si queremos eliminar una fila, 
uso el metodo drop(<fila>, axis=0)
"""
df.drop('a', axis=0)

"""
Si queremos insertar una columna:
 A) mediante el método insert(n, <nombre>, [elem, elem, elem])
    Este método SI modifica al DF.
    Recibe 3 argumentos:
    1) Posicion donde queremos insertar la columna
    2) el nombre de la columna
    3) los valores mediante una lista 
 B) mediante el método assign(x = [1000,2000,3000,4000])   
    solo recibe un argumento
    la columna q queremos agregar
    NO modifica el DF, genera uno nuevo
"""

df.insert(1, 'Z', [100,200,300,400])
