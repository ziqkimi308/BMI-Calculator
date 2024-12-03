"""
********************************************************************************
* Project Name:  BMI Calculator 2.0
* Description:   This project calculates the BMI of a person
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

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