M=int(input())
P=int(input())
C=int(input())

condition1=M>=35 and P>=35 and C>=35 # all pass
condition2=M+P>=90 or P+C>=90 or C+M>=90 # scoring good 

result=condition1 and condition2 # all pass with good score 
print(result)