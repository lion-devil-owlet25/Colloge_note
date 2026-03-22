#A simple calculator.

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))

print('''Press 1 for Addition
         Press 2 for Subtraction
         Press 3 for Multiplication
         Press 4 for division''')
choice = int(input('Enter your choice: '))

if choice == 1:
    sum1 = number1+number2
    print('The sum of',number1,"and", number2,"is",sum1)
elif choice == 2:
    diff = number1-number2
    print('The difference of',number1,"and", number2,"is",diff)
elif choice == 3:
    prod = number1*number2
    print('The product of',number1,"and", number2,"is",prod)
elif choice == 4:
    if number2!=0:
        quot = number1/number2
        print('The quotient of',number1,"and", number2,"is",quot)
    else:
        print("We can not divide a number by zero.")
else:
    print('Invalid Choice.')
