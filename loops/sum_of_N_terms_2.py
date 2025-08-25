'''
write a program to print sum of N terms in X series 
    X,XX,XXX,....N terms
'''
N=int(input())

X=input()

sum=0 

for i in range(1,N+1):
    term=int(X *i)
    sum+=term 

print(sum)