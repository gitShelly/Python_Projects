print("Get access to the BMI calculator")
height=float(input("Enter your height in metres-->"))
weight=float(input("Enter your weight in kilos-->"))
bmi=weight/(height**2)
# to round the number and not use int conversion we use round()
bmi_round=round(bmi,2)
# we are using f strings 
print(f"Your BMI according to W={weight} and H={height} is {bmi_round}")

if(bmi_round<18.5):
    print("underweight")
elif(bmi_round>=18.5 and bmi_round<25):
    print("healthy")
elif(bmi_round>=25 and bmi_round<29.9):
    print("overweight")
else:
    print("obesity")
    
