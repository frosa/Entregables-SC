# -*- coding: utf-8 -*-
"""
Created on Tue May 01 20:10:15 2018

@author: Ivan
"""
import numpy as np
import matplotlib.pyplot as plt




R = 10000.
L = 0.001

w0 = 300;#Frecuencia de inicio para hacer la funcion de transferencia (rad/s)
w1 = 600000.; #Frecuencia en la que acaba (rad/s)

W = np.arange(w0,w1,100)
n=np.ones(len(W))
H = 0.5*n
plt.plot(W/(2*np.pi),(20*np.log10(abs(H))),'o')

plt.xlabel(u'Frecuencia [Hz]')
plt.ylabel(u'Ganancia del sistema (dB)')
plt.title(u'(1) Función de transferencia')
plt.xscale('log')#Escala logaritmica en x
plt.show()


plt.plot((W/(2*np.pi)),(360/(2*np.pi))*np.arctan2(H.imag,H.real),'o') 

plt.xlabel(u'Frecuencia [Hz]')
plt.ylabel(u'Fase del sistema [grados]')
plt.title(u'(1) Diagrama de fase')
plt.xscale('log')
plt.show()

R = 2200.
L = 0.015

w0 = 300;#Frecuencia de inicio para hacer la funcion de transferencia (rad/s)
w1 = 600000.; #Frecuencia en la que acaba (rad/s)

W = np.arange(w0,w1,100)
n=np.ones(len(W))
H = 0.5*n
plt.plot(W/(2*np.pi),(20*np.log10(abs(H))),'o')

plt.xlabel(u'Frecuencia [Hz]')
plt.ylabel(u'Ganancia del sistema (dB)')
plt.title(u'(2) Función de transferencia')
plt.xscale('log')#Escala logaritmica en x
plt.show()


plt.plot((W/(2*np.pi)),(360/(2*np.pi))*np.arctan2(H.imag,H.real),'o') 

plt.xlabel(u'Frecuencia [Hz]')
plt.ylabel(u'Fase del sistema [grados]')
plt.title(u'(2) Diagrama de fase')
plt.xscale('log')
plt.show()


