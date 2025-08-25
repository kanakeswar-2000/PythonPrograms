'''
   A number is indivisible , if it is not divisible by 2 to 9
'''

N=int(input())

count=0 

for i in range(2,10):
    if N%i==0:
        count+=1 

if count>0 :
    print("Divisible Number")

else:
    print("Indivisble Number")