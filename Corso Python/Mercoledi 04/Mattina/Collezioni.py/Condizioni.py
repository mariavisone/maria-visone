# provo la condizione if
x = 10
y = 20 
if (x < y):
    print("perfetto")

# provo if e else
numero = 10
if numero > 0:
    print("il numero è positivo")
else:
    print("Blocco Else")

#if all'iniizo e else alla fine, posso avere un if dentro l'altro e elif sempre in mezzo
numero = 10
if numero > 0:
    print("il numero è positivo")
elif numero < 0:
    print("il numero è negativo")
else:
    print("Blocco Else")

# match in python

comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuti.") 


    






