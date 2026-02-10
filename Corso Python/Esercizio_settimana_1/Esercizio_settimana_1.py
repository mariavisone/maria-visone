#chiedi all'utente il suo nome e salutalo (Variabile tipo str + funzione print e input)

nome = input("inserisci il tuo nome: ")
print("Ciao, ", nome , "! Benvenuta in Python!")

#chiedi all'utente la sua età e quella di suo padre. poi stampale e addizionale (somma con int)
etàM = int(input("la tua età è: "))
etàP = int(input("l'eta di tuo padre è: "))
somma = etàM + etàP
print(somma , "è la somma della tua età e quella di tuo padre, curioso!")

#I BOOLEANI con confronto
#chiedi l'altezza del''utente. 
#crea una variabile booleana che vale: 
#true se l'altezza supera o uguale a 170cm altrim falsa

altezza = int(input("inserisci la tua altezza: "))
sei_alta = "Complimenti superi la media italiana!"
sei_alta = altezza >= 170 #la mia variabile booleana con una condizione 
print(sei_alta)



#stampa una lista con i dati dell'utente raccolti fin ora.

#chiedi all'utente se vuole aggiungere altro oltre alle info già date da porre nel sistema utilizzando if-elif-else

lista = [nome, etàM, altezza ]
print("i dati aggiunti al sistema sono: ", lista)
#if-elif-else
richiesta = input("vuoi aggiungere qualcosa alla lista da aggiungere al tuo cv?si / no")
if richiesta == "si":
    print("perfetto")
    info1 = int(input("Dimmi se desideri: sostituire = 1, inserire = 2 o rimuovere =3 un info"))
    if info1 == 1:
        print("Bene")
        info2 = input("vuoi sostituire la tua altezza con la tua residenza? si / no")
        if info2 == "si":
            print("proseguiamo")
            info3 = input("inserisci la tua residenza: ")
            lista[2] = info3
            print(lista)
        else:
            print("okay proseguiamo")
    elif info1 == 2:
        print("perfetto, 'vuoi inserire i tuoi anni di esperienza lavorativa nel settore della moda? si / no")
        info12 = input("risposta: ")
        if info12 == "si":
            print ("perfetto")
            info4= int(input("inserisci gli anni di esperienza: "))
        lista.append(info4)
        print(lista)
    elif info1 == 3:
        print("vuoi rimuovere qualche dato? si / no")
        info5= input("risposta: ")
        if info5 == "si":
            print("vuoi rimuovere altezza? si o no")
            info6 = input("risposta: ")
            if info6 == "si":
                lista.remove(altezza)
                print(lista)
    else:
        print("perfetto la tualista dati è definita")
else: 
    print("il tuo cv è completo")

#chiedi all'utente se vuole sapere quanit anni gli/le mancano alla pensione e stampa 
#crea un conteggio usando while
#anni_lavorativi_per_pensione = 40
pensione = input ("vuoi sapere quanti anni ti mancano alla pensione? si / no")
info4 = int(input("anni di esperienza lavorativa: "))
if pensione == "si":
    conteggio = info4 + 1
    while conteggio < 40:
        print (conteggio)
        conteggio += 1
    print ("siccome ti servono 40 anni di contributi alla pensione, sopra troverai conteggiati gli anni rimanenti")
else:
    print("Ok proseguiamo.")

#chiedi all'utente di inserire i suoi certificati con ogni certificato il tipo e l'anno di conseguimento
certificati = int(input("quanti certificati vuoi inserire nel tuo cv?"))
for i in range(1, certificati + 1, 1):
    print (i)
    tipo = input("tipo di certificato: ")
    anno = input("anno: ")

#fai un recap di dati fin ora inseriti sotto il profilo di modella. usando le funzioni

info3 = input("inserisci la tua residenza: ")
print("Ecco un recap dei dati inseriti a sistema per il tuo profilo")
modella = [nome, etàM, altezza, info3, info4]

def stampa_persona(modella):
    print("Nome:", modella[0])
    print("Età:", modella[1])
    print("Altezza:", modella[2])
    print("Residenza:", modella[3])
    print("Anni di esperienza:", modella[4])

stampa_persona(modella)