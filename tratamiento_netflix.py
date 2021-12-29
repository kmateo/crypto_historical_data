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

#df_net['date_added'] = df_net['date_added'].apply(lambda x: pd.to_datetime(str(x), format='%m%d%Y'))











print(df_net.head(5))
print(df_net.dtypes)
