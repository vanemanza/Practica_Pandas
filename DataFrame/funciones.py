import pandas as pd
import numpy as np

usuarios = {
    'nombre':['Eduardo', 'Uriel', 'Marines', 'Fernando'],
    'calificacion': [9.5,10,8.5,8],
    'edad':[25,32,28,42],
    'aprobado':[True, False, True, False]
    }

df = pd.DataFrame(usuarios)

"""
Como aplicar una funcion a cada elemento de una columna:
Utilizo el método apply(<funcion>, axis=n)
Recibe como 1er argumento una funcion,
como 2do argumento el eje.  axis = 0 --> recorre columnas
                            axis = 1 --> recorre filas
Obtenemos una nueva Serie!
No se modifica el DF
si quiero modificarlo, le asigno la nueva serie a nuestra columna.
Ahora quiero recorrer el DF fila x fila
"""
#sumar 1 a la edad de cada usuario
df.apply(lambda row: row['edad'] + 1, axis=1)

"""
Salida:
0    26
1    33
2    29
3    43
dtype: int64
"""

"""
Obtenemos una nueva Serie!
No se modifica el DF
si quiero modificarlo, le asigno la nueva serie a nuestra columna.
"""

df.edad = df.apply(lambda row: row['edad'] + 1, axis=1)

