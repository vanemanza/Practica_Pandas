import pandas as pd
import numpy as np

"""
consultas sobre el archivo users.csv de Código Facilito.
"""

archivo = pd.read_csv('../Data/users.csv', usecols=['nombre', 'edad', 'genero', 'pais', 'email'])
df = pd.DataFrame(archivo)

"""
Obtener el nombre de todos los usuarios con edad > 20
CF-> df[ df.edad > 20].nombre
"""
df.loc[df.edad > 20, 'nombre']

"""
Obtener el nombre de todos los usuarios de sexo fem y edad > 20
"""
df.loc[(df.edad > 20) & (df.genero == 'female'), 'nombre']

"""
Obtener todos los usuarios cuyo el email NO termine el @gmail.com
"""
df.loc[ ~ df.email.str.endswith('@gmail.com')]

"""
Obtener todos los usuarios de Alemania, Finlandia y Canadá:
"""
df.loc[ df.pais.isin(['Germany', 'Finland', 'Canada'])]

"""
Obtener el nombre y el email, de los usuario fem > 20 y de Alemania, Finlandia y Canadá:
"""
df.loc[(df.genero == 'female') & (df.edad > 20) & (df.pais.isin(['Germany', 'Finland', 'Canada'])), ['nombre', 'email']     ] 

"""
Obtener los diez usuarios de mayor edad
CF -> df.sort_values('edad', ascending=False).head(10)
"""
df.loc[:, ['nombre', 'edad']].sort_values('edad', ascending=False).head(10)
