def ntriangle(num):
        tot=int(num*(num+1)/2)
        return tot

def factorcount(x):
        factorcount=0
        for r in range(1,x+1):
                if x%r==0:
                        factorcount=factorcount+1
        return factorcount

p=1
status=True
while status==True:
        t=ntriangle(p)
        print('Triangle Number',p,'=',t,end='\t\t')
        f=factorcount(t)
        print('Factor Count :',f)
        if f>200:
                status=False
        p=p+1

print()
print('Answer :',t)
