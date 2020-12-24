weight=input("Enter your weight:")
check=input(" 'L' to convert to pounds and 'K' to convert to kilograms:")
if check == 'L' or check == 'l':
    ans=float(weight)*2.20462
    print("Weight in pounds:"+str(ans))
elif check == 'K' or check == 'k':
    ans=float(weight)*0.453592
    print("Weight in kg:"+str(ans))
else:
    print("Error!")

