x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

x = ["apple", "banana"]

print("banana" in x)
print("apple" in x)
print("carrot" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
print("apple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
print("Apple" not in fruits)
print("apple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("e" in text)
print("Hello" in text)
print("z" not in text)

print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)