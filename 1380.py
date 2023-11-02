a=int(input())

for i in range(1,a,1):
    if(i>6):
        continue
    if(a-i>6):
        continue
    print(i,a-i)
    
