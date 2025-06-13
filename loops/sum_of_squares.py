'''
read a number N and print sum of squares of N numbers starting with 1
'''

N=int(input())
count=1 
sum_of_squares=0 

while count<=N:
    sum_of_squares=sum_of_squares+count**2 
    count+=1 
print(sum_of_squares)
