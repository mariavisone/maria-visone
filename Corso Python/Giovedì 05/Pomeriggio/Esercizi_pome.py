#eserzizio completo 
#p1 
#Chiedi all'utente di inserire un numero intero positivo

n = int(input("inserisci un numero intero positivo"))
#1
while n <= 0:
    n = int(input("Errore, inserisci un numero intero positivo"))

#2
lista = [] #creo una lista vuota
for i in range (1, n + 1, 1): #definisco il range
    lista.append(i) #aggiungo i valori di quel range alla lista
print("questa è la lista di numeri interi casuali ", lista")


#3 utilizza un ciclo for per calcolare e stampare la somma dei num pari nella lista

sommmapari = 0 
for numero in lista: #per ogni numero nella lista
    if numero % 2 == 0: #dividi il numero per 2 e se il resto è 0 allora è pari
        sommapari += numero #se il numero è pari si aggiunge alla somma
    print("otteniamo come somma dei numeri pari: ", sommapari)


#4 utilizza un ciclo for per stampare tutti i numeri dispari nella lista
numeridis = 0
for numero in lista: #per i numeri in lista
    if numero % 2 != 0: #se quando li divido per 2 mi da un resto diverso da zero sono dispari
        numeridis.append(numero)
print(nuemridis)

#5 utilizza una funz per determinare se un num è primo. 
# la funzione deve restituire true se il numero è primo, altrimenti False
for numero in lista: # ciclo che prende ogni numero nella lista
    if numero < 2:
        continue # i numeri <2 non sono primi, salta al numero successivo
    primo = True #assumo che il valonumero sia primo
    for i in range (2, numero): #creo un ciclo dove provo tutti i numeri da 2 fino a n-1 escludendo quinid 1 e se stesso per prendere tutti i numeri ma non quei due 
        if numero % i == 0: #se i che divide n da resto 0 allora n non è primo, poichè abbiamo trovato un divisore
            primo = False #il numero non è primo
            break #finisco il ciclo controlliamo oltre
    if primo: 
        print(numero, "è un numero primo")
    else:
    

#6 utilizza un ciclo for per stampare tutti i numeri primi della lista
sommatotprimi = 0 
for numero in lista: 
    sommatotprimi += numero
print (sommatotprimi)

#7 una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo
#stampa il risultato

if sommatotprimi < 2
    print("la sonnna tot non è un num primo")
else: 
    primo = True #supponendo che la somma sia primo
    for i in range ( 2, sommatotprimi):
        if sommatotprimi % i == 0: # se troviamo un divisore allora
            primo = Falso 
            break
    if primo:
        print("la somma totale è un numero primo")
    else: 
        print("la somma totale non è un num primo")
