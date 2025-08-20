'''
    write a program to print the greatest number among the given N numbers
'''

N=int(input())

greatest_number=0
for i in range(N):

    number=int(input())

    if (number>greatest_number):
        greatest_number=number 
    
print(greatest_number)
