file = open('temp.txt' , 'r')

'''
read () -> dispaly a file content as it is 
readline () -> dispaly single line of data at a time
readlines() ->  it will display backward slash also 
'''
print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())  #empty list

file.close()