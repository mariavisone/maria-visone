'''class Persona():
    pass

mirko_OBJ = Persona()

#spiegazione di Class

class Automobile:
    numero_di_ruote = 4

    def __init__(self, marca, modello):
            self.marca = marca
            self.modello = modello
    def stampa_info(self):
        print("L'automobile è una" , self.marca, self.modello)  


auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()
'''
#tipi non basilari
class MioOggetto:

    def __init__(self):
        pass

    def __str__(self):
        #viene richiamato quando facciamo : print(istanza_di_Persona)
        return "ciao Mirko sono un metodo speciale"

obj = MioOggetto()
print(type(obj))

print("-----------------")

print("esempio io string")
print(obj)