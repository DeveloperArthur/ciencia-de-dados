# -*- coding: utf-8 -*-
"""pandas-dataframe.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18nhLdvEh-l9zSVjjaHyWtLB-yYnoHd5q
"""

import pandas as pd
import numpy as np

data = {'Estado' : ['São Paulo', 'São Paulo', 'São Paulo', 'Paraná', 'Paraná', 'Paraná', 'Bahia', 'Bahia'], 
        'Ano' : [2000, 2001, 2002, 2001, 2002, 2003, 2000, 2001], 
        'População':[1.5, 1.8, 2.2, 1, 2, 3, 1.1, 1.3]}

frame = pd.DataFrame(data)
frame

frame.head(3)

frame.tail(3)

frame2 = pd.DataFrame(data, columns=['Ano', 'Estado', 'População'])
frame2

frame2 = pd.DataFrame(data, columns=['Ano', 'Estado', 'População'], index=['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete'])
frame2

frame2 = pd.DataFrame(data, columns=['Ano', 'Estado', 'População', 'Debt'], index=['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete'])
frame2

frame2.columns

frame2.index

frame3 = frame2.append(frame, ignore_index=True)
frame3

frame4 = frame.append(frame2, ignore_index=True)
frame4

frame4[['Estado', 'Ano']]

frame4['soma']=0
frame4

colunas = ['Ano', 'Estado', 'soma']

for x in colunas:
  print(frame4[x])

colunas = ['Ano', 'Estado', 'soma']
frame4[colunas]

frame4.loc[10]

frame4.loc[10:]

frame4.loc[:10]

frame4.loc[2:7]

frame4['soma'] = np.arange(16)
frame4

indexe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
indexe[3]

s_valor = pd.Series([10, 20, 30], index=[11,12,14])
s_valor

frame4['soma'] = s_valor;
frame4

frame4[frame4['soma'].isna()]

frame4[~frame4['soma'].isna()]

frame4[frame4['soma'] == 10]

frame4.soma > 10

frame4['soma'].count()

frame4['soma'].fillna(frame4['soma'].mean())

frame4['Regiao'] = frame4.Estado == 'Bahia'
frame4

frame4[frame4['Ano'] == 2000]
#frame4[frame4['Ano'] == 2001]
#frame4[frame4['Ano'] == 2002]
#frame4[frame4['Ano'] == 2003]

import matplotlib.pyplot as plt
frame6 = frame4.groupby(['Ano']).mean()
frame6.plot(kind='bar')
plt.show()