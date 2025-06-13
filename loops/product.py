'''
    read two numbers X and N and print the product of N numbers after X
'''
X=int(input())
N=int(input())

count=1 
product=1 

while count<=N:
    X=X+1
    product=product*X
    count+=1
print(product)
