import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Tamaño de la muestra
n = 7614
# Frecuencias absolutas
nj = np.array([145, 2415, 3456, 852, 459, 157, 130])
# Hacer una grafica de barras
plt.bar(np.arange(len(nj)), nj)
# plt.xticks(np.arange(len(nj)), ['145', '2415', '3456', '852', '459', '157', '130'])
# Mostrar la grafica
# plt.show()
# print(pd.cut(nj, bins=10).categories)
# a = pd.concat([pd.cut(nj, bins=10), pd.Series(nj)], axis=1)

# pd.concat()

arr = np.array(np.arange(5))
arr1 = [*arr]
print(arr)
print(arr1/2)
