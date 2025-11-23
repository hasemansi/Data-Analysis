import numpy as np
a=np.zeros(8,dtype='int')
print(a)

#2D using numpy
b=np.zeros((3,3),dtype='int')
print(b)

c=np.ones((2,3),dtype='int')
print(c)

d=np.ones(6,dtype='int')
print(d)

#program 2
#arange(start ,end,stepsize)
a1=np.arange(10)
print(a1)

a2=np.arange(1,10,2)
print(a2)

#reshape
a3=np.arange(2,21,2).reshape(5,2)
print(a3)

#linspace
a4=np.linspace(0,10,5) # it divide the 0 to 10 number in 5 equal sectors
print(a4)

a5=np.linspace(0,20,10)
print(a5)

#eye
q1=np.eye(4,dtype='int')
print(q1)

#program 3
q2=np.full((2,3),5)
print(q2)

# Accessing the element from 1 day 

q3=np.array([10,20,30,40,50])
print(q3[1])

print(q3[-1])

a11 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a11[0,2])
print(a11[2,2])