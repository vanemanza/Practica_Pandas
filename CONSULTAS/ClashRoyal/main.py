import pandas as pd

datos = pd.read_csv('clashrds.csv')
#print(datos)

df = pd.DataFrame(datos, columns=['Card', 'Cost', 'Count', 'Damage', 'Damage/sec', 'DeathDamage', 'Health', 'HitSpeed', 'Level', 'MaxSpawned', 'Radius', 'Range', 'SpawnDPS', 'SpawnDamage', 'SpawnHealth', 'SpawnSpeed', 'SpawnerHealth', 'TroopSpawned', 'Type'])

df['Count'][20] = '3'

df['Count'] = pd.to_numeric(df['Count'])
df['Damage'] = pd.to_numeric(df['Damage'])
