#chiedi all'utente il suo nome e salutalo (Variabile tipo str + funzione print e input)

nome = input("inserisci il tuo nome: ")
print("Ciao, ", nome , "! Benvenuta in Python!")

#chiedi all'utente la sua età e quella di suo fratello. poi stampale e addizionale (somma con int)
etàM = int(input("la tua età è: "))
etàF = int(input("l'eta di tuo fratello è: "))
somma = etàM + etàF
print(somma) 
 
#I BOOLEANI con confronto
#chiedi l'altezza del''utente. 
#crea una variabile booleana che vale: 
#true se l'altezza supera o uguale a 170cm altrim falsa

altezza = int(input("inserisci la tua altezza: "))
sei_alta = altezza >= 170 #la mia variabile booleana con una condizione 
print(sei_alta + "Complimenti superi la media italiana!")

#collezioni - lista- insiemi -tuple
stampa una lista con i dati dell'utente raccolti fin ora.
chiedi all'utente se vuole aggiungere altro oltre alle info già date da porre nel sistema

lista = [nome, etàM, altezza ]
#if-elif-else
richiesta = input("vuoi aggiungere qualcosa alla lista da aggiungere al tuo cv?si / no")
if richiesta == "si":
    print("perfetto")
    info1 = int(input("Dimmi se desideri sostituire = 1, inserire = 2 o rimuovere =3 un info"))
    if info1 == 1:
        print("Bene")
        info2 = input("")
    elif info1 == 2:
        pass
    elif info1 == 3:
        pass
    else:
        pass
else:
    pass



                  
                  
