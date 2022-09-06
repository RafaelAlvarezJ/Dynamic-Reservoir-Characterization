# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:18:32 2022

@author: rafa_
"""
import CDY 
import numpy as np
import matplotlib.pyplot as plt
#import Units as u
#from numba import njit

"""
CÁLCULO DE PRESIONES MÁS ALLÁ DEL RADIO DEL POZO, A PARTIR DE LA SOLUCIÓN 
lÍNEA-FUENTE.

Calcular la presión en el yacimiento a un radio de 1, 10, 100 y 1000 ft durante
todo el tiempo que es válida la solución línea fuente. El pozo (que produce a 
gasto constante) y yacimiento tienen las siguientes características:
"""

q = 20 #STB/d
h = 150 #ft
B = 1.475 #RB/STB
re = 3000 #ft
Pi = 3000 #psi
phi = 0.23
ct = 1.5E-05 #psia-1
mu = 0.72 #cp
rw = 0.5 #ft
k = .1 #0.12 #md

t1 = (3.975E+05)*phi*mu*ct*rw**2/k
t2 = 948*phi*mu*ct*re**2/k
t = np.array([t1, 5, 10, 20, 100, 500, 1000, 2000])
r =np.linspace(0.1, 1000, 1000)

P = CDY.Tarea2a(t, r, phi, mu, ct, k, h, q, B, Pi)

plt.figure("Example_1.1", figsize=(10,8))

plt.xscale("log")
for i in range (len(t)):
    plt.plot(r, P[i][:], label = f"t [h] = {t[i]} ")
    
plt.ylabel("$P_{(r,t)}$ [psia]")
plt.xlabel("$r$ [ft]")
plt.legend()
plt.title("IARF, Constant-Rate Production From a Line-Source Well")
plt.title("Calculations of Pressures Beyond the Wellbore with the Line-Source-Solution")
plt.grid()

plt.savefig("Example_1a.png",dpi=300)

    