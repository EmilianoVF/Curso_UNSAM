
#%%

def busqueda_binaria(lista,x):
    pos=-1
    izq=0
    der=len(lista)-1
    while izq<=der:
        medio=(izq+der)//2
        if lista[medio]==x:
            pos= medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return medio if pos==-1 else pos 




def donde_insertar(lista,x):
    return busqueda_binaria(lista,x)
