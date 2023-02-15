# Read two integer values. 
# After this, calculate the product between them and store the result in a variable named PROD. 

a,b = map(int, input().split(" "))

product = a * b

print(f"PROD = {product}")