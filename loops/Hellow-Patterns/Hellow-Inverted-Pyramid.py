'''
Given an integer N , write a program to print inverted pyramid with N rows.
'''


N=int(input())

for i in range(N):
    if(i==0):
        row="* "* N
    elif(i==N-1):
        first_spaces=" "*i
        row=first_spaces+"*"
    else:
        first_spaces=" "*i
        hellow_spaces=" "*(2*(N-i-2))
        row=first_spaces+"* "+hellow_spaces+"*"
    
    print(row)
        



