#inversa di una matrice

import numpy as np

#creazione di una matrice quadrata
A = np.array([[1,2], [3,4]])

#calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)

#norma di un vettore

#creazione di un vettore
v = np.array([3,4])

#calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)

#numpy.linalg.colve
#quidni creazioen della matrice A e di un vettore B
A = np.array([[3,1], [1,2]])
B = np.array([9,8])

#risoluzioen del sistema di equazioni Ax = B
x = np.linalg.solve(A,B)
print("soluzione x:", x)

#LA TRASFORMATA DI FOURIER DISCRETA (DFT)
#per analizzare le frequenze dei segnali

# Creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della Trasformata di Fourier DFT
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)

#BROADCASTING
arr = np.array([1, 2, 3, 4])
scalar = 10 #lo scalare è il num da aggiungere ad ogni elem dell'array

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result)  # Output: [11 12 13 14]
