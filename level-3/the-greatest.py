# Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". 

# Input
# The input file contains 3 integer values.

# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.

a,b,c = map(int, input().split(" "))

if a > b and a > c:
  print(f"{a} eh o maior")
elif b > a and b > c:
  print(f"{b} eh o maior")
else:
  print(f"{c} eh o maior")