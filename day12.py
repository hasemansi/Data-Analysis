import numpy as np
arr1=np.full((3,3),5)
print(arr1)

#program 2
a=np.arange(10)
print(a)

b=np.arange(5,15)
print(b)

c=np.arange(5,20,2)
print(c)

#slicing

arr=np.array([1,2,3,4,5,6,7])
print(arr)

print(arr[1:])
print(arr[1:5])
print(arr[:])
print(arr[:5])

# slicing of 2D array
q1=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(q1)

#print(Row,Column)
print(q1[0:3,1:3])
print(q1[0:,:1])