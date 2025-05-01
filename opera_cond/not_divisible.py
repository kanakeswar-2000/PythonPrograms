N=int(input())

# check whether N is not divisible by 2,3,5,7
R1=N%2
R2=N%3
R3=N%5
R4=N%7 

if (R1!=0 and R2!=0 and R3!=0 and R4!=0):
    print(True)
else:
    print(False)