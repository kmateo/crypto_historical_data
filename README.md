# Extracción de datos históricos de CoinMarketCap.

Diego Álvarez Padrón

Kevin Mateo García

## Contenido del repositorio:

- README.md -- Integrantes del grupo e instrucciones de uso del programa.
- cryptoHistory.py -- Código del programa.
- ExtraccionDatosHistoricos.pdf -- Documento PDF con las respuestas a los apartados 1-10.
- DOI de Zenodo -- https://doi.org/10.5281/zenodo.5639736
- Vídeo explicativo de la práctica -- https://drive.google.com/file/d/13flSwAg1aI2yrwJX3aa3uZVcaXTdaOsR/view?usp=sharing

## Instrucciones de uso.

El programa extrae los datos históricos procedentes de CoinMarketCap, requiere como parámetros de entrada un intervalo de fechas. Los datos de CoinMarketCap se registran por semanas, el intervalo de fechas servirá para que se descarguen los datos de las semanas que se encuentran entre dicho intervalo.
El formato de dichas fechas será %d-%m-%Y

```
python3 cryptoHistory.py --startDate 01-10-2020 --endDate 10-10-2020
```
