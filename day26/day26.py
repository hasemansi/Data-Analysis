# Merging , Joining , Concatenation
# adding rows

import pandas as pd
df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["sarika","ram","charlie"]
})
df2 = pd.DataFrame({
    "ID":[4,5,6],
    "Name":["sham","ramesh","suresh"]
})

#concat
result1=pd.concat([df1,df2],ignore_index=True)
print(result1)

# example for adding columns
df3 = pd.DataFrame({
    "Name":["sairka","ram","sham"],
    "Age":[11,22,33]
})
df4 = pd.DataFrame({
    "Salary":["10000","20000","30000"],
    "Depart":["IT","HR","IT"]
})

result2=pd.concat([df1,df2],axis=1)
print(result2)


# program 3 merging operation
# sql inner join , left join , outer join , right join 

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Salary":["5000","6000","7000"]
})

result3=df1.merge(df2,on='ID',how='inner')
print(result3)

result4=df1.merge(df2,on='ID',how='left')
print(result4)

result5=df1.merge(df2,on='ID',how='right')
print(result5)

result = df1.merge(df2,on="ID",how="outer")
print(result)