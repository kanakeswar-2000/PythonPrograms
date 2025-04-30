code1=input()
code2=input()

str1=code1[:3]
str2=code2[:3]

if (str1=="DIS" or str2=="DIS"): # any one of the code contains "DIS"
    print("Discount")
else:
    print("No Discount")