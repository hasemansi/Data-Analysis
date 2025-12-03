import pandas as pd
data={
    'Name':['Alice','Bob','John','Rhiya','Pooja'],
    'Department':['HR','Manager','IT','IT','Finanace'],
    'Age':[25,37,57,39,28],
    'Salary':[10000,50000,35000,75000,49000]
}
df=pd.DataFrame(data)
print(df)

# filter salary > 60000
print(df[df['Salary']>60000])

# program 2
# print only IT department empployees
print(df[df['Department']=='IT'])

#filter using two conditions 
# IT | HR
print(df[(df['Department']=='IT') | (df['Department']=='HR')])

#filter using two conditions 
# IT and salary > 60000
print(df[(df['Department']=='IT') & (df['Salary']>60000)])


# filtering operation based on sorting
print(df.sort_values(by='Salary',ascending=False))

print(df.sort_values(by='Salary'))


# Add a conditional columns if salary > 60000 ---> HIGH or LOW
df['Status']=df['Salary'].apply(lambda x:'High' if x>60000 else 'Low')
print(df)

# salary above 55000 and below 65000
print(df[(df['Salary']>55000) & (df['Salary']<65000)])


# select the records not belong to IT or HR department
res=~df['Department'].isin(['IT','HR'])
print(df[res])