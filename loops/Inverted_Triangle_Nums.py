'''
Given a number N , print inverted triangle with numbers
'''

N=int(input())

for i in range(N):
    spaces=" "*i 
    numbers=str(N)*N 
    print(spaces+numbers)
    N=N-1