'''
Given two numbers X and N write a program to print sum of N terms in th given series 
     
    X2 , -X4 ,X6 ,....N terms

'''

X=int(input())
N=int(input())

sum1=0 
sum2=0 

for i in range(1,N+1):
    if (i%2==1):
        sum1=sum1+X**(2*i)
    else:
        sum2=sum2+X**(2*i)

total_sum=sum1-sum2 

print(total_sum)
