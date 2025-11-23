# # difference between array and list
# import array

# x=array.array('i',[1,2,3,4,5,6,7,8,9])

# print(x[0:-4])
# print(x[0:7:2])

# #program 1
# print(x)
# print(type(x))

# #indexing and slicing
# #x[start:stop:stride]
# z=x[1:4]
# print(z)

# b=x[0:]
# print(b)

# c=x[:4]
# print(c)

# #program 3
# import array

# h1=array.array('i',[11,22,33,44,55,66,77,88,99])
# h1=h1[1:4]
# print(h1)
# for x in h1[1:4]:
#     print(x)

# for x in h1[6:]:
#     print(x)


import array
h11=array.array('i',[11,22,33,44,55,66,77])
h11.append(33)
print(h11)

e1=h11.count(33)
print(e1)

h11.insert(6,89)
print(h11)

h11.remove(77)
h11.pop()
print(h11)