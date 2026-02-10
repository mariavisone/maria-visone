#Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"),
#con un metodo per mostrare le info e un metodo per cambiare stato.

#Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi 
#permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

#Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”,
# segnare un pacco come “consegnato” e 
# calcolare il peso totale dei pacchi ancora non consegnati.

#Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.

class Pacco:  #classe che rappresenta il pacco
    def __init__(self, codice, peso):  #il costruttore mi delinea le info del pacco con codice e peso
        self.codice = codice
        self.peso = peso
        self.stato = "in magazzino"  #stato iniziale
    def info_pacco(self):
        print("codice pacco: ", self.codice,"peso: ", self.peso, "kg, ", "Stato: ", self.stato)
    def cambio_stato(self, nuovo_stato):
        self.stato = nuovo_stato
        print("il pacco", self.codice, "è ", self.stato)


class Magazzino:
    def __init__ (self):
        self.pacchi = []   
    #aggiungi pacco al dizionario
    def aggiungi_pacco (self, pacco): 
        self.pacchi.append(pacco)
    #posso anche cercare il pacco con key e quindi utilizzando get---
    def cerca_per_codice (self, codice): #self rappresenta il magazzino 
        for i in self.pacchi:  #per ogni pacco nella lista selfpacchi
            if i.codice == codice:  #se c'è un codice già nel sistema (i.codice) che è uguale al codice inserito che sto cercando adesso
                return i  #restituisci il pacco trovato
    
    def mostra_pacco_per_stato (self, stato):
        print("il pacco è:", stato)
        trovato = False
        for i in self.pacchi: #controlla tutti i pacchi nella lista 
            if i.stato == stato:  #e se il pacco ha quello stato 
                i.info_pacco()    #allora mostrami le info su quel pacco info_pacco
                trovato = True
            else:
                print("Nessun pacco trovato")

    def peso_totale_pacchi_non_cons(self):
        totale = 0
        for i in self.magazzino.pacchi:
            if i.stato != "consegnato":
                totale += p.peso


class GestorePacchi:
    def __init__ (self, magazzino):
        self.magazzino = magazzino
    
    def metti_in_consegna(self, codice, magazzino):
        pacco = magazzino.cerca_per_codice(codice) 
        if pacco is None:
            print("Pacco " , codice, "non trovato")
        else:
            if pacco.stato == "in magazzino":
                pacco.cambia_stato("in cosegna")
                print("il pacco ", codice, "è in consegna.")
            else:
                print("pacco" , codice, "non in magazzino")

    def consegna(self, codice, magazzino):
        pacco = magazzino.cerca_per_codice(codice)
        if pacco.stato == "in consegna":
            pacco.cambia_stato("consegnato")
            print("Pacco,", codice, "è stato consegnato")
        else:
            print("pacco", codice, "non trovato")

#calcolare il peso totale dei pacchi ancora non consegnati
    def peso_totale_pacchi_noncons(self):
        totale = 0
        if 

    







