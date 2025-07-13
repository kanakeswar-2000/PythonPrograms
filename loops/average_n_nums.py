'''
    given number N , read N inputs and print the average of N numbers
'''

N=int(input())

sum=0 

for i in range(N):
    num=int(input())
    sum+=num 
average=sum/N 

print(average)




