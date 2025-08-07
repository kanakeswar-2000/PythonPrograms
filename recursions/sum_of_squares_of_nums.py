def sum_of_squares_of_nums(numbers):

    each_num=int(numbers[0])
    if len(numbers)==1:
        return each_num ** 2
    return each_num ** 2 + sum_of_squares_of_nums(numbers[1:])

numbers=input().split()

result=sum_of_squares_of_nums(numbers)

print(result)