# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:43:41 2022

@author: rafa_

Pressure Test Simulator.
For simulating well pressure response, applying superposition in time (multiple
rates) and in space (impermeable seal).

Simulador de pruebas de presión. 
Se simula la respuesta de presión en el pozo, aplicando los principios de 
superposición en tiempo y en espacio para simular varios gastos y una falla 
impermeable.
"""
import CDY 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"DATA"
pi = 5000 #psi
h = 150 #ft
B = 1.475 #RB/STB
ct = 1.50E-05 #psia-1
mu = 0.72 #cp
phi = 0.23
rw = 0.5 #ft

k = 11 #md
L = 200 #ft
s = -0.8

q = np.array([0, 1000, 1500, 0,1500])# [BPD], q = [0, q0, q1, ... , qn]
#t = np.array([0, 96, 96, 96, 72])    # tiempo 
t2= np.array([0, 96, 192, 288, 360]) # tiempo acumulado

"CREATING DATAFRAME FROM EXCEL FILE"
df1 = pd.read_excel("project_1.xlsx", "Presion")
df2 = pd.read_excel("project_1.xlsx", "Gasto")

qo = np.zeros(len(df1)); aux = 0
for i in range(len(df1)): # presiones
    qo[i] = df2["qo [bpd]"][aux] 
    if [i] == df2["t [h]"][aux]:
        aux += 1
df1["qo [bpd]"] = qo
del i, df2, qo, aux

"SIMULATOR"
p = CDY.simulador_a(t2, pi, k, phi, mu, ct, q, rw, L, s, B, h)
   
"PLOTS"
tiempo = np.arange( t2[-1] )

plt.title(f"k={k} [md], L={L} [ft], s={s}")
plt.scatter(df1["t [h]"], df1["Pwf [psia]"], label="Gauge pressure")
plt.scatter(tiempo, p, label="Calculated pressure")
#plt.plot(df1["t [h]"], df1["qo [bpd]"], label="qo [bpd]")

plt.grid()
plt.legend()
plt.xlabel("t [h]")
plt.ylabel("Pwf [psia]")
#plt.savefig("fig8.png", dpi=600)

"GIFS"
# framesPress[0].save('presion2D.gif', format='GIF', append_images=framesPress[1:], save_all=True, duration=200, loop=0)  #Crea el gif de la presión con las imagenes guardadas en la lista de frames