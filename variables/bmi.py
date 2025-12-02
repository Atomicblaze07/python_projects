# Function to calculate BMI and categorize it
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 16:
        category = "Very underweight"
    elif bmi <= 18.5:
        category = "Underweight"
    elif bmi <= 25:
        category = "Healthy"
    elif bmi <= 30:
        category = "Overweight"
    else:
        category = "Very overweight"
    return bmi, category

# Given weight in kg and height in meters
weight = 92.3
height = 1.86

bmi_value, bmi_category = calculate_bmi(weight, height)

print(f"BMI: {bmi_value:.2f}")
print(f"Category: {bmi_category}")
