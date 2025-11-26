# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) / 1.8

# Ask user for input
temp_f = float(input("Enter temperature in Fahrenheit: "))
temp_c = fahrenheit_to_celsius(temp_f)

# Print formatted result
print(f"{temp_f}°F is equal to {temp_c:.2f}°C")