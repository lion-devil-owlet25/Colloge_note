# while loop example

# calculate the number of digits

num = int(input("Enter the number: "))
num1 = num

no_digits=0

while num!=0:
    no_digits = no_digits+1
    num = num //10
    
print("The number of digits in",num1,"is",no_digits)
