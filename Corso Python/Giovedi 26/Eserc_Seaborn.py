'''Esercizio Medio: Normalizzazione dei Dati

Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.

Fornisci un codice che:
Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne altezza e peso.
Stampa sia il DataFrame originale sia quello modificato per compararli.'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#creo prima il dataframe
np.random.seed(10)  #numeri csuali fissi

altezza = np.random.randint(150,200, size=10)
peso = np.random.randint(45,100, size=10)
eta = np.random.randint(18, 79, size=10)

df = pd.DataFrame ({
    "altezza": altezza,
    "peso": peso,
    "eta": eta
})
print(df)   #dataframe creato

#-- NORMALIZZO min-max per altezza e peso

colonne_da_normalizzare = ["altezza", "peso"]                    
df_normalizzato = df.copy() #creo una copia del df originale
df_normalizzato[colonne_da_normalizzare]= df_normalizzato[colonne_da_normalizzare] = (df[colonne_da_normalizzare] - df[colonne_da_normalizzare].min()) / (df[colonne_da_normalizzare].max() - df[colonne_da_normalizzare].min())
print("DataFrame normalizzato (altezza e peco tra 0 e 1): \n")
print(df_normalizzato)
print("dataframe originale: ", df)


#PROVO AD AGGIUNGERE UN ISTOGRAMMA 
#della colonna alt normalizzata
plt.figure()
sns.histplot(data=df_normalizzato, x="altezza", bins=10)  #10 è il num di colonne
plt.title("Distribuzione Altezza Normalizzata")
plt.xlabel("Valori Normalizzati")
plt.ylabel("Frequenza")
plt.show()

#provo a fare l'istogramma della colonna altezza originale
plt.figure()
sns.histplot(data=df, x="altezza", bins=10)  #10 è il num di colonne
plt.title("Distribuzione Altezza Originale")
plt.xlabel("Valori Originali")
plt.ylabel("Frequenza")
plt.show()
