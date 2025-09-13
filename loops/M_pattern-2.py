'''
 Given a number N write a program to print letter M with *'s using two pyramids with N rows
'''
N=int(input())

for i in range(1,N+1):
    first_spaces=" "*(N-i)
    mid_spaces=" "*(2 *(N-i)-1) 
    stars="* "*i 
    print(first_spaces+stars+mid_spaces+stars)
