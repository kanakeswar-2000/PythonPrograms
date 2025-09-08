'''
    write a program to print pyramid with numbers given N as number
'''

N=int(input())
count=1
for i in range(1,N+1):
    spaces=" "*(N-i)
    numbers=(str(i)+" ")* count
    print(spaces+numbers)
    count=count+1