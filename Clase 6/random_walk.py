#%%
import numpy as np
import matplotlib.pyplot as plt
from documentacion import valor_absoluto


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)    
    return pasos.cumsum()


N = 10000

plt.plot(randomwalk(N))
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.show()


'''
Defino la cercania como las suma de distancias parciales al eje y
'''

caminatas = [randomwalk(10000) for _ in range(12)]
distancias_parciales = []
for caminata in caminatas:
    distancias_parciales.append([valor_absoluto(caminata[j]) for j in caminata])
suma_distancia_parciales = [sum(distancias) for distancias in distancias_parciales]
caminata_lejana = suma_distancia_parciales.index(max(suma_distancia_parciales))
caminata_cercana = suma_distancia_parciales.index(min(suma_distancia_parciales))


fig = plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
for caminata in caminatas:
    plt.plot(caminata)
plt.xticks([])
inferior, superior = plt.ylim()
plt.title('12 Caminatas al azar')

plt.subplot(2, 2, 3)
plt.plot(caminatas[caminata_lejana])
plt.xticks([])
plt.ylim([inferior, superior])
plt.title('La caminata que mas se aleja')

plt.subplot(2, 2, 4)
plt.plot(caminatas[caminata_cercana])
plt.xticks([]), plt.yticks([])
plt.title('La caminata que menos se aleja')

plt.tight_layout()
plt.show()