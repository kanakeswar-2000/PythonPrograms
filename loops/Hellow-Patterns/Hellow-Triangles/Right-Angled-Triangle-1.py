''' 
Given an integer N , write a program to print right angled triangle of N rows using "*" s

'''

N=int(input()) 

for i in range(1,N+1):
    if (i==1 or i==2 or i==N):
        print("* "*i)
    else:
        spaces="  "*(i-2) 
        print("* "+spaces+"* ")
    