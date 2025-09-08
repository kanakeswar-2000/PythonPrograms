'''
    given a number N ,write a program to print N rows with stars in pyramid format
'''

N=int(input())

for i in range(1,N+1):
    spaces="  "*(N-i)
    stars="* "*(2*i-1)
    print(spaces+stars)