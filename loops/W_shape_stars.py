'''
write a program to read number N and print w shape with N rows using stars
'''

N=int(input())

print("* " *(2*N-1))

for i in range(1,N):
    spaces=" "*i
    stars="* "*(N-i) 
    mid_spaces=" "*(2*(i-1))
    print(spaces+stars+mid_spaces+stars)
