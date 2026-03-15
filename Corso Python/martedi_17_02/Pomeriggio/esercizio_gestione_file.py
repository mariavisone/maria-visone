'''Scrivete un programma che genera 5 numeri
casuali e li salva su un file,
l’utente dovrà cercare di indovinarne almeno 2 oppure
avrà perso. '''

#randint può avere dei parametri
import random

numeri = [] #insieme vuoto che conterrà i 5 num generati
#il programma importa il numero casuale 
for i in range(0,5): #i ci serve solo per far ripetere il ciclo 5 volte 
    numero = random.randint(1,100) #genera un numero tra 1 e 100
    numeri.append(numero) #aggiunge il numero alla lista

#salvo i numeri in un file csv
#scrivi una funzione per salvare i numeri
def scrivifile(lista, nome_file): #creo una funzione chiamata scrivifile dicendo cosa deve fare ovvero lista dei 5 numeri e specificare il nome del file
    with open("file2.txt","w") as file: #apro il file 
        file.write(",".join(str(n) for n in lista))  #write scrive dentro il file- ",".join prende tutti i numeri in lista e li mette in fila separati da una virgola
#str(n) for n in lista  - trasformo in stringa n, per ogni n in lista
#qui avro esattamente trasformato la lista dei 5 numeri [4,56,78,5,3] --> "4,56,78,5,3"
#oppure uso for: for numero in lista: file.write(str(numero) + ",")

#chiamo la funzione per slavare i numeri
scrivifile(numeri, "file2.txt")  #richiamo la funzione creata dando come lista = numeri e nome_file = file2.txt
print("numeri generati salvati su file2.txt") #serve come controllo

#--main
#chiedi all'utente di indovinare 5 numeri
print("prova ad indovinare almeno 2 num tra quelli generati dal sistema")

tentativo = 0 #conta i tentativi dell'utente
indovinati = 0 #conta i num indovinati

while tentativo < 5:  #finché i tentativi sono meno di 5. il ciclo while si ripete 5 volte
    numero = int(input("Inserisci un numero: "))  #1 tentativo
    if numero in numeri:  #se l'utente ha indovinato e quindi il numero è in numeir (lista iniziale)
        indovinati += 1 #incrementa indovinati
    tentativo += 1 #aggiugno un tentativo in tentativi e passo al prossimo tentativo

if indovinati >=2: #se l'utente ha indovinato almeno 2 numeri
    print("complimenti hai vinto! hai indovinato", indovinati, "numeri")
else:
    print("ahi perso mi dispiace, hai indovinato" , indovinati, "numeri")

#mostra i numeri generati dal sistema
print("i numeri generati erano:", numeri)