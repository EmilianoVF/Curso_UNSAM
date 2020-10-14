
import os
import time
import informe


def vigilar(nombre_archivo):
    f = open(nombre_archivo, encoding='UTF-8')
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        else:
            yield line


if __name__ == '__main__':
    camion = informe.leer_camion('/home/emiliano/Desktop/Curso_UNSAM/Data/camion.csv')
    for line in vigilar('/home/emiliano/Desktop/Curso_UNSAM/Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            if volumen > 1000:
                print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
