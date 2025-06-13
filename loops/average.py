'''
    read the N numbers and find the average of N numbers
'''

N=int(input())

count=1
sum=0

while count<=N:
    number=int(input())
    sum=sum+number
    count=count+1

average=sum/N 
print(average)