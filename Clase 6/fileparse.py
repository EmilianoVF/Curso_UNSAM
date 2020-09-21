#%%i
import csv
import gzip
from pathlib import Path


def itero(filas, select, types, has_headers):
    if has_headers:
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila:
                continue
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    if not has_headers:
        registros = []
        for fila in filas:
            if not fila:
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = tuple(fila)
            registros.append(registro)
    return registros


def itero_iterables(filas, select, types, has_headers):
    if has_headers:
        headers = filas[0]
        if select:
            indices = [headers.index(nom_col) for nom_col in select]
            headers = select
        else:
            indices = []
        registros = []
        for fila in filas[1:]:
            if not fila:
                continue
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = dict(zip(headers, fila))
            registros.append(registro)

    if not has_headers:
        registros = []
        for fila in filas:
            if not fila:
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = tuple(fila)
            registros.append(registro)
    return registros


def parse_csv(filas, select=None, types=[str, int, float],
              has_headers=True):
    if type(filas) in [list, tuple]:
        registros = itero_iterables(filas, select, types, has_headers)
    else:
        suffix = (Path(filas).suffix)
        if suffix == '.csv':
            with open(filas) as f:
                filas = csv.reader(f)
                registros = itero(filas, select, types, has_headers)
        if suffix == '.gz':
            with gzip.open(filas, 'rt') as f:
                filas = csv.reader(f)
                registros = itero(filas, select, types, has_headers)      
    return registros
