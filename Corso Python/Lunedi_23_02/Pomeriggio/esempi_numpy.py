import numpy as np

#creazione di un array unidimensionale
arr = np.array([1,2,3,4,5])

'''
#creazione di un array bdimensionale
arr2d = np.array([1,2,3], [4,5,6])   '''

#utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape) # Output: (5,) grandezza dell array
print ("Dimensioni dell'array:", arr.ndim) # Output: 1- 
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print( "Numero di elementi:", arr.size) # Output: 5- lunghezza della lista
print("Somma degli elementi:", arr.sum()) # Output: 15 - sum fa la sommma dei elementi all interno
print ("Media degli elementi:", arr.mean()) # Output: 3.0 - la media degli elementi all interno
print("Valore massimo:", arr.max()) # Output: 5 - il valore massimo
print("Indice del valore massimo:", arr.argmax()) # Output: 4 - riporta l'indice del valore massimo


arr = np.arange(10)
print(arr)  #---stampa da 0 a 10

arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)
#--crea due liste una da 0 a 2 e una da 3 a 5

