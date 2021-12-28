import requests
import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from scipy.spatial.distance import cdist

#Cargamos csv generado
df = pd.read_csv("Historico_desde_2013.csv")

comprobar_nulos = df.isnull().values.any()

#Eliminar columnas innecesarias
df = df.drop(columns = ['Unnamed: 1'])
#Adaptar nombres col
df = df.rename(columns={'Cap. de Mercado':'Capitalizacion', 'Símbolo':'Simbolo', 'Unnamed: 0':'Fecha'})


#Eliminamos simbolo innecesario $
df["Capitalizacion"] = df["Capitalizacion"].str.replace("$","")
df["Precio"] = df["Precio"].str.replace("$","")

#Transformamos de object a float, redondeamos a 2 deciamales
#A LA HORA DE TRANSFORMAR DE OBJECT A FLOAT LA CAP DE MERCADO ME LA PONE A NaN TODA LA COLUMNA
df["Precio"] = df["Precio"].apply(pd.to_numeric, errors='coerce')
df["Precio"] = pd.Series([round(val, 2) for val in df["Precio"]])
#df["Capitalizacion"] = df["Capitalizacion"].apply(pd.to_numeric, errors='coerce')

#Aplicamos tipo y formato fecha
df['Fecha'] = df['Fecha'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))

# Comprobamos Valores nulos
comprobar_nulos = df.isnull().values.any()
if(comprobar_nulos == False):
    print("El dataframe no tiene valores nulos")
else:
    print("El dataframe si tiene valores nulos")


#Comprobamos Valores duplicados
valores_duplicados = df.duplicated().values.any()
if(valores_duplicados == False):
    print("El dataframe no tiene valores duplicados")
else:
    print("El dataframe si tiene valores duplicados")

#FALTA DETECCION DE OUTLIERS (VALORES EXTREMOS) mediante un boxplot donde se vean los puntos fuera de la caja que seran outliers
#prueba = df['Precio']
#plt.boxplot([prueba]);
#plt.show()

#print(df.dtypes)
#print(df)

############################################ ANALISIS ###########################################

#Estadistica descriptiva de variables numéricas (Precio, Rank y faltaría Cap. Mercado
stats_price = df['Precio'].describe()
print('Estadistica sobre variable Precio: ')
print(stats_price)
print(end ='\n')
print('Estadistica sobre variable Ranking: ')
stats_rank = df['Rank'].describe()
print(stats_rank)
print(end ='\n')
#stats_cap = df['Capìtalizacion'].describe()
#print(stats_cap)
