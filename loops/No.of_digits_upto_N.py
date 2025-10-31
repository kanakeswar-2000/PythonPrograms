'''
Write a program to read the number N and finds the count of digits from 1 to N
'''

N=int(input())

count_of_digits=0 

for i in range(1,N+1):
    num=str(i)
    digits=len(num)
    count_of_digits+=digits 

print(count_of_digits)