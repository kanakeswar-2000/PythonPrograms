'''
    sum of even numbers from M to N
'''

M=int(input())
N=int(input())
sum_of_even_numbers=0
for i in range(M,N+1):
    if (i%2==0):
        sum_of_even_numbers+=i 
print(sum_of_even_numbers)


