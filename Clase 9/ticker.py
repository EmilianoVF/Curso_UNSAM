from vigilante import vigilar
import csv
import informe
import formato_tabla


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila


def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    encabezado = formateador.encabezado(['nombre', 'precio', 'volumen'])
    print(encabezado)
    for fila in filas:
        data = [fila['nombre'], str(fila['precio']), str(fila['volumen'])]
        formateador.fila(data)


if __name__ == '__main__':
    ticker('/home/emiliano/Desktop/Curso_UNSAM/Data/camion.csv',
           '/home/emiliano/Desktop/Curso_UNSAM/Data/mercadolog.csv', 'html')
