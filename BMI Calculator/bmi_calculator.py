print("Welcome to BMI calculator!")
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

print(f"Your BMI is : {int(bmi)}")