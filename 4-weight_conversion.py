# Python weight converter (kg to pound and vice versa)

weight=float(input("enter the weight:"))
unit=input("Kilograms or pounds? (k or l):")

if unit=='k':
    weight=weight * 2.205
    unit='lbs.'
elif unit=="l":
    weight=weight / 2.205
    unit='kgs.'
else:
    print(f"your enter {weight} is invalid")

print(f"your weight is:{round(weight,2)}{unit}")