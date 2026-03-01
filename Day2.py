#Hello, This is Day 2 of Learning Python.
#Python Tutorial
#Python HOME
#Python Intro
#Python Get Started
#Python Syntax
#Python Output
#Python Comments
#yesterday i learned about all these.

#Today i will start learning from variables.
print("Variables are containers for storing data values.")
x = 7
y = "Garima Kanwar"
print (x)
print(y)
print("Variables do not need to be declared with any particular type, and can even change type after they have been set.")
x = 7 #x is of type int
print(x)
x = "Garima Kanwar" #x is now of type str
print(x)

#casting
print("If you want to specify the data type of a variable, this can be done with casting.")
x = str(3) # s will be '3'
y = int(3) #y will be 3
z = float(3) # x will be 3.0
print (x)
print(y)
print(z)

#get the type
print("you can get the data type of a variable with the type() funcation")
x = 7
y = "Garima Kanwar"
print(type(x))
print(type(y))
z = "Hey my name is garima" , 16 , "is my age"
print(type(z))

#single or double quotes
print("String variables can be declared wither by using single or double quotes")
x = "Garima kanwar"
y = 'Garima kanwar'
print(x)
print (y)
print("x and y both are the same")


#case sensitive
print("variables names are case sensitive.")
a = 7
A = "Gairma kanwar"
print("These are two different variables.")
print(a)
print(A)


#variable names
print("A variable can have a short name or a more descriptinve name(age.carname, total_Volume).")
print("Rules of python variables")
print("A variable name must start wit a letter or the underscore character.")
print("A variable name cannot start with a number.")
print("A variable name can only contain alpha - numeric charavters and underscores (A-x, 0-9, and _)")
print ("Varibale names are case sensitive (age, Age and AGE are three different variables.")
print("A variable can not be any of hte python keywords")

#multiwords variables names
print("Variable names with more than one word can be difficult to read.")
print("For this we use several techniques")
print( "1. Camel Case : Each word, expect the first, starts with a capital letter ")
myVariableName = "Garima"
print(myVariableName)
print("2. Pascal Case : Each word starts with a capital Letter")
MyVariableName = "Garima"
print(MyVariableName)
print("3. Snake Case : Each word is separated by an underscore character")
my_variable_name = "Garima" 
print(my_variable_name)
