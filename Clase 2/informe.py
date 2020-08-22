import csv
import sys

def leer_camion(nombre_archivo):
    with open('/home/emiliano/Desktop/Curso_UNSAM/ejercicios_python/'+nombre_archivo) as f:
        readCSV=csv.reader(f,delimiter=',')
        encabezados=next(readCSV)
        costo_total=0.0
        data=[]
        for row in readCSV:
            record=dict(zip(encabezados,row))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                continue
            record['cajones']=ncajones
            record['precio']=precio
            data.append(record)
    return data



def leer_precios(nombre_archivo):
    with open('/home/emiliano/Desktop/Curso_UNSAM/ejercicios_python/'+nombre_archivo,'rt') as f:
        data={}
        for row in f:
            r=row.split(',')
            try:
                r[1]=float(r[1])
            except ValueError:
                continue 
            except IndexError:
                continue
            data[r[0]]=r[1]
    return data



precios_venta=leer_precios('Data/precios.csv')
precios_costo=leer_camion('Data/camion.csv')

def informe(precios_venta,precios_costo):
    total=[]
    for cajon in precios_costo:
        if cajon['nombre'] in precios_venta:
            diferencia_porcajon= precios_venta[cajon['nombre']]-cajon['precio']
            if diferencia_porcajon > 0:
                print('ganas $', round(diferencia_porcajon,2), 'por cajon de ',cajon['nombre'],'que vendas')
            if diferencia_porcajon < 0:
                print('perdes $', round(diferencia_porcajon,2), 'por cajon de ',cajon['nombre'],'que vendas')

            total.append(diferencia_porcajon*cajon['cajones'])

    if sum(total)>0:
        print('si vendes todos los cajones ganas $', round(sum(total),2) )


    if sum(total)<0:
        print('si vendes todos los cajones perdes $', round(sum(total),2) )
        print('La vida es dura')



print('''
        ganas $ 8.02 por cajon de  Lima que vendas
        ganas $ 15.18 por cajon de  Naranja que vendas
        ganas $ 2.02 por cajon de  Caqui que vendas
        ganas $ 29.66 por cajon de  Mandarina que vendas
        ganas $ 33.11 por cajon de  Durazno que vendas
        ganas $ 15.79 por cajon de  Mandarina que vendas
        ganas $ 35.84 por cajon de  Naranja que vendas
        si vendes todos los cajones ganas $ 15314.95
''')