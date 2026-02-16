'''
Given a number N , Write a program to print a inverted left angled triangle of N rows using stars(*)
'''

N=int(input()) 

for i in range(N):
    if (i==0):
        print("* "*N)
    elif(i==N-1):
        print("*")
    else:
        spaces="  "* (N-i-2)
        print("* "+spaces+"*")