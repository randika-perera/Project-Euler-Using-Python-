def digitsum(number):
        s=str(number)
        tot=0
        for x in s:
                tot=tot+int(x)
        return tot

maxdigitalsum=0

for a in range(1,100):
        for b in range(1,100):
                temp=a**b
                d=digitsum(temp)
                if d>maxdigitalsum:
                        maxdigitalsum=d

print(maxdigitalsum)
