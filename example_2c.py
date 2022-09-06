# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 16:08:40 2022

@author: rafa_
"""
#import CDY 
import numpy as np
#import matplotlib.pyplot as plt

"""
ANÁLISIS DE UN POZO A PARTIR DE UNA PRUEBA DE PI.

Se tienen los siguientes datos de un pozo al que se realizó una prueba de 
índice de productividad:
    
    a) Estimar el índice de productividad del pozo. 
    b) Estimar la permeabilidad de la formación a partir de esa información.
    c) Si a partir de un análisis de núcleo se determina que la permeabilidad de 
    la formación es de 50 md, determinar si el pozo tiene daño.

"""

q = 100 #STB/d
h = 10 #ft
B = 1.5 #RB/STB
re = 1000 #ft
p_promedio = 2000 #psi
mu = 0.5 #cp
rw = 0.25 #ft
pwf = 1500 #psi
k = 50 # md (de núcleo)

# Índice de productividad para yacimientos bajosaturados
J = q/(p_promedio-pwf)
print(f"El índice de productividad J es: {J} [BPD/psi] ")

# Con la ecuación de la diapositiva anterior a este ejercicio
kj = J*141.2*B*mu*(np.log(re/rw) -3/4)/h
print(f"La permeabilidad promedio kj es: {kj} [md] ")

# Despejando el daño de las ecuaciones
s = (1-k/kj)*(3/4-np.log(re/rw))
print(f"El daño s es: {s} ")

#J2 = kj*h/(141.2*B*mu*(np.log(re/rw) -3/4) )
#print(J2)
