'''Esercizio Completo: Analisi Statistiche di Giocatori di Basket
Scenario
Sei un analista di una squadra di basket e vuoi studiare le prestazioni dei giocatori. Devi:
Creare classi per rappresentare giocatori e partite (OOP). fatto
Generare dati casuali di punti, rimbalzi e assist (NumPy).
Organizzare i dati in un DataFrame (Pandas).
Analizzare e filtrare i dati.(media punti per giocatore, valutazione media per giocatore, partite con piu di 10 punti e 10 rimbalzi
Visualizzare i risultati (Matplotlib / Seaborn)'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#classe Giocatore 
class Giocatore:
    def __init__(self, nome, ruolo):
        self.nome = nome
        self.ruolo = ruolo

#classe per le statistiche di una partita
class Partita:
    def __init__(self,giocatore,punti,rimbalzi,assist):
        self.giocatore = giocatore
        self.punti = punti
        self.rimbalzi = rimbalzi
        self.assist = assist 
        #per la valutazione ad esempio punti valgono 0.6, rimbalzi 0,2, assist 0.2
        self.valutazione = 0.6 * punti + 0.2 * rimbalzi + 0.2 * assist


#Generare dati casuali di punti, rimbalzi e assist (NumPy).
giocatori = ["Maria", "Martina","Agostina", "Carmen", "Sara"]
ruoli= ["Playmaker", "Guardia", "Shooter", "Ala", "Pivot"]


#genero dati casuali con numpy relativia alle statistiche delle partite di ogni singola giocatrice
np.random.seed(10)  #mantengo fisso la serie di numeri casuali generata ogni volta che eseguo il programma


#genero i dati random per 12 partite
player= np.random.choice(giocatori, 12)
player_ruolo = [ruoli[giocatori.index(nome)] for nome in player] #ruoli mappati per ogni giocatore
punti = np.random.randint(0, 38, 12)
rimbalzi = np.random.randint(0, 14, 12)
assist = np.random.randint(0, 12, 12)
peso_punti = 0.6
peso_rimbalzi = 0.2
peso_assist = 0.2
valutazione = peso_punti*punti + peso_assist*assist + peso_rimbalzi*rimbalzi


#creo il mio dataframe 
df = pd.DataFrame({
    "Giocatore": player,
    "Ruolo": player_ruolo,
    "Punti": punti,
    "Rimbalzi": rimbalzi,
    "Assist" : assist,
    "Valutazione" : valutazione
})

print(df)

#ANALISI DEI DATI

#punti medi per giocatore
punti_medi = df.groupby("Giocatore")["Punti"].mean()  #valori medi dei punti per ogni gioc
print("Punti medi per giocatore: ", punti_medi)

#valutazione media per giocatore
vautazione_media = df.groupby("Giocatore")["Valutazione"].mean()
print("la valutaizone media è: ", vautazione_media)

#seleziona le partite in cui il giocatore ha fatto una doppia doppia, piu di 10pts e piu di 10 rimbalzi 
partite_ottime = df[(df["Punti"] > 10) & (df["Rimbalzi"] > 10)]
print(partite_ottime)


#VISUALIZZAZIONE
# 1. Punti medi per giocatore
plt.figure(figsize=(8,5))
sns.barplot(x=punti_medi.index, y=punti_medi.values, palette="Blues_d")
plt.title("Punti medi per giocatore")
plt.ylabel("Punti medi")
plt.xlabel("Giocatore")
plt.show()

# 2. Valutazione media per giocatore
plt.figure(figsize=(8,5))
sns.barplot(x=vautazione_media.index, y=vautazione_media.values, palette="Greens_d")
plt.title("Valutazione media per giocatore")
plt.ylabel("Valutazione media")
plt.xlabel("Giocatore")
plt.show()




