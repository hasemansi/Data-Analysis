# numpy array vs python list
import numpy as np
from numpy import array

list1=[1,2,3,4,5]
arr=np.array([6,7,8,9,5])

print(list1)
print(arr)

print(type(list1))
print(type(arr))

print(list1 * 2) # it twice the array element in a single array
print(arr * 2) # it multiplies each array element with 2

# Arithematic operation using numpy array
# add subtract multiply and divideby 2 each array element

print('Array Addition : ',arr+2)
print('Array Subtraction : ',arr-2)
print('Array Multiplication : ',arr*2)
print('Array Division : ',arr/2)

# range(startIndex,endIndex(not included),stepSize)
a1=np.array([1,2,3,4,5,6])
a2=np.zeros(5,dtype='int')
a3=np.ones(4,dtype='int')
a4=np.arange(2,21,2)
a5=np.arange(50,0,-5)
a6=np.linspace(1,10,5)
print(a6)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

print(np.arange(1,11,1).reshape(2,5)) # row, column
print(np.arange(1,11,1).reshape(5,2)) # row column