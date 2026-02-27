'''2. pip sta per Pip Install Packages ma in realtà questo acromino cambia sempre. pip è il sistema di gestione dei pacchetti/librerie in python. pip permette di installare facilmente i diversi pacchetti e 
di base possiamo dire che aggiunge, rimuove e gestisce i pacchetti.
pip riesce a fare cinque cose:
1.installazione di pacchetti, e cioè ci permette di installare in python una specifica librerai di una specifica versione
2. gestisce le dipendenze, cioè quando installiamo una qualsiasi libreria, installiamo automaticamente tutte le sue funzionalità laterali necessarie per farla funzionare
3. Aggirona i paccgetti
4. gestisce le versioni, ci permette di scegliere in downgrade e l'upgrade di un pacchetto 
5. integrazione con ambienti virtuali, cioè permette di creare ambienti isolati per gestire le dipendenze in modo indipendente

3. l'analisi dati è un processo strutturato che consiste nell'esaminare, pulire e interpretare i dati utilizzando struemnti statistici con l'obiettivo di individuare informazioni e prendere decisioni basate sui dati. 
l'analisi dei dati parte da un obiettivo specifico, utilizza strumenti matematici e statistici, permette di individuare pattern, correlazioni tra i dati e alla fine trasforma dati grezzi in informazioni comprensibili
La programmazione OOP si concentra invece su un organizzazione del codice fondata su classi e oggetti, mentre invece l'analisi dati si concentra sugli obiettivi che vogliamo raggiungere con i dati che abbiamo.

7. Numpy, l'acronimo di Numerical Python, è una libreria open-source fondamentale per il calcolo scientifico e l'elaborazione dei dati in python. numpy supporta due cose: operazioni vettoriali e gli array.
le operazione vettoriali rendono inutili fare un ciclo array perchè queste operano su tutta la lunghessa dell'array. 
Numpy offre diverse funzionalità:
- supporta array multidimensionali ovvero un nuvo tipo di collezione/struttura dati di Numpy
- formisce funzioni e metodi, applicabili su tutto l'array che fanno per noi operazioni matematiche
- numpy lavora a motore aperto e cioè ha strumenti per integrare il codice C/C++ e Fortran
quindi possiamo dire che numpy è alla base di tutte le librerie perchè è modificabile, settabile, strutturabile a seconda delle richeste che abbiamo
in particolare, numpy supporta operazioni vettoriali ovvero delle operazioni aritmetiche sugli array applicate su tutti gli elementi di un array come ad esempio aggiungere 10 ad ogni elemento all'interno dell'array
numpy supporta anche funzioni universali ovver funzioni che operano su tutti gli elementi dell'array e cioè element-wise ma che restituisce un risultato unitario, come ad esempio np.subtract().
Le principali keywords di numpy sono:
-ndarray: è una struttura dati mutidimensionale ovvero puo avere dimensione 1D,2D,3D... un array è omogeneo, vettorializzato, è modificabile, ordinato e gli elementi all'interno sono indicizzabili. si crea con np.array(). il tipo e arr con parentesi quadre o tonde + quadre se stiamo convertendo da una lista
- dtype: è una proprietà che ci permette di capire che tipo di dati abbiamo nel nostro array
-shape: è una proprietà che restituisce la forma del nostro array, ad esempio se abbiamo 4 righe e 3 colonne, la shape sarà (4,3)
-reshape: è una propietà che ci permette di cmabiare la fomra del nostro array senza modificarne i dati all'interno
- arange: è una proprietà che ci permette di creare un nuovo array con valori sequenziali, coem il range in puthon.
infatti nlela sua sintassi vi è un valore di start, un valore di stop e il valore che rappresenta il passo della nostra sequenza numerica
-linspace : crea una sequenza numerica equidistante. la sintassi è proprio np.linspace
-random : genera array con valori casuali. esempio, np.random.randint(1,10, size=4)
- funzioni aritmetiche, le quali sono per il 90% operazioni vettoriali. esempio np.add(),np.subtract()
-funzzoni matematiche, le quali sono per il 50% operaz vettoriali e 50% funz universali
- funzioni statistice, le quali sono per il 90% funz universali.
In numpy, è importante definire l'indexing, il fancy indexing, lo slicing ed infine il broadcasting
l'indexing è una proprietà che offre numpy per accedere a tutti gli elementi di un array poichè ognuno di essi corrisponde ad un indice. tramite questo, possiamo prendere uno o piu valori all'interno dell'array,
 da un valore possiamo prenderne molti.
lo slicing è una proprietà che offre numpy che ci permette di estrapolare una parte del nostro array, utilizzando uno start come inizio, un valore come fine e il passo
lo start di default è zero, lo stop non viene mai incluso e il passo di default è 1
il fancy indexing invece permette di selezionare specifici elementi non contigui, quindi non fa una selezione rettangolare come invece fa lo slicing, ma può prendere vari indici di posizione e crea sempre una copia dei dati selezionati
il broadcasting è una potente funzione di numpy che permette di eseguire operazioni aritmetiche e di lavorare con array di forma diversa adattadoli e rendendoli compatibili, rendendo quindi piu semlice la scrittura di un codice. 
questa specifica proprietà è resa possibile poichè va ad espandere automaticamente l'array con dimensione piu piccola per renderlo compatibile. due array si dicono compatibili se sono di dimensione uguale o se uno dei due ha dimensione 1. as esempio se la dimensione di 
un array è 1 allora usa lo stesso valore piu volte per raggiungere le dimensioni dell'altro. 
il broadcasting infatti agisce su 3 principi: allineamento delle dimensioni cioè numpy controlla se le dimensioni sono compatibili e allinea gli array partendo dalla dimensione piu a destra, espansione delle dimesioni ovvero va ad espandere automaticamente uno dei due array laddove non sono compatibili e uno dei due ha dimensione 1, e applicazione delle operazioni e cioè avendo la stessa dimensione numpy applica le funizoni universali e operazioni su tutti gli elementi. 
questi 3 principi evitano che il programmatore debba generare piu copie di un array per adattarne le dimensioni e rnde il coidce molto piu leggibile
importante è precisare che il braodcasting viene sfruttato in pandas da funzionalità evolute e da altri sistemi, può essere considerata la base di altre operazioni.

#10
Pandas è la libreria utilizzata in python per la manipolazione e analisi dei dati, in particolare ci ocncentrasulla pre-analisi dei dati ovvero il processo di preparazioen dei dati e la pulizia dei dati ovvero la gestione di dati mancanti, duplicati, convertire tipi di dato.
Pandas introduce due strutture di dati: DataFrame e Series
il dataframe è una struttura dati bidimensionale, composta da righe e colonne. ogni colonna può avere vari tipi di dati, ex. str,int,float, booleani
la series è una struttura dati unidimensionale con una sola colonna di dati, infatti può essere considerata come una colonna del Dataframe. tutti gli elementi all'interno hanno un topo tipo di dato.
Pandas possiede principalmente 4 capacità, la prima è la manipolazione dei dati, cioè include funzioni di selezione e filtraggio di elementi, modifica l'ordine dei dati, li rimuove li combina con altri dataset, cambia la struttura organizzativa. La seconda è la pulizia dei dati ovvero offre funzioni per gestire dati mancanti e duplicati, può rimuoverli. La terza è l'analisi dei dati con funzioni che permettono l'aggregazione dei dati. La quarta è l'Interoperabilità ovvero Pandas lavora bene con altre librerie senza alcun problema perche ha strutture compatibili e sono progettate per collaborare 

pandas ha piu caartteristiche: 
-indicizzazione avanzata: permette ai programmatori di accedere ad ogni dato e piu dati, e manipolarli. offre infatti il multiindex cioè un'indicizzazione con più indici. es df_multindex = df.set_index(["città", "nome"]) e poi seleziono tutte le persone di roma con l'index roma. 
-permettte di unire e concatenare più array, usando il merge per unire e il concat per concatenare, gestendo gli indici che non si allineano
- risistemazione e pivot: permette di cambiare i dati, trasformarli creando una tabella pivot creando una tabella con un formato piu adatto all'analisi che vogliamo svolgere. serve soprattutto quando abbiamo una grande quantità di dati e vogliamo sintetizzarli in un formato piu gestibile e appropriato alla nostra analisi
- gestione del tempo: pandas possiede delle funzionalità che ci permettono di manipolare le date e orarri, genera periodi di tempo e cambia la frequenza dei dati, attraverso funzioni come rolling, windowing, ecc. 

#12
il dataframe è una struttura dati bidimensionale, composta da righe e colonne. ogni colonna può avere vari tipi di dati, ex. str,int,float, booleani. quindi è: eterogeneo, ordintato, modif,bidimensionale, parentesi: []
la series è una struttura dati unidimensionale con una sola colonna di dati, infatti può essere considerata come una colonna del Dataframe. tutti gli elementi all'interno hanno un tipo tipo di dato. quindi è:omogenea, ordinata, modificabile, monodimensionale e le parentesi usate: []
un array invece è una struttura dati sia mono che multidimensionale composto da elementi di uno stesso tipo (omogeneo) e permette di eseguire velocemente calcoli numerici. quindi è: omogeneo, ordinato, modificabile, tipo è multidimensionale, le parentesi : [] con indici numerici
abbiamo bisogno di queste strutture perchè ognuna di essa ha delle funzionalità proprie e necessarie relativale al funzionamento della stessa libreria per soddisfare la nostra richiesta. gli array ci permetton di effettuare calcoli matematici velocemente su una grande quanittà di dati, supportano operazioni vettoriali senza il bisogno del ciclo for e supportano l'algebra lineare
le series servono quando abbiamo ad esmepio solo una colonna di dati e vogliamo fare un'analisi su quella
i dataframe quando vogliamo analizzare i dati con rappresentazioni tabellari e colonne di diverso tipo

#la visualizzazioen dei dati e la rappresentazione dei dati, più precisamente è la trasformazione dei dati in grafici così da renderli piu comprensibili. Lo si fa principamlemnte con Matplotlib e seabron
è importante stabilire 3 obiettivi: informativo cioè comunica i dati in modo preciso e chiaro, esplorativo cioè usato per mettere in risalto e scoprire specifici pattern e correlazioni tra dati o anomalie, e narrativo cioè racconta una storia con i dati
Definire questi 3 scopi è importante per scegliere il giusto tipo di grafico e comunicare correttamente i risultati. La scelta del grafico dipende maggiormente dal tipo di dato su cui stiamo lavorando e cosa volgiamo mostrare. 
abbiamo diversi tipi di dati: categorici, continui, distribuzione, correlazione e composizione. 