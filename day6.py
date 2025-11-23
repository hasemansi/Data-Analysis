import array

arr1=array.array('i',[1,2,3,4,5,6,7,8,9])
arr2=array.array('i',[111,222,333])
print(arr2)
print(arr1)

arr1.append(11)
print(arr1)

print(arr1.count(3))
arr1.extend(arr2)
print(arr1)


#tofile()
import array as arr 
# f=open('myfile.txt','wb');
# arr3=arr.array('i',[1,2,3,4,5,6,7,8])
# print("Array in the file :",arr3)
# arr3.tofile(f)
# f.close()

#fromfile()

#open file for reading
# f=open('myfile.txt','rb')
# #initialize 1 array with integer type
# array1=arr.array('i')
# #initialize 2 array with integer type
# array2=arr.array('i')
# #read 3 items from file
# array1.fromfile(f,3)
# print("Appended array:",array1)
# #Moving the cursor to the first position
# f.seek(0)
# #read 6 items from file
# array2.fromfile(f,6)
# print("Appended array:",array2)
# #close file
# f.close()

#fromlist
lst=[11,22,33,44,55]
array3=arr.array('i')
array3.fromlist(lst)
print(array3)

#fromstring
str2="mansi"
array3.pop()
print(array3)

print(array3.itemsize)
print(array3.typecode)