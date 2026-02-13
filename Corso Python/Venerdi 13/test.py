''' python è un linguaggio di programmazione ovvero un linguaggio che contiene comandi di controllo e struttura. In specifico: python è un linguaggio interpretato, orientato agli oggetti, ad alto livello, dinamicamente tipizzato, semplice.
si definisce interpretato perchè il programmatore scrive il codice e la macchina lo traduce, se è correttamente scritto
E' orientato agli oggetti in quanto deve ripettare le 3 regole dell'OOP ovvero incapsulamento (per la protezione dati), ereditarietà(riutilizzo del codice in altre classi) e polimorfismo(flessibilità)
è definito ad alto livello poichè è piu vicino al linguaggio umano che a quello della macchina
è dinamicamente tipizzato poichè ogni valore ha un tipo, possiamo cambiare il tipo del valore ma non possiamo avere un valore senza un tipo
una caratteristica unica di python è l'indentazione ovvero lo spazio tra margine e riga di codice; ogni volta che ho as esmepio un nuovo blocco di codice devo aumentare il livello di indentazone 
per usare python dobbiamo istallare un IDE ovvero un programma che ci aiuta a sceivere il codice tutto in un unico ambiente chje è isolato dal sistema operativo o da altri programmi. quest'isolamento avviene perchè specifacemnte nell'IDE si va a scaricare l'estenzione di python come sistema integrato e si lavora li. 
in python si utilizzano funzioni incorporate ovvero print() input() len()  ovvero che possono essere utilizzare senza richiami esterni. E in python, fondamentali per la programmazione sono le variabili che possono essere di tipo basilari e non (rispettivaemnte che sono già esistenti all'interno di python e oggetti che invece creo io come liste e tuple, insiemi) '''




# 5
una collezione è un insieme di variabili salvate in unico punto in memoria. per i programmatori sono molto utili. ci sono 4 tipi di collezioni: liste, tuple, insiemi e dizionari
questi possoono essere modificabili, non modificabili e dinamiche.
le liste sono le strutture dati piu utilizzate. sono collezioni ordinate, modificabili e eterogenee. vengono definite con il tipo list con le parentesi []. ad esempio: listaX = [1, 2, "Marco", 300,]
In una list aposso aggiungere, rimuovere o sostituire un valore grazie agli indici di posizione e con funzioni specifiche. aggiungere con .append(), rimuovere con .remove() o sostituire indicando l'indice di posizione
Una tupla hanno una struttura simile alle liste ma non sonno modificabili,  sono ordinate, miste e il tipo è tuple con (). ex. tupla = (3, 5)
un insieme invece rappresenta una struttura di dati, ovvero una collezione non ordinata,modificabile e può essere mista. il tipo è set con {}. ex. set1 = {1, 2, 4, 4}
un dizionario invece è una struttura dati che permette di memorizzare i dati sottoforma di chiavi e valori. sono utili per creare oggetti e tabelle ad esempio
può essere misto in parte ovvero semieterogeneo, ordinato e modificabile. il tipo è dict con {chiave : valore }
la chiave è sempre una stringa mentre il valore può essere una stringa o un numero. si può accdere ai valori con la chiave corrispondente. ex. di dizionario dove la chiave è il nome e il valore è l'età: dict ={"nome": 3, ..}
#7
una classe è una struttura che raggruppa oggetti. in specifico è un disegno tecnico dell'oggett oche vogliamo creare, il suo blueprint.
possiamo avere il nome di una classe ma una classe può avere infiniti oggetti all'interno. ogni classe può avere: variabili e attributi, metodi semplici, metodi speciali e altre classi all'interno. 
gli attributi in specifico sono le caratteristiche dell'oggetto mentre i metodi sono le funzioni associate alla classe che operano sugli oggetti (chiamati anche istanze) e possono essere di 3 tipi: metodi statici, metodi decorati e metodi di istanza.
i metodi speciali che conosciamo sono: il costruttore e  il tool string. il costruttore veien invocato automaticamente al momento della creazione dell'oggetto ed è rappresetnato con __init__ e serve a creare e iniziare l'oggetto, e ha bisogno del parametro self. 
il tool string invece serve a definire come un oggetto deve essere stampato

#
La programmazione orientata agli oggetti OOP si basa su 3 concetti fondamentali: 
incapsulamento, ereditarietà, polimorfismo e più un concetto alla base di tutt’e tre ovvero l’astrazione, che permette alle 3 regole di lavorare contemporaneamente. 
Le tre regole collaborano tra loro e se una non funziona, nessuna delle 3 funziona. l'incapsulamento permette di nascondere i dettagli interni di una classe a livello di sicurezza del codice
l'ereditarietà è invece la capacità d iuna classe di avere un padre, e un figlio che può ereditare i suoi metodi e attributi se vogliamo. una classe può avere infiniti padri e infiniti figli, questa caratteristica è chiamata mmultiproprietarietà
il polimorfismo invece permette di cambiare forma e/o comprotamento ad un elemento x senza cambiarne il tipo.
ex. di ereditarietà con ereditarietà mutipla usando il nome della classe dove eredita e cosa eredita.

classe Maria:
    def __init__(self, età, colorecapelli):
        self.età = età
        self.colorecapelli = colorecapelli

classe Pippo(Maria):
    def __init__(self, età, colorecapelli, altezza):
    Maria.__init__(self, età, colorecapelli)
    self.altezza = altezza

ex incapsulamento: #con nome che diventa privato
class Persona:
    def.__init__(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome

ex. polimorfismo:
class Cane:
    def verso (self):
        print("bau")
class Gatto:
    def verso (self):
        print("miao")

def fai_verso (animale):
    animale.verso()
    


  #12
  Git è un sistema/tecnologia di versionamento, ovvero un sistema che registrale modifiche ad un file, o un insieme di file, cosicchè possiama piu avanti nel tempo richiamare le versioni specifiche. Git serve a gestire il codice emergente e consente a più individui di lavorare insieme su uno stesso progetto avendo lo storico delle modifiche apportate. 
Questo lo fa tramite 3 capacità. La prima è conservare la storia, che permette di tracciare ogni modifica con autorre della modifica e data. 
La seconda capacità è il branching e merging, ovvero che da un main file può creare dei branch indipendenti.
Successivamente i cambiamenti apportati nel branch possono essere integrati al progetto principale.
La terza capacità è la gestione di conflitti ovvero git riesce a risolvere i conflitti che sorgono laddove ad esempio codici uguali da piu autori. È importante precisare che Git è singolo per ogni, di base è una versione generalista ma che su ogni pc è diversa. 
Su Git esiste infatti il commit che ci permette di salvare lo stato attuale dei file con una specifica descrizione, come se il sistema stesse facendo una fotografia del progetto in un determinato momento
GIThub invece è il prodotto, è una piattaforma che serve as usare la tecnologiadi versionamento condivisa, permette di lavorare piu efficacemente su progetti insieme, possiamo lavorare con tutte le caratteristiche funzionali di git, ma lavorando in gruppo. Quando invece lavoriamo su git ognuno lavora sulla sua versione unica e questo non ci permette di lavorare insieme pienamente.

#13
l'astrazione è la capacità dell'oop di far funzionare le 3 regole fondamentali insieme. in pratica, ci permette di nascondere i dettagli interni dall'implementazione reale, di come la uso e quindi far vedere solo cosa fa e come la vado ad autilizzare. 
l'astrazione in python si ha tramite utilizzo di metodi astratti e classi astratte. la classe astratta non può essere istanziata ma serve come modello per le altre classi. 
i metodi astratti invece sono definiti all'interno di una classe astratta e devono essere implementati nelle classi derivate che ereditano dalla classe astratta. le classi astratte utilizzano il decoratore @abstractmetod, che impone che le sottoclassi abbiano quello specifico metodo passato subito dopo il decoratore.nelle classi astratte possono esserci entrabi i metodi , astratti e concreti.