import pandas as pd
import csv
import numpy as np
from datetime import datetime

#Cargamos csv generado
df_net = pd.read_csv("Netflix_titulos.csv")

############################### LIMPIEZA ###############################
#Borrado de columnas innecesarias
df_net = df_net.drop(columns = ['description'])
df_net = df_net.drop(columns = ['cast'])

#Formateo de fecha
df_net['date_added'] = df_net['date_added'].apply(lambda x: pd.to_datetime(str(x), format='%B%d%Y'))

#Cambio de object a float/int/datetime


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







print(df_net.head(5))
print(df_net.dtypes)
