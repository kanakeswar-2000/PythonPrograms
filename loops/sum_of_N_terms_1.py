'''
Given an interger N write a program to print sum of N terms in the series 
    2,22,222,....N terms
'''

N=int(input())

sum=0
for i in range(1,N+1):
    term=int("2"*i)
    sum+=term 
print(sum)