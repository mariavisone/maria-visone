#Matplotlib 
'''
Esercizio Facile: Calcolo di Statistiche di Base
Testo dell'esercizio:
Hai a disposizione un dataset, che devi autogenerare, contenuto in un DataFrame pandas con una singola colonna temperature che rappresenta la temperatura giornaliera in una città per un mese.
Scrivi un programma Python che calcoli e stampi le seguenti statistiche:
* La temperatura massima
* La temperatura minima
* La temperatura media
* La mediana delle temperature '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#nuemri casuali fissi
np.random.seed(10)

#genero le temperature casuali
temperature_possibili = [21,23,25,26,28,30]

temperature = np.random.choice(temperature_possibili, size=365)

df = pd.DataFrame({"temperature": temperature})


#calcolo statistiche
temp_max = df["temperature"].max()
temp_min = df["temperature"].min()
temp_mean = df["temperature"].mean()
temp_median= df["temperature"].median()

#creo istogramma
data = df["temperature"]

plt.figure()
plt.hist(data, bins=len(temperature_possibili), color="skyblue")   #data sono l'insieme di numeri che voglio rappresentare, bins il num di colonne
plt.title('Istogramma delle temperature')
plt.xlabel('Temperatura (°c)')
plt.ylabel('Frequenza')
plt.text(27,40, "Min " + str(temp_min) + "°c", fontsize=9) #plt.text(x,y,"testo")
plt.text(21,60, "Max " + str(temp_max) + "°c", fontsize=9)
plt.text(27, 70, "Media: " + str(temp_mean) + "°C")
plt.text(27, 65, "Mediana: " + str(temp_median) + "°C")
plt.show()

#provo il grafico a linee
#crea un grafico a linee
#rivedi meglio!!