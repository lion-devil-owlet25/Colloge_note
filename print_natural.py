range1=int(input("Enter your range: "))

print("The natural numbers upto",range1,":")
for i in range(1,range1+1):
    if i!=range1:
        print(i,end=", ")
    else:
        print(i,end=".")
