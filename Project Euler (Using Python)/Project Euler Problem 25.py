L=[1,1]
temp=0

while len(str(temp))<1000:
        temp=L[-1]+L[-2]
        L.append(temp)
print(L)
print('Number :',L[-1],end='\t')
print('Index :',len(L))
