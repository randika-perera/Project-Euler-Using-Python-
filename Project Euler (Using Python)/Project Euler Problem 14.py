import sys

def collatzcount(num):
        global count
        if num==4:
                count=count+3
        else:
                if num%2==0:
                        count=count+1
                        return collatzcount(num//2)
                else:
                        count=count+1
                        return collatzcount(3*num+1)
        return count




maxcount=0
maxcountnum=0
number=1
while number<1000000:
        count=0
        c=collatzcount(number)
        if c>maxcount:
                maxcount=c
                maxcountnum=number
        number=number+1

print(maxcountnum)
        
        
