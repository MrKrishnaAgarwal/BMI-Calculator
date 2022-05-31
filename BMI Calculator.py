print("Welcome to the BMI Calculator")
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print ("Your BMI is: ",BMI)
if BMI < 16:
    print("You are Severely underweight")
elif 16 <= BMI < 18.5:
    print("You are Underweight")
elif 18.5 <= BMI < 25:
    print("You are Normal")
elif 25 <= BMI < 30:
    print("You are Overweight")
else:
    print("You have Obese")
print("Thank you for using the BMI Calculator")
input("Press Enter to exit")