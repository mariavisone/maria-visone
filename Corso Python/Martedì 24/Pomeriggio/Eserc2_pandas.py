'''Esercizio 2: Manipolazione e Aggregazione dei Dati
Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
1. Caricare i dati in un DataFrame.
2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
4. Trovare il prodotto più venduto in termini di Quantità.
5. Identificare la città con il maggior volume di vendite totali.
6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
8. Visualizzare il numero di vendite per ogni città.'''

import pandas as pd
import numpy as np

#creazione di un database come esercizio1 random


prodotti = ['Iphone','Powerbank','Tablet','Headphones','Piastra','pc','smartwatch']
citta = ['Udine', 'Napoli', 'Roma', 'Parma', 'Torino', 'Milano', 'Latina', 'Fondi']

#creo il mio dizionario 
data = {
    'Prodotto': np.random.choice(prodotti, 20),
    'Quantita': np.random.randint(2, 10, 20),
    'Citta' : np.random.choice(citta, 20),
    'Prezzo Unitario' : np.random.randint(100, 1500, 20)
}
#lo trasmormo in dataframe
df = pd.DataFrame(data)
print("DataFrame originale: ")
print(df)

#2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
#Quantità e Prezzo Unitario.
df['Totale Vendite'] = df['Quantita']*df['Prezzo Unitario']
print(df)

#3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
totale_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
print(totale_per_prodotto)

#4 Trovare il prodotto più venduto in termini di Quantità.
quantita_per_prodotto = df.groupby('Prodotto')['Quantita'].sum()
prodotto_più_venduto = quantita_per_prodotto.idmax()
print("Il prodotto piu venduto: " , prodotto_più_venduto, "con un numero di unità vendute pari a ", quantita_per_prodotto, "unita")

#5 Identificare la città con il maggior volume di vendite totali.
vendita_per_citta = df.groupby('Citta')['Totale Vendite'].sum()
citta_max = vendita_per_citta.idmax() #resittuisce come prima la città con e venite massime
totale_citta_max = vendita_per_citta.max()   #restituisce il valore massimo delle vendite di quella città
print("La citta con il maggior numero di vendite: ", citta_max, "con ", totale_citta_max, "vendite")

#6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 900 euro).
df_superior = df[df['Totale Vendite'] > 900] 

#7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.

df = df.sort_values(by='Totale Vendite', ascending= False)

#8. Visualizzare il numero di vendite per ogni città.
vendite_per_citta = df['Citta'].value_counts() #seleziona la colonna città, conta quante volte ogni città appare nel dataframe