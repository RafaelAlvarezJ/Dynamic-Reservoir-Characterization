# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 00:09:57 2022

@author: rafa_
"""
import CDY 
import numpy as np
import matplotlib.pyplot as plt
import Units as u
"""
USO DE SUPERPOSICIÓN EN TIEMPO

Determinar el perfil de presión en un pozo observador que se encuentra cerrado 
y que está a 500 ft de un pozo que produjo durante 5 días a razón de 300 STB/D, 
para luego cerrarse durante 20 días. Elabore un gráfico de p VS t y determine 
si el yacimiento regresa a su presión original en ese tiempo. El pozo y 
yacimiento tienen las siguientes características:
"""

pi = 2500 #psi
h = 43 #ft
B = 1.32 #RB/STB
ct = 1.80E-05 #psia-1
mu = 0.44 #cp
phi = 0.16
k = 25 #md
q0 = 0 #STB/d
q1 = 300 #STB/d
q2 = 0 #STB/d
r = 500 #ft
t1 = 5.0*24 #horas
t2 = 20.0*24 #horas
t = 25.0*24 #horas

q = np.array([q0, q1, q2])
t_array = np.array([t1, t2, t]) 

tiempo = np.linspace(1,t,1000)
p = np.zeros(len(tiempo))

aux1 = 70.6*B*mu/(k*h)
n = k/(phi*mu*ct) # difusividad hidráulica

for i in range (len(tiempo)):
    p[i] = pi + aux1*(q[1]-q[0])*CDY.IntExp(948*r**2/(n*tiempo[i]) )
    
    if tiempo[i]>t1:
        p[i] = p[i]+aux1*(q[2]-q[1])*CDY.IntExp(948*r**2/(n*(tiempo[i]-t_array[0]) ) )

                            
plt.plot(tiempo*u.hr/u.day,p)
plt.title("Simulación de una prueba de incremento")
plt.xlabel("Tiempo [D]")
plt.ylabel("Presion [psia]")
plt.grid()


