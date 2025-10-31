'''
write a program to read the number N and print the diamond symbol with numbers
'''

N=int(input())

for i in range(1,N+1):
    spaces=" "*(N-i)
    num=str(i)
    row=spaces+(num+" ")*i
    print(row)
    
for i in range(1,N):
    spaces=" "*i
    num=str(N-i)
    row=spaces+(num+" ")*(N-i)
    print(row)




