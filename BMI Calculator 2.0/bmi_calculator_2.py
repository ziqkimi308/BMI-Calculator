print("Welcome to BMI Calculator 2.0")
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))
bmi = round((weight / height ** 2), 2)
if bmi < 18.5:
    print(f"BMI: {bmi} | Underweight")
elif 18.5 < bmi < 25:
    print(f"BMI: {bmi} | Normal weight")
elif 30 > bmi > 25:
    print(f"BMI: {bmi} | Overweight")
elif 35 > bmi > 30:
    print(f"BMI: {bmi} | Obese")
elif bmi > 35:
    print(f"BMI: {bmi} | Clinically obese")