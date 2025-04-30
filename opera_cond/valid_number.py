Number=input()
first_digit=Number[0]
second_digit=Number[1]
third_digit=Number[2]

condition1=first_digit!="5"  or second_digit!="5" or third_digit!="5" # anyone digit not equal to 5 
Number=int(Number)
condition2=Number>300 and Number<700 # number is in between 300 and 700 

if (condition1 and condition2):
    print("Valid Number")
else:
    print("Not a Valid Number")
