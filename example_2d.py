# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:51:19 2022

@author: rafa_
"""
import CDY 
import numpy as np
import matplotlib.pyplot as plt

"""
COMPARACIÓN DE SOLUCIONES A LA ECUACIÓN DE DIFUSIÓN

Realizar un gráfico comparativo donde se pueda observar el comportamiento de la
presión para los casos de yacimiento infinito, yacimiento cerrado y yacimiento
con fronteras a presión constante. Anotar observaciones y/o comentarios al
respecto. Considerar los siguientes datos:
"""

q = 250 #STB/d
h = 30 #ft
B = 1.2 #RB/STB
re = 1000 #ft
Pi = 2500 #psi
mu = 0.5 #cp
rw = 0.333 #ft
k = 12 #md
phi = 0.12
ct = 2.00E-05 #psia-1
s = 2

n = k/(phi*mu*ct) # difusividad hidráulica

t = np.linspace(0.1, 1000, 1000) # hrs

a = np.zeros( len(t) )
b = np.zeros( len(t) )
c = np.zeros( len(t) )

# Rango de validez del IARF
t_inf = 3.975e+5*rw**2/n
t_sup = 948*re**2/n

print (f"Intervalo del IARF [h]: {t_inf} a {t_sup}")



for i in range ( len(t) ):
    a[i] = CDY.Pwf_radial(phi, mu, ct, q, B, k, h, Pi, s, t[i], rw)
    
    if t[i]>t_sup:
        b[i] = CDY.Pwf_pseudoest(phi, mu, ct, q, B, k, h, Pi, s, t[i], rw, re)
        c[i] = CDY.Pwf_est(phi, mu, ct, q, B, k, h, Pi, s, t[i], rw, re)    
    else: 
        b[i] = a[i]
        c[i] = a[i]


plt.figure("Example_1d", figsize=(10,8))

plt.title("Comparison of Solutions to the Diffusivity Equation")

plt.plot(t, a, label="Infinite Acting Radial Flow")
plt.plot(t, b, label="Pseudo Steady State Flow")
plt.plot(t, c, label="Steady State Flow")

plt.xlabel("t [h]")
plt.ylim([1400, 2400])
plt.ylabel("Pwf [psia]")
plt.legend()
plt.grid()

plt.savefig("Example_1d.png",dpi=300)