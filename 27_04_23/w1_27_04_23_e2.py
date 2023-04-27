def calculate_bmi(height, weight):
    return format(weight/((height/100)**2), ".3f")
height, weight = float(input("Enter your height(cm) : ")), float(input("Enter your weight(kg) : "))
print(f"Your bmi score is {calculate_bmi(height, weight)}")

#OUTPUT
"""
Enter your height(cm) : 180
Enter your weight(kg) : 65
180.0 65.0
Your bmi score is 20.062
"""