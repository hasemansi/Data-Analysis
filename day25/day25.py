import pandas as pd
data = {
    "Region": ["East", "West", "East", "North", "West", "North", "East"],
    "Salesperson": ["Amit", "Neha", "Pooja", "John", "Bob", "Riya", "Alias"],
    "Product": ["Mobile", "Laptop", "Laptop", "Mobile", "Mobile", "Laptop", "Laptop"],
    "Units": [5, 3, 7, 2, 4, 6, 8],
    "Revenue": [50000, 90000, 140000, 30000, 45000, 120000, 160000]
}
df=pd.DataFrame(data)
print(df)

# Program 1
#pd.pivot_table(data,values,index,columns,aggfunc)
# total revenue by region
a=pd.pivot_table(data=df,values='Revenue',index='Region',aggfunc=sum)
print(a)

#program 2
# unit sold by product and region
b=pd.pivot_table(data=df,values='Units',index='Region',columns='Product',aggfunc=sum)
print(b)

#program 3
# revenue by person sum / mean
c=pd.pivot_table(data=df,values='Revenue',index='Salesperson',aggfunc=['sum','mean'])
print(c)

#program 4
# units sum , revenu sum , region wise
d=pd.pivot_table(data=df,values=['Units','Revenue'],index='Region',aggfunc=sum)
print(d)

#program 5
# region wise transactions for unit on products
e=pd.pivot_table(data=df,values='Units',index='Region',columns='Product',aggfunc=["count"])
print(e)
#program 6
# create a dataframe with no values
f=pd.pivot_table(data=df,values='Units',index='Region',columns='Product',aggfunc=["count"],fill_value=0)
print(f)
print(df)
#program 7
# Region , SalesPerson ----> revenue (sum)
g=pd.pivot_table(data=df,values='Revenue',index=['Region','Salesperson'],aggfunc=sum)
print(g)