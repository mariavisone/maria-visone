#andiamo a creare un sistema ripetibile che simuli un teatro:
'''Classe Base: Posto
 Attributi privati: _numero (intero): il numero del posto.
   _fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).
 Metodi: __init__(numero, fila): inizializza il posto impostando _occupato a False.
prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato. 
libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato. 
Getter: per recuperare il numero, la fila e lo stato (occupato/libero). 
Classi Derivate 
PostoVIP: Attributi 
aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
 Metodi: Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
   PostoStandard: Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
Metodi: Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione. 
Classe Teatro 
Attributi: _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard). 
Metodi: aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto. 
stampa_posti_occupati(): stampa tutti i posti che risultano occupati'''

 #creo una classe base Posto
class Posto:
    def __init__ (self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False #all'inizio il posto è libero

#scirvi un metodo per prenotare 
    def prenota(self):
        if self._occupato == False: #se il posto è libero
            print("il posto" , self._numero,"in fila", self._fila, "è libero")
        else:
            print("il posto", self._numero, "in fila", self._fila, "è già occupato")

#scrivi un metodo per liberare il posto
    def libera (self):
        if self.occupato == False: #se il posto è libero
            print ("il posto", self._numero, "in fila", self._fila, "non è prenotato")
        else:
            print("il posto" , self._numero, "in fila", self._fila, "è stato liberato")

#adesso utilizzo il getter per recuperare il numero, la fila e lo stato (occupato/libero).
    def get_numero(self):   #con il get recupero gli attributi senza modificarli
        return self._numero
    def get_fila(self):
        return self._fila
    def get_occupato(self):
        return self._occupato

#classi derivate: postovip e postostandard
class PostoVip(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila) #richiamo il costruttore della superclasse posto
        self.servizi_extra = servizi_extra 

#ora sovrascrivo il metodo prenota
    def prenota(self):
        if self._occupato == False: #se il posto è libero
            print("il posto" , self._numero, "in fila", self._fila, "è stato prenotato con successo")
            print("Puoi accedere e gestire ", self.servizi_extra)
        else:
            print("il posto", self._numero, "è già occupato")

#creo la sottoclasse il postostandard
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo): #riprendo il costruttore della classe posto per il nuemro e fila
        super().__init__(numero, fila)
        self.costo = costo  #attributo costo definito
    def prenota(self):  #sovrascrivo prenota
        if self._occupato == False: #se il posto è libero
            print("il posto" , self._numero, "in fila", self._fila, "è stato prenotato con successo")
            print("puoi vedere il costo del posto scelto: ", self.costo)
        else:
            print("il posto", self._numero, "è già occupato")

class Teatro:
    def __init__ (self):
        self._posti = []
    #metodo aggiungi_posto(posto) per aggiungere un nuovo posto alla lista
    def aggiungi_posto (self, posto):
        self._posti.append(posto) #sto aggiungendo il posto alla lista vuota _posti
        print("hai aggiunto un nuovo posto in", self._posti)
    def prenota_posto (self, numero, fila):  #per prenotare questo posto con uno specifico numero e fila
        for posto in self._posti: #ceerco prima il posto nella lista dei posti (standard e vip), se lo trovo 
            if posto.get_numero() == numero and posto.get_fila() == fila: #se lo trovo 
                posto.prenota() #in tal caso prenoto il posto riprendendo il metodo prenota sopra 
                return #per uscire dal metodo
    def stampa_posti_occupati(): #per stampare tutti i  posti occupati nel teatro
    #se io ho una lista self._posti dove si trovano i posti prenotati, perche quella list ala creo con i posti che ci inserisco ogni volta che prenoto, allora batsa pritnare quella lista ?! no uso la sunfione get_occupati
        for posto in self._posti: #per ogni posto nella lista self.posti
            #uso def get_occupato(self) che ancora devo usare e che mi fa effettivamente i posti occupati
            if posto  get_occupato() 

            