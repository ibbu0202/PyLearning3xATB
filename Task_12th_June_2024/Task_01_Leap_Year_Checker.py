# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible xby 400.
# Use an if-else statement to make this determination.
# Input = 2024


year = int(input("Enter the year that needs to be checked: "))
result = "Leap year" if year % 400 == 0 else "Leap year" if year % 4 == 0 and year % 100 != 0 else "not a Leap year"
print(result)
