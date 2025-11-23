from array import *
#from list create array
#loop --> total
#mark/total+100  = percentage

# listS=input("Enter the marks").split(',')
listI=[int(x) for x in input('Enter the marks').split(',')]
#[4,5,6,7,8]
marks=array('i',listI)
sum=0
for x in marks:
    sum+=0

print("The total mark are:{sum}")
print((sum/50)*100)

#program 2
#