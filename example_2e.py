# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:43:58 2022

@author: rafa_
"""
import CDY 
import numpy as np
import matplotlib.pyplot as plt

"""
USO DE SUPERPOSICIÓN EN ESPACIO PARA MODELAR UNA FALLA CERCANA A UN POZO

Un pozo está a 350 ft (L=350 ft) al oeste de una falla de inclinación NS. Se 
sabe, por una prueba, que tiene un daño de 5 y que produce de forma constante a 
razón de 350 STB/D. Elabore un gráfico que compare el perfil de presión medida 
en el pozo (pwf) con el perfil de presión que habría si no existiera la falla. 
Considere 500 horas de producción y los datos siguientes:
"""

q = 350 #STB/d
h = 50 #ft
B = 1.13 #RB/STB
re = 3000 #ft
pi = 3000 #psi
mu = 0.5 #cp
rw = 0.333 #ft
pwf = 1500 #psi
t = 192 #hrs
k = 25 #md
phi = 0.16
ct = 2.00E-05 #psia-1
L = 350 #ft
s = 5



t = np.linspace(1, 500, 499)
a = np.zeros(len(t)) # Pwf con falla
b = np.zeros(len(t)) # Pwf sin falla

for i in range (len(t)):
    a[i], b[i] = CDY.Tarea2e(phi, mu, ct, q, B, k, h, pi, s, t[i], rw, L)
    
plt.plot(t, a, label=f"Perfil de presión con falla a {L} [ft]")
plt.plot(t, b, label="Perfil de presión sin falla")
plt.xlabel("Tiempo [h]")
plt.ylabel("Pwf [psia]")
plt.legend()
plt.grid()

