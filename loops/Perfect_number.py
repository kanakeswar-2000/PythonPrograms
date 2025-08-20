'''
    Write a program to check whether the number is a perfect number or not
    A number is a perfect number , when sum of all factors of the number (except the number) is the number itself
'''

N=int(input())

sum=0

for i in range(1,N):
    if (N%i==0):
        sum=sum+i 

if (sum==N):
    print("Perfect Number")
else:
    print("Not a Perfect Number")