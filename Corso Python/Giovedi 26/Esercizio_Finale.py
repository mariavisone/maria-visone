'''L'obiettivo di questo esercizio è generare un set di dati di serie temporali utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:
1. Generazione dei Dati: Utilizzare NumPy per generare una serie temporale di 365 giorni di dati, simulando il numero di visitatori giornalieri in un parco. 
Assumere che il numero medio di visitatori sia 2000 con una deviazione standard di 500. Inoltre, aggiungere un trend crescente nel tempo per simulare l'aumento della popolarità del parco.
2. Creazione del DataFrame: Creare un DataFrame pandas con Le date come indice e il numero di visitatori come colonna.
3. Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.
4. Visualizzazione dei Dati:
* Creare un grafico a linee del numero di visitatori giornalieri.
* Aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale.
* Creare un secondo grafico che mostri la media mensile dei visitatori.'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1. GENERAZIONE DEI DATI
np.random.seed(42)  #rendiamo fissi i numeri casuali quando rieseguiamo il codice

#genero numero di visitatori giornalieri per un anno
visitatori = np.random.normal(2000, 500, 365)  #(media, dev std, giorni)

#aggiungo trend fittizio per simnulare la crescita dei visitatori, anuuale 
#imposto l'incremento +400
trend = np.linspace(0,1000, 365)  # crea 365 numeri equidistanti, simula una crescita progressiva durante l’anno
visitatori_con_incremento = visitatori + trend
visitatori_con_incremento = np.round(visitatori_con_incremento).astype(int) #per trasformarlo in un numero intero

#2. CREA DATAFRAME
#genero l'indice di date annuale - crea una sequenza di date con data_range
date = pd.date_range(start="2025-01-01", periods=365, freq="D")

#Creo dataframe 
df = pd.DataFrame({
    "Visitatori": visitatori_con_incremento    #colonna
}, index= date)   #uso le date come indici

print(df)

#3.
#Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la deviazione standard.
#calcolo media visitatori per mese
media = df.groupby(df.index.month).mean().round(decimals=0)  #
dev_std = df.groupby(df.index.month).std().round(decimals=0)
print("La media di visitatori per mese: \n", media)
print("La deviazione standard è: \n", dev_std)

#4.
#Creare un grafico a linee del numero di visitatori giornalieri.
#mettiamo i due grafici affiancati per una migliore visualizzazioen dei dati

#creo una figura che contiene 2 sottografici ax1 e ax2
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,10))
#per aggiungere lo spazio verticale tra i 2 grafici
plt.subplots_adjust(hspace=0.4) 

#Grafico 1: Grafico dell' andamento con il trend dell'incremento annuale 
df['Media_Centrata'] = df['Visitatori'].rolling(window=7).mean()

ax1.plot(df.index, df['Visitatori'], label='Visitatori Giornalieri', alpha=0.4, color='steelblue')
ax1.plot(df.index, df['Media_Centrata'], label='Media Mobile 7gg', color='red', linewidth=2)
ax1.set_title('Andamento Giornaliero e Trend Settimanale')
ax1.set_ylabel('Numero Visitatori')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

#.strftime è una funzione che formatta le date in stringhe leggibili - %B indica il nome completo del mese 'January. February..
media_mensile = df['Visitatori'].resample('ME').mean()

ax2.bar(media_mensile.index.strftime('%B'), media_mensile.values, color='skyblue', edgecolor='navy')
ax2.set_title('Media Mensile dei Visitatori')
ax2.set_ylabel('Media Visitatori')
ax2.set_xlabel('Mese')
plt.xticks(rotation=45) # Ruota i nomi dei mesi per leggerli meglio
plt.show()