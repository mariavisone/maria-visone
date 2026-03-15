#esempio visualizzazione dati
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configura Seaborn
sns.set_theme(style="darkgrid") #applica il tema di dafault di seabon

# Crea alcuni dati
data = np.random.normal(size=100) 

# Crea un grafico
sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.show()



#matplotlib
#crea un grafico a linee
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

#creare un grafico a barre
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()
'''
#crea un istogramma
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)   #data sono l'insieme di numeri che voglio rappresentare, bins il num di colonne
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()
'''
#crea unon scattern plot
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y) #prende il primo valore di x e il primo valore di y, e crea un punto (x1,y1)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
'''
#GRAFICO A barre
import seaborn as sns
import matplotlib.pyplot as plt

# Dati di esempio
tips = sns.load_dataset("tips")

# Creare un grafico a barre
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Conto Totale per Giorno')
plt.show()



#GRAFICO A LINEE
#import seaborn as sns
import matplotlib.pyplot as plt

# Dati di esempio
fmri = sns.load_dataset("fmri")

# Creare un grafico a linee
sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event")
plt.title('Segnale FMRI nel Tempo')
plt.show()



#GRAFICO ISTOGRAMMA E KDE
import seaborn as sns
import matplotlib.pyplot as plt

# Generare dati casuali
data = sns.load_dataset("penguins")

# Creare un istogramma con KDE
sns.histplot(data=data, x="flipper_length_mm", kde=True)
plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
plt.show()

