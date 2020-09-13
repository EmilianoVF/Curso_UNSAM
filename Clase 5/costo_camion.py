
#%%
from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    camion=leer_camion(nombre_archivo)
    costo_total=0.0
    for row in camion:
        costo_total+=row['cajones']*row['precio']

    return costo_total