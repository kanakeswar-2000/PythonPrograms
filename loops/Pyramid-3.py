'''
   Given a number N , write a program to print a pyramid of 2 * N -1 rows using numbers
'''

N=int(input())

for i in range(1,N+1):
    print((str(i)+" ")*i)

for i in range(1,N):
    num=N-i
    print((str(num)+" ")*(N-i))