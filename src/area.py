# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.

a,b,c = map(float, input().split(" "))

pi = 3.14159

triangle = ((a * c) / 2)
circle = (pi * (c ** 2))
trapeze = (((a + b) * c ) / 2)
square = (b ** 2)
retangle = (a * b)

print(f"TRIANGULO = {triangle:.3f}")
print(f"CIRCULO = {circle:.3f}")
print(f"TRAPEZIO = {trapeze:.3f}")
print(f"QUADRADO = {square:.3f}")
print(f"RETANGULO = {retangle:.3f}")