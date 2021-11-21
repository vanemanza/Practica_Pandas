import pandas as pd
import numpy as np

usuarios = {
    'nombre' : ['vane', 'reni', 'faus', 'augus'],
    'calificacion' : [9, 10, 8.5, 9.5],
    'edad' : [46, 17, 15, 11],
    'aprobado': [True, False, True, False]
    }

"""
Crear un DataFrame a partir de un diccionario,
mediante la clase DataFrame.
pd.DataFrame(<diccionario>).
Obtengo un objeto de tipo DataFrame.
"""

# df = pd.DataFrame(usuarios)

"""
si quiero definir los indices:
indes = ['ind1', 'ind2', 'ind3]
"""

df = pd.DataFrame(usuarios, index=['a', 'b', 'c', 'd']) 

"""
Puedo acceder a cada columna x sus llaves o mediante un atributos.
"""

df['nombre'] # mediante llave
df.nombre # mediante atributo

"""
Salida en ambos casos:
a     vane
b     reni
c     faus
d    augus
"""
# si quiero obtener los valores de una columna
# obtengo un array

df.calificacion.values

"""
Puedo conocer las columnas de un DF a traves de su 
atributo columns.
"""
df.columns # obtengo un objeto
"""
Para obtener los INDICES->
"""
df.index # obtengo un objeto
"""
Para obtener los valores ->
"""
df.values # obtengo un array con todos los valores
       # array([    ['vane', 9.0, 46, True],
       #             ['reni', 10.0, 17, False],
       #            ['faus', 8.5, 15, True],
       #            ['augus', 9.5, 11, False]], 
       #        dtype=object)
df.values.ndim # obtengo la dimension del array

"""
Para definir con que columnas quiero trabajar,
uso el parametro 'columns'
"""
df = pd.DataFrame(usuarios, index=[1,2,3,4], columns=['calificacion', 'aprobado'])

"""
Crear un DF a partir de una Matriz:

"""
matriz = np.arange(12).reshape(3,4)
df2 = pd.DataFrame(matriz)

"""
Podemos renombrar las columnas o las filas:
"""

df2 = pd.DataFrame(matriz, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c'])

#  Renombrar las columnas o los indices-->
df2.columns = 'AB', 'BB', 'CB', 'DB'
df2.index = '1a', '2b', '3c'

"""
Si tengo q modificar una columna o un indice puntual:
Uso el metodo rename(columns={'AB':'ab'})
"""
df2.rename(columns={'AB':'ab'})
#df2.rename(index={'1a':'1A'})
