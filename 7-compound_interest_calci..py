# Compund interest calculator using python: 
# total compound interest = principle(p) * (1+rate/100) to the power time(t)

principle=0
rate=0
time=0

while True :
    principle=float(input("Enter the principle amount:"))
    if principle<0:
        print("principle amount is less than 0")
    else:
        break

while True :
    rate=float(input("Enter the rate amount:"))
    if rate<0:
        print("rate amount is less than 0")
    else:
        break

while True :
    time=float(input("Enter the duration in years:"))
    if time<0:
        print("time cannot be less than 0")
    else:
        break

total= principle * pow((1 + rate / 100),time)
print(f"the amount after the {time} is {total}")

