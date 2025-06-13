'''
  print rectangle with M rows and N columns starting with 1
'''

M=int(input())
N=int(input())

count=1 

while count<=M:
    num=str(count)+" "
    row=num*N 
    print(row)
    count+=1