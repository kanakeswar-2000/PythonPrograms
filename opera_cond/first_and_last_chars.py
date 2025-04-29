string=input()
n=int(input())
l1=len(string)

first_part=string[:n]
second_part=string[l1-n:]

result=first_part==second_part

print(result)