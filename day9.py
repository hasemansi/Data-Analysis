# Explain what is numpy ?
# install and import numpy 
# creating numpy arrays 
# understanding difference between list and numpy arrays
# basic  attributes and methods 

# [1,2,3,4,5]
# ["chinmay","deshpand",44,66]
# int , float , string , boolean


# why numpy ?
# python libraby for numerical computation
# fast operation on large data set 
# mathematical , logical and statistical opeartions
# integration with other python librabies , pandas ,scikit-learn 

from numpy import *
a=array([1,2,3,4,5])
print(a)
print(a.ndim)
print("Type:",type(a))
print("Data Type",a.dtype)
print("")

# program 2
arr2 = array([1.5,2.5,3.6,4.7,5.8,6.9])
print(arr2)
print("type:",type(arr2))
print("data type:",arr2.dtype)
print(arr2.ndim)

#program 3
arr3=array([[1,2,3,4],[5,6,7,8]])
print(arr3)
print(arr3.dtype)
print(arr3.ndim)
print(arr3.shape)

# program 4
# string array
strarr=array(["mansi","tejas","Rushi"])
print(strarr)

#program 5
arr4=array([1,2,3,4,4.5])
print(arr4)
print(type(arr4))
print(arr4.dtype)
print(arr4.size)
print(arr4.itemsize)
print("*********************")
#program 6
matrixC = array([11,22,33])
print(matrixC+1)
print(matrixC*2)
print(matrixC/4)
print(matrixC%4)