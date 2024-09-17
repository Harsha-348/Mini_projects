# Height converter from cm to feet and vice versa

height=float(input('enter your height:'))
unit=input('centi-meter or feet?(CM or F):')

if unit=='F':
    height= height * 30.48
    print(f"your weight is:{round(height,2)} CCms")
elif unit=='CM':
    height=height /30.48
    print(f"your weight is:{round(height,2)} FEET")
  
else:
    print(f"enterer {unit} is invalid")



