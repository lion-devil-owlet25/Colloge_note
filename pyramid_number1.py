range1=int(input('\nEnter your range: '))

for i in range(1,range1+1):
    
    for j in range(range1,i,-1):
        print(' ',end='') 

    for k in range(1,i*2):
        print(i,end='')
    
    print()
