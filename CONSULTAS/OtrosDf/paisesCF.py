import pandas as pd
import numpy as np


archivo = pd.read_csv('../DATA/paises.csv', usecols=['pais', 'poblacion'], na_values='N/S')
df = pd.DataFrame(archivo)
print(df)

"""
0) Modifiqué el elem 196 q daba error xq tenia una colum de mas
1) convertí todos los valores N/S a NaN --> en la lectura agrego el parametro: na_values='N/S'
2) Borrar todas las filas que tengan NaN
"""
df = df.dropna()
"""
3) mostrar los 10 paises mas poblados ->     pais   poblacion
                        67              Filipinas  99.900.177
                        44    Ciudad del Vaticano         921  x mal
                        124              Kiribati      92.533  x mal
                        91                Hungría   9.982.000
                        26                Bolivia   9.947.418
                        33                Burundi   9.863.117
                        185  República Dominicana   9.823.821
                        24            Bielorrusia   9.685.000
                        88                  Haití   9.648.924
                        210                Suecia   9.555.893

4) mostrar los 10 paises menos poblados ->    pais      poblacion
                            86   Guinea Ecuatorial      1.014.999
                            43              Chipre      1.102.677
                            220     Timor Oriental      1.154.625
                            92               India  1.173.108.018 x mal
                            224  Trinidad y Tobago      1.228.691
                            65             Estonia      1.291.170
                            144           Mauricio      1.294.104
                            42               China  1.330.044.000 x mal
                            207        Suazilandia      1.354.051
                            71               Gabón      1.545.255

5) verificar el tipo de dato de poblacion y pasar a int
df = df.apply( lambda row : int(str(row['poblacion']).replace('.', '')), axis=1)
"""

# O sea q hice? 
# Primero convertí la columna 'poblacion' a int
paisesdf = df.apply( lambda row : int(str(row['poblacion']).replace('.', '')), axis=1)

# Despues le asigné esa nueva serie al DF (a la columna 'poblacion')
df['poblacion'] = paisesdf

# Ahora vuelvo a obtener el listado de paises mas y menos poblados:
mas_poblados = df.sort_values('poblacion', ascending=False).head(10)
"""
Nueva salida corregida-->
               pais   poblacion
42            China  1330044000
92            India  1173108018
64   Estados Unidos   310232863
93        Indonesia   242968342
29           Brasil   201103330
168        Pakistán   184404791
17        Bangladés   156118464
160         Nigeria   154000000
189           Rusia   140702000
118           Japón   127288000
"""

menos_poblados =  df.sort_values('poblacion', ascending=True).head(10)
"""
Nueva salida corregida -->
                    pais      poblacion
44      Ciudad del Vaticano        921
156                   Nauru      10065
228                  Tuvalu      10472
193              San Marino      31477
150                  Mónaco      32965
132           Liechtenstein      35000
192  San Cristóbal y Nieves      51134
54                 Dominica      72813
3                   Andorra      84000
6         Antigua y Barbuda      86754
"""

# sin los id-->
lista_de_paises = list(mas_poblados['pais'])
lista_poblaciones = list(mas_poblados['poblacion'])
nuevoDF = pd.DataFrame(lista_poblaciones, index=[lista_de_paises])
