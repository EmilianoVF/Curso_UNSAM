#%%
import random
import matplotlib.pyplot as plt

def reparto(naipes):
    mis_cartas=[]
    for carta in range(3):
        carta=random.choice(naipes)
        mis_cartas.append(carta)
        index=naipes.index(carta)
        naipes.pop(index)
    return mis_cartas

def sumo_envido(lista):
    repetidas=len(lista)
    for i in range(repetidas):
        if lista[i]>=10:
            lista[i]=0
    valores=sorted(lista)
    if repetidas>2:
        envido=20+sum(valores[-2:])
    else:
        envido=20+sum(valores)

    return envido

def envido(lista):
    palos=[palo[1] for palo in lista]
    valor=[palo[0] for palo in lista]
    envido=0
    for i in range(2):
        carta=palos[i]
        index_repetidos=[k for k,j in enumerate(lista) if j[1]==carta ]
        repetidos=len(index_repetidos)
        if repetidos>1:
            envido=sumo_envido([valor[i] for i in index_repetidos])
    return envido


def envido_en_una_mano():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos] 
    cartas=reparto(naipes)
    return envido(cartas)

#%%

N=100000
E=[]
for i in range(N):
    ipa=envido_en_una_mano()
    if ipa==0:
        ipa=19
    E.append(ipa)

plt.hist(E,bins=15,range=[19,33],align='mid')
plt.show()

#%%




print(sumo_envido([10,7]))
