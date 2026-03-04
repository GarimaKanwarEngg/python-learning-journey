#Python Tutorial
#Python HOME
#Python Intro
#Python Get Started
#Python Syntax
#Python Output
#Python Comments
#Python Variables
#Python Data Types
#Python Numbers
#Python Casting
#Python Strings
#Python Booleans
#P#ython Operators
#Python Operators
#Arithmetic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators

print("Till now i have learned all these topics")
print("Todayy i'll start from identity operators.")
print("Identity Operators")
print("These are useed to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#The is not operator returns True if both variables do not point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#python membership operators
print("Membership operators are used to test if a sequence is presented in an object : in or not in")
