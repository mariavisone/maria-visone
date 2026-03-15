'''Scrivete un gioco in cui il giocatore 1 inserisce un
numero da 1 a 100 e il giocatore2 ha 5 tentativi per
indovinare il numero.
Il programma fornisce suggerimenti (troppo alto,
troppo basso), termina quando l'utente indovina
correttamente, quando i tentativi finiscono o se
scrive «mi arrendo».
#fallo così
giocatore1 = int(input("Inserisci un numero da 1 a 100: "))

tentativi_rimasti = 5

while tentativi_rimasti > 0:
    risposta = input("Indovina il numero o scrivi 'mi arrendo': ")

    if risposta == "mi arrendo":
        print("Hai perso! Il numero era", giocatore1)
        break
    else:
        giocatore2 = int(risposta)
        if giocatore2 != giocatore1:
            tentativi_rimasti -= 1
            if giocatore2 > giocatore1:
                print("Numero troppo alto")
            else:
                print("Numero troppo basso")
            print("Tentativi rimasti:", tentativi_rimasti)
        else:
            print("Complimenti! Hai indovinato il numero", giocatore1)
            break

if tentativi_rimasti == 0:
    print("Hai esaurito i tentativi! Il numero era", giocatore1)

'Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave.



alfabeto = "abcdefghijklmnopqrstuvwxyz"

parola = input("Inserisci una parola: ").lower() #mi trasformo tutto in minuscolo
chiave = 3 #imposto di quanto voglio spostare le lettere
scelta = input("Scrivi 'criptare' o  'decriptare': ")

risultato = ""  #questo sarebbe la stringa che conterrà la parola nuova criptata o decriptata

for lettera in parola: #prende ogni lettera in parola
    if lettera in alfabeto: #controllo se quella lettera è in alfabeto, come s efosse una condizione booleana quindi restituisce true se è contanuta in alfabeto
        posizione = alfabeto.index(lettera)  #cerco la posizione della lettera in alfabeto
#ad esempio se è a l'output sarà #0

        if scelta == "criptare":
            nuova_posizione = (posizione + chiave) % len(alfabeto)
        else:
            nuova_posizione = (posizione - chiave) % len(alfabeto)

        risultato += alfabeto[nuova_posizione] #ogni volta aggiungiamo la lettera in risultato
    else:
        risultato += lettera   #se la lettera non è in alfabeto, copiala così com'è in risultato

print("Risultato:", risultato)

#un altro esercizo
Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma'''

#utente = input("inserisci una frase: ").lower() #la trasformo tutto in minuscolo
#tolgo gli spazi

def controllo_palindroma (frase):
    frase = frase.lower()  #la trasformo tutto in minuscolo
    
#per togliere gli spazi tra una parola e un'altra
#mi creo una stringa vuota e poi usando un ciclo for verifico che ogni carattere non sia uno spazio
    frase_pulita = ""
    for carattere in frase:
        if carattere != " ": #se non è vado ad aggiungere quel carattere alla frase, uno ad uno
            frase_pulita = frase_pulita + carattere
        else: 
            print("attenzione è stato trovato un carattere speciale", carattere)
    print(frase_pulita)
    frase_invertita = frase_pulita[::-1] #inverto la stringa

    if frase_pulita == frase_invertita:
        return "è palidroma"
    else:
        return "non è palindroma"        


#chiediamo all'utente
testo = input("inserisci una frase: ")

#stampo il risultato 
print(controllo_palindroma(testo))


