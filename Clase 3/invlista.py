
#%%
lista_numeros=[1,2,3,4,5]

lista_ciudades=['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

'''
print(lista_numeros[::-1])
[5, 4, 3, 2, 1]
'''

'''
print(lista_ciudades[::-1])
['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
'''


'''
Trato de invertir sin usar [::-1]

medio raro
'''

def invertir_lista(lista):
    invertida=[]
    for i in range(len(lista)):
        j=len(lista)-1-i
        invertida.append(lista[j])
    return invertida

'''
print(invertir_lista(lista_ciudades))
['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
'''

'''
print(invertir_lista(lista_numeros))
[5, 4, 3, 2, 1]
'''
        