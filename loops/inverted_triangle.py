'''
    write program to take number N as input and print N rows in inverted triangle format 
'''

N=int(input())

for i in range(N):
    print("* " * N)
    N=N-1