#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


nombre_cientidico_veredas = 'Tipuana tipu'
nombre_cientifico_parques = 'Tipuana Tipu'

df_veredas = pd.read_csv('/home/emiliano/Desktop/Curso_UNSAM/Data/arbolado-publico-lineal-2017-2018.csv')
df_parques = pd.read_csv('/home/emiliano/Desktop/Curso_UNSAM/Data/arbolado-en-espacios-verdes.csv')

cols_veredas = ['altura_arbol', 'diametro_altura_pecho']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == nombre_cientidico_veredas][cols_veredas].copy()
cols_parques = ['altura_tot', 'diametro']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == nombre_cientifico_parques][cols_parques].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'})
df_tipas_parques = df_tipas_parques.rename(columns={'altura_tot': 'altura'})
df_tipas_veredas['ambiente'] = ['veredas' for _ in range(df_tipas_veredas.shape[0])]
df_tipas_parques['ambiente'] = ['parques' for _ in range(df_tipas_parques.shape[0])]
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


sns.boxplot(x=df_tipas['ambiente'], y=df_tipas['altura'])
plt.show()
sns.boxplot(x=df_tipas['ambiente'], y=df_tipas['diametro'])
plt.show()

'''
Para que funcione con otras especies unicamente hay que cambiar
el nombre de las especies. Se puede hacer con una funcion porque no ...
'''
