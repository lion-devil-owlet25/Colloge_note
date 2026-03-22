#Python String Operations
#Compare Two Strings

str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"
str4 = "hello, world!"
# compare str1 and str2
print(str1 == str2)
str2=str1
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)
print(str1 == str4)

#Join Two or More Strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

#Iterate Through a Python String
greet = 'Hello'
# iterating through greet string
for letter in greet:
    print(letter)

#Python String Length

greet = 'Hello'

# count length of greet string
print(len(greet))

#String Membership Test

print('a' in 'program') 
print('at' not in 'battle')

