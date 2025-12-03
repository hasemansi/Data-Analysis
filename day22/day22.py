import pandas as pd
data={
    'Name':['Alice','Bob','John','Rhiya','Pooja'],
    'Department':['HR','Manager','IT','IT','Finanace'],
    'Age':[25,37,57,39,28],
    'Salary':[10000,50000,35000,75000,49000]
}
df=pd.DataFrame(data)
print(df)


# select a salary greater than 55
q1=df['Salary']>55000
print(df[q1])

# or
print(df[df['Salary']>55000])

# print employee of IT
q2=df['Department']=='IT'
print(df[q2])


# print employee of IT and salary greater than 55
q3=(df['Department']=='IT') & (df['Salary']>55000)
print(df[q3])


# print user of department IT or HR
q4=(df['Department']=='IT') | (df['Department']=='HR')
print(df[q4])

# Sorting of data 
q5=df.sort_values(by='Salary',ascending=False) # descending
print(q5)
q6=df.sort_values(by='Salary') # asscending
print(q6)