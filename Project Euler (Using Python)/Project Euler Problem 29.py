L=[]
for a in range(2,101):
        for b in range(2,101):
                L.append(a**b)
S=set(L)
LL=list(S)
LL.sort()
print(LL)
print('Size :',len(LL))
