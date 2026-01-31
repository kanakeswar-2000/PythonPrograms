'''
Given numbers M and N , write a program to print a rectangle of M rows and N columns
with "*" in the borders and "0" inside the rectangle.
'''

M=int(input())

N=int(input())

zeros="0 "*(N-2)

for i in range(M):
    if (i==0 or i==M-1):
        print("* " * N)
    else:
        print("* "+zeros+"*")
        