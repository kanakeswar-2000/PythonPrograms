T=float(input())
if T<0:
    print("Freezing weather")
elif T<10:
    print("Very Cold weather")
elif T<20:
    print("Cold weather")
elif T<30:
    print("Normal")
elif T<40:
    print("Hot")
else:
    print("Very Hot")