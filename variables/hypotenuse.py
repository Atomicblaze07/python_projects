# Pythagorean Theorem

a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2 + b**2) ** 0.5

print(c)
# Get input values from the user allowing decimals
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))

# Calculate the hypotenuse
c = (a**2 + b**2) ** 0.5

# Print the result with two decimal places
print(f"The length of the hypotenuse is {c:.2f}")
