'''
    print factorial of given number N
'''

N=int(input())

factorial=1 

for i in range(1,N+1):
    factorial=factorial * i 
print(factorial)
