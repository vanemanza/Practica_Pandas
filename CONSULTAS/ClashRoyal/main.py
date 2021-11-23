import pandas as pd
import numpy as np

datos = pd.read_csv('../DATA/clashrds.csv')
#print(datos)

df = pd.DataFrame(datos, columns=['Card', 'Cost', 'Count', 'Damage', 'Damage/sec', 'DeathDamage', 'Health', 'HitSpeed', 'Level', 'MaxSpawned', 'Radius', 'Range', 'SpawnDPS', 'SpawnDamage', 'SpawnHealth', 'SpawnSpeed', 'SpawnerHealth', 'TroopSpawned', 'Type'])

df['Count'][20] = '3'

df['Count'] = pd.to_numeric(df['Count'])
df['Damage'] = pd.to_numeric(df['Damage'])

"""
Quiero cambiar los indices para q empiecen desde el 1
"""
df.index = list(np.arange(1,71))

"""
Quiero ver q tipo de dato es cada columna
"""

for column in df.columns:
    tipo = df[column].dtype
    print(f'{column} = {tipo}')
    
"""
Agrupar por tipo:
"""
Tropas = df.loc[df.Type == 'Troops and Defenses']
Hechizos = df.loc[df.Type == 'Damaging Spells']
Spawners = df.loc[df.Type == 'Spawners']
