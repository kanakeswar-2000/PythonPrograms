def largest_square(numbers):
    each_num=int(numbers[0])
    if len(numbers)==1:
        return each_num ** 2 
    return max(each_num,largest_square(numbers[1:]))

numbers=input().split()

result=largest_square(numbers)

print(result)