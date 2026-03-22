range1=int(input('\nEnter your range: '))
ch=65
for i in range(1,range1+1):
    for j in range(1,i+1):
        print(chr(ch),end='')
    ch+=1
    print()
