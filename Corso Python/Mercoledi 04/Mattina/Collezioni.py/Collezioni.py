# crea una lista di numeri, nomi e lista mista modificabile
numeri = [2, 3, 4, 5]
nomi = ["Alice", "Mirko", "Maria"]
misto = [1, "due", True, 10.4]

# provo ad accedere agli elementi della lista tramite indice
numeri = [1, 4, 5, 6]
print(numeri [3])
print(numeri[1])

# prova a sbagliare dando un indice inesistente e copia l'errore nel file testo nella folder eccezioni conosciute
lista = [a , b, c]
print(lista[5])

# usa i metodi con le liste
numeri = [3, 1, 4, 2, 5]
print(len(numeri))
numeri.append(6)
print(numeri)
numeri.insert(2, 10)
print(numeri)
numeri.remove(4)
print(numeri)


""" # crea una tupla e vedi se si può aggiundere una position
punto = (3, 4)
punto[0] = 5 """

"""punto.insert(2, 2)
print(punto) """

# prova tuple packing o tuple unpacking
punto = 3, 4
x , y = punto 
print(x, y)

#prova a trasformare una tupla in lista
tupla = 2, 3, 4
lista2 = list(tupla)
print(lista2)

# crea insieme utilizzando la funzione da una lista 
set1 = set([1, 2, 3, 4, 5])
set2 = {1, 2, 3, 4, 5}
print(set2)

# metodi tra due insiemi
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))










