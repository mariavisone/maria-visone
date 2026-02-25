'''Pandas
Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 

1. Caricare i dati in un DataFrame autogenerandoli casualmente .
2. Visualizzare le prime e le ultime cinque righe del DataFrame.
3. Visualizzare il tipo di dati di ciascuna colonna.
4. Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
5. Identificare e rimuovere eventuali duplicati.
6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
7. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
8. Salvare il DataFrame pulito in un nuovo file CSV '''

import pandas as pd
import numpy as np

#creo una lista di nomi
#creo una lista di età
#creo una lista di città
#poi creo un dizionario con random.choice prendendo nomi casuali dalla lista creata (almeno 20) e per l'età il random.randint da 18 a 75
#poi creo il dataframe

#lista nomi

nomi = ['Marco','Luca','Paola','Anastasia','Francesco','Gaia','Giovanni',
        'Maria', 'Davide', 'Carmen','Anna', 'Annahiara','Ilaria']
citta = ['Udine', 'Napoli', 'Roma', 'Parma', 'Torino', 'Milano', 'Latina', 'Fondi',
        'Caserta', 'Brescia', 'Como', 'Bari']

#creo il mio dizionario 
data = {
    'Nome': np.random.choice(nomi, 20), #mi da 20 nomi casuali tra quelli nella lista nomi
    'Eta': np.random.randint(18, 75, 20),
    'Citta' : np.ranodm.choice(citta, 20)
}
#lo trasmormo in dataframe
df = pd.DataFrame(data)
print("DataFrame originale: ")
print(df)

#2. Visualizzare le prime e le ultime cinque righe del DataFrame.
print("Ecco le prime 5 righe del DataFrame: ")
print(df.head(5))  #restituisce le prime 5 righe
print("Ecco le ultime 5 righe del DataFrame: ")
print(df.tail(5))  #restituisce le ultime 5 righe

#3. Visualizzare il tipo di dati di ciascuna colonna.
print("il tipo di dati di ciascuna colonna: ")
print(df.dtypes) #restituisce il tipo di dati per ogni colonna

#4. Calcolare statistiche descrittive di base per le colonne numeriche (media,
#mediana, deviazione standard).

#mi calcolo la media dell'età
media_eta = df['Età'].mean()
print("Media eta: ", media_eta)

#la mediana
mediana_eta = df['Eta'].median()
print("Mediana eta: ", mediana_eta)

#std
dev_std = df['Eta'].std()
print("Deviazione Standard: ", dev_std)

#5. Identificare e rimuovere eventuali duplicati.
# Rimozione dei duplicati
df = df.drop_duplicates()
print("Duplicati rimossi:")
print(df)

#66. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.



