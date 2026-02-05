# Esercizio Completo Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

#Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
#Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
#Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
#Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.

n = int(input("inserisci un numero intero positivo: "))
 
#1 

while n <= 0:
    n = int(input("errore. inserisci un numero intero che dev'essere positivo"))


#2
sommapari = 0
for i in range (1, n + 1, 1):
    if i % 2 == 0:
        sommapari = sommapari + i
print("la somma dei numeri pari è: ", sommapari)


#3
for i in range(1, n + 1, 1):
    if i % 2 != 0:
        print(i)

#4 
if n < 2:
    print( n, "non è un numero primo")
else:
    if n % n == 0:
        print("ok verifichiamo ancora")
        if n % 1 == 0:
            print(n, "è un numero primo") 





