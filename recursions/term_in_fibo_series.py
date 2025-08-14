'''
    recursively find N th term in fibonacci series
'''
n=int(input())
def fibonacci(n):
    if (n<=1):
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

result=fibonacci(n)
print(result)
