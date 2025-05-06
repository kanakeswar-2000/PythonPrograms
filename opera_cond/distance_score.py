D=int(input())
first_50=50*3
next_50=50*5 
next_100=100*6 
if D<=50:
    score=D*3 
elif D<=100:
    remaining_distance=D-50
    remaining_score=remaining_distance*5
    score=first_50+remaining_score
elif D<=200:
    remaining_distance=D-100
    remaining_score=remaining_distance*6 
    score=first_50+next_50+remaining_score
else:
    remaining_distance=D-200 
    remaining_score=remaining_distance*10
    score=first_50+next_50+next_100+remaining_score
score=score+100 
print(score)

