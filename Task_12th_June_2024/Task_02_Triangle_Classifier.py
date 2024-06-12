# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).


side1 = float(input("Enter the length of side1:\n"))
side2 = float(input("Enter the length of side2:\n"))
side3 = float(input("Enter the length of side3:\n"))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
