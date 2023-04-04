numerator=1
denominator=1

for x in range(10,100):
        for y in range(10,100):
                a=str(x)
                b=str(y)
                if a[0]!=0:
                        a0=int(a[0])
                if a[1]!=0:
                        a1=int(a[1])
                if b[0]!=0:
                        b0=int(b[0])
                if b[1]!=0:
                        b1=int(b[1])
                try:
                        if a1!=0 and b1!=0 and x/y<1:
                                if a0==b0 and x/y==a1/b1 and a1!=b1 : 
                                        print(x,'/',y)
                                        numerator=numerator*x
                                        denominator=denominator*y
                                if a0==b1 and x/y==a1/b0 and a1!=b0 :
                                        print(x,'/',y)
                                        numerator=numerator*x
                                        denominator=denominator*y
                                if a1==b0 and x/y==a0/b1 and a0!=b1 :
                                        print(x,'/',y)
                                        numerator=numerator*x
                                        denominator=denominator*y
                                if a1==b1 and x/y==a0/b0 and a0!=b0 :
                                        print(x,'/',y)
                                        numerator=numerator*x
                                        denominator=denominator*y
                except ZeroDivisionError:
                        pass
                        
print()
print('Numerator :',numerator)
print('Denominator :',denominator)

