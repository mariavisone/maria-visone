'''Scrivete un programma che genera 5 numeri
casuali e li salva su un file,
l’utente dovrà cercare di indovinarne almeno 2 oppure
avrà perso. '''

#genera 5 numeri in una lista

from random import randint  #importiamo solo num int

numeri = []  #lista vuota dei 5 numeri che il sistema genererà
count = 0
#for i in range(0,5): #ripeto il ciclo 5 volte 
while count <5:  
    numero = randint(1, 50) #per ogni ciclo sceglie un num random
    if numero not in numeri: #se non è in numeri (per evitare di aggiungere uno stesso num)
        numeri.append(numero)  #aggiungo num alla lista vuota creata
        count +=1
    
        
#salvare numeri in un file file3.txt 

def scrivifile(lista): #scrivo una funzione per salvare i numeri generati
    stringa = ",".join(str(numero) for numero in lista)   #trasformo la lista di numeri in stringa perchè file.write accetta solo stringhe
    with open("file3.txt","w") as file:   #apro il file e lo tengo aperto
        file.write(stringa)   #scrivo la stringa nel file

#stringa = ",".join(str(numero) for numero in lista) 
#per ogni numero dentro la lista trasformalo in stringa e uniscili con una virgola e scrivili nel file, questo perchè file.write accetta solo stringhe
#",".join = mette una virgola tra ogni elemento della lista 

scrivifile(numeri)

print("I numeri generati sono stati salvati su file3.txt")


#--main 
#prima leggiamo il file

with open("file3.txt", "r") as file: 
    contenuto = file.read()

print(contenuto)

#chiediamo all'utente di indovinare almeno due numeri
print("prova ad indovinare almeno 2 numeri (da 1 a 50) dei 5 numeri generati dal sistema")
indovinati = 0

for i in range(5):  #ciclo deve ripetersi 5 volte
    try:
        tentativo = int(input("inserisci un numero: ")) #chiediamo il numero all'utente #inserire un try e except per controllare che l'utente inserisca un num e non una parola
    except:
        print("devi inserire un numero int da 1 a 50. Riprova")
        continue #torna all'inizio del ciclo senza contare in tentativo
    
    if tentativo in numeri:
        print("hai indovintato")
        numeri.remove(tentativo)    #per rimuovere il tentativo se indovinato dalla lista indovinati
        indovinati += 1
    else:
        print("Riprova")

if indovinati >= 2:
    print("hai vinto, hai indovinato", indovinati, "numeri")
else:
    print("hai perso, hai indovinato", indovinati, "numeri")








