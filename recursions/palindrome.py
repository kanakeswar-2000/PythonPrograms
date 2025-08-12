'''
    check whether given string is a palindrome
'''

string=input()
string=string.lower()

def is_palindrome(string):

    if (len(string)==0):
        return True 
    elif (string[0]!=string[-1]):
        return False 
    return is_palindrome(string[1:-1])

result=is_palindrome(string)

print(result)





