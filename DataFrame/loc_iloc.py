import pandas as pd
import numpy as np 

"""
El atributo loc permite obtener info del DF 
a partir de etiquetas. 
"""
usuarios = {
    'nombre':['Eduardo', 'Uriel', 'Marines', 'Alex', 'Fernando'],
    'edad': np.random.randint(15,30,5),
    'calificaion': np.random.randint(5,10,5),
    'email': ['edu@mail.com','uri@mail.com', 'mari@mail.com', 'ale@mail.com', 'fer@mail.com' ]
}

df = pd.DataFrame(usuarios, index=list('abcde'))

"""
Sabemos q podemos acceder a los elem de una columna
x su llave -> df['edad']
Obtenemos una Serie.
Pero no podemos acceder a un indice de esa Serie
xq nos da error.

Si necesitamos obtener info a partir de un indice
usamos el atr loc
df.loc[<indice>] -> y obtenemos como resultado la fila
que hace referencia a ese indice.

"""
# Obtener los datos de una fila x su indice
df.loc['a']

# Obtener un rango de ciertas filas -> 
"""
1) Para obtener todas las columnas de ese rango:
"""
df.loc['a':'c']
"""
2) Para obtener algunas columnas de ese rango:
df.loc['a':'c', <nombre de la columna q deseo>]
"""
df.loc['a':'c', 'nombre']
"""
3) si quiero obtener mas columnas, agrego una lista 
con los nombre de las columnas.
df.loc['a':'c', ['nombre', 'edad']]
"""
df.loc['a':'c', ['nombre', 'edad']]

# Realizar otras consultas con una condicion->
# Todos los usuarios con calificacion > 7
df.loc[ df.calificacion > 7 ]
# Nombre de los usuarios con calificacion > 7
df.loc[ df.calificacion > 7, 'nombre']
# Nombre y Edad de los usuarios con calificacion > 7
df.loc[ df.calificacion > 7, ['nombre', 'edad']]
# Los 3 primeros usuarios con la calificacion mas alta
df.loc[:, ['nombre', 'calificacion']].sort_values('calificacion', ascending=False).head(3)

#--------------------------------------------------------------

"""
Con iloc no trabajo con etiquetas, sino con POSICIONES
"""
# X EJ df.loc['a'] == df.iloc[0]
# obtener un rango:
df.iloc[0:4]
# Trabajar con columnas puntuales, mediante una posicion:
df.iloc[0:4, 0]
df.iloc[0:4, [0,2]]

"""
Tambien podemos:
- Filtrar
- Ordenar
- Agrupar
"""