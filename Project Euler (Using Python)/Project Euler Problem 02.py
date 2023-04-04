
fiblist=[1,2]
while fiblist[-1]<4000000:
        newvalue=fiblist[-1]+fiblist[-2]
        fiblist.append(newvalue)

eventotal=0
for x in fiblist:
        if x%2==0:
                eventotal=eventotal+x
print(eventotal)
