'''
Given a number N , write a program to print pyramid of N rows using numbers
'''

N=int(input())

for i in range(1,N+1):
    numbers=(str(i)+" ")*i
    spaces=" "*(N-i)
    print(spaces+numbers) 
