'''
Given a number N . Write a program to print Right Angled Triangle of N rows using 
dots (".") in the borders and zeros ("0") inside the triangle.
'''
N=int(input())

for i in range(1,N):
    if (i==1 or i==2):
        print(". "*i)
    else:
        zeros="0 "*(i-2)
        print(". "+zeros+".")
print(". "*N)

