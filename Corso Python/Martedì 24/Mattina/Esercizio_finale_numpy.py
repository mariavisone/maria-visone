'''Crea uno script Python che esegua i seguenti passaggi:
1. Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49 più altre 50 posizioni casuali tra 49 e 101.
* Stampa l'array, il suo dtype e la sua shape.
2. Modifica il tipo di dato (dtype) dell'array in float64.
* Verifica e stampa di nuovo dtype e shape.
3. Utilizza lo slicing per ottenere:
o i primi 10 elementi o gli ultimi 7 elementi
* gli elementi dall'indice 5 all'indice 20 escluso o ogni quarto elemento dell'array
4. Modifica tramite slicing gli elementi dall'indice 10 a 15 (escluso
assegnando loro il valore 999.
5. Utilizza la fancy indexing per selezionare:
* gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
* tutti gli elementi pari dell'array utilizzando una maschera booleana
* tutti gli elementi maggiori della media dell'array
6. Stampa:
* l'array originale dopo tutte le modifiche o tutti i sotto-array ottenuti tramite slicing e fancy indexin'''

import numpy as np

#1
#creo un array con arange
array_definito = np.arange(0,50)

#prendo i 50 num casuali da 49 a 101, size = 50
array_random = np.random.randint(49,102, 50)

#unisco i due array 
array = np.concatenate((array_definito, array_random))
#Stampa l'array, il suo dtype e la sua shape.
print("array originale:", array)
print("il dtype:", array.dtype)
print("la shape dell'array:", array.shape)

#2 Modifica il tipo di dato (dtype) dell'array in float64.
array = np.array(array, dtype ='float64') 
print("array modificato:", array.dtype)  #stmapo il dtype con verifica
print("la shape del nuovo array modif:", array.shape) #stampo la sua shape

#3 Utilizza lo slicing per ottenere:o i primi 10 elementi o gli ultimi 7 elementi
slicing_1 = array[-7:]   #parte dal -7 e va fino alla fine len(array)
print("gli ultimi 7 elementi:", slicing_1)

# slicing: gli elementi dall'indice 5 all'indice 20 escluso o ogni quarto elemento dell'array
slincing_2 = array[5:20]
print("elementi dall'indice 5 all'indice 20 escluso:", slincing_2)

#ogni quarto elemento dell'array
slicing_3 = array[0:102:4]   #oppure slicing_3 = array[::4] ovvero 0: len(array): 4
print("ogni quarto elemento dell'array:", slicing_3)

#4 Modifica tramite slicing gli elementi dall'indice 10 a 15 (escluso
#assegnando loro il valore 999
array[10:15] = 999
print("array post modif con 999: ", array)

#5. Utilizza la fancy indexing per selezionare:
#gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
indices = np.array([0, 3, 7, 12, 25, 33, 48])
print(array[indices])

#tutti gli elementi pari dell'array utilizzando una maschera booleana
nu_pari = array[array %2 == 0 ] 
print("i numeri pari dell'array:", nu_pari)

#tutti gli elementi maggiori della media dell'array
media = array.mean()
print("media degli elementi:", media)
#sleleziono gli elementi magigorni della media
num_magg_media = array[array > media]
print("i numeri nell'array maggiori della media sono:", num_magg_media)

#6 stampa - l'array originale dopo tutte le modifiche 
# o tutti i sotto-array ottenuti tramite slicing e fancy indexin'''

#print array finale modif
print("array modificato finale, con modifica 999", array)
print("array modificato:", array.dtype)
print("gli ultimi 7 elementi:", slicing_1)
print("elementi dall'indice 5 all'indice 20 escluso:", slincing_2)
print("ogni quarto elemento dell'array:", slicing_3)
print("Numeri in posizioni specifiche:", array[indices])
print("i numeri pari dell'array:", nu_pari)
print("i numeri nell'array maggiori della media sono:", num_magg_media)
