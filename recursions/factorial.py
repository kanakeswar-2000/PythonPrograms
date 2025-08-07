def compute_factorial(N):
    if (N==1):
        return 1 
    return N * compute_factorial(N-1)

N=int(input())

factorial=compute_factorial(N)

print(factorial)