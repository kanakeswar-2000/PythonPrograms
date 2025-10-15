'''
Given an integer N , write a program to print butterfly using 2N-1 stars 
'''

N=int(input())

for i in range(1,N+1):
    stars="* "*i
    spaces="  "*(N-i)*2
    print(stars+spaces+stars)

for i in range(1,N):
    stars="* "*(N-i)
    spaces="  "*i*2
    print(stars+spaces+stars)