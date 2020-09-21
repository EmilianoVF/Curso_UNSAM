def buscar_u_elemento(lista, elem):
    for i, num in enumerate(lista[::-1]):
        if elem == num:
            return len(lista)-i-1
    return -1


'''
print(buscar_u_elemento([1,2,3,2,3,4],3))
4
'''


def buscar_n_elemento(lista, elem):
    i = 0
    for lta in lista:
        if elem == lta:
            i += 1
    return i


'''
print(buscar_n_elemento([1,2,1,2,1,4],1))
3
'''


def maximo(lista):
    if len(lista) > 1:
        m = lista[0] 
        for e in lista[1:]:
            if e > m:
                m = e
    else:
        m = lista[0]
    return m


'''
print(maximo([-1,-2,-3,-4,-77]))
-1
'''


def minimo(lista):
    if len(lista) > 1:
        m = lista[0]
        for e in lista[1:]:
            if e < m:
                m = e
    else:
        m = lista[0]
    return m


'''
print(minimo([-4,-66]))
'''
