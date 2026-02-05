""" # 1 crea una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se farti passare o no (3 livelli fate un paragone con ==
altezza1 = int(input("quanto sei alta?"))
if altezza1 > 165:
    print("sono abbastanza alta")
    if altezza1 ==166:
        print("sono più alta della media nazionale femminile italiana")
        if altezza1 > 190:
            print("sono la più alta della sezione")
        else:
            print("non sono la più alta della sezione")
    else:
        print("non sono più alta della media nazionale femminile italiana")
else:
    print("non sono abbastanza alta")


nome = input("Inserisci il nome: ")

if nome == "Maria":
    print("Brava Maria")
    eta = int(input("Inserisci l'età: "))
    if eta == 28:
        citta = input("Inserisci la città: ")
        print("perfetto")
        if citta == "Napoli":
            print("Verifica completata")
        else:
            print("Città errata")
    else:
        print("Età errata")
else:
    print("Nome errato") 

#2 andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di crud basilare (aggiungi rimuovi elimina)
lista = ["maria", "basket", "pop", 19]
richiesta = input("vuoi modificare la lista?")
if richiesta == "si":
    richesta = input("vuoi inserire, sostituire, eliminare?")
    if richiesta == "inserire":
        lista.insert("pallavolo", 3)
        print(lista)
    elif richiesta == "sostituire":
        lista[4] = 33
        print(lista) 
    elif richiesta == "eliminare":
        lista.remove("pop")
        print(lista)
else: 
    print("task not completed")


#3 """


#1
# scrivi un programma che chieda all'utente la sua età. se l'età è inferiore a 18anni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film". Altrimenti, dovrebbe stampare "puoi vedere questo film"
età = int(input("Inserisci la tua età: "))

match età:
    case _: 
        if età < 18:
            print("Mi dispiace, non puoi vedere questo film")
        else:
            print("Puoi vedere questo film")

#2 
n1 = input("inserisci un numero: ")
n2 = input("Inserisci un altro numero: ")


match calcoli