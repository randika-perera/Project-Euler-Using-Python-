import time
start=time.time()


def div(rem,num):
        global digitlist
        q=rem//num
        r=rem%num
        if r==0:
                digitlist=[]
                return
        else:
                if len(digitlist)>0 and (r in digitlist):
                        if r==digitlist[-1]:
                                return
                        else:
                                i=digitlist.index(r)
                                nextdigit=digitlist[i+1]
                                p=(10*r)%num
                                if p==nextdigit:
                                        return
                else:
                        digitlist.append(r)
                        return div(10*r,num)

maxrecurringpartsize=0
currentnum=1

print('Size of recurring part')
for x in range(2,1001):
        digitlist=[]
        div(1,x)
        print(str(1)+'/'+str(x),'\tRecurring part size =',len(digitlist))
        if len(digitlist)>maxrecurringpartsize:
                maxrecurringpartsize=len(digitlist)
                currentnum=x

print()
print('Longest recurring cycle')
print(str(1)+'/'+str(currentnum),'\tRecurring part size =',maxrecurringpartsize)


end=time.time()
print()
timeelapsed=end-start
print('Time taken for execution  = ',timeelapsed)
