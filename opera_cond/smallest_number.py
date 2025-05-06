A=int(input())
B=int(input())
C=int(input())

A_smallest=A<B and B<C 
B_smallest=B<C 

if A_smallest:
    print(A)
elif B_smallest:
    print(B)
else:
    print(C)
    