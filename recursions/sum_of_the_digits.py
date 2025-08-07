def sum_of_digits(number):
    digit=int(number[0])

    if (len(number)==1):
        return digit 
    return digit + sum_of_digits(number[1:])

number=input()

result=sum_of_digits(number)

print(result)