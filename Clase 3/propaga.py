#%%%

def propaga(lista):
    i=0
    while i<len(lista):
        if lista[i]==1:
            j=i-1
            while (lista[j]==1 or lista[j]==0) and j>=0:
                lista[j]=1
                j-=1           
            j=i
            while j<=len(lista) and (lista[j]==1 or lista[j]==0):
                lista[j]=1
                j+=1
                if j == len(lista):
                    break
            i=j
        i+=1
    return lista

'''
print(propaga([1,0,0,0,0,-1,0,0,-1,1,1,1,-1,0,0,0,1]))
[1, 1, 1, 1, 1, -1, 0, 0, -1, 1, 1, 1, -1, 1, 1, 1, 1]
'''

def propaga2(lista):
    for i in range(1,len(lista)):
        if lista[i-1]==1 and lista[i]!=-1:
            lista[i]=1
    lista=lista[::-1]
    for i in range(1,len(lista)):
        if lista[i-1]==1 and lista[i]!=-1:
            lista[i]=1
   
    return lista[::-1]

'''
print(propaga2([1,0,0,0,0,-1,0,0,-1,1,1,1,-1,0,0,0,1]))
[1, 1, 1, 1, 1, -1, 0, 0, -1, 1, 1, 1, -1, 1, 1, 1, 1]
'''
