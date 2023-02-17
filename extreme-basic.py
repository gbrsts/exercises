# Read 2 variables, named A and B and make the sum of these two variables, assigning its result to the variable X. 
# Print X as shown below. Print endline after the result otherwise you will get “Presentation Error”.

a,b = map(int, input().split(" "))

x = a + b

print(f"X = {x}")