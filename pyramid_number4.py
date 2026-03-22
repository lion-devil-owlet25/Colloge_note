range1=int(input('\nEnter your range: '))

for i in range(1,range1+1):
    
    for j in range(range1,i,-1):
        print(' ',end='') 
        
    for k in range(1,i+1):
        print(k,end='')
        
    for l in range(i-1,0,-1):
        print(l,end='') 
    print()
