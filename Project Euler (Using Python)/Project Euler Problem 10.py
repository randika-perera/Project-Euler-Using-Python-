import time
start=time.time()



primelist=[]
num=2
while num<2000000:
        temp=int(num**0.5)+1
        for r in range(2,temp):
                if num%r==0:
                        break
        else:
                primelist.append(num)
        num=num+1
print('Answer :',sum(primelist))




end=time.time()
elapsed=end-start
print('Time elapsed :',elapsed)
