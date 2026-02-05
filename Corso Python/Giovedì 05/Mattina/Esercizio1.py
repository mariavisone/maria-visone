# 1
'''
scelta = input("Vuoi inserire un numero o una stringa?: ")
while True:
    if scelta == "numero":
        print("okay determino se è pari o dispari")
        num = int(input("inserisci un numero: "))
        if num % 2 == 0:
            print("il numero è pari")
        else:
            print("il numero è dispari")
    elif scelta == "stringa":
        print("perfetto")
        info1 = input("Aggiungi la tua stringa: ")
        print("Hai inserito:", info1)
    else:
        print("Non puoi proseguire")
    x = input("vuoi ripetere?: ")
    if x == "no":
        break
'''

#2 
scelta1 = int(input("Inserisci un numero che indichi l'inizio del tuo intervallo: "))
scelta2 = int(input("Inserisci un numero, più grande del primo, che indichi la fine del tuo intervallo: "))

numeri_primi = []
numeri_nonprimi = []

for numero in range(scelta1, scelta2 + 1):
    if numero < 2:
        numeri_nonprimi.append(numero)
        continue
for 







