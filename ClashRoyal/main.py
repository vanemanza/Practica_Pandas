import pandas as pd
import numpy as np


datos = pd.read_csv('clashrds.csv')
#print(datos)

df = pd.DataFrame(datos, columns=['Card', 'Cost', 'Type'])
print(df)