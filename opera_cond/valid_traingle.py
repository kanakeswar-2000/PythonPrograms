A=int(input())
B=int(input())
C=int(input())

is_condition1_valid=A+B>C
is_condition2_valid=B+C>A 
is_condition3_valid=C+A>B 

is_valid_traingle=is_condition1_valid and is_condition2_valid and is_condition3_valid 

print(is_valid_traingle)