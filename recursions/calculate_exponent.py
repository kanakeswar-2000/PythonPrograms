'''
    write a program to recursively compute the value of A raised to the power of B
'''
A=int(input())
B=int(input())
def calculate_power(A,B):
    if (B==0):
        return 1
    
    return A * calculate_power(A,B-1)


result=calculate_power(A,B)

print(result)