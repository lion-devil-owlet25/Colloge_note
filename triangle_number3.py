range1=int(input('\nEnter your range: '))
start=1
for i in range(1,range1+1):
    for j in range(1,i+1):
        print(start,end='')
        start+=1
    print()
