'''
Given a number N , Write a program to print right angled triangle of N rows using stars(*)
'''

N=int(input())

for i in range(N):

    first_spaces="  "*(N-i-1) 

    if (i==0):
        print(first_spaces+"*")
    elif (i==N-1):
        print("* "*N) 
    else:
        hellow_spaces="  "*(i-1) 
        print(first_spaces+"* "+hellow_spaces+"*") 







