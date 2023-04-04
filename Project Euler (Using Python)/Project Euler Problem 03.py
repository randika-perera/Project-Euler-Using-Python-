num=600851475143

for d in range(1,num+1):
        if num%d==0:
                f=d
                temp=int(f**0.5)+1
                for n in range(2,temp):
                        if f%n==0:
                                break
                else:
                        print(f)
