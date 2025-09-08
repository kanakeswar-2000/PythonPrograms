''''
    write a program to print inverted pyramid with stars
'''

N=int(input())

for i in range(N):
    spaces=" "*i 
    stars="*"*(2*N-1)
    print(spaces+stars)
    N=N-1