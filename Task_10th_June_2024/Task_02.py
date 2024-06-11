# Develop a Python script that calculates the square and cube of a given number.
# given number = 2, gives sq = 4 and cube = 8

number = 2
square = number ** 2
cube = number ** 3
print(square)
print(cube)


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than or equal to the second number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The first number is greater than second number" if num1 > num2 else "first number is less than second number" if num1 < num2 else "first number is equal to second number")