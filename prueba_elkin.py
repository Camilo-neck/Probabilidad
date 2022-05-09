# import pandas as pd

# DATA = pd.read_csv('Parciales/Parcial 1/datos_brutos_asociacion.csv')

# print(DATA.head())

f = open('Parciales/Parcial 1/datos_brutos_asociacion.csv', 'r')
for line in f:
	print(line)
f.close()
