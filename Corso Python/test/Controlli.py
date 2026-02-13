#creo la classe che mi registra chi prova ad entrare 
#vorrei registrare chi entra e se 
'''Classe ControlloAccesso
Tiene traccia di tutti i movimenti dei dipendenti: entrata e uscita
Ogni volta che un dipendente prova a entrare o uscire:
Controlla se può farlo (es. se ha un badge valido)
Registra nome, tipo di movimento (“Entrata” o “Uscita”) e turno
Salva il tutto in una lista privata (log)'''

class ControlloAccesso:
    def __init__(self): 
        self.__registro_accessi = [] #creo una lista vuota per registrare tutti gli ingressi rendendola privata
    #se il badge è valido allora il dipendente entra 
    def registra_ingresso(self, dipendente):
        badge = dipendente.get_badge()  #predno il badge del dipendente

        if badge is not None: #controllo se il badge esiste, se il badge è valido registro il nome e registro l'entrata con il turno)
            self.__registro_accessi.append(dipendente.nome, "Entrata", dipendente.turno)
            print ("accesso consentito a ", dipendente.nome)
            return True
        else:
            pass
