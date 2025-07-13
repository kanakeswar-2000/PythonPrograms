'''
    print sum of squares of first N natural numbers
'''

N=int(input())

sum_of_squares=0 

for i in range(1,N+1):
    square=i**2 
    sum_of_squares+=square 
print(sum_of_squares)