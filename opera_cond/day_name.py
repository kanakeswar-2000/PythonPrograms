'''
given weekday of the first day of the month and 
determine the day of the week of the given date of the month
'''

D=input()
D=D.lower()
N=int(input())

R=N%7
if (D=="sunday"):
    if R==1:
        day="Sunday"
    if R==2:
        day="Monday"
    if R==3:
        day="Tuesday"
    if R==4:
        day="Wednesday"
    if R==5:
        day="Thursday"
    if R==6:
        day="Friday"
    if R==0:
        day="Saturday"
if D=="monday":
    if R==0:
        day="Sunday"
    if R==1:
        day="Monday"
    if R==2:
        day="Tuesday"
    if R==3:
        day="Wednesday"
    if R==4:
        day="Thursday"
    if R==5:
        day="Friday"
    if R==6:
        day="Saturday"
if D=="tuesday":
    if R==6:
        day="Sunday"
    if R==0:
        day="Monday"
    if R==1:
        day="Tuesday"
    if R==2:
        day="Wednesday"
    if R==3:
        day="Thursday"
    if R==4:
        day="Friday"
    if R==5:
        day="Saturday"
if D=="wednesday":
    if R==5:
        day="Sunday"
    if R==6:
        day="Monday"
    if R==0:
        day="Tuesday"
    if R==1:
        day="Wednesday"
    if R==2:
        day="Thursday"
    if R==3:
        day="Friday"
    if R==4:
        day="Saturday"
if D=="thursday":
    if R==4:
        day="Sunday"
    if R==5:
        day="Monday"
    if R==6:
        day="Tuesday"
    if R==0:
        day="Wednesday"
    if R==1:
        day="Thursday"
    if R==2:
        day="Friday"
    if R==3:
        day="Saturday"
if D=="friday":
     
    if R==1:
        day="Friday"
    if R==2:
        day="Saturday"
    if R==3:
        day="Sunday"
    if R==4:
        day="Monday"
    if R==5:
        day="Tuesday"
    if R==6:
        day="Wednesday"
    if R==7:
        day="Thursday"
     
     
if D=="saturday":
    if R==0:
        day="Saturday"
    if R==1:
        day="Sunday"
    if R==2:
        day="Monday"
    if R==3:
        day="Tuesday"
    if R==4:
        day="Wednesday"
    if R==5:
        day="Thursday"
    if R==6:
        day="Friday"
    
print(day)
