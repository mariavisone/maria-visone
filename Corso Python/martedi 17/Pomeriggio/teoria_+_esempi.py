"""var = "l'altro giorno la prof ha citato dante:\"nel mezzo del cammin...\""

print(var)
raw_s = r'Hi\nHello'

print(raw_s)




nome = "tommaso"
#print("la mia età è",eta,"il mio nome è",nome)
#risultato = "la mia età è",eta,"il mio nome è",nome
#print(risultato)
print("la mia età è "+str(eta)+" il mio nome è "+nome)

print(f"la mia età è {eta} il mio nome è {nome}")

print(type(eta))

eta = 39
nome,cognome = "tommaso","muraca"

print(nome)

eta = eta+1

numero = input("scrivi un numero: ")

print(int(numero) +10)


if int(eta) >= 18:
    print("maggiorenne")
else:
    print("minorenne")

eta = 39

patente = True

bevuto = False

if eta < 18:print("non puoi guidare perchè sei minorenne")
elif patente == False:print("non puoi guidare perchè non hai la patente")
elif bevuto:print("non puoi guidare perchè hai bevuto")
else:print("puoi guidare")



if eta >= 18 and patente and bevuto == False:
    print("puoi guidare")
else:
    print("non puoi guidare")

    
1: non puoi guidare perchè sei minorenne
2: non puoi guidare perchè non hai la patente
3: non puoi guidare perchè hai bevuto
4: puoi guidare

eta = 39
if int(eta) >= 18:
    pass
    #print("maggiorenne")
else:
    print("minorenne")

print("maggiorenne" if eta >=18 else "minorenne")

var = "maggiorenne" if eta >=18 else "minorenne"


lista = []
num1 = input("inserisci un numero:")
lista.append(num1)
num2 = input("inserisci un numero:")
lista.append(num2)
num3 = input("inserisci un numero:")
lista.append(num3)

counter = 0
while counter < 3:
    num = input("inserisci un numero:")
    lista.append(num)
    counter+=1



while True:
    uscita = input("vuoi uscire:")
    if uscita == "si":
        break
    print("continua ciclo")

bitcon = "salita"

while True:
    if bitcon == "discesa":
        continue
    print("investi")


lista = [1,1.4,"stringa",["zero","uno","due"]]

print(lista[-1][1])

lista2 = lista


lista = ["zero","uno","due","tre","quattro","cinque"]
lista2 = lista[::-1]
lista2 = lista[1:5]
lista2 = lista[:5]
lista2 = lista[2:]
lista2 = lista[1:5:2]
print(lista2)



lista = ["zero","uno","due","tre","quattro","cinque"]
lista2 =[1,2,3]
#lista.append()
#lista.insert(1, "altro")
#lista[1] ="altro"
#print(lista.extend(lista2))
#lista.sort(reverse=True)
#lista.reverse()
print(lista.index("tre"))


lista = ["zero","uno","due","tre","quattro","cinque"]
#lista.remove("tre")
#del lista[3]
lista.pop(3)
print(lista)


var = "CiAo"
print(var.lower())
print(var.upper())
#print(var.startswith("ci"))
#print(var.endswith("tutti"))
#print(var.isalnum())
#print(var.isdecimal())


var = "ciao a tutti"

#var = var.replace("albero","qualcuno")

print(var.count("arrivederci"))


nomi = "tommaso michele alfredo teresa"

nomiL = nomi.split()

print(len(nomiL))

lista = ['tommaso', 'michele', 'alfredo', 'teresa']

#nome1,nome2,nome3,nome4 = lista
#nome1,_,_,_ = lista

lista = ['tommaso', 'michele', 'alfredo', 'teresa']

sep = "-"

stringa = sep.join(lista)
print(stringa)

lista = ['tommaso', 'michele', 'alfredo', 'teresa']
stringa = "ciao a tutti"

print("ci" in stringa)

stringa2 = stringa[1:5]

#print(stringa2)


lista = ['tommaso', 'michele', 'alfredo', 'teresa']
stringa = "ciao a tutti"

for nome in lista:
    print(nome)

print("dopo,", nome)


count =0
while count < 3:
    print("ciao")
    count+=1

lista = [0,1,2]

for el in range(3):
    print("ciao")
print(list(range(10,1,-1)))

lista = ['tommaso', 'michele', 'alfredo', 'teresa']

index = 0

while index < len(lista):
    print(lista[index])
    index+=1

for nome in lista:
    print(nome)


lista = ['tommaso', 'michele', 'alfredo', 'teresa']

lista2 = []
for nome in lista:
    if "a" in nome:
        lista2.append(nome)
lista3 = [nome for nome in lista if "a" in nome]
print(lista3)

lista = [1,2,3]
tupla = (1,2,3)
set1 = {1,2,3}

set1.add("ciao")
print(set1)
for key in cliente1:
    print(key)


cliente1 = {"nome":"tommaso","cognome":"muraca","eta":39}
cliente2 = {"nome":"teresa","cognome":"rossi","eta":18}



clienti ={1:cliente1,
          2:cliente2}

#for key,valore in clienti.items():
#    print(key,valore)
print(cliente1.items())
print(cliente1.keys())
print(cliente1.values())


cliente1 = {"nome":"tommaso","cognome":"muraca","eta":39}
print(cliente1.get("nome","elemento non trovato"))
print(cliente1.setdefault("nome","alfredo"))
print(cliente1)


lista = ["tommaso","teresa","alfredo"]

for i,nome in enumerate(lista):
    print(f"indice:{i}, nome:{nome}")


tupla = (5,1,12,7,3)

print(sorted(tupla, reverse=True))

lista = ['tommaso', 'michele', 'alfredo', 'teresa']

lista3 = [nome for nome in lista if "a" in nome]
print(lista3)

diz1 = {nome:nome+str(1) for nome in lista if "a" in nome}
print(diz1)


def somma(**a):
    print(a,type(a))
    print(a["num1"] +1)

somma(num1=15,num2=5,num3=10)


def somma(a,b):
    val = a+b
    print(val)
    return val

val =somma(5,10)

print(val)


eta = 18

def aumentaEta(eta):
    eta = eta +1
    return eta

print("prima",eta)
eta =aumentaEta(eta)
print("dopo",eta)


eta = 18

def aumentaEta():
    global eta
    eta = eta +1
    

print("prima",eta)
aumentaEta()
print("dopo",eta)

numero = 15

def funzMy(a):
    print(a+numero)

funzMy(10)

def funzMy():
    val = 15

funzMy()
print(val)

numeri = [1,2,3,4,5]

def moltiplica(a):
    return a*3

numeri = list(map(moltiplica, numeri))
print(numeri)

numeri2 =[]
for i in numeri:
    numeri2.append(moltiplica(i))
print(numeri2)


def pari(n):
    return n%2 == 0

numeri = [1,2,3,4,5]

#numeri = list(map(pari, numeri))

#print(numeri)

NuovaListaPari= []
for i in numeri:
    if not pari(i):
        #NuovaListaPari.append(i)
        numeri.remove(i)
print(numeri)

def pari(n):
    return n%2 == 0

numeri = [1,2,3,4,5]

numeri = list(filter(pari, numeri))

print(numeri)



def doppNumero(x):
    return x*x

lambda x:x*x

numeri = [1,2,3,4,5]

#def moltiplica(a):
#    return a*3

numeri = list(map(lambda x:x*3, numeri))
print(numeri)




"za", 3

"cd",3

"za"

import random as rd

#print(rd.random())

from random import randint, choice

#print(randint(1,100))

lista = [1,2,13,5,88]

print(choice(lista))

import funzioni

funzioni.somma(10,12)

funzioni.divisione(12,0)

from lib.funzioni import somma

somma(10,11)


import math

print(math.sqrt())


import datetime

#print(datetime.date(2026,2,17))

#print(datetime.time(15,40,00))
# print(datetime.datetime(2026,2,17,15,41,0))
print(datetime.datetime.now().month)


numero = input("inserisci un numero: ")
try:
    print(int(numero)+5)

except (TypeError or ValueError) as e:
    print("tipo non valido!",e)
except ValueError as e:
    print("numero non valido!",e)
except:
    print("errore!")

print("proseguo programma")
"""
#r leggere
#a appendere (aggiungere alla fine)
#w sovrascrivere
#x solo a creare il file
def leggifile():
    with open("file.txt","r") as file:
        contenuto = file.read()
    return contenuto



cont =leggifile()
listaR = cont.split("\n")
matrice1 =[]
['nome,cognome,indirizzo', 
 'tommaso,muraca,via roma', 
 'giovanni,rossi,via milano', 
 'teresa,verdi,via torino']
for riga in listaR:
    matrice1.append(riga.split(","))


matrice = [x.split(",") for x in listaR]
#print(matrice)
[['nome', 'cognome', 'indirizzo'],
 ['tommaso', 'muraca', 'via roma'],
 ['giovanni', 'rossi', 'via milano'], 
 ['teresa', 'verdi', 'via torino']]

for riga in range(1,len(matrice)):
    if matrice[riga][1] == "rossi":
        matrice[riga][1] = "verdi"

#print(matrice)

[['nome', 'cognome', 'indirizzo'],
 ['tommaso', 'muraca', 'via roma'], 
 ['giovanni', 'verdi', 'via milano'], 
 ['teresa', 'verdi', 'via torino']]

#matrice[2][0] = "alfredo"


listaC = []
for riga in matrice:
    listaC.append(",".join(riga))

#print(listaC)

listaC2 = [",".join(x) for x in matrice]
#print(listaC2)

stringaF = "\n".join(listaC2)

def scrivifile(stringa):
    with open("file2.txt","w") as file:
        file.write(stringa)

scrivifile(stringaF)
