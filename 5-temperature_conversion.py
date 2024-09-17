# python code for temperature converter(celcius to fahrenheit)

unit=input("which measure is ur temperature in(celcius or fahrenheit)(C or F):")
temp=float(input("enter the temperature:"))

if unit=="C":
    temp= round((9 * temp) / 5 + 32,1)
    print(f"the converted temperature from celsius to fahrenheit is {temp}°F") 
elif unit=="F":
    temp=round((temp-32)* (5 / 9),2)
    print(f"the converted temperature from fahrenheit to celcius is {temp}°C") 
else:
    print(f"{unit} entered value is invalid")

