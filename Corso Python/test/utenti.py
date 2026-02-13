#metto qui la classe utente ceh deve avere attributi genererici ovvvero nome e badge, caratteristiche ceh tutti devono condividere
#coem se fosse la mia superclasse

class Utente:
    def __init__(self,nome, badge):
        self.nome = nome
        self.__badge = badge  #il badge lo metto privato e potrò accedervi solo con un metodo 
    #quindi uso il get per ottenere poi il badge che è privato (sto usando l'incapsulamento)
    def get_badge(self):
        return self.__badge
    #devo scrivere una stringa che printa le info
    def mostra_info(self):
        print("Salve ", self.nome, "il suo badge è: ", self.get_badge())   #qui ho usato l'incapsulamento

#creo la classe che mi definisce il dipendente
class Dipendente(Utente):
    def __init__(self, nome, badge, turno, ruolo):
        super().__init__(nome, badge)   #concetto di ereditarietà da classe utente
        self.turno = turno
        self.ruolo = ruolo 
    def mostra_info(self):   #ho un polimorfismo con lo stesso nome ma coon comportamento diverso
        print("Salve ", self.nome, "il suo badge è: ", self.get_badge(), "turno: ", self.turno, "e ruolo: ", self.ruolo )
