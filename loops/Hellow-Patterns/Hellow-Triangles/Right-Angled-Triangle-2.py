'''
Given an integer N , write a program to print Right Angled Triangle of N rows 
using stars(*) , pipe(|) , slash(/) 
'''

N=int(input())

for i in range(1,N+1):
    if(i==1):
        print("- "*N) 
    else:
        spaces="  "*(N-i) 
        print("| "+spaces+"/")