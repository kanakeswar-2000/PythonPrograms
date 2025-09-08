'''
    print a right angled triangle with N rows of stars
'''

N=int(input())

for i in range(1,N+1):
    first_spaces="  "*(N-i)
    stars="* " * i 
    print(first_spaces+stars)