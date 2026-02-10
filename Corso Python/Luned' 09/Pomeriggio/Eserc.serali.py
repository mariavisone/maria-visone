'''import time  # importiamo il modulo per lavorare con il tempo

# 1️⃣ Creo il decoratore
def tempo_di_esecuzione(func):
    def wrapper(*args, **kwargs):
        start = time.time()             # prendo il tempo all'inizio
        risultato = func(*args, **kwargs)  # chiamo la funzione originale
        end = time.time()               # prendo il tempo alla fine
        print(f"Tempo di esecuzione: {end - start:.4f} secondi")
        return risultato               # restituisco il risultato originale
    return wrapper  # restituisco la nuova funzione "decorata"
def conta_fino_a_milione():
    somma = 0
    for i in range(1_000_000):
        somma += i
    return somma
@tempo_di_esecuzione
def conta_fino_a_milione_decorata():
    somma = 0
    for i in range(1_000_000):
        somma += i
    return somma
conta_fino_a_milione_decorata()'''

import time
def decoratore(func):
    def wrapper (*args, **kwargs):
        print("start")
        risultato = func(*args, **kwargs)
        print ("end")
        return risultato
    return wrapper
@decoratore
def sottrai(a, b):
    return a - b

z = sottrai(10, 5)
print("risultato: ", z)

