import numpy as np

#linespace

arr = np.linspace(0,1,5)
print(arr)

#random

random_arr = np.random.rand(3,3)
#matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

#sum, mean, std
arr = np.array([1,2,3,4,5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)


print("Sum:", sum_value) 
print("Mean:", mean_value)
print("Standard Deviation:", std_value)

#reshape
reshaped_arr = arr.reshape((2, 3)) 
print(reshaped_arr)