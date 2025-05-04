days=int(input())

no_of_years= int(days/365) 
remaining_days=days % 365 

no_of_weeks=int(remaining_days/7) 
remaining_days=days%7 

print("{} years".format(no_of_years))
print("{} weeks".format(no_of_weeks))
print("{} days".format(remaining_days))

