# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:19:15 2022

@author: rafa_
"""
import numpy as np
#import Units as u
from numba import njit

@njit
def IntExp(ARG):
    # Función que cálcula la Integral Exponencial Ei
    
    # if ARG < 0.01:
    #     FUN = 1.781*np.log(ARG)
    
    if ARG < 1.0:
        
        a0 = -0.57721566
        a1 =  0.99999193
        a2 = -0.24991055
        a3 =  0.05519968
        a4 = -0.00976004
        a5 =  0.00107857

        FUN = a0 + a1*ARG + a2*ARG**2 + a3*ARG**3
        FUN = FUN + a4*ARG**4 + a5 * ARG**5 - np.log(ARG)
    
    #elif ARG >= 1.0 & ARG < 10.0:
    elif ARG < 10.0:

        a1 = 8.57332874
        a2 = 18.05901697
        a3 = 8.634760892
        a4 = 0.2677737343

        b1 = 9.573322345
        b2 = 25.632956148
        b3 = 21.0996530827
        b4 = 3.95849669228

        FUN = ARG**4 + a1*ARG**3 + a2*ARG**2 + a3*ARG + a4;
        FUN = FUN / (ARG**4 + b1*ARG**3 + b2*ARG**2 + b3*ARG + b4);
        FUN = FUN / (ARG*np.exp(ARG));
    
    else:

        a1 = 4.03640
        a2 = 1.15198
        b1 = 5.03637
        b2 = 4.19160

        FUN = ARG**2+a1*ARG+a2;
        FUN = FUN / (ARG**2 + b1 * ARG + b2)
        FUN = FUN / (ARG * np.exp(ARG))
        
    return (-FUN)

def Tarea2a(t, r, phi, mu, ct, k, h, q, B, Pi):
    
    A = np.zeros([len(t), len(r)]) 
    
    aux1 = 948*phi*mu*ct/k
    aux2 = 70.6*q*B*mu/(k*h)
    
    for i in range (len(t) ):
        for j in range (len(r) ):
            
            A[i][j] = aux1*( r[j]**2/t[i] ) 
            A[i][j] = IntExp( A[i][j] )
            A[i][j] = aux2*A[i][j] + Pi
            
    return (A)

def skin(phi, mu, ct, q, B, k, h, Pi, Pwf, t, rw):
    
    aux1 = k*h*(Pi-Pwf)/(70.6*q*B*mu)
    aux2 = IntExp(948*phi*mu*ct*rw**2/(k*t))
    s = 0.5*(aux1 + aux2)
    
    return (s)

@njit
def Pwf_radial(phi, mu, ct, q, B, k, h, Pi, s, t, rw):
    # Flujo transitorio radial, con producción a gasto constante a partir de un 
    # pozo representado por una línea fuente, tanto sin factor de daño como con 
    # factor de daño y almacenamiento en el pozo.
    
    aux1 = 70.6*q*B*mu/(k*h)
    aux2 = IntExp(948*phi*mu*ct*rw**2/(k*t))
    pwf = Pi+aux1*(aux2-2*s)
    
    return (pwf)

def Pwf_pseudoest(phi, mu, ct, q, B, k, h, Pi, s, t, rw, re):
    # Flujo pseudo-estacionario con producción a gasto constante, a partir de 
    # un pozo representado por fuente cilíndrica en un yacimiento cerrado
    
    aux1 = 141.2*q*B*mu/(k*h)
    aux2 = 0.000527*k*t/(phi*mu*ct*re**2)+np.log(re/rw)-3/4+s
    pwf = Pi-aux1*aux2
    
    return (pwf)

def Pwf_est(phi, mu, ct, q, B, k, h, Pi, s, t, rw, re):
    # Flujo estacionario con producción a gasto constante, a partir de un pozo
    # representado por una fuente cilíndrica en un yacimiento con fronteras 
    # externas a presión constante
    
    aux1 = 141.2*q*B*mu/(k*h)
    aux2 = np.log(re/rw)+s
    pwf = Pi-aux1*aux2
    
    return (pwf) #+17

def Tarea2b(phi, mu, ct, q, B, k, h, Pi, s, t, rw):
    
    A = np.zeros([len(s), len(t)])
    
    # aux1 = 948*phi*mu*ct*rw**2/k
    # aux2 = 70.6*q*B*mu/(k*h)
    
    for i in range (len(s)):
        for j in range (len(t)):
            
            A[i][j] = Pwf_radial(phi, mu, ct, q, B, k, h, Pi, s[i], t[j], rw)
            
    return (A)
          
@njit  
def Tarea2e(phi, mu, ct, q, B, k, h, Pi, s, t, rw, L):
    # Función creada para simular el comportamiento de UNA barrera impermeable
    
    aux1 = 70.6*q*B*mu/(k*h)
    n = k/(phi*mu*ct) # Difusividad hidráulica
    
    Pwf_confalla = Pi+aux1*( IntExp(948*rw**2/(n*t)) - 2*s + IntExp(948*(2*L)**2/(n*t)) )
    Pwf_sinfalla = Pi+aux1*( IntExp(948*rw**2/(n*t)) - 2*s)
    
    return (Pwf_confalla, Pwf_sinfalla)

def simulador_a(t2, pi, k, phi, mu, ct, q, rw, L, s, B, h):
    p = np.ones(t2[-1])*pi   # Se registra la P cada hora
    n = k/(phi*mu*ct) # difusividad hidáulica
    a = 70.6*B*mu/(k*h)
    for i in range (1, t2[-1]): # ciclo temporal    
        aux1 = np.zeros(len(q)-1) # cada elemento equivale a una DP por gasto
        for j in range (1,len(q)): # ciclo espacial (barre los gastos)
            aux = np.zeros(2) # [0] = DP en el pozo, [1] = DP por la falla
            if (t2[j-1] < i):
                aux[0] = np.log(1688*rw**2/(n*(i-t2[j-1]) )) - 2*s # pozo
                if L == 0: # falla
                    aux[1] = 0
                else:
                    aux[1] = IntExp(948*(2*L)**2/(n*(i-t2[j-1]) )) 
                aux1[j-1] = np.sum(aux)*(q[j]-q[j-1])
        p[i] += np.sum(aux1)*a 
    return (p)
