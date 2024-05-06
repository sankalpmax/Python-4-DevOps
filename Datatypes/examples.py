# Varibales and Basic opeartions

a = 10
b = 20
sum_result = a + b
diff_result = a - b
mul_result = a*b
div_result = a/b 


print(sum_result, diff_result, mul_result ,div_result)

# LIST (Creating a list and manipulating)

my_list = (10 , 20 , 30 , 40 , 50)
print(" list of num:" , my_list)
print(" accessing num at:",my_list[2])

my_list = list(my_list)                     # modifying the list 
my_list[2] = 60                             # converting tuple to list
print("modified list: ",my_list)

my_list.append(70)                   # append adding value to the list
print(my_list)              
my_list.remove(20)                   # removing the value fromt the list 
print(my_list)


# TUPLE data type (creating and accessing tuple)

my_tuple = (10 , 20 , 30 , 40)
print("my elements in tuple: " , my_tuple)
print("specified element: " , my_tuple[2])

# DICTONARY data types (creating a dictonary values)

my_dict = {"name" : "sankalp" , "age" : 24 , "gender":"male"}
print("my personal data: ", my_dict)  # printing the key value
print("my name:", my_dict["name"])    # accessing the key value
print("my age:", my_dict["age"])      # accessing the key value

my_dict["email"] = "sankalparava619@gmail.com"   # adding new key value to the dict
print("my mail id updated:", my_dict)

# SET data types (creating a operating on set)

my_set = {10, 20 , 30 , 40 , 50}
print(my_set)
my_set.add(60)
print(my_set)

