# Armstrong Number.

def power(x,y):
    pw=1
    for i in range(1,y+1):
        pw=pw*x
    return pw

def isArmstrong(num):
    
    num1=num2=num
    no_of_dig=0

    while num!=0:
        no_of_dig+=1
        num=num//10
    sum=0

    while num1!=0:
        rem=num1%10
        sum=sum+power(rem,no_of_dig)
        num1=num1//10

    if num2==sum:
        return True
    else:
        return False

number=int(input("Enter your Number:"))

if isArmstrong(number):
    print(str(number)+" is an Armstrong number.")
else:
    print(str(number)+" is not an Armstrong number.")
