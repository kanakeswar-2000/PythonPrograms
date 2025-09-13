'''
 Given a number N write a program to print M with *'s using two right angled triangles with N rows
'''

N=int(input())

for i in range(1,N+1):
    stars="* "*i 
    spaces="  "* 2 * (N-i)
    print(stars+spaces+stars)