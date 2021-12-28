from bs4 import BeautifulSoup
import requests
import argparse
import pandas as pd
from datetime import datetime
from IPython.display import display
import csv
import numpy as np

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
