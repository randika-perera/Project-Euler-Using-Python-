##        NW_Pattern=4*n**2-6*n+3
##        NE_Pattern=4*n**2-4*n+1
##        SW_Pattern=4*n**2-8*n*5
##        SE_Pattern=4*n**2-10*n+7

diagonalsize=1001
end=(diagonalsize//2+1)+1

NW_sum=0
for n in range(1,end):
        NW_sum=NW_sum+4*n**2-6*n+3

NE_sum=0
for n in range(1,end):
        NE_sum=NE_sum+4*n**2-4*n+1

SW_sum=0
for n in range(1,end):
        SW_sum=SW_sum+4*n**2-8*n+5

SE_sum=0
for n in range(1,end):
        SE_sum=SE_sum+4*n**2-10*n+7

Diagonal_sum=NW_sum+NE_sum+SW_sum+SE_sum-4+1

print(Diagonal_sum)


