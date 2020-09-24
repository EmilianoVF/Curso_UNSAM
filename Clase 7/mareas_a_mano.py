#%%
import pandas as pd
import numpy as np

df = pd.read_csv('/home/emiliano/Desktop/Curso_UNSAM/Data/OBS_SHN_SF-BA.csv',
                 index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()

delta_t = -1  # tiempo que tarda la marea entre ambos puertos

delta_h = 15  # diferencia de los ceros de escala entre ambos puertos

dh_shift = pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T
dh_shift.plot()
