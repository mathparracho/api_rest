
import sys

from unidecode import unidecode

#analise requerida
tipo = int(sys.argv[1])

#set the required country
country = sys.argv[2]

#set the required country
analise = int(sys.argv[3])



import pandas as pd
import pyodbc
import urllib.request

import numpy as np
import json

#get the database

server = 'scoutfy-db.cdnl3plncvrr.sa-east-1.rds.amazonaws.com,1433' 
database = 'panorama' 
username = 'admin' 
password = 'Scoutfy20' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


if (tipo == 0):

    data = pd.read_sql_query('SELECT * FROM [panorama].[dbo].[athletics]',cnxn)
    data = data.replace(['nan'],float('NaN'))
    paises = data['Country'].tolist()
    index = []
    for counter in range(len(paises)):
        if paises[counter] != country:
            index += [counter]
    data = data.drop(index)

    if(analise == 0):
        ## Numero de Atleticas
        athletics = data["Item ID"].tolist()
        numero_atleticas = len(athletics)
        print('{"numero_atleticas" :',numero_atleticas,"}")

    if(analise == 1):
        ## Distribuição por Estado (Dados)
        estados = data["State"].tolist()
        dic = {}

        for estado in estados:
            estado = unidecode(estado)
            if estado != estado.upper():
                pass
            elif dic.get(estado) == None:           #or if a[1] in dic:
                dic[estado] = 1
            elif dic.get(estado) != None:         #or if a[1] not in dic:
                dic[estado] += 1
        resjson = json.dumps(dic)
        print(resjson)



