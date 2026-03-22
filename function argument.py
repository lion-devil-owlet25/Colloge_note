print('Positional arguments')
#Required or Positional arguments
def add_numbers(a, b):
    sum1 = a + b
    print('Sum:', sum1)

add_numbers(2, 3)
#add_numbers(3)
#add_numbers(2, 3,6)
print()


print('Default arguments')
#default arguments
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2.5, 3)

#  function call with one argument
add_numbers(6)

# function call with no arguments
add_numbers()
print()

print('Keyword arguments')
#Keyword arguments
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info('Cartman','Eric')
display_info(last_name = 'Cartman', first_name = 'Eric')
print()

print('Arbitrary arguments')
#Arbitrary arguments
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
find_sum(4)
find_sum(4,9,8,7)
find_sum()







