#Esempio di contenimento/incapsulamento
class Computer:
 def __init__(self, nome_proc):
   self.__processore = nome_proc # Attributo privato

 def get_processore(self):
   return self.__processore

 def set_processore(self, processore):
   self.__processore = processore

pc = Computer("Intel i5")
print(pc.get_processore()) 

# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 

# Modifica l'attributo privato tramite il setter
print(pc.get_processore())



#esempio2 

# Variabile globale
numero = 10

def funzione_esterna():
    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)    

    def funzione_interna():
        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)


#3 esempio di variabili private
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"


obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata)  # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata)  # Funzionerà, ma non è buona prassi


#esempio di metodi privati..
class Maria:

    def __privato(self):
        print("sono un metodo privato")
    def pubblico(self):
        self.__privato()

M = Maria
print("sono un metodo privato")


