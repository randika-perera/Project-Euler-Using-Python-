def fact(n):
        if n==1:
                return 1
        else:
                return n*fact(n-1)

num=fact(100)
snum=str(num)
digitsum=0
for x in snum:
        digitsum=digitsum+int(x)
print(digitsum)
