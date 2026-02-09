import numpy as np


#NUMPY ARRAYS

lista = [1,2,3]
listb = [1,2,3]
listc = []

for aval, bval in zip (lista, listb):
    listc.append(aval+bval)
#print (listc)

"""
a= np.array([[1,2,3]])
b= np.array([[1,2,3]])

c = a+b
print(c)

"""

#ARRAY SHAPES
a = np.array([0,1,2], ndmin=2)

print(a.shape)

min_val=3
max_val=10
nb_val=4
arr3=np.linspace(min_val,max_val,nb_val)
print("arr3=", arr3)


#SORTING ARRAYS
x = np.array([1,9,7,6])
print(np.sort(x))

x2= np.array([[1,4,2],
              [1,9,8]])

x3= np.array([[1,4,6],
              [4,8,4],
              [2,6,2]])
print("sort rows = ", np.sort(x2))
print("####")
print("sort columns = ", np.sort(x3, 0))
