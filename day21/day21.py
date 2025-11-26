import pandas as pd

data=pd.DataFrame({
    "Id":[101,102,103],
    "Name":["Alice","Bob","Johny"],
    "Age":[25,30,48]
},index=['A','B','C'])
print(data)

# program 1 writing with index
# data.to_csv('emp.csv')

# without index
# data.to_csv('emp1.csv',index=None)  #use can also use index=False

# program 3
# writing CSV usually with |
data.to_csv('emp2.csv',index=False,sep='|')


# program 4
# witing to excel
# data.to_excel('emp3.xlsx')

#without index
# data.to_excel('emp4.xlsx',index=None)

# # with sheet name
# data.to_excel('emp5.xlsx',index=None,sheet_name='EmpData')

# to json file
# data.to_json('emp6.json')

# to make it readable
data.to_json('emp7.json',orient='records')