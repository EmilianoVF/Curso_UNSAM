#%%
def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de un numero
    '''
    return n if n > 0 else - n


def suma_pares(lista):
    '''
    Toma un iterable y devuelve la suma de los 
    numeros pares que se encuentran en la lista
    '''
    res = 0
    for e in lista:
        if e % 2 == 0:
            res += e
    return res


def multiplico(a, b):
    '''
    Realiza la multiplicacion de dos numeros enteros y positivos
    '''
    res = 0
    nb = b
    while nb != 0:
        res += a
        nb -= 1
    return res


def collatz(n):
    '''
    Toma un numero entero positivo y devuelve la cantidad de pasos
    que hay en la orbita del numero n .
    mas informacion sobre la conjetura de Collatz
    https://es.wikipedia.org/wiki/Conjetura_de_Collatz
    '''
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
