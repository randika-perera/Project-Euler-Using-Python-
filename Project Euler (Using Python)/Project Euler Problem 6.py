sum=0
for x in range(1,101):
        sum=sum+x
squareofsum=sum**2

sumofsquares=0
for x in range(1,101):
        sumofsquares=sumofsquares+x**2

answer=squareofsum-sumofsquares
print(answer)
