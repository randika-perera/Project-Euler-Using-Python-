def palindromecheck(x):
        s=str(x)
        if s==s[::-1]:
                return True
        else:
                return False

L=[]

for n in range(1,1000000):
        decimalN=n
        if palindromecheck(decimalN):
                b=bin(n)
                binaryN=b.lstrip('0b')
                if palindromecheck(binaryN):
                        L.append(n)

print(L)
print()
print(sum(L))
