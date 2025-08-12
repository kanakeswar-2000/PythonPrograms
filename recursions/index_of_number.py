'''
return the index of the first occurence of the number in the list
'''
L=input().split()
N=input()

def get_index_of_number(L):

    each_num=L[0]

    if (each_num==N):
        return 0 
    return 1 + get_index_of_number(L[1:])


index=get_index_of_number(L)

print(index)


