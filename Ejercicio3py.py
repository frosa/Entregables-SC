# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:48:53 2018

@author: Ivan
"""

import numpy as np
import matplotlib.pyplot as plt

tiemposignal=2.
fs=44100./1.
sam=(tiemposignal*fs)
#A
t=np.arange(0.,tiemposignal,1/fs)#Array de tiempos
f=1./tiemposignal
y=np.cos(2*np.pi*f*t)#Señal muestreada
plt.plot(t,y)
plt.xlabel(u'Tiempo[s]')
plt.ylabel(u'f(t)')
plt.title(u'Coseno muestreado durante 2 segundos')
plt.show()
#B
Fnss=(np.fft.fft(y))#Obtenemos los valores de los coeficientes de Fourier
Fn=np.fft.fftshift(Fnss)/sam#Ponemos la componente de frecuencia cero en el medio y normalizamos los valores de Fn dividiendo por el numero de muestras
n=np.arange((-len(Fn)/2.),(len(Fn)/2.),1)#Valores de las n
freq=n*f#~Valores de las frecuencias asociadas a cada valor de n
plt.plot(freq, abs(Fn.real))
plt.xlabel(u'Frecuencia[Hz]')
plt.ylabel(u'|Fn|')
plt.title(u'Coeficientes de Fourier')
plt.show()
#C
R=4075.#Resistencia en ohmios
#Coseno como Voltage
Pv=(np.abs(Fn)**2)/R#Calculamos la potencia de cada coeficiente
plt.plot(freq,Pv)
plt.xlabel(u'Frecuencia[Hz]')
plt.ylabel(u'Potencia [W]')
plt.title(u'Espectro de potencia (Voltaje)')
plt.show()
#Coseno como Intensidad
Pi=(np.abs(Fn)**2)*R#Calculamos la potencia de cada coeficiente
plt.plot(freq,Pi)
plt.xlabel(u'Frecuencia[Hz]')
plt.ylabel(u'Potencia [W]')
plt.title(u'Espectro de potencia (Intensidad)')
plt.show()