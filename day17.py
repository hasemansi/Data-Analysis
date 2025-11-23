# sorting searching

import numpy as np

# program 1
a=np.array([10,45,37,38,9,49])
print(np.sort(a))

#program 2
mat=np.array([
    [11,32,93],
    [84,51,63],
    [57,98,79]
])

print(mat)
print(np.sort(mat))
print(np.sort(mat,axis=1))
print(np.sort(mat,axis=0))

#program 3
# argsort
#                     0  1   2   3   4
a1=np.array([10,30,27,50,47])
a2=np.array([65,57,38,49,50])
indices=np.argsort(a1)
print(indices)
print(a1[indices])
print(a2[indices])

print("*********************")

# Searching with conditions

q1=np.array([10,20,30,40,50,60,70,80])
res=np.where(q1>40)
print(res)
print(q1[res])

res1=np.where(q1%3==0)
print(q1[res1])

# conditional statement using np.where 
marks=np.array([34,48,79,80,78,90,68,59])
result=np.where(marks>60,"Pass","Fail")
print(result)

# search sorted arrays 
ar1=np.array([11,22,33,44,55,66,77,88])
ar2=np.searchsorted(ar1,45)
print(ar2)
print(ar1)

# counting non zeros 
arr3 = np.array([44,56,0,78,66,0])
print(np.count_nonzero(arr3))

# any 
print(np.any(arr3>70))

# all
print(np.all(arr3>70))

# Unique values and frequenc
arr = np.array([1,2,3,2,3,4,6,5])
values,count=np.unique(arr,return_counts=True)
print(values)
print(count)