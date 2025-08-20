'''
    A number is an Armstrong number only when sum of powers of all the digits is the number itself,
      where power is no of digits in the number
'''

N=input()

K=len(N)

sum=0 

for digit in N:
    sum=sum + int(digit) ** K 

N=int(N)

if (sum==N):
    print("Armstrong Number")

else:
    print("Not an Armstrong Number")