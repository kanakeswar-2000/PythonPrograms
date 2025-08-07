def sum_of_nums(N):
    if (N==1):
        return 1 
    else:
        return N + sum_of_nums(N-1)

N=int(input())

sum=sum_of_nums(N)
print(sum)