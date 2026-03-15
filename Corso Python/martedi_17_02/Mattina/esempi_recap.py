def somma():
    print(5+5)

somma()
#questa è una funzione che non riceve nessun argomento..
#ma posso dare alla funzione argomenti infiniti
def somm (a,b):
    print(a+b)

somm(1,2)


def somma (a=0, b=0):
    print(a+b)

somma(15,5,10) #non si può

def somma (a,b):
    print(a+b)

val = somma(5,10)
print(val) # non mi darà nullaaa
#non si fa
#ma per restituire un valore all'esterno della funzione
#devo sempre utilizzare return
def somma(a,b):
    val = a+b
    print(val)
    return val  #in questo modo se io scrivo la variabile val all'interno di ttutto il codice mi restituisce 
#la somma 
val = somma(10, 5)
print(val)

eta = 18

def aumentaEta():
    global eta  #svriviamo questo perchè voglio modificare l'età
    eta = eta +1

print ("prima", eta)
aumentaEta()

numero = 15
def funzMy(a): #qui siccome non la sto modificando non mi serve scrivere global a
    print(a+numero)

funzMy(10)

#se invece io facessi 
def FunzMy():
    val = 15

#mettiamo caso che ho una lsita di valori
numeri = [1,2,3,4,5]

#voglio avere una lista dove ognuno di questi numeri viene moltiplicato per 3
numeri2 = []

for i in numeri:
     numeri2.append(i*3)
print(numeri2)

#ora facciamo la stessa cosa ma i*3 la mettiamo come una funzione
numeri = [1,2,3,4,5]
def moltiplica(a):
    return a*3
numeri2 = []

for i in numeri:
    numeri2.append(moltiplica(i))
print(numeri2)

#invece di for posso usare map 
numeri = list(map(pari, numeri))



#un altra cosa , definisco prima la funzione
def pari(n):
    return n%2 == 0

numero = [1,2,3,4,5]
numeri2 = []
#l'obiettivo è filtrare solo i nuemri pari da quella lista
for i in numeri:
#questa lista deve contenere solo i numeri pari )
    if pari(i):
        numeri2.append(i)
print(numeri2)

#oppure non creo una nuova lista ma rimuovo i numeri non pari
numero = [1,2,3,4,5]
for i in numeri:
    if not pari(i):
        numeri2.remove(i)
print(numeri2)

#esiste anche filter, filtra un elemento data una funzione. quindi definisco prima la funzione
def pari(n):
    return n%2 == 0
#e poi filtro ogni elemento per quella funzione
numero = [1,2,3,4,5]

numeri = list(filter(pari, numeri))

print(numeri)

#lambda
#esempio di una funzione
def doppNumero(x):
    return x*x

lambda x:x*x   #si scrive lambda,l'elemnto che accetta e : l'elaborazione che fa
#se riprendiamo l'esercizio di prima
numero = [1,2,3,4,5]
#prima nell'eserizio di prima potevamo fare 
numeri = list(map(lambda x:x*3, numeri))
print(numeri)

#per importare una libreria esterna
import random as rd  #importo tutta la libreria ma questo appesantisce il codice

from random import randint, choice #importo solo una funzione specifica
print (randint(1,100))

lista = [1,2,13,5,88]

print(choice(lista))  #ci restituisce un valore random nella lista
#posso importare una funzione da un altro file qui scrivendo la stessa cosa
#posso importare anche una libreria dei calcoli matematici 
import math
print(math.sqrt())

#posso anche importare il giorno di oggi da una libreria datetime
import datetime
print(datetime.datetime.now()) #il primo datetime richiama il modulo. il secondo richiama la classe e now è un metodo della classe datetime che restituisce data e ora attuali

#come si gestiscono gli errori in pyhton all'interno di python
numero = (input ("inserisci un numero: "))
print (int(numero) + 5)
print("proseguo programma")

#gestire gli errori su pyhton si usa il costrutto try,except
try: #costrutto per provare un print 
    print (int(numero) + 5) #nel caso in cui produca errore, il programma non crasha
except:#se il print non va entro in questo print, in questo modo becco tutti gli errori
    print("numero non valido")
print("proseguo programma")

##scrivo anche cattura quest'errore e se becchi quest'errore
try: #costrutto per provare un print
    print (int(numero) + 5)
except TypeError as e: #se il print non va, per beccare un errore specifico, se becco questo errore entro in questo print
    print("numero non valido", e)
print("proseguo programma")

#oppure possoscrivere
except ValueError as a:
    print("tipo non valido", e)
print ("proseguo programma")

'''come leggere un csv con python
esmepio basilare: '''

nome,cognome,indirizzo
tommaso,muraca, via roma
maria, visone, via torino
rita, torre, via atellana


with open ("file:txt","r") as file: #il with open () #finche sei qui dentro il file è aperto, quando finisce il with il file è chiuso
#il ("file:txt","r")  il path del file file:text e come lo voglio leggere #r leggere, a aggiungere alla fine, w spvrescrivere, x crea il file
# as file per poterlo gestire con quel nome
    contenuto = file.read()  #per leggere cosa c'è dentro il file
print(contenuto)  #cosi vado a leggere ciò che c'è nel file

def leggifile():
    with open("file.txt", "r") as file:
        contenuto = file.read()
def scrivifile():
    with open("file2.txt", "r") as file: #file2 non è presente quindi in questo modo creo un file2 
        file.write("ciao") #sto scrivendo qualcosa nel file2

scivifile()

#posso anceh aggiungere una parole nel file
def scrivifile():
    with open("file2.txt", "a") as file: #file2 non è presente quindi in questo modo creo un file2 
        file.write("Maria") #sto scrivendo qualcosa nel file2
scrivifile()

cont = leggifile ()
print (cont)

cont = leggifile()
listaR = cont.split("\n")
print(listaR) #cosi divido ogni a capo 
matrice = [x.split(".") for x in listaR] #oppure posso utilizzare il for riga in listaR: matrice2.append.(riga.split(","))
#print (matrice)
for riga in range(len(matrice)):
    if matrice[riga][1] =="rossi":
        matrice[riga][1] = "verdi"

print(matrice)

#se io invece ho la matrice e vorrei convertirla in stringa come prima
#come faccio?
listaC =[]
for riga in matrice:
    listaC.append(",".join(riga))
print(listaC)
#oppure posso scirvere direttamente(senza fare il ciclo for)
listaC2= [",".join(x) for x in matrice]
print(listaC2)

#per trasformarlo in una stringa finale 
stringaF = .. 
print(stringaF)

