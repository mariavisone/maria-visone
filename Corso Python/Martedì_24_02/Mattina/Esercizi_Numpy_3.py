'''Esercizio 1: Somma e Media di Elementi
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e
100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.

Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

import numpy as np
#1 

#Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
arr_random = np.random.randint(1,101, size=15)
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


#3
Esercizio 3: Operazioni con Fancy Indexing
Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1), (1,3), (2,2) e (3,0)
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
dell'array (considerando la numerazione delle righe che parte da o).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10
al loro valore.
'''
import numpy as np

#Creare un array NumPy di forma (4, 4) contenente numeri casuali tra 1 e 50
arr = np.random.randint(10,51, size=(4,4))
print("Array 4x4: ", arr)

#Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1), (1,3), (2,2) e (3,0)
righe = np.array([0,1,2,3]) #contiene gli indici delle righe selezionate
colonne = np.array([1,3,2,0])  #gli indici delle colonne selezionate

elem_selezionati = arr[righe,colonne]  #creo un nuovo arr chiamato elementi selezionati e predno dall'arr solo gli elementi che corrispondono a ciascuna coppia di riga e colonna indicato negli array righe colonne 
print("gli elementi selezionati sono:", elem_selezionati)

#utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
seleziona_righe = arr[1::2, :] #1: seleziona la riga 1 e :2 seleziona ogni due, : tutte
print("righe dispari:" , seleziona_righe)

#Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10
#al loro valore.

scalar = 10 #lo scalare è il num da aggiungere ad ogni elem dell'array

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = elem_selezionati + scalar
print(result)  


