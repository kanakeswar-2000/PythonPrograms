A=int(input())
B=int(input())
C=int(input())

cond1=A>9 and A<21 
cond2=B>9 and B<21 
cond3=C>9 and C<21 

if (cond1 or cond2 or cond3):
    print("True")
else:
    print("False")