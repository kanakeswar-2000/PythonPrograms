Number=input()


first_digit=Number[0]
value1= int(first_digit) ** 4

second_digit=Number[1]
value2=int(second_digit) ** 4

third_digit=Number[2]
value3=int(third_digit)**4 

fourh_digit=Number[3]
value4=int(fourh_digit) **4 

total_sum= value1+value2+value3+value4

if (total_sum==int(Number)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")