import pandas as pd
import numpy as np

"""
Podemos ordenar los DF mediante - indices
                                - columnas
"""

archivo = pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'])

paisesdf = pd.DataFrame(archivo )

# Ordenamiento x Indices:
"""
Genera un nuevo DF ordenado x los indices. 
No modifica el DF original.
El ordenamiento x default será ascendente.
"""
paisesdf.sort_index()

"""
Para ordenar de forma descendente, paso x parametro -> ascending=False
"""

paisesdf.sort_index(ascending=False)

# Ordenamiento x Columnas:
"""
Uso el metodo sort_values(<columna>)
Recibe x argumento el nombre de la columna x la queremos ordenar. 
El ordenamiento x default también es ascendente.
Genera un nuevo DF, no modifica el original.
Si quiero q sea descendente tambien le paso el parametro ascending=False
"""
paisesdf.sort_values('poblacion', ascending=False)
