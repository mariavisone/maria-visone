'''👤 Per Maria (Path 1: Biologia e Deep Learning)

**Domanda:** "Perché hai scelto la funzione di attivazione `sigmoid` nell'ultimo strato e non la `softmax`?"
* **Risposta Pro:** "Questa è una classificazione **Multi-Label**, non Multi-Class. 
Un farmaco può avere più Meccanismi d'Azione (MoA) contemporaneamente. 
La `softmax` costringe la somma delle probabilità a 1 (una sola risposta giusta), 
mentre la `sigmoid` permette a ogni neurone di dare una probabilità indipendente tra 0 e 1."

**Domanda:** "A cosa serve il `Dropout(0.3)` che hai inserito tra gli strati?"
* **Risposta Pro:** "È una tecnica di regolarizzazione per contrastare l'**Overfitting**. 
Durante l'addestramento, 'spegniamo' casualmente il 30% dei neuroni. 
Questo impedisce alla rete di memorizzare i dati a memoria e 
la costringe a imparare pattern generali, 
migliorando la capacità del modello di rispondere a dati nuovi."

👤 Speaker 2: Maria (Path 1: Biological MoA)
**Celle di riferimento nel Notebook:** [5] - [11]

* **Cella [5]:** Preprocessing (filtro `ctl_vehicle` e `QuantileTransformer`).
* **Cella [6]:** Architettura della Rete Neurale (Multi-Layer Perceptron).
* **Cella [9-11]:** Training del modello e grafici della Loss e dell'AUC.
* **Cosa dire:** "Seguendo il Path 1, ho lavorato sulle celle dalla 5 alla 11.
 Ho normalizzato i dati genetici e costruito una rete neurale multi-label.
Come potete vedere dai grafici (Cella 11), 
il modello impara correttamente a distinguere i meccanismi d'azione biologici.


# DualPath-MedAI
---
## Link utili DataSet

1. [Link Dataset Mechanisms of Action (MoA) Prediction](https://www.kaggle.com/c/lish-moa/data)
2. [Link Dataset Drugs, Side_Effects & Medical_Conditions](https://www.kaggle.com/datasets/nailasrivastava/drugs-side-effects-and-medical-conditions)
---
## 🧬 Documentazione Dataset: Mechanisms of Action (MoA)

Il dataset MoA è strutturato in due matrici principali: le **features** (dati di input) e i **targets** (output da predire). Essendo dati anonimizzati, la seguente mappatura è fondamentale per le fasi di preprocessing e feature engineering.

### 1. File: `train_features.csv` (Variabili Indipendenti)
Questa matrice contiene i parametri del test e le misurazioni biologiche su cui il modello neurale cercherà i pattern.

* **`sig_id`**: Identificativo univoco del campione testato.
* **`cp_type`**: Tipo di trattamento.
    * `trt_cp`: Farmaco reale.
    * `ctl_vehicle`: Sostanza di controllo neutra (solvente). *Nota: queste righe vanno rimosse durante il cleaning poiché non attivano alcun meccanismo d'azione.*
* **`cp_time`**: Durata dell'esposizione al trattamento in ore (valori possibili: 24, 48, 72).
* **`cp_dose`**: Dosaggio somministrato (basso = `D1`, alto = `D2`).
* **`g-[0-771]`**: 772 feature continue. Misurano l'**espressione genica** (come hanno reagito i geni al farmaco).
* **`c-[0-99]`**: 100 feature continue. Misurano la **vitalità cellulare** (percentuale di cellule sopravvissute).

---

### 2. File: `train_targets_scored.csv` (Variabili Dipendenti)
Queste sono le etichette di ground truth per l'addestramento supervisionato.

* **`sig_id`**: Chiave primaria per il join con le features.
* **206 Colonne Target**: Ognuna rappresenta un distinto Meccanismo d'Azione biologico. I valori sono strettamente binari:
    * `1`: Il farmaco ha attivato il meccanismo.
    * `0`: Nessuna attivazione.
---
---
## Iniziamo
- carichiamo i file principali con Pandas e verifichiamo la corretta lettura
---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold
# 1. Carichiamo i file principali di training
moa_train = pd.read_csv('data/moa/train_features.csv')
targets = pd.read_csv('data/moa/train_targets_scored.csv')

# (Sostituisci il nome del file clinico se diverso da quello estratto)
clinical_data = pd.read_csv('data/clinical/drugs_side_effects_drugs_com.csv')

# 2. Stampiamo le dimensioni (righe, colonne)
print(f"Dimensioni MoA (Features): {moa_train.shape}")
print(f"Dimensioni MoA (Target): {targets.shape}")
print(f"Dimensioni Dati Clinici: {clinical_data.shape}")
print("\n", "*" * 50)

# 3. Guardiamo le prime 3 righe per capire la struttura
display(moa_train.head(3))
# Controlliamo tramite info e describe
print("Moa Dataset:\n")
moa_train.info()
print("\n", "*" * 50)
display(moa_train.describe())
print("\n", "*" * 50)

# Controllo valori nulli e tipi di dato nel dataset clinico
print("Valori mancanti per colonna nel dataset clinico:")
display(clinical_data.isnull().sum())
print("\n", "*" * 50)

print("\nTipi di dato:")
display(clinical_data.dtypes)
print("\n", "*" * 50)
---
### Cerchiamo sig_id
---
#sig_id search
display(moa_train.head(3))
print("\n", "*" * 50)
---
### Creiamo delle liste per isolare le features per tipologia
---
# Creiamo delle liste per isolare le features per tipologia
gene_features = [col for col in moa_train.columns if col.startswith('g-')]
cell_features = [col for col in moa_train.columns if col.startswith('c-')]
cat_features = ['cp_type', 'cp_time', 'cp_dose']

display(f"Totale feature Geniche (g-): {len(gene_features)}")
display(f"Totale feature Cellulari (c-): {len(cell_features)}")
print("\n--- Valori Categorici ---")
display(f"Tipi di trattamento (cp_type): {moa_train['cp_type'].unique()}")
display(f"Tempi di esposizione (cp_time): {moa_train['cp_time'].unique()}")
display(f"Dosaggi (cp_dose): {moa_train['cp_dose'].unique()}")
print("\n", "*" * 50)
---
### Ipotetica normalizzazione
- filtraggio cp_type == ctl
_vehicole
---
# filtriamo cp_type
print('Shape prima del filtro:',moa_train.shape)

moa_train = moa_train[moa_train['cp_type'] == 'trt_cp']

print('Shape dopo il filtro:',moa_train.shape)
print("Valori cp_type dopo il filtro:", moa_train['cp_type'].unique())
print(f"Tempi di esposizione (cp_time): {moa_train['cp_time'].unique()}")
print("\n", "*" * 50)
---
- drop della colonna dopo il filtraggio perché adesso sappiamo che ormai sono tutti `cp_type == 'trt_cp'`
---
# droppiamo la colonna
moa_train = moa_train.drop(columns=['cp_type'])
display(moa_train.head(3))
print("\n", "*" * 50)
display(moa_train.info())
print("\n", "*" * 50)
display(moa_train.dtypes)
print("\n", "*" * 50)
---
### Merge del dataframe targets
---
#join tra i dui dataframe per escludere gli stessi record di cp_type
targets = targets[targets['sig_id'].isin(moa_train['sig_id'])]

# controllo per il check di confronto
display(moa_train.shape, targets.shape)
print("\n", "*" * 50)

# merge
data = moa_train.merge(targets, on='sig_id')

# lettura di data
display(data.shape)
print("\n", "*" * 50)
---
### Plot e controllo visivo per controllo della distribuzione quindi standardizzazione
- g-0 g-1
- c-0 c-1
---
# Selezioniamo 2 feature geniche e 2 cellulari a caso per il plot
features_to_plot = ['g-0', 'g-1', 'c-0', 'c-1']

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for i, col in enumerate(features_to_plot):
    ax = axes[i//2, i%2]
    # Usiamo seaborn per un istogramma con la curva di densità (KDE)
    sns.histplot(data[col], bins=50, kde=True, ax=ax, color='teal')
    ax.set_title(f'Distribuzione di {col}')

plt.tight_layout()
plt.show()
---
### Trasformazione in numeri `cp_dose` e `cp_time`

1. `cp_dose`: è binaria (D1, D2). La mappiamo in 0 e 1.
  - `D1 = 0`: dose bassa
  - `D2 = 1`: dose alta
2. `cp_time`: contiene ore (24, 48, 72). Possiamo semplicemente dividerla per 72 per scalarla proporzionalmente tra 0 e 1
---
# 1. Mappatura binaria per la dose
data['cp_dose'] = data['cp_dose'].map({'D1': 0, 'D2': 1})

# 2. Scaliamo il tempo di esposizione tra 0 e 1
data['cp_time'] = data['cp_time'] / 72.0

# Check visivo del risultato
display(data[['cp_time', 'cp_dose']].head())
---
### Controllo valori nulli e set `sig_id` come id del dataset
---
# 1. Controllo finale e assoluto sui valori mancanti
print(f"Totale valori nulli nel dataset MoA unito: {data.isnull().sum().sum()}")

# 2. Spostiamo sig_id come indice del DataFrame
data = data.set_index('sig_id')

# Verifica finale della struttura
display(data.head(3))
---
## 🧠 Architettura del Modello: Separazione tra X (Features) e Y (Targets)

In ogni progetto di Machine Learning supervisionato, il dataset deve essere concettualmente e strutturalmente diviso in due matrici principali prima dell'addestramento o della selezione delle variabili:

* **X (Le Features / Input):** Rappresentano gli "indizi" o le variabili indipendenti. Nel nostro progetto MoA, queste sono l'espressione genica (`g-`), la vitalità cellulare (`c-`), il tempo di esposizione e la dose. Sono i dati puri che il modello analizzerà per scovare dei pattern.
* **Y (I Targets / Output):** Rappresentano le "soluzioni" o la variabile dipendente (ground truth). Nel nostro caso, sono le 206 colonne dei Meccanismi d'Azione. È esattamente ciò che la rete neurale deve imparare a predire.

### ⚠️ Perché applicare VarianceThreshold SOLO sulle Features (X)?
Il `VarianceThreshold` è un filtro che rimuove le colonne con una varianza vicina allo zero (ovvero dati "piatti" che non cambiano quasi mai e non offrono potere predittivo).

I nostri Target (**Y**) sono matrici sparse composte quasi interamente da zeri, poiché l'attivazione di un farmaco per un meccanismo specifico è un evento biologicamente raro. Se applicassimo il filtro sull'intero dataset unito, l'algoritmo eliminerebbe per errore le colonne dei Target scambiandole per "dati inutili", distruggendo l'obiettivo del progetto.

**Regola d'oro:** Le tecniche di riduzione della dimensionalità si applicano sempre e solo alla matrice **X**.

---
from sklearn.feature_selection import VarianceThreshold

# 1. Isolare X (features) e Y (targets) per non distruggere le etichette
target_cols = [col for col in targets.columns if col != 'sig_id']
feature_cols = [col for col in data.columns if col not in target_cols]

X = data[feature_cols]
Y = data[target_cols]

# Feature engineering biologico
# Calcoliamo tutto in blocco per evitare PerformanceWarning
feat_engineered = pd.DataFrame({
    "g_mean": X[gene_features].mean(axis=1),
    "g_std": X[gene_features].std(axis=1),
    "c_mean": X[cell_features].mean(axis=1),
    "c_std": X[cell_features].std(axis=1),
})
feat_engineered["gc_ratio"] = feat_engineered["g_mean"] / (feat_engineered["c_mean"] + 1e-6)

# Interaction biologiche
# gxc_mean = attivazione gene × risposta cellulare:
feat_engineered["gxc_mean"] = X[gene_features].mean(axis=1) * X[cell_features].mean(axis=1)
# gxc_std = variazione biologica combinata
feat_engineered["gxc_std"] = X[gene_features].std(axis=1) * X[cell_features].std(axis=1)

# stress cellulare stimato
# cell_stress = dispersione vitalità cellule
feat_engineered["cell_stress"] = feat_engineered["c_std"] / (feat_engineered["c_mean"] + 1e-6)

# gene_activation = attivazione genica relativa
feat_engineered["gene_activation"] = feat_engineered["g_std"] / (feat_engineered["g_mean"] + 1e-6)

# Unione features originali + ingegnerizzate
X_final = pd.concat([X, feat_engineered], axis=1)

print("Shape features dopo feature engineering:", X_final.shape)

# 2. Inizializzare il selettore (0.01 significa scartare feature quasi costanti al 99%)
selector = VarianceThreshold(threshold=0.01)

# 3. Fit e transform, ma ricostruiamo il DataFrame per non perdere i nomi delle colonne
X_reduced = selector.fit_transform(X_final)
X_reduced_df = pd.DataFrame(X_reduced,
                            columns=X_final.columns[selector.get_support()],
                            index=X_final.index)

print(f"Features originali: {X.shape[1]}")
print(f"Features mantenute: {X_reduced_df.shape[1]}")
print(f"Features scartate per bassa varianza: {X.shape[1] - X_reduced_df.shape[1]}")
### visualizzazione del plot
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Calcoliamo la varianza per ogni singola feature in X
variances = X_final.var()

# 2. Creiamo l'istogramma delle varianze
plt.figure(figsize=(10, 5))
sns.histplot(variances, bins=100, kde=True, color='indigo')

# 3. Tracciamo la nostra soglia di taglio (0.01)
plt.axvline(x=0.01, color='red', linestyle='--', label='Soglia (Threshold = 0.01)')

plt.title('Distribuzione della Varianza nelle Features (X)')
plt.xlabel('Varianza')
plt.ylabel('Frequenza (Numero di Features)')
plt.legend()
plt.tight_layout()
plt.show()
## MultilabelStratifiedKFold
Invece dello split facciamo il Multilabel Stratified Split per mantenere la stessa distribuzione dei target in ciascun fold.
Divide cioè il dataset in 5 fold in cui cerca di mantenere la stessa distribuzione di target positivi.
mskf = MultilabelStratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

for train_idx, val_idx in mskf.split(X_reduced_df, Y):

    X_train = X_reduced_df.iloc[train_idx]
    X_val = X_reduced_df.iloc[val_idx]

    Y_train = Y.iloc[train_idx]
    Y_val = Y.iloc[val_idx]

    break # Serve a usare solo il primo fold come validazione

print("Train shape:", X_train.shape)
print("Validation shape:", X_val.shape)

## Standardizzazione delle Feature (StandardScaler)

Prima di addestrare i modelli di Machine Learning è utile normalizzare le variabili.  
Nel nostro dataset le feature (espressione genica e cellulare) possono avere scale molto diverse.

Per questo utilizziamo **StandardScaler**, che trasforma ogni variabile in modo che abbia:

- media = 0
- deviazione standard = 1

La trasformazione applicata è:
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_val_scaled = pd.DataFrame(
    X_val_scaled,
    columns=X_val.columns,
    index=X_val.index
)

print("Shape dopo scaling:", X_train_scaled.shape)
## Riduzione della Dimensionalità con PCA

Il dataset contiene centinaia di feature biologiche (geni e cellule), molte delle quali sono correlate tra loro.

Per ridurre la dimensionalità e il rumore nei dati utilizziamo **Principal Component Analysis (PCA)**.

La PCA:

- combina le feature originali in nuove variabili chiamate **componenti principali**
- mantiene la maggior parte della varianza dei dati
- riduce il numero di variabili da analizzare

Nel nostro caso riduciamo le feature a **200 componenti principali**, mantenendo la maggior parte dell'informazione utile per il modello.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 1. Recuperiamo TUTTE le feature che sono sopravvissute ai filtri precedenti
surviving_cols = X_train_scaled.columns.tolist()

# 2. Definiamo quali NON sono continue (quelle da escludere dalla PCA)
other_features = ['cp_time', 'cp_dose']

# 3. Le feature continue sono semplicemente tutte le rimanenti!
continuous_features = [col for col in surviving_cols if col not in other_features]

# PCA solo sulle feature continue
pca = PCA(n_components=200, random_state=42)

# Fit PCA sul train
X_train_continuous = X_train_scaled[continuous_features]
X_val_continuous = X_val_scaled[continuous_features]

X_train_pca = pca.fit_transform(X_train_continuous)
X_val_pca = pca.transform(X_val_continuous)

# Ricostruiamo DataFrame PCA con colonne nominate
X_train_pca_df = pd.DataFrame(X_train_pca, index=X_train.index)
X_val_pca_df = pd.DataFrame(X_val_pca, index=X_val.index)

X_train_pca_df.columns = [f"PC{i}" for i in range(X_train_pca_df.shape[1])]
X_val_pca_df.columns = X_train_pca_df.columns

# Uniamo i dati PCA con le feature non continue ('cp_time', 'cp_dose')
X_train_final = pd.concat([X_train_pca_df, X_train[other_features]], axis=1)
X_val_final = pd.concat([X_val_pca_df, X_val[other_features]], axis=1)

# Controllo shape per confermare l'allineamento
print("X_train_final shape:", X_train_final.shape, "| Y_train shape:", Y_train.shape)
print("X_val_final shape:", X_val_final.shape, "| Y_val shape:", Y_val.shape)

# Grafico varianza spiegata
plt.figure(figsize=(8,5))
plt.plot(np.cumsum(pca.explained_variance_ratio_), color='#00bfa5', linewidth=2)
plt.xlabel("Numero componenti")
plt.ylabel("Varianza spiegata cumulativa")
plt.title("Varianza spiegata dalla PCA")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Dataset finale
final_train = pd.concat([X_train_final, Y_train], axis=1)
final_val = pd.concat([X_val_final, Y_val], axis=1)

print("Shape train dataset:", final_train.shape)
print("Shape validation dataset:", final_val.shape)
---
#### Esportazione del DataFrame pulito e normalizzato
---

# 4. Ricongiungiamo X pulita e Y per il salvataggio finale
final_data = pd.concat([X_train_pca_df, Y_train], axis=1)

# Esportazione del DataFrame pulito e normalizzato
final_data.to_csv('data/new_data/moa/moa_ready.csv', index=False)
print("Dataset MoA pronto e salvato in: data/new_data/moa/moa_ready.csv")
### Dobbiamo costruire una rete neurale in grado di prevedere non una, ma ben 206 probabilità diverse contemporaneamente.

Il primissimo passo è ricaricare il nostro dataset definitivo e preparare i tensori per Keras, dividendo i dati in un set di addestramento e uno di validazione.
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import json
from sklearn.model_selection import train_test_split

# 1. Carichiamo il dataset pulito
data = pd.read_csv('data/new_data/moa/moa_ready.csv')

# 1. Feature (tutte tranne le ultime 206)
feature_cols = data.iloc[:, :-206].columns.tolist()
with open('feature_cols.json', 'w') as f:
    json.dump(feature_cols, f)

# 2. Target (le ultime 206)
target_labels = data.iloc[:, -206:].columns.tolist()
with open('target_labels.json', 'w') as f:
    json.dump(target_labels, f)

print(f"JSON Generati! Features: {len(feature_cols)} | Targets: {len(target_labels)}")

# 2. Separiamo X e Y (sappiamo che i target sono le ultime 206 colonne)
X = data.iloc[:, :-206].values
Y = data.iloc[:, -206:].values

X_train, X_val, Y_train, Y_val = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print(f"Training Features (X_train): {X_train.shape}")
print(f"Training Targets (Y_train): {Y_train.shape}")

print("\n", "*" * 50)

print(f"TensorFlow Version: {tf.__version__}")
print(f"Shape delle Features (X): {X.shape}")
print(f"Shape dei Target (Y): {Y.shape}")
## 🔗 Integrazione Dati: Il Ponte verso i Farmaci (train_drug.csv)

Il file `train_drug.csv` contiene la mappatura tra gli esperimenti e le molecole.
Carichiamo questo dataset per esaminare come associare i nostri dati attuali (`sig_id`) ai farmaci (`drug_id`). Questa operazione è propedeutica per il successivo *merge* con i dati clinici avanzati.
# 1. Carichiamo la mappatura dei farmaci di Kaggle
drugs_moa = pd.read_csv('data/moa/train_drug.csv')

# 2. Stampiamo le info essenziali
print(f"Dimensioni mappatura farmaci: {drugs_moa.shape}")
print(f"Numero di farmaci unici: {drugs_moa['drug_id'].nunique()}")
display(drugs_moa.head())
## 🧬 Data Merging: Associazione Esperimenti-Farmaci

Eseguiamo una `Left Join` per unire le feature di addestramento (`train_features.csv`) con i codici dei farmaci (`train_drug.csv`). 
La chiave di unione è `sig_id` (l'identificativo univoco dell'esperimento). Questo passaggio è fondamentale per raggruppare le reazioni biologiche per singola molecola prima di introdurre il dataset clinico.
# 1. Ricarichiamo le features originali di training
train_features = pd.read_csv('data/moa/train_features.csv')

# 2. Eseguiamo il merge (Left Join) basato sulla colonna 'sig_id'
train_features_with_drugs = pd.merge(train_features, drugs_moa, on='sig_id', how='left')

# 3. Verifica strutturale
print(f"Dimensioni features originali: {train_features.shape}")
print(f"Dimensioni dopo il merge: {train_features_with_drugs.shape}")
display(train_features_with_drugs[['sig_id', 'drug_id']].head())
### Addestramento Neural Network con Keras Sequential
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
import joblib

# 1. LA SOLUZIONE NUCLEARE: Rileggiamo i target dal file originale su disco
# Così bypassiamo qualsiasi variabile sovrascritta o corrotta in memoria.
targets_df = pd.read_csv('data/moa/train_targets_scored.csv')
targets_df = targets_df.set_index('sig_id')

# Usiamo i nostri dati di input scalati (che hanno mantenuto gli indici sig_id corretti)
X_train_nn = X_train_scaled
X_val_nn = X_val_scaled

# Peschiamo i target esatti allineati riga per riga con le X
Y_train_nn = targets_df.loc[X_train_nn.index]
Y_val_nn = targets_df.loc[X_val_nn.index]

print(f"Shape perfettamente allineate! X_train: {X_train_nn.shape} | Y_train: {Y_train_nn.shape}")

# 2. Definizione dell'architettura Multi-Label
model = keras.Sequential([
    layers.Input(shape=(X_train_nn.shape[1],)),
    
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(256, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    # Output Layer (206 nodi, attivazione sigmoid)
    layers.Dense(206, activation='sigmoid') 
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['AUC'])

early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

print("Avvio addestramento Rete Neurale MoA...")
history = model.fit(
    X_train_nn, Y_train_nn,
    validation_data=(X_val_nn, Y_val_nn),
    epochs=50,
    batch_size=128,
    callbacks=[early_stop]
)

# 3. Valutazione
val_loss, val_auc = model.evaluate(X_val_nn, Y_val_nn)
print(f"Validation Loss: {val_loss}")
print(f"Validation AUC: {val_auc}")

# 4. Salvataggio definitivo per Streamlit
model.save("moa_model.h5")
joblib.dump(scaler, "moa_scaler.pkl")

print("Modello (moa_model.h5) e Scaler salvati!")
## Visualizzazioni delle metriche di training:
1. Training vs Validation Loss → vedi se il modello sta overfittando (val_loss sale mentre loss scende).

2. Training vs Validation AUC → quanto bene il modello distingue i target positivi dai negativi nel tempo.
### Commento rapido del grafico di training

Il grafico mostra un andamento **positivo e stabile** del modello:

- **Loss (sinistra):** la `training loss` cala rapidamente e poi si appiattisce; la `validation loss` segue lo stesso trend e resta vicina.  
    ➜ Segnale di buona convergenza, con overfitting contenuto.

- **AUC (destra):** sia `training AUC` che `validation AUC` crescono in modo regolare fino a ~0.80, con gap ridotto tra le due curve.  
    ➜ Il modello sta imparando pattern utili e mantiene una buona capacità di generalizzazione.

**Sintesi:** training efficace, miglioramento progressivo e nessuna divergenza critica tra train e validation.

import matplotlib.pyplot as plt

# 1. Recupero dinamico e sicuro delle chiavi metriche (ignora maiuscole/minuscole e suffissi)
auc_key = [k for k in history.history.keys() if 'auc' in k.lower() and 'val' not in k.lower()][0]
val_auc_key = [k for k in history.history.keys() if 'auc' in k.lower() and 'val' in k.lower()][0]

loss = history.history['loss']
val_loss = history.history['val_loss']
auc = history.history[auc_key]
val_auc = history.history[val_auc_key]

epochs = range(1, len(loss) + 1)

# 2. Configurazione visiva avanzata del plot
plt.figure(figsize=(14, 6))

# Plot Loss
plt.subplot(1, 2, 1)
plt.plot(epochs, loss, color='#00bfa5', linewidth=2.5, label='Training Loss')
plt.plot(epochs, val_loss, color='#ff5252', linewidth=2.5, linestyle='--', label='Validation Loss')
plt.title('Loss nel Training (Binary Crossentropy)', fontsize=14, pad=15)
plt.xlabel('Epoche', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)

# Plot AUC
plt.subplot(1, 2, 2)
plt.plot(epochs, auc, color='#00bfa5', linewidth=2.5, label='Training AUC')
plt.plot(epochs, val_auc, color='#ff5252', linewidth=2.5, linestyle='--', label='Validation AUC')
plt.title('AUC nel Training (Area Under Curve)', fontsize=14, pad=15)
plt.xlabel('Epoche', fontsize=12)
plt.ylabel('AUC', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()
## Training XGBoost model
import xgboost as xgb
import numpy as np
import joblib
from sklearn.metrics import roc_auc_score
from tqdm import tqdm

print("\nTraining XGBoost models...")

xgb_models = []

# Loop sui 206 target usando le Y blindate (Y_train_nn)
for i in tqdm(range(Y_train_nn.shape[1])):

    model = xgb.XGBClassifier(
        n_estimators=400,
        learning_rate=0.05,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        eval_metric='auc',
        tree_method='hist',
        n_jobs=-1
    )

    # Usiamo direttamente X_train_final (che è già un DataFrame)
    # ed estraiamo la i-esima colonna da Y_train_nn
    model.fit(
        X_train_final,
        Y_train_nn.iloc[:, i],
        eval_set=[(X_val_final, Y_val_nn.iloc[:, i])],
        verbose=False
    )

    xgb_models.append(model)

print(f"\nAddestrati {len(xgb_models)} modelli XGBoost!")

# Salvataggio modelli
joblib.dump(xgb_models, "xgb_206_models.pkl")

print("Modelli XGBoost salvati!")
## Plot di visualizzazione delle performance di tutti i 206 modelli XGBoost:
- Calcola l’AUC per ciascun target usando le predizioni del modello corrispondente.
- Salva tutte le AUC in auc_list.
- Bar plot: ogni target come barra con la sua AUC.
- Istogramma: distribuzione generale delle AUC tra tutti i target.
- Stampa la media AUC, ignorando i target rari che non hanno entrambe le classi.
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import numpy as np

# Array per salvare le AUC di tutti i target
auc_list = []

# Loop sui 206 modelli
for i, model in enumerate(xgb_models):
    # Predizione probabilità classe positiva
    y_pred = model.predict_proba(X_val_final)[:, 1]

    # Usiamo i target blindati e allineati!
    target_true = Y_val_nn.iloc[:, i]
    
    # Calcolo AUC solo se il target ha almeno due classi
    if len(np.unique(target_true)) > 1:
        auc = roc_auc_score(target_true, y_pred)
        auc_list.append(auc)
    else:
        auc_list.append(np.nan)

# Convertiamo in array numpy per comodità
auc_array = np.array(auc_list)
mean_auc = np.nanmean(auc_array)

# --- PLOT 1: AUC per target ---
plt.figure(figsize=(14, 6))
plt.bar(range(len(auc_array)), auc_array, color='#48cae4', alpha=0.9)
plt.axhline(y=mean_auc, color='#ff5252', linestyle='--', linewidth=2, label=f'Media AUC: {mean_auc:.4f}')
plt.xlabel("Target Index (0-205)", fontsize=12)
plt.ylabel("AUC Score", fontsize=12)
plt.title("Performance (AUC) per ciascun Target XGBoost", fontsize=14, pad=15)
plt.ylim(0.5, 1.0)
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

# --- PLOT 2: Distribuzione delle AUC ---
plt.figure(figsize=(10, 5))
plt.hist(auc_array[~np.isnan(auc_array)], bins=25, color='#00bfa5', edgecolor='black')
plt.axvline(x=mean_auc, color='#ff5252', linestyle='--', linewidth=2, label=f'Media: {mean_auc:.4f}')
plt.xlabel("Valore AUC", fontsize=12)
plt.ylabel("Frequenza (Numero di Target)", fontsize=12)
plt.title("Distribuzione delle AUC sui 206 Target MoA", fontsize=14, pad=15)
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print(f"AUC medio XGBoost su tutti i target validi: {mean_auc:.4f}")
## Addestramento modello LightGBM
import lightgbm as lgb
import joblib
from tqdm import tqdm

print("Training LightGBM models...")

lgb_models = []

for i in tqdm(range(Y_train_nn.shape[1])):  # 206 target
    model = lgb.LGBMClassifier(
        n_estimators=400,
        learning_rate=0.05,
        max_depth=8,
        subsample=0.8,
        colsample_bytree=0.8,
        n_jobs=-1
    )
    # Usiamo le variabili blindate e allineate
    model.fit(X_train_final, Y_train_nn.iloc[:, i])
    lgb_models.append(model)

joblib.dump(lgb_models, "lgb_206_models.pkl")
print("Modelli LightGBM MoA salvati!")
## Training LightGBM model
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
import joblib

estimators = joblib.load('lgb_206_models.pkl')
print(f"Caricati {len(estimators)} modelli LightGBM.")

# Usiamo la shape corretta
Y_pred = np.zeros_like(Y_val_nn, dtype=float)

for i, clf in enumerate(estimators):
    Y_pred[:, i] = clf.predict_proba(X_val_final)[:, 1]

auc_list = []

for i in range(Y_val_nn.shape[1]):
    # Estraiamo il target corretto
    target_true = Y_val_nn.iloc[:, i]
    
    if len(np.unique(target_true)) > 1:
        auc = roc_auc_score(target_true, Y_pred[:, i])
        auc_list.append(auc)
    else:
        auc_list.append(np.nan)

mean_auc = np.nanmean(auc_list)

print(f"AUC medio LightGBM (solo target validi): {mean_auc:.4f}")
print(f"Numero di target considerati: {np.sum(~np.isnan(auc_list))}/{Y_val_nn.shape[1]}")
## Valutazione del modello XGBoost
import numpy as np
from sklearn.metrics import roc_auc_score

# Array predizioni con la shape corretta e allineata
Y_pred = np.zeros_like(Y_val_nn, dtype=float)

# Usiamo X_val_final che è già un DataFrame pronto
for i, model in enumerate(xgb_models):
    Y_pred[:, i] = model.predict_proba(X_val_final)[:, 1]

# Calcolo AUC per ogni target
auc_list = []

for i in range(Y_val_nn.shape[1]):
    # Estraiamo il target corretto in modo blindato
    target_true = Y_val_nn.iloc[:, i]

    if len(np.unique(target_true)) > 1:
        auc = roc_auc_score(target_true, Y_pred[:, i])
        auc_list.append(auc)
    else:
        auc_list.append(np.nan)

mean_auc = np.nanmean(auc_list)

print(f"AUC medio XGBoost: {mean_auc:.4f}")
print(f"Target valutati: {np.sum(~np.isnan(auc_list))}/{Y_val_nn.shape[1]}")
### Plot XGBoost
import matplotlib.pyplot as plt
import numpy as np

# Convertiamo la lista calcolata nel blocco precedente in array
auc_array = np.array(auc_list)
mean_auc = np.nanmean(auc_array)

# --- PLOT 1: AUC per ogni target ---
plt.figure(figsize=(14, 6))
plt.bar(range(len(auc_array)), auc_array, color='#48cae4', alpha=0.9)
plt.axhline(y=mean_auc, color='#ff5252', linestyle='--', linewidth=2, label=f'Media AUC: {mean_auc:.4f}')
plt.xlabel("Indice Target (0-205)", fontsize=12)
plt.ylabel("AUC Score", fontsize=12)
plt.title("Performance (AUC) per ciascun Target", fontsize=14, pad=15)
plt.ylim(0.5, 1.0)
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

# --- PLOT 2: Distribuzione delle AUC ---
plt.figure(figsize=(10, 5))
plt.hist(auc_array[~np.isnan(auc_array)], bins=25, color='#00bfa5', edgecolor='black')
plt.axvline(x=mean_auc, color='#ff5252', linestyle='--', linewidth=2, label=f'Media: {mean_auc:.4f}')
plt.xlabel("Valore AUC", fontsize=12)
plt.ylabel("Frequenza (Numero di Target)", fontsize=12)
plt.title("Distribuzione delle AUC sui 206 Target", fontsize=14, pad=15)
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
## Front-end
import json

# 1. Salvataggio Feature (Input)
# Estraiamo i nomi esattamente come li ha visti la Rete Neurale
feature_names = X_train_nn.columns.tolist() 

with open('feature_cols.json', 'w') as f:
    json.dump(feature_names, f)

print(f"Salvate {len(feature_names)} feature in 'feature_cols.json'")

# 2. Salvataggio Target (Output)
# Estraiamo le etichette esatte dell'output layer
target_names = Y_train_nn.columns.tolist() 

with open('target_labels.json', 'w') as f:
    json.dump(target_names, f)

print(f"Legenda MoA salvata! Creato file con {len(target_names)} etichette.")
## Rete 2: Medical & Side Effects
import pandas as pd

# Percorsi dei file
path_cleaned = 'data/clinical/drugs_cleaned_dataset.xls'
path_side_effects = 'data/clinical/drugs_side_effects_drugs_com.csv'

# 1. Caricamento Side Effects (CSV standard)
df_side_effects = pd.read_csv(path_side_effects)

# 2. Caricamento Cleaned Dataset (Tentativo automatico)
try:
    # Tentativo 1: È un TSV mascherato da Excel
    df_cleaned = pd.read_csv(path_cleaned, sep='\t')
    print("drugs_cleaned_dataset caricato come file di testo!")
except Exception:
    # Tentativo 2: È un vero vecchio Excel (se ti dà errore qui, apri il terminale e fai 'pip install xlrd')
    df_cleaned = pd.read_excel(path_cleaned, engine='xlrd')
    print("drugs_cleaned_dataset caricato come vero Excel!")

# --- ESPLORAZIONE ---
print("\n--- DRUGS CLEANED INFO ---")
print(df_cleaned.info())

print("\n--- SIDE EFFECTS INFO ---")
print(df_side_effects.info())

display(df_side_effects.head(3))
## 🏥 Rete 2: Medical & Side Effects (NLP Pathway)
In questa sezione costruiamo il secondo pilastro dell'architettura **DualPath-MedAI**. 
Affrontiamo un problema di **Multi-Label Classification** con dataset ad alta dimensionalità testuale:
1. **Feature Engineering (X):** Utilizzo di `TfidfVectorizer` per trasformare le condizioni mediche e le classi dei farmaci in vettori numerici (NLP).
2. **Target Encoding (Y):** Utilizzo di `MultiLabelBinarizer` per mappare gli effetti collaterali multipli in una matrice sparsa binaria.
3. **Modello Deep Learning:** Rete fully-connected con output `Sigmoid` e loss `binary_crossentropy` per calcolare probabilità indipendenti su 1827 possibili effetti avversi.
### Estrazione dei Target (Y)
Serve a "smontare" le frasi degli effetti collaterali, pulirle e creare la matrice degli output per la rete:
from sklearn.preprocessing import MultiLabelBinarizer
import re

# Lavoriamo sul dataset pulito
df = df_cleaned.copy()

# Funzione per pulire il testo e creare liste di effetti singoli
def extract_effects(text):
    if type(text) != str:
        return []
    # Mettiamo in minuscolo, togliamo parentesi e dividiamo per virgola o punto e virgola
    text = re.sub(r'[()]', '', text.lower())
    effects = [e.strip() for e in re.split(r'[,;]', text) if e.strip()]
    return effects

# Applichiamo la funzione
df['side_effects_list'] = df['side_effects'].apply(extract_effects)

# Trasformiamo le liste in una matrice di 0 e 1 (One-Hot Encoding per target multipli)
mlb = MultiLabelBinarizer()
Y_medical = mlb.fit_transform(df['side_effects_list'])

print(f"Matrice Target (Y) creata! Shape: {Y_medical.shape}")
print(f"Numero totale di effetti collaterali unici: {len(mlb.classes_)}")
print("\nEsempio dei primi 10 effetti categorizzati:")
print(mlb.classes_[:10])
### Vettorizzazione Input e Creazione Modello
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import tensorflow as tf

# 1. Uniamo le informazioni chiave in un'unica stringa per ogni farmaco
df['features_text'] = df['medical_condition'].astype(str) + " " + df['drug_classes'].astype(str)

# 2. Trasformiamo il testo in numeri con TF-IDF
tfidf = TfidfVectorizer(max_features=500) # Limitiamo a 500 parole chiave
X_medical = tfidf.fit_transform(df['features_text']).toarray()

print(f"Matrice Input (X) creata! Shape: {X_medical.shape}")

# 3. Divisione Train/Test
X_train_m, X_test_m, Y_train_m, Y_test_m = train_test_split(X_medical, Y_medical, test_size=0.2, random_state=42)

# 4. Architettura della Rete Neurale (Multi-Label)
model_medical = Sequential([
    Dense(256, activation='relu', input_shape=(X_medical.shape[1],)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    # L'ultimo layer DEVE avere lo stesso numero dei target e attivazione SIGMOID
    Dense(Y_medical.shape[1], activation='sigmoid') 
])

# Compilazione: Sostituiamo 'accuracy' con 'AUC' specifico per multi-label
model_medical.compile(
    optimizer='adam', 
    loss='binary_crossentropy', 
    metrics=[tf.keras.metrics.AUC(multi_label=True, name='auc')]
)

print("\nArchitettura Modello Medical:")
model_medical.summary()
import joblib
from tensorflow.keras.callbacks import EarlyStopping

print("Avvio addestramento modello Medical...")

# Usiamo l'EarlyStopping per fermare l'addestramento se non migliora, evitando l'overfitting
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Addestramento (batch_size piccolo perché abbiamo solo 251 farmaci)
history_medical = model_medical.fit(
    X_train_m, Y_train_m,
    validation_data=(X_test_m, Y_test_m),
    epochs=40,
    batch_size=16, 
    callbacks=[early_stop],
    verbose=1
)

# --- SALVATAGGIO ASSET PER IL FRONTEND ---
model_medical.save('medical_model.h5')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
joblib.dump(mlb, 'mlb_binarizer.pkl')

print("\nAddestramento completato!")
print("Modello (medical_model.h5) e Trasformatori NLP (.pkl) salvati correttamente.")
## Plot del training
import matplotlib.pyplot as plt

# Recupero dinamico delle metriche dal dizionario history
auc_key = [k for k in history_medical.history.keys() if 'auc' in k.lower() and 'val' not in k.lower()][0]
val_auc_key = [k for k in history_medical.history.keys() if 'auc' in k.lower() and 'val' in k.lower()][0]

loss = history_medical.history['loss']
val_loss = history_medical.history['val_loss']
auc = history_medical.history[auc_key]
val_auc = history_medical.history[val_auc_key]

epochs = range(1, len(loss) + 1)

plt.figure(figsize=(14, 6))

# Plot Loss
plt.subplot(1, 2, 1)
plt.plot(epochs, loss, color='#00bfa5', linewidth=2.5, label='Training Loss')
plt.plot(epochs, val_loss, color='#ff5252', linewidth=2.5, linestyle='--', label='Validation Loss')
plt.title('Loss NLP (Binary Crossentropy)', fontsize=14, pad=15)
plt.xlabel('Epoche', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)

# Plot AUC
plt.subplot(1, 2, 2)
plt.plot(epochs, auc, color='#00bfa5', linewidth=2.5, label='Training AUC')
plt.plot(epochs, val_auc, color='#ff5252', linewidth=2.5, linestyle='--', label='Validation AUC')
plt.title('AUC NLP (Multi-Label)', fontsize=14, pad=15)
plt.xlabel('Epoche', fontsize=12)
plt.ylabel('AUC', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()
## Training LightGBM
import lightgbm as lgb
import numpy as np
import joblib
from tqdm import tqdm

print("\nTraining LightGBM models for Medical dataset...")

lgb_medical_models = []

for i in tqdm(range(Y_train_m.shape[1])):
    # Controllo di sicurezza: addestriamo solo se ci sono sia 0 che 1
    if len(np.unique(Y_train_m[:, i])) > 1:
        model = lgb.LGBMClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=8,
            subsample=0.8,
            colsample_bytree=0.8,
            n_jobs=-1
        )
        model.fit(X_train_m, Y_train_m[:, i])
        lgb_medical_models.append(model)
    else:
        # Manteniamo l'array a lunghezza fissa per non sfasare gli indici
        lgb_medical_models.append(None)

modelli_validi = sum(x is not None for x in lgb_medical_models)
print(f"Elaborazione completata. Modelli validi addestrati: {modelli_validi} su {Y_train_m.shape[1]}")

# Salvataggio
joblib.dump(lgb_medical_models, "lgb_medical_models.pkl")

print("Modelli LightGBM Medical salvati!")
## Valutazione LightGBM
import numpy as np
from sklearn.metrics import roc_auc_score

Y_pred = np.zeros_like(Y_test_m, dtype=float)

# 1. Effettuiamo le predizioni solo se il modello è stato addestrato (non è None)
for i, model in enumerate(lgb_medical_models):
    if model is not None:
        Y_pred[:, i] = model.predict_proba(X_test_m)[:, 1]

auc_list = []

for i in range(Y_test_m.shape[1]):
    # 2. Calcoliamo l'AUC solo se ci sono almeno 2 classi nel test set E il modello esiste
    if len(np.unique(Y_test_m[:, i])) > 1 and lgb_medical_models[i] is not None:
        auc = roc_auc_score(Y_test_m[:, i], Y_pred[:, i])
        auc_list.append(auc)
    else:
        auc_list.append(np.nan)

mean_auc = np.nanmean(auc_list)

print(f"AUC medio LightGBM Medical sui target validi: {mean_auc:.4f}")
## Training XGBoost
import xgboost as xgb
import numpy as np
import joblib
from tqdm import tqdm

print("\nTraining XGBoost models for Medical dataset...")

xgb_medical_models = []

for i in tqdm(range(Y_train_m.shape[1])):
    # Stesso controllo di sicurezza fatto per LightGBM
    if len(np.unique(Y_train_m[:, i])) > 1:
        model = xgb.XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric='auc',
            tree_method='hist',
            n_jobs=-1
        )
        model.fit(X_train_m, Y_train_m[:, i])
        xgb_medical_models.append(model)
    else:
        # Segnaposto per i target non addestrabili per mantenere l'allineamento
        xgb_medical_models.append(None)

modelli_validi = sum(x is not None for x in xgb_medical_models)
print(f"Elaborazione completata. Modelli validi addestrati: {modelli_validi} su {Y_train_m.shape[1]}")

# Salvataggio corretto (rimosso il doppio 'medical_medical')
joblib.dump(xgb_medical_models, "xgb_medical_models.pkl")

print("Modelli XGBoost Medical salvati!")
## Valutazione XGBoost
import numpy as np
from sklearn.metrics import roc_auc_score

Y_pred = np.zeros_like(Y_test_m, dtype=float)

# 1. Predizioni sicure: saltiamo i modelli contrassegnati come None
for i, model in enumerate(xgb_medical_models):
    if model is not None:
        Y_pred[:, i] = model.predict_proba(X_test_m)[:, 1]

auc_list = []

# 2. Calcolo AUC solo per i target validi e per i quali esiste un modello
for i in range(Y_test_m.shape[1]):
    if len(np.unique(Y_test_m[:, i])) > 1 and xgb_medical_models[i] is not None:
        auc = roc_auc_score(Y_test_m[:, i], Y_pred[:, i])
        auc_list.append(auc)
    else:
        auc_list.append(np.nan)

mean_auc = np.nanmean(auc_list)

print(f"AUC medio XGBoost Medical sui target validi: {mean_auc:.4f}")