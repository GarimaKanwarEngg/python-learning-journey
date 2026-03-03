#Hey this is 4th day of learning python
print("Today i gonna learn fron python casting.")
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)


# Create an integer
x = int(1)
# Convert to float
a = float(x)
print(float(x))
# Convert to string
b = str(x)
print(str(x))
# Print values
print(a)
print(x)
print(b)

#strings in python
print("Hello")
print('Hello')
#quotes inside a quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#strings are arrays
a = "Hello, World!"
print(a[1])


#looping in strings
for x in "banana":
  print(x)

  #string length
a = "Hello, World!"
print(len(a))

#slicing strings
#means you can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])
print(b[2:10])
print(b[10])
print(b[2])

#slice from the start
a = "Garima kanwar"
print(a[:5])

#slice to the end
a = "Garima kanwar"
print(a[5:])

#negative indexing
#use negatice indexes to start the slice from the end of the string.
b = "Garimakanwarrr"
print(b[-5:-2])
print(b[-5:])
print(b[:-5])

#modify strings
#python has a set of built-in methods that you can use on strings.
x = "garimakanwarrr"
print(x)
print(a.upper()) #uppercase
print(a.lower()) #lowercase
print(a.strip()) #returns a trimmed version of the string.

#replace string
a = "hold"
print(a)
print(a.replace("h","b"))

#string concatenation
a = "Garima"
b = "Kanwar"
c = a + " " + b
print(c)
