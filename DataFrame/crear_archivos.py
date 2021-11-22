import pandas as pd
import numpy as np

"""
Para persistir un DF podemos usar el metodo-> to_csv()
Recibe como argumento el nombre del archivo q deseamos crear.csv
si queremos almacenar ciertas columnas, usamos el parametro columns, 
y por medio de una lista definimos q columnas queremos almacenar.
Si no queremos guardar los indices, agregamos el parametro index=False
"""

archivo = pd.read_csv('users.csv')
usuarios2 = pd.DataFrame(archivo, columns=['nombre', 'edad', 'pais'])
usuarios2.to_csv('usuarios2.csv')
