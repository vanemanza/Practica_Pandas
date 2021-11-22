import pandas as pd
import numpy as np

"""
Para leer un archivo csv, usamos la funcion -> pd.read_csv()
Recibe como argumento el archivo con el q vamos a trabajar. 

Los archivos csv separan la información x comas, 
pero si la info se separa mediante otro caracter podemos indicar
bajo q caracter se está separando la información,mediante el uso de 
metodo demiliter. 

Con el método header, puedo indicar a traves de q registro quier
que se comience la lectura.

"""

usersdf = pd.read_csv('users.csv', delimiter=',',header=5 )
print(usersdf)
"""
Para acceder a los primeros registros uso el método head()
Por default visualizo los primeros 5 registros. 
Pero puedo pasarle como argumento la cantidad de registros 
que quiero visualizar.
df.head(<cantidad>)

Para acceder a los ultimos registros uso el método tail()
Nos devuelve los ultimos 5 registros. 
Tambien le puedo pasar x arg la cantidad q necesito ver.

"""

"""
Para reemplazar los valores nulos x np.NaN, 
lo puedo indicar desde la lectura del archivo, 
a traves del parametro na_value = 'N/S' x ej
"""

paisesdf = pd.read_csv('paises.csv', usecols=['pais', 'poblacion', 'long', 'lat'], na_values='N/S')
print(paisesdf)

# para obtener los paises q si tienen valor población
print(paisesdf[ paisesdf.poblacion.notnull()])

"""
Para cambiar el tipo de un registro, x ejemplo los valores
de poblacion son tipo object y los quiero cambiar a int -->

Puedo usar una funcion lambda mediante metodo apply
1) obtengo la poblacion
    paisesdf.apply( lambda row: row['poblacion'], axis=1)

2) elimino los NaN y obtengo solo los paises con poblacion
    paises = paisesdf[ paisesdf.poblacion.notnull()]

3) ahora convierto a str y reemplazo los puntos x nada, 
    y x ultimo lo convierto a entero.
    paises.apply( lambda row: int(str(row['poblacion]).replace('.', '')) , axis=1)
4) por ultimo actualizo la columna poblacion:
    paises.poblacion = paises.apply( lambda row: int(str(row['poblacion]).replace('.', '')) , axis=1)
"""
