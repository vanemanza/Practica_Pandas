import numpy as np
import pandas as pd

"""
la clase nan de numpy 
Representa la ausencia de valor. 
Not a number 
NaN == None(python)
"""

lista = [10, 20, np.NaN, 40, np.NaN]
a = pd.Series(lista) 

"""
en principio parece q la serie almacena 5 elementos, 
pero solo almacena 3, ya q los NaN no poseen valor.
"""

"""
Para conocer si la serie posee nulos, 
puedo usar la funcion-->   isnull(<serie>)
el argumento es la serie a evaluar,
y retorna una serie de booleanos.
Los elem q devuelvan False, contienen un valor.
Los elem q devuelvan True son NaN.
"""

pd.isnull(a)    # 0 False
                # 1 False
                # 2 True
                # 3 False
                # 4 True

"""
Otra forma es con notnull()
Devuelve los valores opuestos a isnull
"""    

pd.notnull(a)   # 0 True
                # 1 True
                # 2 False
                # 3 True
                # 4 False            

"""
Tambien se puede hacer con el metodo isnull()
Se aplica directamente a la serie
"""               

a.isnull()      # 0 False
                # 1 False
                # 2 True
                # 3 False
                # 4 True


"""
Para eliminar los valores nulos uso el metodo dropna()
Genera una nueva serie sin los null.
La serie original queda igual.
"""

a.dropna()  # 0    10.0
            # 1    20.0
            # 3    40.0

"""
Si no quiero eliminar los valores nulos y solo quiero cambiar el valor,
uso el metodo fillna(<nuevo valor>)
Obtengo una nueva serie con los NaN reemplazados.
"""            
a.fillna(99)

"""
Si quiero obtener todos los elem q tengan valor, lo hago con notnull()
"""

a[ a.notnull()]
