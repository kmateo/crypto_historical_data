from bs4 import BeautifulSoup
import requests
import argparse
import pandas as pd
from datetime import datetime
from IPython.display import display
import csv
import numpy as np

#Cargamos csv generado
df = pd.read_csv("Historico_desde_2013.csv") 

#Valores nulos
comprobar_nulos = df.isnull().values.any()
if(comprobar_nulos==False):
    print("El dataframe no tiene valores nulos")
else:
    print("El dataframe si tiene valores nulos")

#Valores duplicados
valores_duplicados = df.duplicated().values.any()
if(valores_duplicados==False):
    print("El dataframe no tiene valores duplicados")
else:
    print("El dataframe si tiene valores duplicados")

#Eliminar columnas innecesarias
df = df.drop(columns = ['Unnamed: 1'])
#Adaptar nombres col
df = df.rename(columns={'Cap. de Mercado':'Capitalizacion', 'Símbolo':'Simbolo', 'Unnamed: 0':'Fecha'})


#Eliminamos simbolo innecesario $
df["Capitalizacion"] = df["Capitalizacion"].str.replace("$","")
df["Precio"] = df["Precio"].str.replace("$","")

#Aplicamos tipo y formato fecha
df['Fecha'] = df['Fecha'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))


print(df)
print(df.dtypes)
