primecount=0
num=2

while primecount<10001:
        temp=int(num**0.5)
        for r in range(2,temp+1):
                if num%r==0:
                        break
        else:
                print('Prime Number : ',num,end='\t')
                primecount=primecount+1
                print('PN# :',primecount)
        num=num+1
