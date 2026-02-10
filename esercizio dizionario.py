#esercizio : sistema di gestione negozio
#1
#gestione Clienti

#3 classi:
#i clienti comprano
#l'inventario contiene articoli
#amministratori controllano tutto
#prima creo la classe articolo

import random  #genero un budget casuale per ogni cliente

class Utente:   #crea classe utente/cliente con un nome, budget e lista acquisti
    def __init__(self, nome):
        self.nome = nome
        self.saldo = random.randit(5 , 150)
        self.acquisti = []   #tiene traccia degli acquisti

    def __init__ (self):
        print(self.nome , "ha un saldo di", self.saldo, "euro.")

    def compra(self,negozio, nome_articolo, quantità):  #il cliente decide di comprare, metodo che permette al cliente di comprare un articolo
        successo = negozio.vendi(self, nome_articolo, quantità) 
        if successo:
            self.acquisti.append((nome_articolo, quantità))

#il negozio deve avere un nome, un inventario e deve tracciare le vendite e guadagni
class Negozio:
    def __init__(self, nome):
        self.nome = nome

        #creo un inventario con il dizionario
        self.inventario = {}

        #traccia delle vendite e guagagni
        self.vendite = []
        self.guadagno_totale = 0

    #per l'inventario    
    def aggiungi_articolo(self, nome_articolo, prezzo, quantità):  #creo un metodo per aggiungere ogni articolo con il nome prezzo e la quantità all'inventario
        self.inventario[nome_articolo] = {"prezzo": prezzo, "quantità": quantità} #prendi il dizionario self.inventario, usa nome_articolo come chiave e poi associo come alla chiave un altro dizionazio
        print("aggiunto:", nome_articolo, "- prezzo:", prezzo, "euro - e quantità: ", quantità)
    def rimuovi_articoli(self, nome_articolo): #èper rimuovere un articolo
        if nome_articolo in self.inventario:
            del self.inventario[nome_articolo]
            print("Articolo rimosso: ", nome_articolo)
        else:
            print("articolo non trovato: ", nome_articolo)
     #funzione per aggiornare il prodotto --- modifica inventario/dizionario       
    def aggiorna_articolo(self, nome_articolo, nuovo_prezzo, nuova_quantità):  #per aggiornare un articolo
        pass




    def inventario_completo(self):
        print( self.inventario,  "è l'inventario di", self.nome)
        pass
        
#finire l'esercizio ma guardandoti ogni step. stasera