# Fibonacci series

# Write a Program to display the Fibonacci series up to n-th term.

num = int(input("Enter Number : "))

x = 0
y = 1
z = 0

for i in range(num):
    print(z, end=" ")
    x = y
    y = z
    z = x + y
