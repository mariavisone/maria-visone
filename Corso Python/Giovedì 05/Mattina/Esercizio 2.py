# Esercizio Completo Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

#Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
#Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
#Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
#Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.

n = int(input("inserisci un numero intero positivo: "))
 
#1 creo un blocco di cicli con while finche utente non mette la condizione desiderata
while n <= 0: #mentre n è minore o uguale di zerp
    n = int(input("errore. inserisci un numero intero che dev'essere positivo: "))


#2 creo una variabile sommapari
sommapari = 0
for i in range (1, n + 1, 1): #per ogni numero da 1 a 
    if i % 2 == 0: #se il numero è pari
        sommapari = sommapari + i #viene sommato alla variabile sommapari data all'inzio
print("la somma dei numeri pari è: ", sommapari)


#3 stampo tutti i numeri dispari da 1 a n
for i in range(1, n + 1, 1): #per ogni numero nel range 1 a n
    if i % 2 != 0: #se il numero è dispari 
        print(i) #stampa

#4 #Utilizzare una struttura if per determinare se n è un numero primo.
# Un numero primo è divisibile solo per 1 e per se stesso. 
# Il programma deve stampare se n è primo o no.

if n < 2:
    print( n, "non è un numero primo")
else: 
    primo = True #assumo che il valore sia primo
    for i in range (2, n): #creo un ciclo dove provo tutti i numeri da 2 fino a n-1 escludendo quinid 1 e se stesso per prendere tutti i numeri ma non quei due 
        if n % i == 0: #se i che divide n da resto 0 allora n non è primo, poichè abbiamo trovato un divisore
            primo = False
            break
    if primo:
        print(n, "è un numero primo")
    else:
        print(n, "non è un numero primo")




