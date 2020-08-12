


def Tiene_Tilde(lapalabra):
    return len(lapalabra) != len(lapalabra.encode())

frase='todos somos programadores'
palabras= frase.split()
frase_t=[]
for palabra in palabras:
    if (Tiene_Tilde(palabra)==False and len(palabra)>1):
        palabra_t=list(palabra)
        if ',' in palabra_t:
            j=1
        else:
            j=0
        if palabra_t[-1-j]=='o':
            palabra_t[-1-j]='e'
            palabra=''.join(palabra_t)
        elif palabra_t[-2-j]=='o':
            palabra_t[-2-j]='e'
            palabra=''.join(palabra_t)
    
    frase_t.append(palabra)

print(" ".join(frase_t))