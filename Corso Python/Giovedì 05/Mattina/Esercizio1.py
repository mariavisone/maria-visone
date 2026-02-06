# 1, Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale. 
# Il programma dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.
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

#2. Intermedio/ Numeri primi in un intervallo :
# Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e
50. #Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti e chiedere se deve ripetere
scelta1 = int(input("Inserisci un numero che indichi l'inizio del tuo intervallo: "))
scelta2 = int(input("Inserisci un numero, più grande del primo, che indichi la fine del tuo intervallo: "))

numeri_primi = []
numeri_nonprimi = []

for numero in range(scelta1, scelta2 + 1):
    if numero < 2:
        numeri_nonprimi.append(numero)
        continue
for 



#3 Chiedi all'utente di inserire due numeri. 
# Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri. 
# Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi".
#  La stessa cosa ma anche per due stringhe (.equal ) e chiedere se deve ripetere ma sono " complementari" solo se hanno tutte le lettere in comune (es: abs/ sab)




