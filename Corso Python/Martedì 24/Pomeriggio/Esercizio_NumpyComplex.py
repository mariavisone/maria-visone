'''Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 20.
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. 
Le operazioni disponibili includono, ogni volta che il sistema conclude un calcolo va salvato su un file txt:
I. Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
2. Estrarre e stampare la sotto-matrice centrale.
3. Trasporre la matrice e stamparla.
4. Calcolare e stampare la somma di tutti gli elementi della matrice.
5. Uscire dal programma o ripetere

import numpy as np

fileName = "matrice.txt"

#funzione per salvare i file
def salvataggio_file (testo):
    with open(fileName, 'a') as f:
        f.write(testo + "\n") 

#funzione per creare la matrice
def crea_matrice():
    righe = int(input("inserisci il numero di righe:"))
    colonne = int(input("inserisci il numero di colonne: "))

    matrice = np.random.randint(1,101, size=(righe,colonne))
    print("Matrice creata: ", matrice)
    salvataggio_file("Matrice creata: ") #passo alla funzione la stringa 
    salvataggio_file(str(matrice))  #prima trasformo la matrice che è un array in str (str(matrice)) e la salvo nel file con la funzione creata prima
                               
#funzione sottomatrice centrale
def sotto_matrice(matrice):
    sotto_matrice = matrice[1:-1, 1:-1]
    print("matrice 4x4:", sotto_matrice)
    salvataggio_file("sotto matrice centrale creata: ")
    salvataggio_file(str(sotto_matrice))

#funzione trasponi matrice
def trasponi_matrice(matrice):
    trasponi = matrice.T
    print("matrice trasposta", trasponi)
    salvataggio_file("matrice trasposta: ")
    salvataggio_file(str(trasponi))

#funzione somma 
def somma_matrice(matrice):
    somma = np.sum(matrice)
    print("la somma: ", somma)
    salvataggio_file(f"Somma matrice: {somma}")

#main

def menu():
    matrice = None

    while True:
        print("\n--- MENU ---")
        print("1. Crea matrice")
        print("2. Sotto-matrice centrale")
        print("3. Trasponi")
        print("4. Somma elementi")
        print("5. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            matrice = crea_matrice()

        elif scelta == "2":
            if matrice is not None:
                sotto_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "3":
            if matrice is not None:
                trasponi_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "4":
            if matrice is not None:
                somma_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "5":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

#avvio programma 
menu()

#PARTE DUE
Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
6. Moltiplicazione Element-wise con un'altra Matrice:
 L'utente può scegliere di creare una seconda matrice delle stesse dimensioni della prima e
   moltiplicarle elemento per eLemento e stampare il risultato.
7. Calcolo della Media degli Elementi della Matrice:
 Calcolare e stampare la media di tutti gli elementi della matrice

def moltiplicazione_Elementwise(matrice):
    righe, colonne = matrice.shape #prendo le dimensioni della matrice creata
    print("la matrice creata ha dimensioni:", righe, "x", colonne)

#creo la seconda matrice con le stesse dimensioni
    matrice2 = np.random.randint(1,101, size=(righe,colonne))
    print("Secodna matrice:", matrice2)
    salvataggio_file("seconda matrice:")
    salvataggio_file(str(matrice2))

#moltiplica elemento per elemento
    risultato = matrice * matrice2
    print("Risultato moltipilcazione", risultato)
    salvataggio_file("risultato moltiplicazione:")
    salvataggio_file(str(risultato))

#Calcolare e stampare la media di tutti gli elementi della matrice
def calcolo_media(matrice):
    media = np.mean(matrice)
    print("La media calcolata deli elementi della matrice:", media)
    salvataggio_file(f"Media degli elementi: {media}")

'''


import numpy as np

fileName = "matrice.txt"

#funzione per salvare i file
def salvataggio_file (testo):
    with open(fileName, 'a') as f:
        f.write(testo + "\n") 

#funzione per creare la matrice
def crea_matrice():
    righe = int(input("inserisci il numero di righe:"))
    colonne = int(input("inserisci il numero di colonne: "))

    matrice = np.random.randint(1,101, size=(righe,colonne))
    print("Matrice creata: ", matrice)
    salvataggio_file("Matrice creata: ") #passo alla funzione la stringa 
    salvataggio_file(str(matrice))  #prima trasformo la matrice che è un array in str (str(matrice)) e la salvo nel file con la funzione creata prima
                               
#funzione sottomatrice centrale
def sotto_matrice(matrice):
    sotto_matrice = matrice[1:-1, 1:-1]
    print("matrice 4x4:", sotto_matrice)
    salvataggio_file("sotto matrice centrale creata: ")
    salvataggio_file(str(sotto_matrice))

#funzione trasponi matrice
def trasponi_matrice(matrice):
    trasponi = matrice.T
    print("matrice trasposta", trasponi)
    salvataggio_file("matrice trasposta: ")
    salvataggio_file(str(trasponi))

#funzione somma 
def somma_matrice(matrice):
    somma = np.sum(matrice)
    print("la somma: ", somma)
    salvataggio_file(f"Somma matrice: {somma}")

def moltiplicazione_Elementwise(matrice):
    righe, colonne = matrice.shape #prendo le dimensioni della matrice creata
    print("la matrice creata ha dimensioni:", righe, "x", colonne)

#creo la seconda matrice con le stesse dimensioni
    matrice2 = np.random.randint(1,101, size=(righe,colonne))
    print("Secodna matrice:", matrice2)
    salvataggio_file("seconda matrice:")
    salvataggio_file(str(matrice2))

#moltiplica elemento per elemento
    risultato = matrice * matrice2
    print("Risultato moltipilcazione", risultato)
    salvataggio_file("risultato moltiplicazione:")
    salvataggio_file(str(risultato))

#Calcolare e stampare la media di tutti gli elementi della matrice
def calcolo_media(matrice):
    media = np.mean(matrice)
    print("La media calcolata deli elementi della matrice:", media)
    salvataggio_file(f"Media degli elementi: {media}")

#main

def menu():
    matrice = None

    while True:
        print("\n--- MENU ---")
        print("1. Crea matrice")
        print("2. Sotto-matrice centrale")
        print("3. Trasponi")
        print("4. Somma elementi")
        print("5. Esci")
        print("6. Moltiplicazione Element-wise con una seconda matrice")
        print("7. media degli elementi della matrice")

        scelta = input("Scelta: ")

        if scelta == "1":
            matrice = crea_matrice()

        elif scelta == "2":
            if matrice is not None:
                sotto_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "3":
            if matrice is not None:
                trasponi_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "4":
            if matrice is not None:
                somma_matrice(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "5":
            print("Uscita dal programma.")
            break

        elif scelta == "6":
            if matrice is not None:
                moltiplicazione_Elementwise(matrice)
            else:
                print("Devi prima creare una matrice.")

        elif scelta == "7":
            if matrice is not None:
                calcolo_media(matrice)
            else:
                print("Devi prima creare una matrice.")

        else:
            print("Scelta non valida.")

#avvio programma 
menu()



    



