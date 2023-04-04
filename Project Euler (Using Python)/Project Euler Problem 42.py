TriangleNumberList=[]
for n in range(1,100):
        temp=int(0.5*(n)*(n+1))
        TriangleNumberList.append(temp)


f=open('words.txt','r')
filecontent=f.read()
s=filecontent.split(',')
namelist=[]
for x in s:
        name=x.strip('""')
        namelist.append(name)

count=0

for word in namelist:
        wordsum=0
        for letter in word:
                wordsum=wordsum+ord(letter)-64
        if wordsum in TriangleNumberList:
                count=count+1

print(count)
