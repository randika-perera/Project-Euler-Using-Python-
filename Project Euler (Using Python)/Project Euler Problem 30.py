L=[]
num=2

while True:
        s=str(num)
        tot=0
        for x in s:
                tot=tot+int(x)**5
        if tot==num:
                L.append(num)
                print(L)
        num=num+1
