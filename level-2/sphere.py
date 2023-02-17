# Make a program that calculates and shows the volume of a sphere being provided the value of its radius (R). 
# The formula to calculate the volume is: (4/3) * pi * R3. Consider (assign) for pi the value 3.14159.

# Input
# The input contains a value of floating point (double precision).

# Output
# The output must be a message "VOLUME" like the following example with a space before and after the equal signal. 
# The value must be presented with 3 digits after the decimal point.

radius = float(input())
pi = 3.14159

volume = ((4/3) * pi * (radius ** 3))

print(f"VOLUME: {volume:.3f}")