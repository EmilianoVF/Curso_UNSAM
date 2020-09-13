#%%
import matplotlib.pyplot as plt
import numpy as np
import random

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def experimento_secuencial_promedio(lista, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(len(lista))
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def busqueda_binaria(lista,x):
    pos=-1
    izq=0
    der=len(lista)-1
    comps = 0
    while izq<=der:
        comps += 1
        medio=(izq+der)//2
        if lista[medio]==x:
            pos= medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return pos, comps

def experimento_binario_promedio(lista, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(len(lista))
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom



len_listas=np.linspace(1,256,50,dtype=int)
cantidad_de_comparaciones_binarias=[]
cantidad_de_comparaciones_lineales=[]

for l in len_listas:
    lista=sorted([random.randint(1,l) for i in range(l)])
    cantidad_de_comparaciones_binarias.append(experimento_binario_promedio(lista,50))
    cantidad_de_comparaciones_lineales.append(experimento_secuencial_promedio(lista,50))


plt.plot(len_listas,cantidad_de_comparaciones_binarias,'r')
plt.plot(len_listas,cantidad_de_comparaciones_lineales,'k')
plt.xlabel('Largo de la lista')
plt.ylabel('Cantidad de comparaciones')
plt.legend(['Busqueda Binaria','Busqueda Lineal'])
plt.xlim((1,100))
plt.ylim((1,cantidad_de_comparaciones_lineales[20]))
plt.show()
