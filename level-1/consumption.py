# Calculate a car's average consumption being provided the total distance traveled (in Km) and the spent fuel total (in liters).

a,b = map(float, input().split(" "))

consume = (a / b)

print(f"{consume:.3f} km/l")