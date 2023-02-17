# Read two integer values, in this case, the variables A and B. 
# After this, calculate the sum between them and assign it to the variable SOMA.

# Input
# The input file contains 2 integer numbers.

# Output
# Print the message "SOMA" with all the capital letters, 
# with a blank space before and after the equal signal followed by the corresponding value to the sum of A and B. 

a,b = map(int, input().split(" "))

summ = a + b

print(f"SOMA = {summ}")