'''
    calculate sum of N terms in harmonic serires 

    1,1/2 , 1/3 ,.......1/N terms 
'''
N=int(input())

def get_sum_of_harmonic_series(N):

    if (N==1):
        return 1 
    return 1/N + get_sum_of_harmonic_series(N-1)

result=get_sum_of_harmonic_series(N)

print(result)
