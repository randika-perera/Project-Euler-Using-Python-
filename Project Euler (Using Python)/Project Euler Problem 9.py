import sys

for a in range(1000):
        for b in range(a):
                for c in range(b):
                        if a**2==b**2+c**2 and a+b+c==1000:
                                print('a =',c)
                                print('b =',b)
                                print('c =',a)
                                print('abc =',a*b*c)
                                sys.exit()
