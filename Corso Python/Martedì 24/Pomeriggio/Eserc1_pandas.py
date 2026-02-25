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
    'Citta' : np.random.choice(citta, 20),
    'Salario' : np.random.randint(1000, 3000, 20)
}
#lo trasmormo in dataframe
df = pd.DataFrame(data)
print("DataFrame originale: ")
print(df)

#Inseriamo volutamente alcuni valori mancanti (NaN) per l'esercizio
df.loc[np.random.choice(df.index, size=3, replace=False), "Eta"] = np.nan
df.loc[np.random.choice(df.index, size=3, replace=False), "Salario"] = np.nan

#inserisco i duplicati
df = pd.concat([df,df.iloc[[0,1]]], ignore_index=True)

print("=== DataFrame generato (con NaN e duplicati) ===")
print(df)
print("\n" + "-"*60 + "\n")


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
media_eta = df['Eta'].mean()
print("Media eta: ", media_eta)

#la mediana
mediana_eta = df['Eta'].median()
print("Mediana eta: ", mediana_eta)

#std
dev_std = df['Eta'].std()
print("Deviazione Standard: ", dev_std)

# (OPZIONALE ma utile) pulizia nomi colonne df.columns = df.columns.str.strip()

# 5) DUPLICATI
duplicati = df[df.duplicated(keep=False)] # keep=False mostra tutti i duplicati (non solo le copie)
print("Righe duplicate prima della rimozione:")
print(duplicati)

df = df.drop_duplicates() # evita inplace, più pulito
print("\nDataFrame dopo rimozione duplicati:")
print(df)

# 6) VALORI MANCANTI con MEDIANA (assicurati che siano numeri)
# Converte a numerico: se trova testo/sporcizia -> NaN (così poi la mediana ha senso)
df["Eta"] = pd.to_numeric(df["Eta"], errors="coerce")
df["Salario"] = pd.to_numeric(df["Salario"], errors="coerce")

# Calcola mediane (saltando automaticamente i NaN)
med_eta = df["Eta"].median()
med_sal = df["Salario"].median()

# Riempie i NaN assegnando la serie risultante (niente inplace)
df["Eta"] = df["Eta"].fillna(med_eta)
df["Salario"] = df["Salario"].fillna(med_sal)

print("\nDataFrame dopo fillna con mediana:")
print(df)

# Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
#persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni:
#Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

#definisco una funz che prende l'età e mi restituisce una categoria
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

#8. Salvare il DataFrame pulito in un nuovo file CSV '''
#prendo la colonna età e creo una funzione con .apply e applico la funz a ogni riga della colonna
df["Categoria Eta"] = df["Eta"].apply(categoria_eta)
print(df)

#salvo su file csv index = False
df.to_csv("dati_puliti.csv", index= False)
print("DataFrame salvato correttamente in dati_puliti.csv")

