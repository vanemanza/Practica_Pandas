import pandas as pd
indices=["A","B","C","D","E"]
usuarios = {
    'Nombre': ["Vane", "Reni", "Faus", "Augus", "Sugi"],
    'Edad': [46, 17, 15, 12, 2],
    'Peso(KG)': [60, 55, 72, 35, 6],
}
df1 = pd.DataFrame(usuarios,index=indices)

mas_jovenes=df1[df1["Edad"]<=12].index
mas_grandes=df1.drop(mas_jovenes)

print("El DF completo es:")
print(df1,"\n")

print("El DF de los usuarios de edad mayor a 12 es:")
print(mas_grandes)

'------------------------------------------------------------------------------------------'

roll_no = [501, 502, 503, 504, 505]
data = {
    'Name': ['Alice', 'Steven', 'Neesham', 'Chris', 'Alice'],
    'Age':  [19, None, 18, 21, None],
    'Income($)': [4000, 5000, None, 3500, None],
    'Expense($)': [3000, 2000, 2500, 25000, None]
}
df2 = pd.DataFrame(data)


#1) notna()
"""
El método DataFrame.notna() NO modifica el DF original, si no que devuelve un objeto booleano con el mismo 
número de filas y columnas que el DataFrame llamante. 
Si un elemento no es NaN, se asigna al valor True en el objeto booleano,
y si un elemento es un NaN, se asigna al valor False.
"""
"""
print("DF original:")
print(df2)

print("")

df22 = df2[df2['Income($)'].notna()]
print("DF despues de eliminar las filas con NaN de la columna Income:")
print(df22)
"""

#2) dropna() 
# data = data.dropna(how='all')
"""
Elimina sólo las filas con valores NaN para todos los campos del DataFrame. 
Establecemos how='all' en el método dropna() para que el método elimine la fila sólo si 
todos los valores de las columnas de la fila son NaN.
"""
# data = data.dropna(subset=["Id"])
"""
Se eliminan todas las columnas del DataFrame que tienen un valor NaN sólo en la columna Id.
"""
# data = data.dropna()
"""
Por defecto, el método dropna() eliminará todas las filas que tengan al menos un valor NaN.
"""