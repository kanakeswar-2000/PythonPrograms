A=int(input())
B=int(input())

R1=A%B
R2=B%A 

if (R1<R2):
    print(R1)
else:
    print(R2)