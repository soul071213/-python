n=input()
r_n=n[::-1]
sum = int(n)+int(r_n)

if str(sum) == str(sum)[::-1]:
    print("YES")
else:
    print("NO")