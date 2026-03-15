'''var = "l'altro giorno la prof ha citato dante:\"nel mezzo del cammin..\""

#create un programma che richiede all’utente tre numeri e verifica la presenza di almeno due numeri uguali, se non ci sono ci restituisce il numero più grande dei tre
welcome= ("inserisci qui sotto 3 numeri n1,n2 n3")
print(welcome)

num1 = int(input("inserisci n1: "))
num2 = int(input("inserisci n2: "))
num3 = int(input("inserisci n3: "))

#verifica la presenza di almeno due numeri uguale
if num1 == num2 or num1 == num3 or num2 == num3:
    print ("okay due dei tuoi numeri sono uguali")
else:
    if num1 > num2 and num1 > num3:
        print ("num1 è il numeor più grande che hai inserito")
    elif num2 > num1 and num2> num3:
        print ("num2 è il numero più grande che hai inserito")
    else:
        print("il num3 è il numero più grande che hai inserito")

#un altro modo per svolgere l'esercizio
lista = []
num1 = input("inserisci un numero:")
lista.append(num1)

num2 = input("inserisci un numero:")
lista.append(num2)

num3 = input("inserisci un numero:")
lista.append(num3)

#poi faccio un ciclo while che  im dice che finche il numero è minore di tre 
#potremmo chidere un numero 
counter = 0
while counter <3 :
    num = input("inserisci unn numero:")
    lista.append(num)
    counter +=1

#facciamo un while piu semplice 
# per ripetere un codice all'infinito
while True:
    print("ciao") 
    break
#chiudere il ciclo infinito uso break

while True:
    uscire = input ("vuoi uscire:")
    if uscire == "si":
        break
    print("contiua ciclo")

#un  altro esercizio per continue
bitcoin ="salita"
while True:
    if bitcoin == "discesa":
        continue
    print("investi")


#parliamo di liste
lista = [1, 1.3, "stringa", ["zero", "uno", "due"]]

print(lista[-1][1])

#se io faccio 
lista2 = lista[1:5] #1 incluso, 5 escluso oppure posso comprendere anche l'indice 0 e faccio [:5] oppure tutti [:]
print(lista2)

#oppure se volessimo invertire tutta la lista
lista2 = lista[::-1] #inverto tutta la lista copiando uttti gli elementi andando di uno in uno partendi dall'ultimo elemento
#oppure
lista2 = lista[1:5:2] 

#metodi delle liste
#ad esempio aggiungere append, insierire in posizioni specifiche con l'indice di posizione
lista = []
#lista.append()
#lista.insert(1,"altro")
#lista[1] = "altro" lo sovrascrivo
##lista.extend(lista2) e print(lista) aggiungo gli elementi di lista 2 in lista 
#print(lista) e non print(lista.append()) perchè non printerà nulla
#lista.reverse() a print(lista)
#lista.sort #li ordina dal piu grande al piu piccolo
#list.sort(reverse = True) #li ordina al contrario
#print(lista.index("tre"))
#lista.remove("tre") e poi #print(lista)
#del lista[3] #mi rimuove l'elemento in posizione 3 (indice di posizione)
#lista.pop() elimina l'ultimo elemento della lista, se gli passo l'indice di posizione tra le parentesi mi rimuove quello

#per verificare come inizia una stringa 
var = "ciao a tutti"
print(var.startswith("ci")) #mi darà true
print(var.endswith("tutti")) 
print(var.isalnum()) #sarà falso

#per convertire una aprola in minuscolo o maiuscolo var.lower() o var.upper()
#per replace 
var = "ciao a tutti"
var = var.replace("tutti" , "qualcuno")
print(var)

#print(var.count("ciao"))
print(var.count("i"))

#se io ho una variabile = "tommaso michele alfredo teresa" #per sapere quanit nomi ci sono in questa stringa
nomiL = nomi.split() #divido ogni nome secodno lo spazio che li divide
print(len(nomiL)) #printo la collection 

#se io ho una lista 
lista = ["tommaso", "michele", "alfredo", "teresa"]
#come faccio a trasformare in stringa questa lista separando i nomi con un separatore
separatore="-"
stringa = separatore.join(lista) #sep li separa e join invece unisce gli elementi di una lista a
print(stringa)

#ciclo for
#avendo una lista ad esempio
lista = ["tommaso", "michele", "alfredo", "teresa"]
#posso fare: for nome in lista 
#print(lista) e mi stampa tutti i nomi 
#for char in stringa: 
#Print(char)  #prendi tutti gli elementi in lista e salvali nella variabile char

lista = ["tommaso", "michele", "alfredo", "teresa"]
#se volessi stampare solo i nomi che contengono la a 
lista2= []
for nome in lista:
    if "a" in nome:
        lista2.append(nome)
#oppure
lista3 = [nome for nome in lista if "a" in nome ]
print(lista3)

#esercizio
scrivete un progrmama che chiede all'utente una serie di parole e restituisci solo le vocali e l'indice della vocale all'interno delle parole

lista = []
vocali = "aeiou"
parole = input("inserisci qui una serie di parole separate da uno spazio: *in minuscolo ")
lista_parole = parole.split()

for parola in lista_parole:
    print(parola)

#sappiamo che ogni elemento parte con indice 0
    indice = 0 
    for lettera in parola: #parola prende il valore di un elemento nella lista lista_parole
        if lettera in vocali:
            print("vocali: ", lettera, "indice:", indice)
        indice += 1
    


#fai come ha fatto lui così 
    index = 0
    while index <= len(parola):
        if parola[index] in vocali:
            print(parola, parola[index], index)

#tuple, set , dizionari

lista = [1,2,3]
tupla = (1,2,3)
set1 = {1,2,3}

#per aggiungere un elemento al set = set1.add("ciao")
#print(set1) e ho aggiunto ciao al set1

#i dizionari 
#i metodi più strutturati per archiviare i dati all'interno del nostro programma di codice
cliente1 = {"nome":"tommaso", "cognome":"muraca", "eta":18}
cliente2= {"nome":"luca", "cognome":"rossi", "eta":22}
#per stampare tutti i nomi
clienti = {1: cliente1,
           2: cliente2}
for key in clienti:
    print(clienti[key]["nome"])  #printo solo i nomi
for key in clienti:
    print(key)
for i, nome in enumerate(lista):
    print("indice:", i, "nome: ", nome)

tupla = (14,3,76,4,9)
print(sorted(tupla)) #ordina la tupla dal piu piccolo al piu grande 


#scrivi un programma che chiede all'utente una stringa e restituisce un dizionario rappresentante la "frequenza di
#comparsa" di ciascun carattere componente la stringa.
#Esempio:Stringa "ababcc", Risultato
#{"a": 2, "b": 2, "c": 2}

dict1 = {} #dizionario vuoto
stringa = input("insersci qui una stringa: ")

for carattere in stringa:
    if carattere not in dict1: #se quel carattere non c'è lo aggiungo con valore 1, se già c'è aumento di 1
        dict1[carattere] = 1
    else:
        dict1[carattere] = dict1[carattere] + 1
        #oppure dict[carattere] += 1

print(dict1)


Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni uno per volta e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10 '''

#mi serve un dizionario per salvare i dati degli alunni


alunni = {}

while True:
    studente = input("inserisci il tuo nome:")
    ut_voti = input("inserisci i tuoi voti con uno spazio tra un voto e l'altro:")
    #trasformo la stringa ut_voti in lista
    

    voti = []

    for voto in ut_voti.split():
        voti.append(float(voto))

    alunni[studente] = voti  #Nel registro alunni, sotto il nome di questo studente, salva questi voti.

    infomedia = input("vuoi sapere la tua media? se si scrivi 'media', altrimenti scrivi 'n'")
   
    if infomedia == "media":
        sommavoti = 0 
        for voto in voti:
            sommavoti += float(voto)

        media = sommavoti / len(voti)
        print(studente, "media: ", media)
        
    else: 
        print("okay inseriamo nel registro un nuovo studente")
        
    

    continua = input("vuoi inserire un altro studente? s/n")

    if continua != "s":
        break

