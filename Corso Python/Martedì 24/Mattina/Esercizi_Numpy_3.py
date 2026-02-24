'''Esercizio 1: Somma e Media di Elementi
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e
100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.

Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.'''

import numpy as np
#1 

#Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
arr_random = np.random.randint(1,101, 15)
print("array generato:", arr_random)

#Calcolare e stampare la somma di tutti gli elementi dell'array.
sum_arr_random = np.sum(arr_random)
print("somma dell'array random:", sum_arr_random)

#Calcolare e stampare la media di tutti gli elementi dell'array.
media = np.mean(arr_random)
print("La media è:", media)

#2
#Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
matrice = np.arange(1,26).reshape(5,5)
print("matrice creata:", matrice)


#Estrarre e stampare la seconda colonna della matrice.
#la seconda colonna avrà indice 1
seconda_colonna = matrice[:, 1]   #: tutte le righe, 1=colonna con indice 1
print("seconda colonna:", seconda_colonna)

#Estrarre e stampare la terza riga della matrice. indice 2
terza_riga = matrice[2, :]  #riga con indice 2 e tutte le colonne

#Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
diagonale = np.diagonal(matrice)
print ("diagonale:")
sum_diagonale = np.sum(diagonale)
print("somma degli elementi della diagonale:", diagonale)
