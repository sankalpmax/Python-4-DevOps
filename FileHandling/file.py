# creating a file and setting in read mode

file = open("sankalp.txt","r")     
content_read = file.read()         # reading the content of the file line by line
content_read = file.readline()     
content_read = file.readlines() 
print(content_read)


# Wrting the contents inside the file by write mode

file = open("sankalp.txt" , "w")                    # file in write mode 
file.write(" i love making projects on devops!\n")  # contents will be on sankalp.txt file
print(file)

# Writing contents at the end by using append mode

file = open("sankalp.txt" , "a")
file.write("New content\n")
print(file)

file.close()                       # closing the file
