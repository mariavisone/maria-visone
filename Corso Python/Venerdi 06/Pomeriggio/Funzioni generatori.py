# Funzioni generatori
# serve per elementi grandi
'''
def fibonacci(n): #definisce il nome di una funz e un paramentro n
    a = 0
    b = 0 #sta definendo due variabili significa a  = 0 e b = 0

    while a < n:  #finche a è inferiore al parametro n
        yield a   #dopo che hai fatto questo passaggio, aspetta che finiscano le altre operazioni che hai 
        a = b
        b = a + b

lista  = list(fibonacci(10))

for x in list(fibonacci(10)):
    print(x)

esempio GeneratorE

for x in list[fibonacci(10)]:
    print(x)


#Decoratori
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()


def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è ", somma(3, 4))
'''

def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))