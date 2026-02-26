'''
Pandas
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di vari attributi del cliente e la loro fedeltà.
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
* ID_Cliente: Identificativo unico per ogni cliente
* Età: Età del cliente
* Durata_Abbonamento: Quanti mesi il cliente è stato abbonato
* Tariffa_Mensile: Quanto il cliente paga al mese
* Dati_Consumati: GB di dati consumati al mese
* Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
* Churn: Se il cliente ha lasciato la compagnia (Si/No)
1. Caricamento e Esplorazione Iniziale:
* Caricare i dati da un file CSV.
* Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti.
2. Pulizia dei Dati:
 Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
* Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3. Analisi Esplorativa dei Dati (EDA):
* Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
* Utilizzare groupby( per esplorare la relazione tra Età, Durata_Abonnamento,
Tariffa_Mensile e la Churn.
* Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4. Preparazione dei Dati per la Modellazione:
* Convertire la colonna Churn in formato numerico (O per "No". 1 per "Si"). o Normalizzare Le colonne numeriche usando numpy per prepararle per la modellazione.

esercizio
possiamo generare dati, farli generare o generare dati fittizi.

'''

import pandas as pd
import numpy as np

np.random.seed(10) #utilizzo gli stessi numeri casuali

#faccio come nell'esercizio di ieri e mi creo un dataferame con le info casuali

#mi creo delle liste specifiche e poi in maniera random il programma sceglie da quelle
#eta
eta_clienti= [20,22,30,25,45,55,43,23,28,31,58]
tariffe_mensili = [15,25,30,35,50,60]
dati_GB = [20,40,50,35, 38,50]
churn = ["Si", "No"]
contatti_servizio_clienti = [1,2,3,4,5,6,7,8]
durata_abbonamento = [6,8,4,5,11,20,36]

#creo il dataframe usando np.random.choice  #con n.Clienti = 100
df = pd.DataFrame({
    "ID_Cliente" : range(1, 101),
    "Eta" : np.random.choice(eta_clienti, 100),
    "Tariffa_Mensile" : np.random.choice(tariffe_mensili, 100),
    "Dati_Consumati" : np.random.choice(dati_GB, 100),
    "Servizio_Clienti_Contatti" : np.random.choice(contatti_servizio_clienti, 100),
    "Churn" : np.random.choice(churn, 100, p=[0.3, 0.7]), #la probabilità che il cliente sceglie si è del 30% e no del 70%
    "Durata_Abbonamento" : np.random.choice(durata_abbonamento, 100)
})

print(df)

#1
#Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e 
print("Esaminiamo la distribuzione dei dati:")
print(df.info())  #info generali sul df
print(df.describe()) #statistiche descrittive
print(df["Churn"].value_counts())  #conteggio i valori della colonna churn

# identificare colonne con valori mancanti.
print("valori mancanti per colonna: ")
print(df.isnull().sum()) #df.isnull() crea un adf booleano: true se manca il valore. sum() somma lungo le righe e ci da il n um dei valori mancanti per colonna

#2 Pulizia dei Dati:
#Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
#Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

#Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
#gestione dei dati mancanti #rimuovi le righe con NaN
df_cleaned = df.dropna(axis=0, how='any', subset=None, inplace=False)
#ho aggiunto i parametri

'''
#o
#laddove ci sono sostituisco NAN con la media della colonna
df["Eta"].fillna(df["Eta"].mean(), inplace=True)
df["Tariffa_Mensile"].fillna(df["Tariffa_Mensile"].mean(), inplace=True)
df["Dati_Consumati"].fillna(df["Dati_Consumati"].median(), inplace=True)
df["Churn"].fillna("No", inplace=True)
'''

#Verificare e correggere eventuali anomalie nei dati 
# es. età negative, tariffe mensili irrealistiche
#eta negative

#mantengo solo le righe con eta possibile (così mi limito a quelle direttamente)
# Mantengo solo le righe con età plausibile (tra 1 e 100)
df = df[(df["Eta"] > 0) & (df["Eta"] <= 100)] #dal dataframe sto eliminando le eta negative o pari a zero & quelle maggiorni di 100

#3
# Analisi Esplorativa dei Dati (EDA):
#Creare nuove colonne che potrebbero essere utili, come Costo_per_GB 
# (tariffa mensile divisa per i dati consumati)

#creo nuove colonne - Costo_per_GB (tariffa mensile / dati consumati)
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]


#Utilizzare groupby( per esplorare la relazione tra Età, Durata_Abbonamento,Tariffa_Mensile e la Churn
#raggruppo i dati per colonna churn(si o no) e poi seleziono le colonne che voglio relazionare tra loro e calcolo la media per ogni colonna
relazione_churn = df.groupby("Churn")[["Eta", "Durata_Abbonamento", "Tariffa_Mensile"]].mean()
#stampo la tabella con le medie per ogni colonna relativamente al si e no del churn
print("tabella di analisi dati dove possiamo notare la relazione tra i vari dati: Età, Durata_Abbonamento,Tariffa_Mensile e la Churn: \n")
print(relazione_churn)

#Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
#devo prima convertire la colonna di churn(si o no) in numeri 
df["Churn_num"] = df["Churn"].replace({"No": 0, "Si": 1})

colonne_numeriche = ["Eta", "Durata_Abbonamento", "Tariffa_Mensile",
                     "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB", "Churn_num"]

possibili_correlazioni = df[colonne_numeriche].corr()
print("Correlazioni tra le variabili numeriche:\n", possibili_correlazioni)

#4.
#Preparazioen dei Dati per la modellazione:
#Convertire la colonna Churn in formato numerico (O per "No". 1 per "Si")
#Normalizzare Le colonne numeriche usando numpy per prepararle per la modellazione.

#converto Si e No di churn in valori numerici - con replace
df["Churn_num"] = df["Churn"].replace({"No": 0, "Si": 1})
print(df)

#Normalizzare Le colonne numeriche usando numpy per prepararle per la modellazione.
#normalizzazione std - Z-score = x - media /std
#in Numpy : seleziono prima le colonne che voglio normalizzare e poi applico il metodo per normalizzare i dati in queste colonne e poi stampo per verificare
#seleziono le colonne:
colonne_selezionate = ["Eta", "Durata_Abbonamento", "Tariffa_Mensile", "Dati_Consumati", "Servizio_Clienti_Contatti","Costo_per_GB"]

#normalizzo con la seguente sintassi di nunmpy: -prendo queste colonne e applico la formula dello z-score
df[colonne_selezionate] = (df[colonne_selezionate] - df[colonne_selezionate].mean()) / df[colonne_selezionate].std().round(2)  #arrotonda a due cifre decimali

print("dataframe con normalizzazione: \n")
print(df)

