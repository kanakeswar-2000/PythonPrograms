'''
    Given a number N , write a program to print pyramid of 2*N-1 rows using + and # 
'''

N=int(input())

for i in range(N):
    no_of_spaces=N-i-1 
    no_of_pluses=i
    print("  "*no_of_spaces+"+ "*no_of_pluses+"#")

for i in range(1,N):
    no_of_pluses=N-i-1
    print("  "*i+"+ "*no_of_pluses+"#")







