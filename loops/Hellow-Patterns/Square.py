'''
Given an integer N , write a program to square with N rows using "*" as borders
and "0" inside.
'''

N=int(input())

zeros="0 "*(N-2)

for i in range(N):
    if (i==0 or i==N-1):
        print("* "*N)
    else:
        print("* "+zeros+"*")
