'''
    Write a program to recursively return a list of N fibonacci terms
'''

N=int(input())

def fibonacci(n):
    if (n<=1):
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

def get_fibonacci_series(N):
    fibonacci_series=[]
    for i in range(N):
        term=fibonacci(i)
        fibonacci_series.append(term)
    return fibonacci_series 

result=get_fibonacci_series(N)

print(result)
