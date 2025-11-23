# Day 2 — Reading & Writing Data (CSV, Excel, JSON)
# Today’s Learning Goals
# Read CSV files
# Read Excel files
# Read JSON files
# Save (write) DataFrames to files
# Important parameters (sep, header, names, index_col)
# Handling missing data while reading

# program 1 -  read csv file
import pandas as pd
f1=pd.read_csv('students.csv')
print(f1)

#without header
f1=pd.read_csv('students.csv',header=None)
print(f1)

# with your own header name
f1=pd.read_csv('students.csv',header=None,names=['Names','Age','City'])
print(f1)

# specific column as index
f1=pd.read_csv('students.csv',index_col='name')
print(f1)

#program 2 - read txt file
f2=pd.read_csv('marks.txt',sep='|')
print(f2)


# program 4
# reading a excel file 
# pip install openpyxl
# pip install numpy
# pip install pandas
df = pd.read_excel('employees.xlsx')
print(df)

# reading the the specific excel sheet
# df = pd.read_excel('employees.xlsx',sheet_name = "sheet1")
# print(df)

df = pd.read_excel('employees.xlsx',header = None)
print(df)

# reading json file 
df = pd.read_json('data.json')
print(df)

# limiting the count of rows
df = pd.read_csv("students.csv",nrows=1)
print(df)