#1 
import random 

def genera_numero (): #definisco la funzione cioè genera un numero
    return random.randint(1, 100) #return fa uscire il numero dalla funzione e quindi posso riutilizzarlo, il range è per generare un numero casuale tra 1 e 100

numero = genera_numero () 
print("Ho scelto un numero tra 1 e 100, prova a indovinarlo")

while True:
    tentativo = int(input("inserisci un numero sapendo che se decidi 0, esci dalla pagina:  "))

    if tentativo == 0:
        print("exit")
        break
    elif tentativo < numero:
        print("il numero da indovinare è più alto di quello scelto")
    elif tentativo > numero:
        print("il numero da indovinare è più basso di quello scelto")
    else:
        print("Bravo, numero esatto!")
        break
    

