#altra slide ristorante
#1.
class Ristorante:
    def __init__(self, nome, tipo_cucina):
            self.nome = nome
            self.tipo_cucina = tipo_cucina
            self.aperto = False   #di default
            self.piatti = [] #lista vuota dei piatti
            self.prezzi = [] #lista vuota dei prezi
    def descrivi_ristorante(self):
          print("il ristorante ", self.nome," è specializzato in ", self.tipo_cucina)
    def stato_apertura(self):
          print("il ristorante è ", self.aperto)
    def apri_ristorante(self):
          self.aperto = True
          print("il ristornate" , self.nome , "è ora aperto.")
    def chiudi_ristorante(self):
          self.aperto = False
          print("Il ristorante", self.nome, "è ora chiuso")
    def aggiungi_al_menu(self,nome_del_piatto, prezzo):
          self.piatti.append(nome_del_piatto)
          self.prezzi.append(prezzo)
          print("al menu abbiamo ", nome_del_piatto, "prezzo: euro ", prezzo)
    def togli_dal_menu(self, nome_del_piatto, prezzo):
          self.piatti.remove(nome_del_piatto)
          self.prezzi.remove(prezzo)
          print ("hai rimosso ", nome_del_piatto, "e ", prezzo, "dal menu.")
    def stampa_menu (self):
          print("il menu del ristorante ",self.nome, "è il seguente: ")
          conteggio = 0
          while conteggio <
                print(nome_del_piatto, "euro ", prezzo)