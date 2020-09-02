#%%
import random
import numpy as np
import matplotlib.pyplot as plt



def crear_album(figus_total):
    return np.zeros((figus_total),dtype=int)

def album_incompleto(A):
    return True if 0 in A else False

def comprar_figus(figus_total):
    return random.randint(0,figus_total-1)

def cuantas_figus(figus_total):
    A=crear_album(figus_total)
    i=0
    while album_incompleto(A):
        A[comprar_figus(figus_total)]+=1
        i+=1
    return i

'''
n_repeticiones=100
cuantas_figus_album_670=[cuantas_figus(670) for i in range(n_repeticiones)]
print('En promedio compras',np.mean(cuantas_figus_album_670), 'figuritas para un albun de 670')
'''

def comprar_paquete(figus_total,figus_paquete):
    return [comprar_figus(figus_total) for i in range(figus_paquete)]

def cuantos_paquetes(figus_total,figus_paquete):
    A=crear_album(figus_total)
    i=0
    while album_incompleto(A):
        for figu in comprar_paquete(figus_total,figus_paquete):
            A[figu]+=1
        i+=1
    return i

'''
cuantos_paquetes_album_670=[cuantos_paquetes(670,5) for i in range(1000)]
'''
'''
print(np.mean(cuantos_paquetes_album_670))
949.181
'''

'''
probabilidad_850_paquetes_o_menos=sum([1 for album in cuantos_paquetes_album_670 if album<=850])
print(probabilidad_850_paquetes_o_menos)
313
'''

'''
plt.hist(cuantos_paquetes_album_670,bins=30)
plt.show()
'''

'''
chance_90_completar_album=max(sorted(cuantos_paquetes_album_670)[0:900])
print(chance_90_completar_album)
1172
'''


def comprar_paquete_sin_repes(figus_total,figus_paquete):
    paquete_sin_repes=comprar_paquete(figus_total,figus_paquete)
    while len(set(paquete_sin_repes))!=5:
        paquete_sin_repes=comprar_paquete(figus_total,figus_paquete)
    return paquete_sin_repes

def cuantos_paquetes_sin_repes(figus_total,figus_paquete):
    A=crear_album(figus_total)
    i=0
    while album_incompleto(A):
        for figu in comprar_paquete_sin_repes(figus_total,figus_paquete):
            A[figu]+=1
        i+=1
    return i

#[cuantos_paquetes_sin_repes(670,5) for i in range(1000)]

'''
cuantos_paquetes_album_670_sin_repes=[cuantos_paquetes_sin_repes(670,5) for i in range(1000)]

print(np.mean(cuantos_paquetes_album_670_sin_repes))
933.648

probabilidad_850_paquetes_o_menos_sin_repes=sum([1 for album in cuantos_paquetes_album_670_sin_repes if album<=850])
print(probabilidad_850_paquetes_o_menos_sin_repes)
338


plt.hist(cuantos_paquetes_album_670_sin_repes,bins=30)
plt.show()


chance_90_completar_album_sin_repes=max(sorted(cuantos_paquetes_album_670_sin_repes)[0:900])
print(chance_90_completar_album_sin_repes)
1137
'''
#%%

import random
import numpy as np

def crear_album_amigues(figus_total,cantidad_amigues):
    albumes_de_amigues=[]
    for i in range(cantidad_amigues):
        albumes_de_amigues.append(-np.ones(figus_total,dtype=int))
    return albumes_de_amigues

def album_incompleto(A):
    return True if -1 in A else False

def album_incompleto_amigues(A):
    return True if any([album_incompleto(A) for A in A]) else False

def comprar_figus(figus_total):
    return random.randint(0,figus_total-1)

def comprar_paquete(figus_total,figus_paquete):
    return [comprar_figus(figus_total) for i in range(figus_paquete)]

def a_quien_le_falta(figu,albumes_amigues):
    for i in range(len(albumes_amigues)):     
        if figu not in albumes_amigues[i]:
            return i
    return 0

            

def cooperar_vs_competir(figus_total,figus_paquete,cantidad_amigues):
    albumes_amigues=crear_album_amigues(figus_total,cantidad_amigues)
    i=0
    while album_incompleto_amigues(albumes_amigues):
        for figu in comprar_paquete(figus_total,figus_paquete):
            amigue=a_quien_le_falta(figu,albumes_amigues)
            print(amigue)
            albumes_amigues[amigue][figu]=figu
        i+=1
    return i

'''
cooperar_5_amigues=[cooperar_vs_competir(670,5,5) for i in range(50)]

print(np.mean(cooperar_5_amigues))
2025.96
'''
'''
probabilidad_850_amigues=sum([1 for album in cooperar_5_amigues if album<=850])

print(probabilidad_850_amigues)
0
'''



