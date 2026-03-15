'''Es1: Linspace, random, sum Descrizione: 
Crea un array utilizzando linspace, cambia La sua forma con reshape, genera un array casuale e calcola la somma degli elementi. 
Esercizio: 1.Crea un array di 12 numeri equidistanti tra 0 e 1 usando Linspace• 
2. Cambia la forma dell'array a una matrice 3x4. 
3. Genera una matrice 3x4 di numeri casuali tra 0 e 1. 
4. Calcola e stampa la somma degli elementi di entrambe le matrici

import numpy as np
#1
#Crea un array di 12 numeri equidistanti tra 0 e 1 usando Linspace•
arr = np.linspace(0,1,12) 
print("array linspace: ", arr)

#2
#Cambia la forma dell'array a una matrice 3x4
matrice = arr.reshape(3,4)
print("Matrice 3x4:", matrice)

#3
#Genera una matrice 3x4 di numeri casuali tra 0 e 1.
matrice_1 = np.random.rand(3,4)
print("matrice con num casuali 3x4:", matrice_1)

#4
#Calcola e stampa la somma degli elementi di entrambe le matrici
somma = np.sum(matrice)
somma_1 = np.sum(matrice_1)
print("la somma dei numeri della prima matrice è ", somma, "la somma dei numeri della seconda matrice è", somma_1)
'''

'''Es2: Linspace, random, sum
Consegna:
1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e
10.
2. Utilizza np. random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3. Somma i due array elemento per elemento per ottenere un nuovo array.
4. Calcola la somma totale degli elementi del nuovo array.
5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6. Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
7. Salva i dati su un file TXT a ogni giro
8. Rendi ripetibile il processo complessivo
9. Chiedi se si vuole sovrascrivere il TXT o no.
Obiettivo:
Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni per la somma parziale e gestire il salvataggio di file in merito'''


import numpy as np

while True: 
    #1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
    arr = np.linspace(0,10,50)
    print("Array con linscpace:", arr)

    #2. Utilizza np. random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
    arr_random = np.random.rand(50)
    print("array random di 50 num casuali:", arr_random)

    #3. Somma i due array elemento per elemento per ottenere un nuovo array.
    array_new= arr + arr_random
    print("somma totale dei deu arrray elemento per elemento:", array_new)

    #4. Calcola la somma totale degli elementi del nuovo array.
    somma_array_new = np.sum(array_new)
    print("la somma totale degli elementi del nuovo array:", somma_array_new)

    #5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
    num_magg_5= array_new[array_new > 5]

    somma = np.sum(num_magg_5)
    print("la somma degli elementi del nuovo array che sono maggiori di 5:", somma)

    #6. Stampa gli array originali, il nuovo array risultante dalla somma e
    # le somme calcolate.
    print("Array originale con linscpace:", arr)
    print("array random di 50 num casuali:", arr_random)
    print("Nuovo array risultante dalla somma:", array_new)
    print("la somma totale degli elementi del nuovo array:", somma_array_new)
    print("la somma degli elementi del nuovo array che sono maggiori di 5:", somma)

    #7. Salva i dati su un file TXT a ogni giro
    file = "dati_salvati.txt"

#uso try & except

    try:
        with open(file, "r"): #provo ad aprirlo in modalità lettura, se il file esiste
            risposta = input("Il file", file, "esiste. Sovrascrivere? (s/n): ").lower()
            if risposta == "s":
                with open(file, "w") as f:
                    f.write("qui sono i tuoi dati. Array linspace: ")
                    f.write(np.array2string(arr, precision =3)) #trasforma array in stringa mostrando solo 3 decimali(più leggibile)
                    f.write("somma totale:")

                print("File sovrascritto")
            else:
                print("File non sovrascritto")
    except: #se invece il file non esiste
        with open(file, "w") as f:
            f.write("Ecco i tuoi dati:")
        print("File creato ocn i tuoi dati")

