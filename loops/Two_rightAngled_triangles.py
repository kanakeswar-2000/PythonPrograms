'''
    Write a program to take number N as input and print 2N rows in triangles format
'''

N=int(input())

for i in range(1,N+1):
    print("* "*i)

for i in range(N):
    print("* "*N)
    N=N-1 