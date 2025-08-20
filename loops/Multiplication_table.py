'''
    write a multiplication table for the given number upto 10
'''

N=int(input())

for i in range(1,11):
    M=int(N) * i
    each_line="{} + {} = {}".format(N,i,M)
    print(each_line)