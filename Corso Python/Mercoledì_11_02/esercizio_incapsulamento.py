#crea una classe conto bancario che incapsula le info di un conto e formisce metodi per gestire il saldo in modo sicuro.
'''L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).'''


#classe contoBancario
class ContoBancario:
    def __init__(self, titolare, saldo):
    self.__titolare = "" #proteggo gli attributi usando __
    self.__saldo = float(saldo) #dovrei fare anche qui 
#valido/controllo che il titolare non sia una stringa vuota con il setter
    def get_titolare(self):
        pass
    
#metodo per il deposita importo
    def deposita_importo (self, importo):
        if importo > 0:
            self.__saldo += importo
            print("Deposito di ", importo, "eseguito con successo.")
        else:
            print("Operazione non valida.")
    def preleva_importo (self, importo):
        if importo <= self.__saldo and importo > 0:
            self.__saldo -= importo
            print("importo di ", importo, "sottratto con successo")
        else:
            print("operazione non riuscita")
    def visualizza_saldo (self):
        print("ecco il tuo saldo:", self.__saldo)

#gestione dei metodi e sicurezza    
#ora creo la classe UtenteGenerico
class UtenteGenerico:
    def __init__ (self, nome):
        self.nome = nome
    def info_utente (self):
        print("utente: ", self.nome)
#creo le due calssi figlie, prima cliente e poi admin inglobate in utente generico
class Cliente (UtenteGenerico):
    def __init__ (self, nome):
        super().__init__ (nome)
    def vedi_conto(self,conto):
        print(conto.visualizza_saldo())  #richiama il saldo nel conto nell'utentegenerico
class Admin (UtenteGenerico):
    def __init__ (self, nome):
        super().__init__ (nome)
    def vedi_conto(self, conto):
        print("il tuo" , conto.__ , "è", conto.visualizza_saldo() )


