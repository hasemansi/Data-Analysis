# universal functions 
# mathematics , trignometric , statistical ufunctions 
# to array

# addition ,subtraction , multiplication 
# division , power , remainder

import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([5,6,7,8,9])

print("Addition : ",np.add(a,b))
print("Subtraction : ",np.subtract(a,b))
print("Multiplication : ",np.multiply(a,b))
print("Division : ",np.divide(a,b))

# program 2
arr=np.array([1,2,3,4,5])
print("Square of array : ",np.square(arr))
sqr=np.square(arr)
print("Square root : ",np.sqrt(sqr))
print(np.exp(arr))
print(np.log(arr))

#Rounding off and absolute values
# Ceiling , Floor , Round , Absolute

arr1 = np.array([3.14,2.67,-5.89,45.67])
print(np.ceil(arr1))

print(np.floor(arr1))  

print(np.round(arr1,2)) # rounding off the values up to given decimal points

print(np.absolute(arr1)) # turns - to +