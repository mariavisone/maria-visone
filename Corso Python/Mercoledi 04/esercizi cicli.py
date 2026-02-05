
#es1
ripeti = "si"

while ripeti == "si":
    numero = int(input("Inserisci un numero: "))

    for i in range( numero, -1, -1):
        print(i)
    
    ripeti = input("Vuoi ripetere? (si/no): ")

#es2
numprimi = []
conteggio = 0

while conteggio < 6:
    numero = int(input("Inserisci un numero: "))

    if numero <2:
        print("Il numero non è primo")
    else:
        primo = True
