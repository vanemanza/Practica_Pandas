lista = [10,20,30,40,50]
diccionario = {'vane':46, 'reni':17, 'faus':15, 'augus':11}
import pandas as pd
"""
Crear una serie a partir de una lista:
Salida-->   0   10
            1   20  
            2   30
            3   40
            4   50
            dtype:int64
"""
a = pd.Series(lista) 

"""
Crear una serie a partir de un diccinario:
Salida -->  vane    46
            reni    17
            faus    15  
            augus   11
            dtype:int64
"""
b = pd.Series(diccionario)

"""
Crear una serie a partir de una lista de Str y pasarla a float:
Salida -->      0   1.0
                1   2.0
                2   3.0
                3   4.0
                4   5.0
                dtype: float32
"""
list_str = ['1', '2', '3', '4', '5']
import numpy as np
c = pd.Series(list_str, dtype=np.float32)

"""
Crear una serie, a partir de una lista de int,
pasarla a float,
cambiar el nombre de los indices(filas).
Salida-->   fila_1      10.0
            fila_2      20.0
            fila_3      30.0
            fila_4      40.0
            fila_5      50.0
            dtype: float32
"""
d = pd.Series(lista, dtype=np.float32, index=['fila_1', 'fila_2', 'fila_3', 'fila_4', 'fila_5'])

d[1] # 20.0
d['fila_2'] # 20.0
d[['fila_1', 'fila_3', 'fila_5']]   # fila_1 10.0  
                                    # fila_3 30.0
                                    # fila_5 50.0
