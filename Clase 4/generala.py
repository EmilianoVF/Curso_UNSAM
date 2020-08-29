#%%
import random
import numpy as np

#%%
def tirar(dados=5,*args):
    if args:
        cantidad_dados=args
    else:
        cantidad_dados=dados   
    return [random.randint(1,6) for i in range(cantidad_dados)]

def es_generala(tirada):
    primer_dado=tirada[0]
    for dado in tirada[1:]:
        if primer_dado!=dado:
            return False
    return True



# %%
N=1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

'''
N=1000000...
Tiré 1000000 veces, de las cuales 739 saqué generala servida.
Podemos estimar la probabilidad de sacar generala servida mediante 0.000739.
'''


#%%



        
def primer_tirada(lista):
    numero=0
    veces_numero=0
    while len(lista)>0:
        dado=lista[0]
        index_repetidos=[k for k,j in enumerate(lista) if j==dado ]
        repetidos=len(index_repetidos)
        if repetidos>veces_numero:
            veces_numero=repetidos
            numero=dado
        if repetidos!=0:
            for repetido in index_repetidos[::-1]:
                lista.pop(repetido)
        else:
            lista.pop(0)
    return numero, veces_numero


def generala_no_servida(lista):
    numero,veces_numero=primer_tirada(lista)
    generala=None
    if veces_numero==5:
        generala=True
        return generala
    if veces_numero!=5:
        for i in range(2):
            tirada=tirar(5-veces_numero)
            veces_numero+=len([k for k,j in enumerate(tirada) if j==numero ])
            if veces_numero==5:
                generala=True
                break
    return generala==True





    




# %%
N=1000000
salio_generala_no_servida = [generala_no_servida(tirar()) for i in range(N)]
G = sum([generala_no_servida(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala no servida o servida no lo se.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')

'''
Tiré 1000000 veces, de las cuales 45615 saqué generala no servida o servida no lo se.
Podemos estimar la probabilidad de sacar generala mediante 0.045615.
'''

    
# %%
