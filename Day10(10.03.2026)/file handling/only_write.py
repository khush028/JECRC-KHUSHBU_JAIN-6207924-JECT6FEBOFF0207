# file = open('temp.txt' , 'w+')
# # file.write("I am the first line")
# file.writelines([
#     'I am the new data \n' ,
#     'sec line \n',
#     'I am new data'
# ])
# file.seek(0)   # if we don't right this it will point to last line that's why blank space it will take back to 0 , specific index 
# print(file.read())

# file.close()


file = open('notes.txt','r')
print(file.read())   # if the file not present and we want to read the data then it will show error (FileNotFoundError)
file.close()