'''
Given a number N , write a program to print a inverted right angled triangle of N rows using stars(*)
'''

N=int(input()) 

for i in range(N):
    first_spaces="  "*i 

    if(i==0):
        print("* "*N) 

    elif (i==N-1):
        print(first_spaces+"* ")
    else:
        hellow_spaces="  "*(N-i-2)
        print(first_spaces+"* "+hellow_spaces+"*")







