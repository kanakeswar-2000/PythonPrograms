M=int(input())
P=int(input())

condition1=M>35 and P>35 
condition2=M+P >=100 

if (condition1 or condition2):
    print("Qualified")
else:
    print("NOT Qualified")