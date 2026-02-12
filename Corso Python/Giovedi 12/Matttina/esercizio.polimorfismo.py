'''creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.'''

#creo una classe generica di metodo di pagamento
class MetodoPagamento:
    def effettua_pagamenti (self, importo):
        print("Metodo non implementato.")

#creo le classi figlie
class CartaDiCredito (MetodoPagamento):
    def effettua_pagamenti (self, importo):
        print("Pagamento di importo: ", importo, "con carta di credito")

#creo la classe figlia Paypal con lo stesso metodo 
class PayPal(MetodoPagamento):
    def effettua_pagamenti (self, importo):
        print("il pagamento di importo ", importo, "è stato effettuato tramite Paypal.")

#creo la classe figlia BonificoBancario con lo stesso metodo
class BonificoBancario(MetodoPagamento):
    def effettua_pagamenti (self, importo):
        print("il pagamento di importo ", importo, "è stato effettuato tramite Bonifico Bancario.")

#devo creare una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.
#creo una clsse per la gestione pagamenti che può usare tutti e 3 i metodi di pagamento facedno un costrutto 


class GestionePagamento:
    def __init__ (self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento #in questo modo metodo_pagaemnto può usare qualsiasi metodo di pagamento carta di credito, paypal e BB
    def pagamento (self, importo): #creo una funzione per effettuare un pagamento
        self.metodo_pagamento.effettua_pagamenti(importo) #predno il metodo di pagamento appena salvato nell'oggetto e richiamo effettua_pagamento con il paramentro importo per sapere quanto pagare 

#devo renderlo ripetiibile e fare il menu di scelte


