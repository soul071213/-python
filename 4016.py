def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)


a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

print(gcd(gcd(a,b),c))