# -*- coding: utf-8 -*-
"""Matrizes e Graficos NUMPY Scatter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16vFY1Pj_GYwQgVwOYGHpvSj4lwPpkKSV
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(16)
b = a^2
c = a.reshape(8,2)
d = np.linspace(0,5,20)
print("-----------------")
print("Matriz a")
print(a)
#python eh diferente, posicao 2 do array = indice 2....
print(a[2])
#a = a * 2
#print(a)
#print(a[2])
#slice pega quantidade, 3 elementos!
print(a[:3])
#slice desconsidera os 3 primeiros elementos e mostra o resto!
print(a[3:])
print("-----------------")

print("Matriz b")
print(b)
print("-----------------")

print("\n\nGrafico com vetor A + B")
plt.figure()
plt.scatter(a, b, linestyle = '--', color = 'r', marker='s', linewidths = 2.0)
plt.title('Matrizes NUMPY Scatter', color = 'w')
plt.xlabel('X', color = 'w')
plt.ylabel('Y', color = 'w')
plt.show()
print("-----------------")

print("Matriz c")
print(c)
print("\n")
print(c[:,0])
print(c[:,1])
print("\n")
print(c[3,:])

print("\n\nGrafico com vetor c[:,0], c[:,1]")
plt.figure()
plt.scatter(c[:,0], c[:,1], linestyle = '--', color = 'b', marker='s', linewidths = 2.0)
plt.title('Matrizes NUMPY Scatter', color = 'w')
plt.xlabel('X', color = 'w')
plt.ylabel('Y', color = 'w')
plt.show()
print("-----------------")

print("Matriz d")
print(d)
print("-----------------")

print("Matriz e")
e = np.linspace(0,1,1000)
print(e)
print("-----------------")