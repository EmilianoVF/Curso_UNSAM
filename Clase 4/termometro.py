#%%
import random
import numpy as np


T=sorted([random.normalvariate(37.5,0.2) for i in range(999)])


print('El maximo de las temperaturas es:', max(T))
print('El minimo de las temperaturas es:', min(T))
print('El promedio de las temperaturas es:', sum(T)/len(T))
print('La mediana de las temperaturas es:', T[round(len(T)/2)])


np.save('/home/emiliano/Desktop/Curso_UNSAM/Data/Temperaturas.npy',T)

#%%
import matplotlib.pyplot as plt

temperaturas=np.load('/home/emiliano/Desktop/Curso_UNSAM/Data/Temperaturas.npy').tolist()

plt.hist(temperaturas,bins=20)
plt.show()

# %%


