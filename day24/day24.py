import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [45000, 60000, 52000, 70000, 65000, 72000],
    "Experience": [2, 5, 3, 10, 7, 12]
}

df=pd.DataFrame(data)
print(df)

#program 1
# average salary by department
group=df.groupby('Department')
print(group)
avgSal=group['Salary'].mean()
print(avgSal)

# program 2
# sum of experience by department
print(group['Experience'].sum())

# program 3
# count of employee by department
print(group['Employee'].count())

# program 4
# multiple aggregations at once

summary=group.agg({
    'Salary' : ['mean','max','min'],
    'Experience':['mean','max']
})
print(summary)

#program 4
# average salary by department greater than 60k
q=group.filter(lambda x : x['Salary'].mean()>60000)
print(q)