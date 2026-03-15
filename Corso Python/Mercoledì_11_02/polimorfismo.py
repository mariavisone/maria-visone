class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")

#overloading

class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
