from bs4 import BeautifulSoup
import requests
import argparse
import pandas as pd
from datetime import datetime
from IPython.display import display
import csv

# Parseamos los valores de entrada, el intervalo de fechas que queremos analizar.
parser = argparse.ArgumentParser()
parser.add_argument("--startDate", help="Introduzca el inicio del intervalo (dd-mm-yyyy) deseado.")
parser.add_argument("--endDate", help="Introduzca el final del intervalo (dd-mm-yyyy) deseado.")
args = parser.parse_args()
startDate = datetime.strptime(args.startDate, "%d-%m-%Y")
endDate = datetime.strptime(args.endDate,"%d-%m-%Y")

# Consultamos la web donde aparecen todos los enlaces de los históricos.
mainURL = "https://coinmarketcap.com/es/historical/"
page = requests.get(mainURL)
soup = BeautifulSoup(page.content, 'html.parser')

# Guardamos los links que corresponden con los distintos históricos.
links = [a['href'] for a in soup.find_all('a', href=True)]
history_links = [link for link in links if link[:15] == '/es/historical/' and len(link)>15]

historical_object = {}

# Adaptamos el formato de las fechas que aparecen en los links.
dates = []
for date in history_links:
    dates.append(datetime.strptime(date[15:-1], '%Y%m%d'))

# Seleccionamos las fechas que se encuentran en el intervalo introducido.
selected_dates = [date.strftime("%Y%m%d") for date in dates if date >= startDate and date <= endDate]

# Comenzamos a descargar históricos de los links con las fechas seleccionadas.
for date_link in selected_dates:
    url = mainURL + date_link
    remaining = len(selected_dates) - len(historical_object)
    print(f'Descargando fecha: {date_link} \n' +
        f' Fechas pendientes: {remaining}')
    historical_object[date_link] = pd.read_html(url)[2][:20]

# Creamos un dataset son todos los valores y sus fechas
data = pd.concat(historical_object)

# Eliminamos las columnas que consideramos innecesarias
data.drop(data.columns.difference(['Rank','Nombre', 'Símbolo', 'Cap. de Mercado', 'Precio']), 1, inplace=True)

#Creamos un dataframe desde el dataset
df= pd.DataFrame(data)

print(df)
print(f'Descarga completa')

#importamos a csv
df.to_csv('coins.csv', index = True)
