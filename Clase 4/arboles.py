#%%
import numpy as np
import matplotlib.pyplot as plt


Jacaranda_D_Y_H=np.load('/home/emiliano/Desktop/Curso_UNSAM/Data/Jacaranda_D_Y_H.npy').tolist()

d=[Jacaranda_D_Y_H[i][0] for i in range(len(Jacaranda_D_Y_H))]
h=[Jacaranda_D_Y_H[i][1] for i in range(len(Jacaranda_D_Y_H))]

plt.scatter(d,h,alpha=0.1)
plt.xlabel('Diamtro [cm]')
plt.ylabel('Altura [m]')
plt.show()


