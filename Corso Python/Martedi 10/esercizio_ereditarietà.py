'''Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.'''

class Prodotto:
    def __init__ (self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    def calcola_profitto (self):
        return self.prezzo_vendita - self.costo_produzione
    
    def descrizione(self):
        return f"{self.nome} (costo: {self.costo_produzione}€, prezzo: {self.prezzo_vendita}€)"


class Elettronica(Prodotto):
    def __init__ (self, nome, costo_produzione, prezzo_vendita, garanzia):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
    def descrizione(self):
        return Prodotto.descrizione() + f" | Garanzia: {self.garanzia_mesi} mesi"

class Abbigliamento(Prodotto):
    def __init__ (self, nome, costo_produzione, prezzo_vendita, materiale):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
    def descrizione(self):
        return Prodotto.descrizione() + f" | Materiale: {self.Materiale}"    



class Fabbrica:
    def __init__(self):
        self.inventario = {} #dizionario di prodotti

    def aggiungi_prodotto(self, prodotto, quantità): #definisco una funzione che aggiunge prodotti all'inventario
        if prodotto in self.inventario:  #se il prodotto esiste già, aumentiamo la quantità
            self.inventario[prodotto.nome]["quantità"] += quantità
        else:   #se il prodotto non esiste già, lo aggiungiamo
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantità: ", quantità}

    #da rivedere non ho ben capito la vendita!!!
    def vendi_prodotto(self, nome_prodotto, quantità):
        disponibili = self.inventario[nome_prodotto]["quantità"]
        if quantità > disponibili:
            print("prodotto disponibile")

    #vendita
        self.inventario[nome_prodotto]["quantità"] -= quantità
        prodotto = self.inventario[nome_prodotto["prodotto"]]
        profitto_totale = prodotto.calcola_profitto() * quantità
        print("Venduti", quantità, "x", nome_prodotto)
        print("il profitto totale è" profitto_totale)
        else:
            if nome_prodotto not in self.inventario:
                print("operaizone nulla, il prodotto non è disponibile.")
#reso prodotto
    def resi_prodotto (self, nome_prodotto, quantità):
        self.inventario[nome_prodotto][quantità] += quantità
        print("reso effettuato: + ", quantità, "x", nome_prodotto)
