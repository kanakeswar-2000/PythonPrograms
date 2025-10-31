'''
write a program to read the number N and print a right angled triangle with N rows
'''

N=int(input())

for i in range(N):
    spaces="  "*i 
    stars="* "*(N-i)
    print(spaces+stars)


