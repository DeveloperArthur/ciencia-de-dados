# -*- coding: utf-8 -*-
"""covid19.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k8aH4kxpZMjJNpIEh9Ryf4EDqe0J3Itl
"""

import os
import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt

#configurando dia de start
startday = '2/26/20'

#criando lista de graficos que serao gerados
plotfiles = ['plot2.png','plot3.png','plot4.png','plot5.png','plot6.png','plot7.png','plot8.png',
             'plot9.png','plot10.png','plot11.png','plot12.png','plot13.png','plot14.png','plot15.png']

def segmenta(df,paises,status, wtodo,startday,cumulativo):
    status = df['Status'] == status
    country = df["Country/Region"].isin(paises)
    df_Country = df[ country & status]
    df_G = df_Country.groupby(['Country/Region','Status']).sum()
    df_GT = df_G.transpose().copy()
    df_GT = df_GT.loc[startday:]
#    if cumulativo=='Acumudado':
#        df_GT = df_GT.cumsum()

    df_G = df_GT.copy()

    if wtodo==1:
        df_G = (df_GT)/(df_GT.max())

    return df_G

def segmenta_rate(df,paises,status, wtodo,startday,cumulativo):

    country = df["Country/Region"].isin(paises)
    df_Country = df[country]
    df_G = df_Country.groupby(['Country/Region','Status']).sum()
    df_GT = df_G.transpose().copy()
    df_GT = df_GT.loc[startday:]
    print(df_GT.tail(3))

#    if cumulativo=='Acumudado':
#        df_GT = df_GT.cumsum()

    df_r = (df_GT.xs('deaths',axis=1, level=1)*100)/df_GT.xs('confirmed',axis=1, level=1)
    print(df_r.tail(3))
    df_G = df_r.copy()

    return df_G

#atribuindo planilhas para variaveis
df0 = pd.read_csv("time_series_covid_19_confirmed.csv")
df1 = pd.read_csv("time_series_covid_19_deaths.csv")
df2 = pd.read_csv("time_series_covid_19_recovered.csv")

#atribuindo uma coluna status em todas as planilhas
df0['Status']='confirmed'
df1['Status']='deaths'
df2['Status']='recovered'

#juntando as 3 planilhas
df = df0.copy()
df = df.append(df1, ignore_index=True)
df = df.append(df2, ignore_index=True)

paises = ['Brazil','France','US','Germany']
#paises = ['Brazil']

grava=True
keydrop =[df.columns[0],df.columns[2],df.columns[3]]
# limpa colunas que não serão usadas
df.drop(columns= keydrop, axis=1, inplace = True)



status_list = ['confirmed','deaths','recovered']
wtodo = [0,1]
wtodo_desc = ['Absoluto','Normalizado','Mortes/Casos']
conta=-1
cumu = ["Acumulado"]

for Acumulado in cumu:
    for todo in wtodo:
        for sta in status_list:
            df_P = segmenta(df,paises,sta,todo,startday,Acumulado)
            df_P.plot(kind='line', stacked=True,figsize=(18.5, 10.5), grid=True)
            indexVector = pd.to_datetime(df_P.index).strftime('%d-%m-%Y')
            plt.xticks(np.arange(len(df_P)), indexVector)
            plt.xticks(rotation=90)
            plt.title('Crescimento '+ Acumulado + ' do Coronavirus: '+wtodo_desc[todo])
            conta += 1
            if grava:
                plt.savefig(os.path.join(plotfiles[conta]), dpi=300, format='png', bbox_inches='tight')
plt.show()
todo=2

df_P = segmenta_rate(df,paises,sta,todo,startday,Acumulado)
df_P.plot(kind='line', stacked=True,figsize=(18.5, 10.5), grid=True)
indexVector = pd.to_datetime(df_P.index).strftime('%d-%m-%Y')
plt.xticks(np.arange(len(df_P)), indexVector)
plt.xticks(rotation=90)
plt.title('Crescimento do Coronavirus: '+wtodo_desc[todo])

conta += 1
if grava:
    plt.savefig(os.path.join(plotfiles[conta]), dpi=300, format='png', bbox_inches='tight')

plt.show()