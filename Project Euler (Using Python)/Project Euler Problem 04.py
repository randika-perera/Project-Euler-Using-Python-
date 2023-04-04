L=[]

for a in range(1,1000):
        for b in range(1,1000):
                x=a*b
                s=str(x)
                rs=(str(x))[::-1]
                if s==rs:
                        L.append(x)

print(max(L))

