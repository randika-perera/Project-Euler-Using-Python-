total=0
for x in range(1,1001):
        total=total+x**x

s=str(total)

ans=s[-10::]

print(ans)
