"""
********************************************************************************
* Project Name:  BMI Calculator
* Description:   This project calculates the BMI of a person
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

print("Welcome to BMI calculator!")
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

print(f"Your BMI is : {int(bmi)}")