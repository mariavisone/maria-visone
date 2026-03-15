'''#creare una classe base membrosquadra e uno squadra che conterà le diverse classi figlie che rappresentano ruoli specificiall'interno della suadra di calci, come giocatore allenatore e assistente.
# Classe MembroSquadra:

Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)
Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro '''


#class MembroSquadra: classe base
#3 Classi figlie: Giocatrice, Allenatrice, Assistente

#class Squadra:
#due squadre che giocano una partita

#classe base deve avere nome età e metodo descrivi()
class MembroSquadra:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    def descrivi (self):
        print("Membro squadra:", self.nome, " , età:", self.età ) 

#creo una classe giocatrice che eredita dalla classe madre, che rappresenta una giocatrice che ha nome, età, ruolo, numero maglia
class Giocatrici(MembroSquadra): #una classe che eredita da membro squadra
    def __init__ (self, nome, età, ruolo, numero_maglia):
        super().__init__(nome, età)  #uso il costruttore della classe madre per età e nome
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.pt = 0   #punti fatti nella partita
    def gioca_partita (self):
        print(self.nome, "sta giocando come: ", self.ruolo, "con numero: ", self.numero_maglia)
    def segnapt (self, punti):
            self.pt += punti
            print("La giocatrice", self.nome, "ha segnato", self.pt)


class Allenatrice (MembroSquadra):
    def __init__(self, nome, età, anni_di_esperienza):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esperienza
    def dirige_allenamento (self):
        print("a dirigere la squadra è ", self.nome, "che ha ", self.anni_di_esperienza, "anni di esperienza in serie A")

class Assistente (MembroSquadra):
    def __init__(self, nome, età, specializzazione):
        super().__init__(nome,età)
        self.specializzazione = specializzazione
    def supporta_team (self):
        if self.specializzazione == "analista di gioco":
            print(self.nome, "è il primo assitente ed è stato preso in qualità di: ", self.specializzazione, " e analizzerà le partite durante il campionato.")
        elif self.specializzazione == "fiosioterapista":
            print(self.nome, "è stato preso in qualità di: ", self.specializzazione, " e sarà di supporto fisico durante il campionato per tutti i giocatori che ne hanno bisogno.")
        else:
            print(self.nome, "suporta la squadra come: ", self.specializzazione)

#adesso creo la squadra con nome , membri (lista vuota), punti segnati = 0
class Squadra:
    def __init__(self, nome):
        self.nome = nome #nome della squadra
        self.membri = [] #creo una lista vuota di membri della squadra
        self.punti_segnati =  0  #punti iniziali a zero
    
#  Avere metodi per:
#aggiungere membri
#far segnare punti
#stampare i dettagli della squadra
    def aggiungi_membro(self, membro):
        self.membri.append(membro)  #per aggiungere un membro alla lista
        for membro in self.membri: #prende tutti i membri nella lista membri
            membro.descrivi() #richiama la descrizione dei membri fatti nella classe membrosquadre
    def segna_punti (self, punti):
        self.punti_segnati += punti #sommo i punti al punteggio esistente
    def info_squadra(self):
        print("la squadra ", self.nome, "ha segnato", self.punti_segnati, "avendo in squadra: ", self.membri)
    
#adesso creo le due squadre
squadra1 = Squadra("Warriors")   #uso il costruttore di squadra per crearne una e chiamarla per nome
squadra2 = Squadra("Spurs")

#ora creo le giocatrici, allenatrici e assistenti per ciascuna scquadra. prima dei Warriors
player1 = Giocatrici("Maria", 28, "Playmaker", 19)  #classe giocatrici inserisco 
player2 = Giocatrici("Martina", 24, "Guardia", 7)
player3 = Giocatrici("Paola", 21, "Shooter", 11)
player4 = Giocatrici("Carmen", 25, "Post", 24)
player5 = Giocatrici("Zoe", 20, "Ala", 2)

allen1 = Allenatrice("Irsi", 43, 15) #nome, età e anni di esperienza

assist1 = Assistente("Patty,", 33, "analista di gioco")

#creo i membri della squadra 2
player6 = Giocatrici("Roby", 28, "Playmaker", 9)  #classe giocatrici inserisco 
player7 = Giocatrici("Sara", 24, "Play/Guardia", 8)
player8 = Giocatrici("Ale", 21, "Guardia", 6)
player9 = Giocatrici("Silvia", 25, "Post", 13)
player10 = Giocatrici("Awa", 20, "Ala/Post", 18)

allen2 = Allenatrice("Andrea", 36, 6)

assist1 = Assistente("Francesco", 30, "fisioterapista")

#aggiungo i miei membri alla squadra warriors sq1
squadra1.aggiungi_membro(player1)
squadra1.aggiungi_membro(player2)
squadra1.aggiungi_membro(player3)
squadra1.aggiungi_membro(player4)
squadra1.aggiungi_membro(player5)

#aggiungo i miei membri alla squadra Spurs sq2
squadra2.aggiungi_membro(player6)
squadra2.aggiungi_membro(player7)
squadra2.aggiungi_membro(player8)
squadra2.aggiungi_membro(player9)
squadra2.aggiungi_membro(player10)

#per mostrare sq1 e sq1 richiamo info_squadra nella classe Squadra
print("La partita sta per iniziare, fischio d'inizio con le squadre in campo")
squadra1.info_squadra()
squadra2.info_squadra()


#2 a metà partita 
print("A metà partita: ")
squadra1.punti_segnati(34)
squadra2.punti_segnati(29)
print(squadra1.nome, " - ", squadra1.punti_segnati)
print(squadra2.nome, " ", squadra2.punti_segnati) 


#A fine partita
print("fine partita")
squadra1.punti_segnati(45)
squadra2.punti_segnati(46)
print(squadra1.nome, " - ", squadra1.punti_segnati)
print(squadra2.nome, " - ", squadra2.punti_segnati) 





