'''
Given N Write a program to print diamond shape using 2 * N -1 rows.
'''

N=int(input())

for i in range(1,N+1):
    first_spaces=" "*(N-i)
    if(i==1):
        row=first_spaces+"*"
       
    else:
        hellow_spaces="  "*(i-2)
        row=first_spaces+"* "+hellow_spaces+"*"
    
    print(row)
        
for j in range(1,N):
    first_spaces=" "*j
    if(j==N-1):
        row=first_spaces+"*"
    else:
        hellow_spaces=" "*(2*(N-j-2))
        row=first_spaces+"* "+hellow_spaces+"*"
    print(row)






