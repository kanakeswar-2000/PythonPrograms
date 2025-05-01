N=int(input())

R1=N%5 
R2=N%7 

if (N<7 or (R1==0 and R2==0)): # N should be divisible by 5 and 7 or lessthan 7 
    print(N)
else:
    print(R1)
    print(R2)