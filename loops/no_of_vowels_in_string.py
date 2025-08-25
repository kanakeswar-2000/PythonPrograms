string=input()
string=string.lower()
vowels=["a","e","i","o","u"]

vowels_count=0 

for char in string:
    if char in vowels:
        vowels_count+=1 

print(vowels_count)