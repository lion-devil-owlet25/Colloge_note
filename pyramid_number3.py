range1=int(input('\nEnter your range: '))
count=0
count1=0
for i in range(1,range1+1):
    
    for j in range(range1,i,-1):
        print(' ',end='') 
        count+=1
    for k in range(0,i*2-1):
        if count<=range1-1:
            print(i+k,end='')
            count+=1
        else:
            count1+=1
            print(i+k-2*count1,end='')
    count1=count= 0
    print()
