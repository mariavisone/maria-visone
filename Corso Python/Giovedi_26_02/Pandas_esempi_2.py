#serie temporali

import pandas as pd
import numpy as np


# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01',
periods=10, freq='ME')

# Creazione di un DataFrame con indice temporale
df = pd.DataFrame({
    'valore': np.random.randint(1,100, size=10)
}, index=date_range)

# Resampling dei dati di una serie temporale
df_resampled = df.resample('ME').mean()

print("DataFrame originale:")
print(df.head())

print("\nDataFrame dopo resampling mensile:")
print(df_resampled)


#datetime
import pandas as pd

# 1️ Creiamo un DataFrame con date come stringhe
df = pd.DataFrame({
    'date': ['2021-01-01', '2021-01-02', '2021-01-03',
             '2021-02-01', '2021-02-02', '2021-02-03'],
    'valore': [10, 20, 30, 40, 50, 60]
})

# 2️ Convertiamo la colonna 'date' in datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

print("DataFrame originale:")
print(df)


# oppure per creare un indice

df.index = pd.to_datetime(df['date'])

