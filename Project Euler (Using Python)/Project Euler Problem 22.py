def namevalue(name):
        val=0
        for l in name:
                lv=ord(l)-64
                val=val+lv
        return val
        

f=open('names.txt','r')
namelist=[]
s=f.read()
L=s.split(',')
N=[]
for p in L:
        temp=p.strip('""')
        N.append(temp)


namelist=sorted(N)
sumnamescores=0

for x in range(0,len(namelist)):
        namescore=(x+1)*namevalue(namelist[x])
        sumnamescores=sumnamescores+namescore

print(sumnamescores)
        
