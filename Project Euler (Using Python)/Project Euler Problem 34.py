L=[]
x=3

from math import *

while True:
        s=str(x)
        tot=0
        for d in s:
                tot=tot+factorial(int(d))
        if tot==x:
                L.append(x)
                print(L)
        x=x+1
        


        
