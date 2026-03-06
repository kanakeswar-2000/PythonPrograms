'''
Given an integer N , write a program to print Pyramid using N rows
'''
N=int(input())

for i in range(N):
    first_spaces=" "*(N-i-1)
    hellow_spaces=" "*(2*i-1)
    if(i==0):
        row=first_spaces+"*"
    elif(i==N-1):
        row= "* "* N
    else:
        row=first_spaces+"*"+hellow_spaces+"*"
    print(row)