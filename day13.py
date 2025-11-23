import numpy as np

mat=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(mat)

print(mat[0:2,1:3])
print(mat[:,:2])
print(mat[1:,:])
print(mat[2,2])
print(mat[1,2])


# Modifying the array
arr=np.array([10,20,30,40,50])
print(arr)
arr[0]=11
print(arr)
# with slicing
arr[1:3]=[22,33]
print(arr)

# Extracting rows and columns

q1=np.arange(1,17).reshape(4,4)
print(q1)

# boolean indexing
bool_mask=arr>30
print(bool_mask)