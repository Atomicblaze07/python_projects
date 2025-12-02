# equation of the form ax^2 + bx + c = 0

# Input values for a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

if d > 0:
    # Two real and distinct roots
    root1 = (-b + (d)**(1/2)) / (2*a)
    root2 = (-b - (d)**(1/2)) / (2*a)
    print("The roots are:", root1, "and", root2)
elif d == 0:
    # One real root (equal)
    root = -b / (2*a)
    print("The root is:", root)
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = (-d)**(1/2) / (2*a)
    print("The roots are:", f"{real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")
