nome = "maria"
età = 28
print(nome, età)
print ("questo è il mio nome:" , nome, "questa è la mia età:" , età)

nome = input("inserisci il tuo nome: ")
età = int( input("inserisci la tua età: "))
print ("Ciao, " + nome + "! Benvenuto in Python!")

# eseguo diversi calcoli con la funzione print 
print(1 + 6)
print (6 - 1)
print(4 / 2)
print(2 ** 3)
print(3 * 2)

# prova concatenazione stringhe
nome = "maria"
saluto = "ciao"
print( nome + " " + saluto)

# questo è un esempio
x = 1
y = 0.2
z = x - y
print(z)


# provo a stampare l'indice della stringa e un valore indicato
s = "Python"
print(s[0])
print(s[2])

# eseguo una concatenazione di str
saluto = "Ciao"
nome = "Maria"
messaggio = saluto +' ' +nome
print(messaggio)

# utilizzo dei metodi come:
s = "Ciao, python!"
print(len(s))
print(s.upper())
print(s.split(','))
print(s.replace('python', 'universo'))

# stampa un carattere
carattere = 'M'
print(carattere)

#i booleani prova 
booleanT = True
booleanF = False

print( booleanT, booleanF )

# booleani con int
booleanT =int(True)
booleanF =int(False)
print( booleanT, booleanF)

#i boleani utilizzano gli operatori logici and, or e not

x = 5
y = 10
z = 7
print( x < y and y >z)
print( x < y and z > y)
print(not(x > y))




