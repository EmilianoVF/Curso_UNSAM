
#%%
import csv
import numpy as np

def leer_parque(nombre_archivo,parque):
    with open('/home/emiliano/Desktop/Curso_UNSAM/Data/'+nombre_archivo) as f:
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


arboleda=leer_parque('arbolado-en-espacios-verdes.csv','TODOS')

H_30_y_40=[arbol['altura_tot'] for arbol in arboleda if arbol['altura_tot']<40 and arbol['altura_tot']>30]

D_30_y_40=[arbol['diametro'] for arbol in arboleda if arbol['altura_tot']<40 and arbol['altura_tot']>30]

Especies_inclinadas=[arbol['nombre_com'] for arbol in arboleda if arbol['inclinacio']>80]


Jacaranda_D_Y_H=[(arbol['diametro'],arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
np.save('/home/emiliano/Desktop/Curso_UNSAM/Data/Jacaranda_D_Y_H.npy',Jacaranda_D_Y_H)


# %%
