# Explain the difference between the = operator and the == operator in Python

# = operator (Assignment operator):

# The "=" is a simple assignment operator. It is used for assignment, such as when assigning a value to a variable.
# It assigns values from right side operands to the left side operand.

A = 1  # Assigns the value 1 to the variable X
B = 'Python'  # Assigns the string 'Python' to the variable B

# == Operator (Equal or relational operator):

# The "==" is an Equal/relational operator for checking equality of two values.
# If the values are same, it will return True, else it will return False.

X = 2
Y = 2
print(X == Y)  # Returns True because A and B have the same values

C = 'Python'
D = 'Java'
print(C == D)  # Returns False because C and D have the different values

# What does the ** operator do in Python, and how is it used

# ** Operator (Exponentiation operator)

# The double star operator, which is denoted by (**), is an arithmetic operator in Python often used for exponentiation.
# It's a power operator that raises the number on its left to the power of the number on its right
# This means that, given two numbers a and b, the expression ‘a**b’ calculates the value of a raised to the power of b

a = 3
b = 2
result = a ** b  # 3 raised to the power of 2
print(result)  # Output: 9

m = 10
n = 2
result = m ** n  # 10 raised to the power of 2
print(result)  # Output: 100

# Uses of ** operator in Python

# In Python, the double asterisks have many uses such as in:
# "Arithmetic operations", "Function arguments", and "Dictionary data structures"

# What does the ^ operator do in Python and in what context is it commonly used?

# ^ operator- (Bitwise XOR operator)

# The ^ (Bitwise XOR) operator compares each bit and set it to 1 if only one is 1
# Otherwise (if both are 1 or both are 0) it is set to 0

a = 4  # Binary: 0100
b = 10  # Binary: 1010
results = a ^ b  # Binary result: 1110
print(results)  # Output: 14

# how it works
# 0100
# 1010
# -------
# 1110  (Which is "14" in decimal)
