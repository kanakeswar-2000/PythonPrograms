def sum_of_nums_of_list(numbers):
    no_of_nums=len(numbers)
    if (no_of_nums==0):
        return 0 
    return int(numbers[0])+sum_of_nums_of_list(numbers[1:])

list_of_nums=input().split()

result=sum_of_nums_of_list(list_of_nums)

print(result)