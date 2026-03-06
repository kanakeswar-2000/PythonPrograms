''''
Given an integer N , write a program to print butterfly with 2 * N rows
'''

N=int(input())

for i in range(1,N+1):
    mid_spaces=2 * (N-i)
    if(i==1):
        row="* "+"  "*mid_spaces+"*"
    else:
        hellow_spaces=2 * (i-2)
        row="* "+" "*hellow_spaces+"* "+"  "*mid_spaces+"* "+" "*hellow_spaces+"*"
    print(row)

for j in range(1,N+1):

    if(j==N):
        row="* "+"  "*mid_spaces+"*"
    else:
         
        row="* "+" "*hellow_spaces+"* "+"  "*mid_spaces+"* "+" "*hellow_spaces+"*"
    mid_spaces+=2
    hellow_spaces-=2
    print(row)