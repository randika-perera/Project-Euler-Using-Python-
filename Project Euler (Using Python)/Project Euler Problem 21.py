def sumofdivisors(num):
        L=[]
        for n in range(1,num):
                if num%n==0:
                        L.append(n)
        return sum(L)

usednumlist=[]
amicablelist=[]
sumdlist=[]

for x in range(1,10000):
        usednumlist.append(x)
        temp=sumofdivisors(x)
        if temp in usednumlist and sumofdivisors(temp)==x and x!=temp:
                amicablelist.append(temp)
                amicablelist.append(x)
print(amicablelist)
print('Sum :',sum(amicablelist))
