import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr)
boolean_arr=arr%2==0
print(boolean_arr)
filter_array=arr[boolean_arr]
print(filter_array)

# Boolean masking applying various condition 

numbers=np.array([10,20,30,40,50,60,70,80])
a1=numbers[(numbers>20) & (numbers<60)]
print(a1)
a2=numbers[(numbers<40) | (numbers>60)]
print(a2)

# Boolean indexing on 2D array 
mat = np.array([
    [10,25,30],
    [40,50,60],
    [70,85,90]
])
# flatten and filter operation in one step
# extract all the elements greater than 50

el=mat[mat>40]
print(el)

#  FANCY ----------------------> INDEXDING

n=np.array([1,2,3,4,5,6,7,8,9])
print(n[[0,2,8]])