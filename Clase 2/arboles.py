import csv
from collections import Counter


# Lectura de Archivo
print('Se imprimen los resultados de los ejercicios')
print('')
print('')
print('Ejercicio 2.22 leer el archivo')
print('')

def leer_parque(nombre_archivo,parque):
    with open('/home/emiliano/Desktop/Curso_UNSAM/ejercicios_python/Data/'+nombre_archivo) as f:
        readCSV=csv.reader(f,delimiter=',')
        encabezados=next(readCSV)
        data=[]
        for row in readCSV:
            record=dict(zip(encabezados,row))
            for key in record.keys():
                try:
                    record[key]=float(record[key])
                except ValueError:
                    continue

            if parque=='TODOS': #cambio para el punto 2.28 extra
                data.append(record)
            elif parque == record['espacio_ve']:
                data.append(record)


    return data


print('imprimo la lista de arboles para "GENERAL PAZ", 690')
print('')
print('')
print('')
print('Ejercicio 2.23 conjunto de especies en un parque o lista')
print('')


def especies(lista_arboles):
    arboles=[]
    for arbol in lista_arboles:
        arboles.append(arbol['nombre_com'])
    return set(arboles)

print('''
        {'Alcanforero', 'Corona de cristo', 'Pino carrasco (Pino de Jerusalén)', 'Ciprés blanco', 'Plátano', 'Chamaecyparis', 'Pino', 'Ginkgo', 'Washingtonia', 
        'Tipa blanca', 'Eucalipto', 'Paraíso', 'Lapacho rosado', 'Pino de las canarias', 'Pindó', 'Roble americano', 'Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)', 
        'Fresno (Fresno común)', 'Cedro de San Juan', 'Olivo', 'Olmo europeo', 'Sauce eléctrico', 'Ceibo', 'Nogal europeo (Nogal común)', 'Morera blanca', 'Cedro del Himalaya', 
        'Roble', 'Visco (Viscote, Arca)', 'Álamo negro', 'Roble común', 'Criptomeria (Cedro del Japón)', 'Ciprés leylandi', 'Acacia negra', 'Juniperus', 
        'Árbol del cielo (Ailanto o Árbol de los dioses)', 'Ciprés', 'Magnolia', 'Olmo', 'Timbó (Oreja de negro)', 'Libocedro (Calocedro)', 
        'Cedro del Atlas (Cedro plateado o Cedro atlántico)', 'Casuarina', 'Washingtonia (Palmera washingtonia)', 'Palma Bangalow  (Palma Rey)', 
        'Morera negra', 'Cedrela', 'Pino del Paraná (Pino de Misiones o Pino de Brasil)', 'Níspero japonés', 'Olivo oloroso', 'Fotinia', 'Fresno americano', 
        'Tuja', 'Tuya oriental', 'Ciprés calvo', 'No Determinado', 'Laurus', 'Tilo', 'Morera de papel (Moral de China)', 'Laurel de jardin (Laurel de flor)', 
        'Caqui', 'Palo borracho rosado', 'Bunya-bunya (Araucaria de Bidwill)', 'Ombú', 'Olea', 'Acacia blanca', 'Jacarandá', 'Ligustro disciplinado (Ligustro variegado)', 
        'Limpiatubos', 'No Determinable', 'Liquidambar', 'Roble sedoso (Grevillea)', 'Ficus', 'Palma de california', 'Ligustro', 'Fenix', 'Arce negundo', 'Álamo blanco piramidal', 
        'Cedro del Himalaya variedad aurea', 'Palmito', 'Cedro', 'Falso Guayabo (Guayaba del Brasil)'}
''')
print('')
print('')
print('')
print('')

print('Ejercicio 2.24')
print('')
def contar_ejemplares(lista_arboles):
    total_arboles=Counter()
    for arbol in lista_arboles:
        total_arboles[arbol['nombre_com']]+=1

    return total_arboles


parques=['GENERAL PAZ', 'ANDES, LOS','CENTENARIO']



def contar_ejemplares_en(parques):
    listas=[]
    for parque in parques:
        data=leer_parque('arbolado-en-espacios-verdes.csv',parque)
        lista=contar_ejemplares(data).most_common(5)
        listas.append(lista)
    for i in range(len(listas)):
        print(parques[i])
        print(listas[i])
    return listas



print('''
        GENERAL PAZ
        [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
        ANDES, LOS
        [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
        CENTENARIO
        [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]
''')
print('')
print('')
print('')
print('')

print('Ejercicio 2.25')
print('')

def obtener_alturas(lista_arboles,especie):
    altura=[]
    for arbol in lista_arboles:
        if especie==arbol['nombre_com']:
            altura.append(arbol['altura_tot'])

    altura_maxima=round(max(altura),2)
    altura_promedio=round(sum(altura)/len(altura),2)
    caracter_especie=len(especie)
    print(f'La altura maxima del {especie:>{caracter_especie}s}, es de {altura_maxima} m y el promedio es de {altura_promedio} m')
    return [altura_maxima,altura_promedio]

def obtener_alturas_en(parques,especie):
    for parque in parques:
        print(parque)
        obtener_alturas(leer_parque('arbolado-en-espacios-verdes.csv',parque),especie)
    return


print('''
        GENERAL PAZ
        La altura maxima del Jacarandá, es de 16.0 m y el promedio es de 10.2 m
        ANDES, LOS
        La altura maxima del Jacarandá, es de 25.0 m y el promedio es de 10.54 m
        CENTENARIO
        La altura maxima del Jacarandá, es de 18.0 m y el promedio es de 8.96 m
''')

print('')
print('Ejercicio 2.26 y 2.27')
print('')
def obtener_inclinaciones(lista_arboles,especie):
    inclinacion=[]
    for arbol in lista_arboles:
        if especie==arbol['nombre_com']:
            inclinacion.append(arbol['inclinacio'])
    return set(inclinacion)






def especimen_mas_inclinado(lista_arboles):
    especies_todas=especies(lista_arboles)
    inclinacion_de_especie=0
    especie_inclinada='alguna'
    for especie in especies_todas:
        inclinacion=max(obtener_inclinaciones(lista_arboles,especie))
        if inclinacion > inclinacion_de_especie:
            inclinacion_de_especie=inclinacion
            especie_inclinada=especie
    return especie_inclinada,inclinacion_de_especie


def especie_mas_inclinada_en(parques):
    for parque in parques:
        lista_arboles=leer_parque('arbolado-en-espacios-verdes.csv',parque)
        especie_inclinada,inclinacion_de_especie=especimen_mas_inclinado(lista_arboles)
        caracter_especie=len(especie_inclinada)
        caracter_parque=len(parque)
        print(f'La especie mas inclinada en {parque:>{caracter_parque}s} es {especie_inclinada:>{caracter_especie}s} con una inclinaion de  {inclinacion_de_especie} grados, esta que se cae!!')
    return


print('''
        La especie mas inclinada en GENERAL PAZ es Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert) con una inclinaion de  70.0 grados, esta que se cae!!
        La especie mas inclinada en ANDES, LOS es Jacarandá con una inclinaion de  30.0 grados, esta que se cae!!
        La especie mas inclinada en CENTENARIO es Falso Guayabo (Guayaba del Brasil) con una inclinaion de  80.0 grados, esta que se cae!!

''')
print('')
print('')
print('')
print('Ejercicio 2.28')
print('')
def especie_promedio_mas_inclinada(lista_arboles):
    especies_todas=especies(lista_arboles)
    promedio_inclinacion_especie=0
    especie_inclinada='alguna'
    for especie in especies_todas:
        inclinacion=obtener_inclinaciones(lista_arboles,especie)
        promedio_inclinacion=sum(inclinacion)/len(inclinacion)
        if promedio_inclinacion > promedio_inclinacion_especie:
            promedio_inclinacion_especie=promedio_inclinacion
            especie_inclinada=especie
    return especie_inclinada,promedio_inclinacion_especie




def especie_promedio_mas_inclinada_en(parques):
    for parque in parques:
        lista_arboles=leer_parque('arbolado-en-espacios-verdes.csv',parque)
        especie_inclinada,promedio_inclinacion_especie=especie_promedio_mas_inclinada(lista_arboles)
        caracter_especie=len(especie_inclinada)
        caracter_parque=len(parque)
        print(f'La especie {especie_inclinada:>{caracter_especie}s} del parque {parque:>{caracter_parque}s} tiene un promedio de inclinaion de  {promedio_inclinacion_especie} grados, esta que se cae!!')
    return 


print('''
        La especie Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert) del parque GENERAL PAZ tiene un promedio de inclinaion de  35.0 grados, esta que se cae!!
        La especie Álamo plateado del parque ANDES, LOS tiene un promedio de inclinaion de  25.0 grados, esta que se cae!!
        La especie Falso Guayabo (Guayaba del Brasil) del parque CENTENARIO tiene un promedio de inclinaion de  34.0 grados, esta que se cae!
''')




# Modifico la funcion de lectura para que pueda no filtrar por nombre de parque utilizando 'TODOS' como nombre de parque


print('Los extra')
print('')
print('')
def especimen_mas_inclinado_todos(lista_arboles):
    inclinacion=[]
    incli=[]
    lat_lon=[]
    especie=[]
    parque=[]
    for arbol in lista_arboles:
        inclinacion.append(arbol['inclinacio'])
    maxima_inclinacion=max(inclinacion)
    index_maxima_inclinacion=[i for i,j in enumerate(inclinacion) if j==maxima_inclinacion]   
    if len(index_maxima_inclinacion) > 1:
        for i in index_maxima_inclinacion:
            incli.append(lista_arboles[i]['inclinacio'])
            lat_lon.append([lista_arboles[i]['lat'],lista_arboles[i]['long']])
            especie.append(lista_arboles[i]['nombre_com'])
            parque.append(lista_arboles[i]['espacio_ve'])
    else:
        i=index_maxima_inclinacion
        incli.append(lista_arboles[i]['inclinacio'])
        lat_lon.append([lista_arboles[i]['lat'],lista_arboles[i]['long']])
        especie.append(lista_arboles[i]['nombre_com'])
        parque.append(lista_arboles[i]['espacio_ve'])
    return especie,incli,parque,lat_lon


def decime_los_inclinados(lista_arboles):
    especie,incli,parque,lat_lon=especimen_mas_inclinado_todos(lista_arboles)
    for i in range(len(especie)):
        #print(especie[i],incli[i],parque[i],lat_lon[i])
        caracter_especie=len(especie[i])
        caracter_parque=len(parque[i])
        #print(caracter_especie,caracter_parque)
        print(f'Ubicado en el parque {parque[i]:>{caracter_parque}s} con latitud de {lat_lon[i][0]:<3f} y una longitud de {lat_lon[i][1]:<3f} se encuentra un {especie[i]:>{caracter_especie}s} con una inclinacion de {incli[i]} grados') 
    return

print('mas inclinados')

print('')
print('')

print('''
        Ubicado en el parque AMEGHINO, FLORENTINO con latitud de -34.6368768575 y una longitud de -58.39515390060001 se encuentra un Timbó (Oreja de negro) con una inclinacion de 90.0 grados
        Ubicado en el parque REPUBLICA del ECUADOR con latitud de -34.5637949947 y una longitud de -58.4219720155 se encuentra un Pata de vaca  (Pezuña de vaca) con una inclinacion de 90.0 grados
        Ubicado en el parque PARQUE DE FLORA NATIVA BENITO QUINQUELA MARTÍN con latitud de -34.634654141599995 y una longitud de -58.366948793599995 se encuentra un Abutilo con una inclinacion de 90.0 grados
        Ubicado en el parque DE SAN BENITO con latitud de -34.5495758129 y una longitud de -58.437764978000004 se encuentra un Cedro del Himalaya con una inclinacion de 90.0 grados
''')


def especimen_mas_alto_todos(lista_arboles):
    inclinacion=[]
    incli=[]
    lat_lon=[]
    especie=[]
    parque=[]
    for arbol in lista_arboles:
        inclinacion.append(arbol['altura_tot'])
    maxima_inclinacion=max(inclinacion)
    index_maxima_inclinacion=[i for i,j in enumerate(inclinacion) if j==maxima_inclinacion]   
    if len(index_maxima_inclinacion) > 1:
        for i in index_maxima_inclinacion:
            incli.append(lista_arboles[i]['altura_tot'])
            lat_lon.append([lista_arboles[i]['lat'],lista_arboles[i]['long']])
            especie.append(lista_arboles[i]['nombre_com'])
            parque.append(lista_arboles[i]['espacio_ve'])
    else:
        i=index_maxima_inclinacion[0]
        incli.append(lista_arboles[i]['altura_tot'])
        lat_lon.append([lista_arboles[i]['lat'],lista_arboles[i]['long']])
        especie.append(lista_arboles[i]['nombre_com'])
        parque.append(lista_arboles[i]['espacio_ve'])
    return especie,incli,parque,lat_lon


print('mas altos')

print('')



def decime_los_mas_altos(lista_arboles):
    especie,incli,parque,lat_lon=especimen_mas_alto_todos(lista_arboles)
    for i in range(len(especie)):
        #print(especie[i],incli[i],parque[i],lat_lon[i])
        caracter_especie=len(especie[i])
        caracter_parque=len(parque[i])
        #print(caracter_especie,caracter_parque)
        print(f'Ubicado en el parque {parque[i]:>{caracter_parque}s} con latitud de {lat_lon[i][0]:<3f} y una longitud de {lat_lon[i][1]:<3f} se encuentra un {especie[i]:>{caracter_especie}s} con una altura de {incli[i]} metros') 


print('''
        Ubicado en el parque REPUBLICA de CHILE con latitud de -34.5818308351 y una longitud de -58.398926961099995 se encuentra un Rosa de Siria con una altura de 54.0 metros
''')

