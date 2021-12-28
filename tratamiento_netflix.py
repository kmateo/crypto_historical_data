import pandas as pd
import csv
import numpy as np

#Cargamos csv generado
df_net = pd.read_csv("Netflix_titulos.csv")

df_net = df_net.drop(columns = ['description'])

 

print(df_net.head(5))

print(df_net.dtypes)
