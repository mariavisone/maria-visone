#esercizio 1 su Classi
#crea una classe chiamata Punto
'''
class Punto:
    def __init__ (self, x, y):
         self.x = x
         self.y = y
    
    def muovi(self)
 #concludi quest'esercizio!! 
    

#es 2
richiesta = "si"

while richiesta == "si":

    class Libro: #definisco la classe Libro
        def __init__ (self, titolo, autore, pagine): #aggiungo il costruttore della classe con degli attributi
            self.titolo = titolo #salvo il titolo come parametro nell'attributo titolo
            self.autore = autore  #salvo l'autore come parametro nell'attributo autore
            self.pagine = pagine #salvo le pagine come paramentro nell'attributo pagine

        def descrizione(self): #questo è un metodo di istanza
                print("Il libro ", self.titolo, " è stato scritto da", self.autore, " e ha ", self.pagine, " pagine.")

    #chiedo i dati all'utente
    titolo = input("inserisci il titolo: ")
    autore = input("inserisci autore: " )
    pagine = int(input("Inserisci il numero di pagine: "))

    libro = Libro(titolo, autore, pagine) #creo l'oggetto libro che poi deve avere la struttura della mia classe

    #richiamo il metodo descrizione definito sopra (il metodo descrizione esiste solo nell'oggetto Libro)
    libro.descrizione()
        
    richiesta = input("vuoi inserire un altro libro? si o no: ")
    if richiesta == "no":
        break
'''


#next slide exercize

class Libro:
    def __init__(self, titolo, autore,pagine):
        self.titolo = titolo #salvo il titolo come parametro nell'attributo titolo
        self.autore = autore  #salvo l'autore come parametro nell'attributo autore
        self.pagine = pagine #salvo le pagine come paramentro nell'attributo pagine
    def descrizione(self): #questo è un metodo di istanza
                print("Il libro ", self.titolo, " è stato scritto da", self.autore, " e ha ", self.pagine, " pagine.")

    #chiedo i dati all'utente
    titolo = input("inserisci il titolo: ")
    autore = input("inserisci autore: " )
    pagine = int(input("Inserisci il numero di pagine: "))

    libro = Libro(titolo, autore, pagine) #creo l'oggetto libro che poi deve avere la struttura della mia classe

    #richiamo il metodo descrizione definito sopra (il metodo descrizione esiste solo nell'oggetto Libro)
    libro.descrizione()

class Biblioteca:
       def _int__(self):
            self.lista = [] #creo una lista vuota come attributo dell'oggetto
       def
