#%%

import csv
import sys
import fileparse as fp


def leer_camion(nombre_archivo):
    data = fp.parse_csv(nombre_archivo, select=['nombre', 'cajones', 'precio'],
                        types=[str, int, float])           
    return data


def leer_precios(nombre_archivo):
    data = fp.parse_csv(nombre_archivo, has_headers=False, types=[str, float])
    return data


def informe_camion(nombre_archivo1, nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)

    def precio_de(fruta):
        for p in precios:
            if p[0] == fruta:
                return p[1]
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('----------')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
    lista = []
    for s in camion:
        lista = ((s['nombre'],s['cajones'], '$'+str(s['precio']),
                 precio_de(s['nombre'])-s['precio']))
        print('%10s %10d %10s %10.2f' % lista)


# informe_camion('/home/emiliano/Desktop/Curso_UNSAM/Data/fecha_camion.csv', '/home/emiliano/Desktop/Curso_UNSAM/Data/precios.csv')
