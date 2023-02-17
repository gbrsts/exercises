# Read 3 floating-point numbers. After, print the roots of bhaskara’s formula.
# If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

# Input
# Read 3 floating-point numbers (double) A, B and C.

# Output
# Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

import math

a,b,c = map(float, input().split(" "))

delta = ((b ** 2) - (4 * a * c))

x1 = (((b * (-1)) + math.sqrt(delta)) / (2 * a))
x2 = (((b * (-1)) - math.sqrt(delta)) / (2 * a))

print(f"R1 = {x1:.5f}")
print(f"R2 = {x2:.5f}") 