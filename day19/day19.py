# +----+---------+-------+----------+
# | ID | Name    | Age   | Salary   |
# +----+---------+-------+----------+
# | 1  | Alice   | 25    | 50000    |
# | 2  | Bob     | 30    | 60000    |
# | 3  | Charlie | 35    | 70000    |
# +----+---------+-------+----------+

# What is a data frame ??
# A 2D table (rows + columns)
# Like Excel or SQL 
# Each column has different data types
# Build on numpy 

# A data frame from python  dictionary

import pandas as pd
#program 1
data={
    "Name":["Mansi","Tejas","Rushi"],
    "class":["MCS","Bcom","Bsc"],
    "age":[22,21,20]
}

d1=pd.DataFrame(data)
print(d1)

data2=[
    {"name":"alice","Age":20},
    {"name":"ram","Age":22},
    {"name":"bob","Age":21}
]
d2=pd.DataFrame(data2)
print(d2)

import numpy as np

a1=np.array([
    [1,'alice',20],
    [2,'bob',22],
    [3,'ram',23]
])
# print(a1)
d3=pd.DataFrame(data=a1,columns=["Id","name","age"])
print(d3)

d4=pd.read_csv('employees.csv')
print(d4)

print('first 5 -----------------')
first5=d4.head()
print(first5)

print('last 5-------------------')
last5=d4.tail()
print(last5)

# colum data types
print(d4.dtypes)
print(d4.describe())
print(d4.shape)
print(d4.columns)

res=d4['Salary']>55000
print(d4[res])