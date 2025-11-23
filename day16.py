# Aggregate functions 

import numpy as np

a=np.array([1,2,3,4,5,6])
print("Addition of array elements: ",np.sum(a))

# program 2
mat = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(mat))

# addition by row
print(np.sum(mat,axis=1))

# addition by column
print(np.sum(mat,axis=0))

# program 3
# mean
a=np.array([1,2,3,4,5,6])
print(np.mean(a))
print(np.median(a))

mat = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.mean(mat))
print(np.mean(mat,axis=0))
print(np.mean(mat,axis=1))

# program 3 ---> median
print(np.median(mat))
print(np.median(mat,axis=0))
print(np.median(mat,axis=1))


# program 4-----> min max
print(np.min(a))
print(np.max(a))

print(np.min(mat))
print(np.max(mat))
print(np.min(mat,axis=0))
print(np.min(mat,axis=0))
print(np.max(mat,axis=1))
print(np.max(mat,axis=0))

# standard deviation
#print(sum([60,70,80,90,100])/5)
#print(sum([10,15,20,5,350])/5)
#((10-80)**2 + (15 - 80)**2+ (20-80)**2+(5-80)**2+(350-80)*2)/5
#std ---> sqrt(var)

# program 5 -----> standard deviation and variance
a1=np.array([10,30,56,74,240])
print("Variance")
print(np.var(a1))
print("Standard Deviation")
print(np.std(a1))
