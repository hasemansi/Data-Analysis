
# What is pandas ?
# How  to install / import pandas
# Series and Data frames basics
# Creating a series 
# Creating a data frame 
# Accessing data

import pandas as pd
# import pandas
# from pandas import Series
# from pandas import *

a=pd.Series([1,3,4,5,6])
print(a)

b=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(b)

marks={ 'english':80,'science':90, 'Maths':100}
print(marks)
# df=pd.Series(marks)
df1=pd.Series(marks)
print(df1)

# DataFrame
# A data frame is 2D table 
# dictionary of list

data={
    'name':['mansi','vrushali','supriya'],
    'age':[22,23,24],
    'city':["Sangamner","Mumbai","Pune"]
}
df1=pd.DataFrame(data)
print(df1)

# Data frame using dictionary 
data1=[
    {'name':'Mansi','age':22},
    {'name':'Vrushali','age':22},
    {'name':'Supriya','age':22}
]
print(data1)
df2=pd.DataFrame(data1)
print(df2)

# Accessing the columns
print(df2['name'])
print(df2['age'])
# Accessing the multiple columns
print(df2[['age','name']])

# Accesing rows using .loc(indexlabe) and iloc(row number)

print(df2.loc[1])
print(df2.iloc[0])
# label 0 , 1, 2
# 0    2000  Akshaya     #0
# 1    3000     Riya     #1
# 2    5000    Karan     #2

# A    2000  Akshaya     #0
# B    3000     Riya     #1
# C    5000    Karan     #2


print(df2.info())
print(df2.describe())