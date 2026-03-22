# create a string using double quotes
string1 = "Python programming"
print(string1)
print()

# create a string using single quotes
string1 = 'Python programming'
print(string1)
print()

greet = 'hello'
#indexing
# access 1st index element
print(greet[1]) # "e"
#negative indexing
# access 4th last element
print(greet[-4]) # "e"

#Slicing

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"
print(greet[:4])  # "Hell"
print(greet[1:])  # "ello"
print(greet[:])  # "Hello"

#Python Strings are immutable

message = 'Hello Friends'

#message[0] = 'h'
print(message)
# assign new string to message variable
message = 'I love Python'
print(message); # prints "Hello Friends"

# multiline string 
message = """
Never gonna give you up
         Never gonna let you down
"""

print(message)

