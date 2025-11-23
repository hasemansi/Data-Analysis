import os
print(os.getcwd()) # give the path of the current directory

#program 2
print(os.listdir())
print(os.listdir("C:/Users/hi/Documents/Desktop/Minskole classes"))

#make new directory
# os.mkdir('mypack') #create a folder
# os.makedirs("mypack3/pack2/pack1")

#remove the directory
# os.rmdir('mypack')
# os.removedirs('mypack3/pack2/pack1')

# check if path is a file or folder
print(os.path.isdir('mypack'))
print(os.path.isfile('day6.py'))
print(os.path.isdir('day6.py'))

# os.makedirs('mypack2/pack1')
print(os.getcwd())
print(os.chdir("C:/Users/hi/Documents/Desktop/Minskole classes/data analysis"))