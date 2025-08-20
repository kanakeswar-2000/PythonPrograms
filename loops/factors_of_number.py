'''
    write a program to print factors of a number in horizontal line
'''

N=int(input())

factors=""

for i in range(1,N+1):
    if (N%i==0):
        factors+=str(i)+" "

print(factors)

