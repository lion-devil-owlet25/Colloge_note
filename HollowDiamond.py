range1=int(input('\nEnter your range: '))

for i in range(1,range1+1):
    
    for j in range(range1-1,i-1,-1):
        print(' ',end='')

    for k in range(1,2*i):
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
        
    print()


for i in reversed(range(1,range1)):
    for j in range(i,range1):
        print(' ',end='')    
    
    for k in range(2*i-1,0,-1):
        if k==1 or k==2*i-1:

            print('*',end='')
        else:
            print(' ',end='')
    print()

