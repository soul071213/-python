# def gcd(a,b):
#     c=0
#     while True:
#         c=a%b
#         a=b
#         b=c
#         if(c==b):
#             break
#     return c/2

# a,b=input().split()
# a=int(a)
# b=int(b)

# print(int(gcd(a,b)))

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)


a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

print(gcd(a,b))