range1=int(input("Enter your range:"))

for i in range(1,range1+1):
    for j in range(range1,i,-1):
        print(' ',end='')
    for k in range(0,i*2-1):
        print("*",end="")
    print()

for i in range(range1-1,0,-1):
    for j in range(i,range1):
        print(' ',end='')    
    
    for k in range(2*i-1,0,-1):
        print("*",end="")
    print()
