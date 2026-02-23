'''Crea
un array NumPy utilizzando arange 
e verifica il tipo di dato (dtype) 
e la forma (shape) dell'array.
Esercizio:
1. Utilizza la funzione np.arange per creare
un array di numeri interi da 10 a 49.
2. Verifica il tipo di dato dell'array e
stampa il risultato.
3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
4. Stampa la forma dell'array.

import numpy as np

arr = np.arange(10,50)
print(arr)

#verifico il tipo di dati dell'array e stampo il risultato
print(arr.dtype)

#cambio il tipo di dato dell'array in float64 e poi verifico il tipo di dato
arr = np.array(arr, dtype ='float32')
print(arr.dtype)   #verifico il tupo di dato

print("forma dell'array: ", arr.shape)  #stampo la forma dell'array

#il numero degli elementi
print("numeri degli elemenit di arr:", arr.size)

#somma degli elementi
print("somma degli elementi:", arr.sum())

#indexing and slicing
arr = np.array([1,2,3,4,5])

#indexing
print(arr[0])

#slicing 
print(arr[1:3])

#boolean indexing
print(arr[arr>2])  

#indexing and slicing
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)

#slicing sulle righe
print(arr_2d[1:3]) 

#slicing sulle colonne
print(arr_2d[:, 1:3]) 

#slicing misto
print(arr_2d[1:3, 1:3])

#slicing 
arr = np.array([0,1,2,3,4,5,6,7,8,9])

#slicing di base
print(arr[2:7])
      
#slicing con passo
print(arr[1:8:2])

#omettere start e stop
print(arr[:5])
print(arr[5:])

#utilizzare indici negativi -- si utilizza quando si hanno più righe
print(arr[-5:])
print(arr[:-5])

#fancy indexing in numpy
arr = np.array([10,20,30,40,50])

#utilizzo di un array di indici
indices = np.array([1,3])
print(arr[indices])

#utilizzo di una lista di indici (che chiamo coome voglio, in questo caso l'ho chiamata indices
indices = [0,2,4]
print(arr[indices])
Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
3. Utilizza lo slicing per estrarre gli ultimi 5 elementi
dell'array.
4. Utilizza lo slicing per estrarre gli elementi dall'indice 5
all'indice 15 (escluso).
5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
6. Modifica,tramite slicing, gli elementi dall'indice 5
all'indice 10 (escluso) assegnando loro il valore 99.
7. Stampa l'array originale e tutti i sottoarray ottenuti tramite
slicing.
Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.

import random
import numpy as np

lista = []

for i in range(20):          # ripete 20 volte 
    numero = random.randint(10, 51)  # numero tra 10 e 51(inclusi)
    lista.append(numero)

arr_originale = np.array(lista)
#NO FAI COSì!!!! --->
arr_originale = np.random.randint(10, 51, size=20)
print(arr_originale)

#slicing per estrarre i primi 10 elementi dell'array
#slicing di base
arr1 = arr_originale[0:11]
print(arr1)

#slicing per printare gli ultimi 5 elementi dell'array
arr2 = arr_originale[-5:]
print(arr2)

#slicing per estrarre gli elementi dall'indice 5all'indice 15 (escluso)
arr3 = arr_originale[5:15]
print(arr3)

#Utilizza lo slicing per estrarre ogni terzo elemento dell'array
arr4 = arr_originale[0:21:3]
print(arr4)

# Modifica,tramite slicing, gli elementi dall'indice 5all'indice 10 (escluso) 
# assegnando loro il valore 99.

arr_modificato = arr_originale.copy()
arr_modificato[5:10] = 99

print(arr_modificato)

#stampa tutto
print("array originale:", arr_originale)
print("gli ultimi 5 elementi dell'array:", arr2)
print("estratto i primi 10 elementi dell'array:",arr1)
print("estratto gli elementi dall'indice 5all'indice 15 (escluso):", arr3)
print("estratto ogni terzo elemento dell'array:", arr4)
print(arr_modificato)
'''

#Consegna:
'''
1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente
numeri interi casuali compresi tra 1 e 100.
2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
3. Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, 
la seconda diventa la penultima, e cosi via).
4. Estrai la diagonale principale della matrice invertita e 
crea un array 1D contenente questi elementi.
5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
6. Stampa la matrice originale, la sotto-matrice centrale estratta, 
la matrice invertita, la diagonale principale e la matrice invertita modificata.
Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array,
applicando operazioni avanzate come L'inversione delle righe e La sostituzione condizionale degli elementi. '''

import numpy as np
import random

#crea matrice 2D di dimensioni 6x6, contenentenum interi casuali compresi tra 1 e 100.
matrice = np.random.randint(1,100,size=(6,6))
print("matrice originale:", matrice)

#Estrai la sotto-matrice centrale 4x4 dalla matrice originale (4righe e 4 colonne)
sotto_matrice = matrice[1:5, 1:5]
print("matrice 4x4:", sotto_matrice)

#inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, 
#la seconda diventa la penultima, e cosi via).
matrice_inv = sotto_matrice[::-1, :]  #inverto le righe senz amod le colonne
print("matrice invertita:", matrice_inv)

#Estrai la diagonale principale della matrice invertita e 
#crea un array 1D contenente questi elementi.
diagonale = np.diag(matrice_inv)  #restituisce un array con gli elementi della diagonale
print("diagonale della matrix inv:", diagonale)

#Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
matrice_modif = matrice_inv.copy()
matrice_modif[matrice_modif %3 == 0] = -1
print("Ecco la matrice modificata con la sostituzione dei multipli di 3 con -1, nella matrice invertita: ", matrice_modif)


#Stampa la matrice originale, la sotto-matrice centrale estratta, 
#la matrice invertita, la diagonale principale e la matrice invertita modificata.
print("La matrice originale: ", matrice)
print("La sottomatrice:", sotto_matrice)
print("la matrice invertita è:", matrice_inv)
print("la diagonale estratta dalla matrix inv:", diagonale)
print("la matrix modificata è:" , matrice_modif)

