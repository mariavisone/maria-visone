'''Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite generato casualmente, 
applicando le tecniche di pivot e groupby.
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che include i seguenti campi:
 "Data", "Città", "Prodotto" e "Vendite". I dati devono essere generati per un periodo di un mese, 
 con vendite registrate per tre diverse città e tre tipi di prodotti.
1. Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.
2. Creazione della Tabella Pivot: Creare una tabella pivot per analizzare le vendite medie di ciascun prodotto per città.
3. Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare Le vendite totali per ogni prodott'''

import pandas as pd
import numpy as np


giorni = 1,3,5,6,7,8,12,15,18,19,30
citta = ['Napoli', 'Roma', 'Milano']
prodotti = ['iphone', 'pc', 'tablet']

# 
giorni_casuali = np.random.choice(giorni,30) 
citta_casuali = np.random.choice(citta, 30)
prodotti_casuali = np.random.choice(prodotti,30)
#genero vendite casuali
vendite_casuali = np.random.randint(5, 100)

#creo il dataframe
vendite_df = pd.DataFrame({
    'Giorno': giorni_casuali,
    'Citta': citta_casuali,
    'Prodotti': prodotti_casuali,
    'Vendite': vendite_casuali
})

print(vendite_df) #stampa il dataframe


#Creazione della Tabella Pivot: Creare una tabella pivot per analizzare le vendite medie di ciascun prodotto per città.

pivot_df = vendite_df.pivot_table(values='Vendite', index='Prodotti', columns= 'Citta', aggfunc='mean')
print(pivot_df)

#Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare Le vendite totali per ogni prodott'''
vendite_totali_prodotto = vendite_df.groupby('Prodotti')['Vendite'].sum()

print(vendite_totali_prodotto)





