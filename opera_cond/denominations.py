A=int(input())
no_of_2000=int(A/2000)
remaining_amount=A%2000
no_of_500=int(remaining_amount/500)
remaining_amount=remaining_amount%500 
no_of_200=int(remaining_amount/200)
remaining_amount=remaining_amount%200
no_of_50=int(remaining_amount/50)
remaining_amount=remaining_amount%50 
no_of_20=int(remaining_amount/20)
remaining_amount=remaining_amount%20
no_of_5=int(remaining_amount/5)
remaining_amount=remaining_amount%5
no_of_2=int(remaining_amount/2)
remaining_amount=remaining_amount%2
no_of_1=remaining_amount
print("2000:"+str(no_of_2000)+" 500:"+str(no_of_500)+" 200:"+str(no_of_200)+" 50:"+str(no_of_50)+" 20:"+str(no_of_20)+" 5:"+str(no_of_5)+" 2:"+str(no_of_2)+" 1:"+str(no_of_1))

