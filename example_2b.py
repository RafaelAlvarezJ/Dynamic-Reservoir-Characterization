# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:34:10 2022

@author: rafa_
"""
import CDY 
import numpy as np
import matplotlib.pyplot as plt

"""
USO DE LA SOLUCIÓN LÍNEA-FUENTE PARA POZOS DAÑADOS O ESTIMULADOS.

Un pozo (que produce a gasto constante) y un yacimiento tienen las 
características mostradas en la tabla:
    
    a) Si la presión en el pozo fue medida en 1500 psia después de 10 horas de 
    producción, calcular el factor de daño. 
    
    b) Posteriormente, el pozo fue estimulado con ácido para eliminar el daño, 
    y posteriormente puesto de nuevo a producción con gasto constante (qb), y 
    después de 6 hrs (tb), la presión fue medida en 2250 psia (pwfb). ¿Se 
    eliminó el daño? 
    
    c) Graficar la presión del yacimiento en función del tiempo y para 5 
    diferentes daños (2 positivos, 2 negativos y un daño cero).
"""


rw = 0.5 #ft
k = 0.1 #md
h = 150 #ft
B = 1.475 #RB/STB
re = 3000 #ft
Pi = 3000 #psi
phi = 0.23
ct = 1.50E-05 #psia-1
mu = 0.72 #cp

ta = 13 #hrs
Pwfa= 1380 #psia
qa = 20 #STB/d

qb = 20 #STB/d
tb = 5 #hrs
Pwfb = 2380 #psia


sa = CDY.skin(phi, mu, ct, qa, B, k, h, Pi, Pwfa, ta, rw)
sb = CDY.skin(phi, mu, ct, qb, B, k, h, Pi, Pwfb, tb, rw)

# Respuesta a incisos a, b
print (f"Daño a: {sa} \nDaño b: {sb}")


# Graficar la presión del yacimiento en función del tiempo y para 
# 5 diferentes daños (2 positivos, 2 negativos y un daño cero).

s = np.array([-2, -1, 0, 4.54, 8])
t = np.arange(10,8500,1)

pwf = CDY.Tarea2b(phi, mu, ct, qa, B, k, h, Pi, s, t, rw)

plt.figure("Example_1.2", figsize=(10,8))
#plt.xscale("log")
for i in range (len(s)):
    plt.plot(t, pwf[i][:], label=f" s={s[i]} " )
    
plt.ylabel("Pwf [psia]")
plt.xlabel("t [h]")
plt.legend()
plt.title("Using the Line-Source Solution for Damaged or Stimulated Wells")
plt.grid()

plt.savefig("Example_1b.png",dpi=300)

